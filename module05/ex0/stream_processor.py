from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    def __init__(self, processor_name: str) -> None:
        self.processor_name = processor_name

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, list)
            and len(data) > 0
            and all(isinstance(item, (int, float)) for item in data)
        )

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric data")
            values: List[float] = [float(item) for item in data]
            total = sum(values)
            average = total / len(values)
            return (
                f"Processed {len(values)} numeric values, "
                f"sum={total:g}, avg={average:.1f}"
            )
        except (TypeError, ValueError) as error:
            return f"Numeric processing failed: {error}"


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Text Processor")

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and not data.startswith(
            ("INFO:", "WARNING:", "ERROR:")
        )

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data")
            characters = len(data)
            words = len(data.split())
            return (
                f"Processed text: {characters} characters, "
                f"{words} words"
            )
        except (AttributeError, ValueError) as error:
            return f"Text processing failed: {error}"


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Log Processor")

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return ":" in data and data.split(":", maxsplit=1)[0] in {
            "INFO",
            "WARNING",
            "ERROR",
        }

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid log entry")
            level, message = data.split(":", maxsplit=1)
            clean_message = message.strip()
            prefix = level
            if level == "ERROR":
                prefix = "ALERT"
            return f"[{prefix}] {level} level detected: {clean_message}"
        except (AttributeError, ValueError) as error:
            return f"Log processing failed: {error}"


def show_processor(processor: DataProcessor, data: Any) -> None:
    print(f"Initializing {processor.processor_name}...")
    print(f"Processing data: {data}")
    if processor.validate(data):
        if isinstance(processor, NumericProcessor):
            print("Validation: Numeric data verified")
        elif isinstance(processor, TextProcessor):
            print("Validation: Text data verified")
        else:
            print("Validation: Log entry verified")
    else:
        print("Validation: Data rejected")
    print(processor.format_output(processor.process(data)))


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric_data = [1, 2, 3, 4, 5]
    text_data = "Hello Nexus World"
    log_data = "ERROR: Connection timeout"

    show_processor(NumericProcessor(), numeric_data)
    show_processor(TextProcessor(), text_data)
    show_processor(LogProcessor(), log_data)

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]
    demo_data: List[Any] = [
        [1, 2, 3],
        "System online",
        "INFO: System ready",
    ]

    for index, processor in enumerate(processors, start=1):
        result = processor.process(demo_data[index - 1])
        print(f"Result {index}: {result}")

    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
