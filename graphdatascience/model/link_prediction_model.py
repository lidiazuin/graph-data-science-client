from dataclasses import dataclass
from typing import Any, Dict, List

from .pipeline_model import PipelineModel


@dataclass(frozen=True, repr=True)
class LinkFeature:
    """
    A link feature of a link prediction pipeline.

    Attributes:
        name: The name of the link feature.
        config: The configuration of the link feature.
    """
    name: str
    config: Dict[str, Any]

    def __str__(self) -> str:
        return f"({self.name}, {self.config})"


class LPModel(PipelineModel):
    def _query_prefix(self) -> str:
        return "CALL gds.beta.pipeline.linkPrediction.predict."

    def link_features(self) -> List[LinkFeature]:
        """
        Get the link features of the pipeline.

        Returns:
            A list of LinkFeatures of the pipeline.

        """
        steps: List[Dict[str, Any]] = self._list_info()["modelInfo"][0]["pipeline"]["featureSteps"]
        return [LinkFeature(s["name"], s["config"]) for s in steps]
