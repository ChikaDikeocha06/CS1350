
import os
import json
import pickle
import shutil


# Problem 1: Security Log Splitter


def split_logs(machines):
    """
    Split each machine's log into info.log, warning.log, and error.log.
    Return counts for each machine.
    """

    counts = {}

    with open("info.log", "w") as info, \
         open("warning.log", "w") as warning, \
         open("error.log", "w") as error:

        output_files = {
            "INFO": info,
            "WARNING": warning,
            "ERROR": error
        }

        for machine, filename in machines.items():

            counts[machine] = {
                "INFO": 0,
                "WARNING": 0,
                "ERROR": 0
            }

            with open(filename, "r") as file:

                for line in file:
                    if not line.strip():
                        continue

                    for level in output_files:
                        if f"[{level}]" in line:
                            output_files[level].write(
                                f"{machine} | {line}"
                            )
                            counts[machine][level] += 1
                            break

    return counts


def print_report(counts, error_file="error.log"):
    """Print the security status report."""

    print("SECURITY LOG REPORT")
    print("=" * 40)

    total_info = 0
    total_warning = 0
    total_error = 0

    for machine, values in counts.items():

        info = values["INFO"]
        warning = values["WARNING"]
        error = values["ERROR"]

        total = info + warning + error

        total_info += info
        total_warning += warning
        total_error += error

        if error >= 2:
            status = "CRITICAL"
        elif error >= 1 or warning >= 1:
            status = "NEEDS ATTENTION"
        else:
            status = "OK"

        print(
            f"{machine}: {total} entries | "
            f"INFO {info} | WARNING {warning} | "
            f"ERROR {error} | Status: {status}"
        )

    print("-" * 40)

    grand_total = total_info + total_warning + total_error

    print(
        f"Total: {grand_total} entries | "
        f"INFO {total_info} | WARNING {total_warning} | "
        f"ERROR {total_error}"
    )

    print("Errors (see error.log):")

    with open(error_file, "r") as file:
        for line in file:
            print("  " + line.rstrip("\n"))


# Test Problem 1

with open("server_a.log", "w") as f:
    f.write("2026-10-05 08:01:12 [INFO] User alice logged in\n")
    f.write("2026-10-05 08:03:45 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:03:59 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:04:10 [ERROR] Account root locked after repeated failures\n")
    f.write("2026-10-05 08:15:30 [INFO] Firewall rules reloaded\n")
    f.write("2026-10-05 09:02:11 [INFO] User alice logged out\n")

with open("server_b.log", "w") as f:
    f.write("2026-10-05 08:00:05 [INFO] System boot complete\n")
    f.write("2026-10-05 08:20:41 [ERROR] Disk encryption service failed to start\n")
    f.write("2026-10-05 08:21:02 [WARNING] Unencrypted volume mounted\n")
    f.write("2026-10-05 08:45:19 [INFO] User bob logged in\n")
    f.write("2026-10-05 09:10:33 [ERROR] Unauthorized access attempt on port 22\n")
    f.write("\n")
    f.write("2026-10-05 09:30:00 [INFO] Backup completed\n")

counts = split_logs({
    "server_a": "server_a.log",
    "server_b": "server_b.log"
})

print(counts)

with open("warning.log", "r") as f:
    print(f.read())

print_report(counts)


# Problem 2: Incident Tracker


def load_incidents(csv_file):
    """Return a list of incident dictionaries."""

    incidents = []

    with open(csv_file, "r") as file:

        header = file.readline()

        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split(",")

            incident = {
                "id": int(parts[0]),
                "machine": parts[1],
                "severity": parts[2],
                "description": parts[3]
            }

            incidents.append(incident)

    return incidents


def save_summary(incidents, json_file):
    """Save a summary to a JSON file and return it."""

    summary = {
        "total": len(incidents),
        "by_machine": {},
        "by_severity": {},
        "high_ids": []
    }

    for incident in incidents:

        machine = incident["machine"]
        severity = incident["severity"]

        if machine not in summary["by_machine"]:
            summary["by_machine"][machine] = 0

        summary["by_machine"][machine] += 1

        if severity not in summary["by_severity"]:
            summary["by_severity"][severity] = 0

        summary["by_severity"][severity] += 1

        if severity == "high":
            summary["high_ids"].append(incident["id"])

    with open(json_file, "w") as file:
        json.dump(summary, file, indent=2)

    return summary


def archive(incidents, folder):
    """Save incidents using pickle and JSON."""

    os.makedirs(folder, exist_ok=True)

    pickle_file = os.path.join(folder, "incidents.pkl")

    with open(pickle_file, "wb") as file:
        pickle.dump(incidents, file)

    machines = {}

    for incident in incidents:

        machine = incident["machine"]

        if machine not in machines:
            machines[machine] = []

        machines[machine].append(incident)

    for machine, machine_incidents in machines.items():

        json_file = os.path.join(folder, machine + ".json")

        with open(json_file, "w") as file:
            json.dump(machine_incidents, file, indent=2)

    return sorted(os.listdir(folder))


def load_archive(folder):
    """Load incidents from the pickle file."""

    pickle_file = os.path.join(folder, "incidents.pkl")

    with open(pickle_file, "rb") as file:
        incidents = pickle.load(file)

    return incidents


# Test Problem 2

with open("incidents.csv", "w") as f:
    f.write("id,machine,severity,description\n")
    f.write("1,server_a,high,Account root locked\n")
    f.write("2,server_b,high,Disk encryption failed\n")
    f.write("3,server_b,low,Unencrypted volume mounted\n")
    f.write("4,server_a,medium,Repeated failed logins\n")
    f.write("5,server_b,high,Unauthorized access on port 22\n")

incidents = load_incidents("incidents.csv")

print(len(incidents))
print(incidents[0])

summary = save_summary(incidents, "summary.json")

print(summary)

with open("summary.json", "r") as f:
    print(json.load(f) == summary)

print(archive(incidents, "archive"))

with open(os.path.join("archive", "server_a.json"), "r") as f:
    print([item["id"] for item in json.load(f)])

restored = load_archive("archive")

print(restored == incidents)


# Problem 3: Workspace Organizer


def organize(folder):
    """Move files into folders based on their extensions."""

    folders = {
        "logs": [],
        "data": [],
        "pickles": [],
        "other": []
    }

    for name in os.listdir(folder):

        source = os.path.join(folder, name)

        # Only move files, not existing folders
        if not os.path.isfile(source):
            continue

        extension = os.path.splitext(name)[1].lower()

        if extension == ".log":
            destination_folder = "logs"

        elif extension in [".csv", ".json"]:
            destination_folder = "data"

        elif extension == ".pkl":
            destination_folder = "pickles"

        else:
            destination_folder = "other"

        target_folder = os.path.join(folder, destination_folder)

        os.makedirs(target_folder, exist_ok=True)

        destination = os.path.join(target_folder, name)

        shutil.move(source, destination)

        folders[destination_folder].append(name)

    for key in folders:
        folders[key].sort()

    return folders


def create_backup(source_dir, backup_root, label):
    """Copy the entire folder into a new backup folder."""

    os.makedirs(backup_root, exist_ok=True)

    backup_name = "backup_" + label

    backup_path = os.path.join(backup_root, backup_name)

    if os.path.exists(backup_path):
        shutil.rmtree(backup_path)

    shutil.copytree(source_dir, backup_path)

    return backup_path


def verify_backup(source_dir, backup_dir):
    """Check if every file exists in the backup with the same size."""

    for root, dirs, files in os.walk(source_dir):

        for filename in files:

            source_file = os.path.join(root, filename)

            relative_path = os.path.relpath(source_file, source_dir)

            backup_file = os.path.join(backup_dir, relative_path)

            if not os.path.isfile(backup_file):
                return False

            if os.path.getsize(source_file) != os.path.getsize(backup_file):
                return False

    return True


def cleanup_old_backups(backup_root, keep):
    """Delete old backups and keep the newest ones."""

    if not os.path.exists(backup_root):
        return []

    backups = []

    for name in os.listdir(backup_root):

        path = os.path.join(backup_root, name)

        if name.startswith("backup_") and os.path.isdir(path):
            backups.append(name)

    backups.sort()

    # Find backups to delete
    if keep < 0:
        keep = 0

    old_backups = backups[:-keep] if keep > 0 else backups

    for name in old_backups:

        path = os.path.join(backup_root, name)

        print(f"Deleting: {path}")

        shutil.rmtree(path)

    return sorted(old_backups)


# Test Problem 3

# Start clean so the test can be run again
for old in ["workspace", "backups"]:

    if os.path.exists(old):
        shutil.rmtree(old)

os.mkdir("workspace")

for name in [
    "a.log",
    "b.log",
    "incidents.csv",
    "summary.json",
    "incidents.pkl",
    "notes.txt"
]:

    with open(os.path.join("workspace", name), "w") as f:
        f.write(f"Test file: {name}\n")

print(organize("workspace"))

print(sorted(os.listdir("workspace")))

for label in ["2026-10-01", "2026-10-02", "2026-10-03"]:

    path = create_backup("workspace", "backups", label)

    print(os.path.basename(path), verify_backup("workspace", path))

# Damage one backup
os.remove(
    os.path.join(
        "backups",
        "backup_2026-10-03",
        "logs",
        "a.log"
    )
)

print(
    verify_backup(
        "workspace",
        os.path.join("backups", "backup_2026-10-03")
    )
)

print(cleanup_old_backups("backups", 2))

print(sorted(os.listdir("backups")))
