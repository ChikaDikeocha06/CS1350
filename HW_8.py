
import os


# Exercise 1: Exception Handling

def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """
    print("\nExercise 1: Exception Handling")

    def process_file(filename):
        """
        Read file, process content, ensure file is closed.
        Return processed content or None.
        """
        file = None

        try:
            file = open(filename, "r")

        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return None

        except PermissionError:
            print(f"Permission denied for '{filename}'.")
            return None

        else:
            content = file.read()
            return content.upper()

        finally:
            if file is not None:
                file.close()
                print(f"File '{filename}' closed.")

    # Test files
    test_files = ["exists.txt", "missing.txt", "/root/file"]

    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")

    # Resource manager
    class ResourceManager:

        def __init__(self, name):
            self.name = name
            self.resource = None

        def acquire(self):
            """Acquire resource - might fail."""
            if self.name == "":
                raise RuntimeError("Resource name cannot be empty.")

            self.resource = True
            print(f"{self.name} resource acquired.")

        def release(self):
            """Release resource - must always happen."""
            if self.resource is not None:
                self.resource = None
                print(f"{self.name} resource released.")

        def use(self):
            """Use resource - only if acquired."""
            if self.resource is None:
                raise RuntimeError("Resource has not been acquired.")

            print(f"Using {self.name} resource.")

    # Test resource management
    rm = ResourceManager("Database")

    try:
        rm.acquire()

    except RuntimeError as e:
        print(f"Error: {e}")

    else:
        rm.use()

    finally:
        rm.release()


# Exercise 2: Custom Exceptions

def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """
    print("\nExercise 2: Custom Exceptions")

    # Create custom exceptions
    class GameError(Exception):
        """Base class for game exceptions."""
        pass

    class InvalidMoveError(GameError):
        """Invalid game move."""

        def __init__(self, position, reason):
            self.position = position
            self.reason = reason
            super().__init__(
                f"Position {position} is invalid: {reason}"
            )

    class GameOverError(GameError):
        """Game has ended."""

        def __init__(self, winner):
            self.winner = winner
            super().__init__(f"Game is over. Winner: {winner}")

    # TicTacToe game
    class TicTacToe:

        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.game_over = False

        def make_move(self, row, col):

            if self.game_over:
                raise GameOverError("Game already finished")

            if not (0 <= row < 3 and 0 <= col < 3):
                raise InvalidMoveError(
                    (row, col), "Position is out of bounds"
                )

            if self.board[row][col] != ' ':
                raise InvalidMoveError(
                    (row, col), "Position is already taken"
                )

            self.board[row][col] = self.current_player
            print(f"Player {self.current_player} placed a mark.")

            # Check for winner
            lines = self.board[:]

            lines.extend([
                [self.board[r][c] for r in range(3)]
                for c in range(3)
            ])

            lines.append([self.board[i][i] for i in range(3)])
            lines.append([self.board[i][2-i] for i in range(3)])

            for line in lines:
                if line.count(self.current_player) == 3:
                    self.game_over = True
                    print(f"Player {self.current_player} wins!")
                    return

            # Check for draw
            if all(cell != ' ' for row in self.board for cell in row):
                self.game_over = True
                print("The game is a draw!")
                return

            # Switch players
            self.current_player = (
                'O' if self.current_player == 'X' else 'X'
            )

    # Test the game
    game = TicTacToe()

    test_moves = [
        (0, 0),
        (0, 0),
        (5, 5)
    ]

    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"Move ({row}, {col}) successful")

        except InvalidMoveError as e:
            print(f"Invalid move: {e}")

        except GameOverError as e:
            print(f"Game over: {e}")


# Exercise 3: File Processing

def practice_3_complete_system():
    """
    Build a complete error handling system
    """
    print("\nExercise 3: File Processing")

    class FileProcessor:

        def __init__(self):
            self.processed_files = []
            self.failed_files = []

        def process_file(self, filename):
            """
            Process a single file with complete error handling.
            """
            file = None

            try:
                file = open(filename, "r")
                content = file.read()
                processed_content = content.upper()

            except FileNotFoundError:
                print(f"File not found: {filename}")
                self.failed_files.append(filename)
                return None

            except PermissionError:
                print(f"Permission denied: {filename}")
                self.failed_files.append(filename)
                return None

            except Exception as e:
                print(f"Error processing {filename}: {e}")
                self.failed_files.append(filename)
                return None

            else:
                self.processed_files.append(filename)
                print(f"Successfully processed: {filename}")
                return processed_content

            finally:
                if file is not None:
                    file.close()
                    print(f"Closed: {filename}")

        def process_directory(self, directory):
            """
            Process all files in directory, collecting errors.
            """
            try:
                files = os.listdir(directory)

                for filename in files:
                    filepath = os.path.join(directory, filename)

                    if os.path.isfile(filepath):
                        self.process_file(filepath)

            except FileNotFoundError:
                print(f"Directory not found: {directory}")

            except PermissionError:
                print(f"Permission denied: {directory}")

            except Exception as e:
                print(f"Directory processing error: {e}")

        def get_report(self):
            """
            Get processing report.
            """
            return {
                "Total Processed": len(self.processed_files),
                "Total Failed": len(self.failed_files),
                "Successful Files": self.processed_files,
                "Failed Files": self.failed_files
            }

    # Test the processor
    processor = FileProcessor()

    test_files = [
        "valid.txt",
        "missing.txt",
        "/root/restricted.txt"
    ]

    for filename in test_files:
        processor.process_file(filename)

    report = processor.get_report()

    print("\nProcessing Report:")
    print(report)


# Run All Exercises

if __name__ == "__main__":
    practice_3_complete_pattern()
    practice_2_custom_exceptions()
    practice_3_complete_system()
