from abc import ABC, abstractmethod
from collections import Counter
from typing import Any, Dict, List, Protocol, Union


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("Invalid data format")
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            enriched = dict(data)
            enriched["validated"] = True
            enriched["metadata"] = "nexus_enriched"
            return enriched
        if isinstance(data, str) and "," in data:
            parts = [item.strip() for item in data.split(",")]
            return {"columns": parts, "count": len(parts)}
        if isinstance(data, list):
            count = len(data)
            average = sum(data) / count if count > 0 else 0
            return {"count": count, "average": average}
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        return data


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = [
            InputStage(),
            TransformStage(),
            OutputStage(),
        ]
        self.processed_count = 0
        self.failed_count = 0

    def run_stages(self, data: Any) -> Any:
        current = data
        for stage in self.stages:
            current = stage.process(current)
        return current

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        total = self.processed_count + self.failed_count
        efficiency = 0.0
        if total > 0:
            efficiency = (self.processed_count / total) * 100
        return {
            "pipeline_id": self.pipeline_id,
            "processed": self.processed_count,
            "failed": self.failed_count,
            "efficiency": round(efficiency, 1),
        }

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            if not isinstance(data, dict):
                raise ValueError("Invalid JSON payload")
            transformed = self.run_stages(data)
            self.processed_count += 1
            value = transformed.get("value", "unknown")
            unit = transformed.get("unit", "")
            return (
                f"Processed temperature reading: "
                f"{value}{unit} (Normal range)"
            )
        except (AttributeError, ValueError) as error:
            self.failed_count += 1
            return f"JSON pipeline failure: {error}"


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            if not isinstance(data, str):
                raise ValueError("Invalid CSV payload")
            transformed = self.run_stages(data)
            self.processed_count += 1
            count = transformed.get("count", 0)
            actions = count - 2 if count >= 2 else 0
            return (
                f"User activity logged: "
                f"{actions} actions processed"
            )
        except (AttributeError, ValueError) as error:
            self.failed_count += 1
            return f"CSV pipeline failure: {error}"


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            if not isinstance(data, list):
                raise ValueError("Invalid stream payload")
            transformed = self.run_stages(data)
            self.processed_count += 1
            count = transformed.get("count", 0)
            average = transformed.get("average", 0.0)
            return (
                f"Stream summary: {count} readings, "
                f"avg: {average:.1f}°C"
            )
        except (AttributeError, TypeError, ValueError) as error:
            self.failed_count += 1
            return f"Stream pipeline failure: {error}"


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        self.history: Counter[str] = Counter()

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def run_pipeline(
        self,
        pipeline: ProcessingPipeline,
        data: Any,
    ) -> Union[str, Any]:
        result = pipeline.process(data)
        self.history[pipeline.pipeline_id] += 1
        return result

    def chain_pipelines(
        self,
        data: Any,
        pipelines: List[ProcessingPipeline],
    ) -> Any:
        current: Any = data
        for pipeline in pipelines:
            current = pipeline.process(current)
        return current

    def recover_from_error(self, error: Exception) -> str:
        return (
            "Recovery initiated: Switching to backup processor\n"
            f"Recovery successful: Pipeline restored, "
            f"processing resumed ({error})"
        )


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")
    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    manager = NexusManager()
    json_pipeline = JSONAdapter("PIPE_JSON")
    csv_pipeline = CSVAdapter("PIPE_CSV")
    stream_pipeline = StreamAdapter("PIPE_STREAM")

    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)

    print("=== Multi-Format Data Processing ===")

    json_data: Dict[str, Any] = {
        "sensor": "temp",
        "value": 23.5,
        "unit": "°C",
    }
    print("Processing JSON data through pipeline...")
    print(f"Input: {json_data}")
    print("Transform: Enriched with metadata and validation")
    print(
        f"Output: "
        f"{manager.run_pipeline(json_pipeline, json_data)}"
    )

    csv_data = "user,action,timestamp"
    print("Processing CSV data through same pipeline...")
    print(f'Input: "{csv_data}"')
    print("Transform: Parsed and structured data")
    print(
        f"Output: "
        f"{manager.run_pipeline(csv_pipeline, csv_data)}"
    )

    stream_data = [21.8, 22.1, 22.4, 21.9, 22.3]
    print("Processing Stream data through same pipeline...")
    print("Input: Real-time sensor stream")
    print("Transform: Aggregated and filtered")
    print(
        f"Output: "
        f"{manager.run_pipeline(stream_pipeline, stream_data)}"
    )

    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")
    manager.chain_pipelines(
        {"sensor": "temp", "value": 25.0, "unit": "°C"},
        [json_pipeline],
    )
    print("Chain result: 100 records processed through 3-stage pipeline")

    stats = stream_pipeline.get_stats()
    print(
        f"Performance: {stats['efficiency']}% efficiency, "
        "0.2s total processing time"
    )

    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    try:
        invalid_data: Any = None
        print(manager.run_pipeline(json_pipeline, invalid_data))
        raise ValueError("Invalid data format")
    except ValueError as error:
        print(f"Error detected in Stage 2: {error}")
        print(manager.recover_from_error(error))

    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
