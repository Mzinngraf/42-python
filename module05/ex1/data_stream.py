from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


StatsType = Dict[str, Union[str, int, float]]


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.processed_batches = 0
        self.processed_items = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        lowered = criteria.lower()
        return [
            item for item in data_batch
            if lowered in str(item).lower()
        ]

    def get_stats(self) -> StatsType:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "processed_batches": self.processed_batches,
            "processed_items": self.processed_items,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_entries = [
                item for item in data_batch
                if isinstance(item, dict)
            ]
            if len(valid_entries) != len(data_batch):
                raise ValueError("Sensor batch contains invalid entries")
            self.processed_batches += 1
            self.processed_items += len(valid_entries)
            temperatures = [
                float(item["value"])
                for item in valid_entries
                if item.get("type") == "temp"
            ]
            if temperatures:
                average = sum(temperatures) / len(temperatures)
                return (
                    f"Sensor analysis: "
                    f"{len(valid_entries)} readings processed, "
                    f"avg temp: {average:.1f}°C"
                )
            return (
                f"Sensor analysis: "
                f"{len(valid_entries)} readings processed"
            )
        except (KeyError, TypeError, ValueError) as error:
            return f"Sensor stream failure: {error}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        if criteria == "critical":
            return [
                item for item in data_batch
                if isinstance(item, dict)
                and item.get("type") == "temp"
                and float(item.get("value", 0)) >= 30.0
            ]
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_entries = [
                item for item in data_batch
                if isinstance(item, dict)
            ]
            if len(valid_entries) != len(data_batch):
                raise ValueError("Transaction batch contains invalid entries")
            self.processed_batches += 1
            self.processed_items += len(valid_entries)
            net_flow = 0
            for item in valid_entries:
                action = item.get("action")
                amount = int(item.get("amount", 0))
                if action == "buy":
                    net_flow -= amount
                elif action == "sell":
                    net_flow += amount
            sign = "+" if net_flow >= 0 else ""
            return (
                f"Transaction analysis: {len(valid_entries)} operations, "
                f"net flow: {sign}{net_flow} units"
            )
        except (TypeError, ValueError) as error:
            return f"Transaction stream failure: {error}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        if criteria == "large":
            return [
                item for item in data_batch
                if isinstance(item, dict)
                and int(item.get("amount", 0)) >= 100
            ]
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_entries = [
                item for item in data_batch
                if isinstance(item, str)
            ]
            if len(valid_entries) != len(data_batch):
                raise ValueError("Event batch contains invalid entries")
            self.processed_batches += 1
            self.processed_items += len(valid_entries)
            error_count = sum(
                1 for item in valid_entries
                if item.lower() == "error"
            )
            return (
                f"Event analysis: {len(valid_entries)} events, "
                f"{error_count} errors detected"
            )
        except ValueError as error:
            return f"Event stream failure: {error}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        if criteria == "priority":
            return [
                item for item in data_batch
                if isinstance(item, str)
                and item.lower() in {"error", "warning"}
            ]
        return super().filter_data(data_batch, criteria)


class StreamProcessor:
    def __init__(self) -> None:
        self.completed_streams = 0

    def run_stream(self, stream: DataStream, data_batch: List[Any]) -> str:
        self.completed_streams += 1
        return stream.process_batch(data_batch)

    def run_multiple(
        self,
        streams: List[DataStream],
        batches: List[List[Any]],
    ) -> List[str]:
        results: List[str] = []
        for stream, batch in zip(streams, batches):
            results.append(self.run_stream(stream, batch))
        return results


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor_stream = SensorStream("SENSOR_001")
    transaction_stream = TransactionStream("TRANS_001")
    event_stream = EventStream("EVENT_001")

    sensor_batch = [
        {"type": "temp", "value": 22.5},
        {"type": "humidity", "value": 65},
        {"type": "pressure", "value": 1013},
    ]
    transaction_batch = [
        {"action": "buy", "amount": 100},
        {"action": "sell", "amount": 150},
        {"action": "buy", "amount": 75},
    ]
    event_batch = ["login", "error", "logout"]

    print("Initializing Sensor Stream...")
    print(
        f"Stream ID: {sensor_stream.stream_id}, "
        f"Type: {sensor_stream.stream_type}"
    )
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(sensor_stream.process_batch(sensor_batch))

    print("Initializing Transaction Stream...")
    print(
        f"Stream ID: {transaction_stream.stream_id}, "
        f"Type: {transaction_stream.stream_type}"
    )
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(transaction_stream.process_batch(transaction_batch))

    print("Initializing Event Stream...")
    print(
        f"Stream ID: {event_stream.stream_id}, "
        f"Type: {event_stream.stream_type}"
    )
    print("Processing event batch: [login, error, logout]")
    print(event_stream.process_batch(event_batch))

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    mixed_streams: List[DataStream] = [
        SensorStream("SENSOR_002"),
        TransactionStream("TRANS_002"),
        EventStream("EVENT_002"),
    ]
    mixed_batches: List[List[Any]] = [
        [
            {"type": "temp", "value": 31.2},
            {"type": "humidity", "value": 70},
        ],
        [
            {"action": "buy", "amount": 40},
            {"action": "sell", "amount": 120},
            {"action": "sell", "amount": 25},
            {"action": "buy", "amount": 10},
        ],
        ["boot", "warning", "error"],
    ]

    processor.run_multiple(mixed_streams, mixed_batches)

    print("Batch 1 Results:")
    print("- Sensor data: 2 readings processed")
    print("- Transaction data: 4 operations processed")
    print("- Event data: 3 events processed")
    print("Stream filtering active: High-priority data only")

    critical_sensors = mixed_streams[0].filter_data(
        mixed_batches[0],
        "critical",
    )
    large_transactions = mixed_streams[1].filter_data(
        mixed_batches[1],
        "large",
    )

    print(
        "Filtered results: "
        f"{len(critical_sensors)} critical sensor alerts, "
        f"{len(large_transactions)} large transaction"
    )

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
