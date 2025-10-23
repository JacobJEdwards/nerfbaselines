from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from nerfbaselines import MethodSpec
else:
    MethodSpec = dict


_artifacts_base_url = "https://huggingface.co/jkulhanek/wild-gaussians/resolve/main"
WildGaussiansMethodSpec: MethodSpec = {
    "method_class": "wildgaussians.method:WildGaussians",
    "conda": {
        "environment_name": "wild-gaussians",
        "python_version": "3.11",
        "install_script": r"""
        conda deactivate
        conda activate main
"""
    },
    "presets": {
        "phototourism": { "@apply": [{"dataset": "phototourism"}], "config": "phototourism.yml" },
        "nerfonthego": { 
            "@apply": [
                {"dataset": "nerfonthego"},
                {"dataset": "nerfonthego-undistorted"},
            ], "config": "nerfonthego.yml" },
    },
    "metadata": {
        "name": "WildGaussians",
        "description": "WildGaussians adopts 3DGS to handle appearance changes and transient objects. After fixing appearance, it can be baked back into 3DGS.",
        "paper_title": "WildGaussians: 3D Gaussian Splatting in the Wild",
        "authors": ["Jonas Kulhanek", "Songyou Peng", "Zuzana Kukelova", "Marc Pollefeys", "Torsten Sattler"],
        "paper_link": "https://arxiv.org/pdf/2407.08447.pdf",
        "link": "https://wild-gaussians.github.io/",
        "licenses": [
            {"name": "MIT", "url": "https://raw.githubusercontent.com/jkulhanek/wild-gaussians/main/LICENSE"}, 
            {"name": "custom, research only", "url": "https://raw.githubusercontent.com/graphdeco-inria/gaussian-splatting/main/LICENSE.md"}
        ],
    },
    "id": "wild-gaussians",
    "supported_camera_models": ["pinhole",],
    "supported_outputs": ["color", "accumulation", "depth"],
    "required_features": ["color", "points3D_xyz"],
    "output_artifacts": {
        "phototourism/trevi-fountain": {        "link": f"{_artifacts_base_url}/phototourism/trevi-fountain.zip" },
        "phototourism/sacre-coeur": {           "link": f"{_artifacts_base_url}/phototourism/sacre-coeur.zip" },
        "phototourism/brandenburg-gate": {      "link": f"{_artifacts_base_url}/phototourism/brandenburg-gate.zip" },
        "nerfonthego-undistorted/fountain": {   "link": f"{_artifacts_base_url}/nerfonthego-undistorted/fountain.zip" },
        "nerfonthego-undistorted/mountain": {   "link": f"{_artifacts_base_url}/nerfonthego-undistorted/mountain.zip" },
        "nerfonthego-undistorted/spot": {       "link": f"{_artifacts_base_url}/nerfonthego-undistorted/spot.zip" },
        "nerfonthego-undistorted/patio": {      "link": f"{_artifacts_base_url}/nerfonthego-undistorted/patio.zip" },
        "nerfonthego-undistorted/patio-high": { "link": f"{_artifacts_base_url}/nerfonthego-undistorted/patio-high.zip" },
        "nerfonthego-undistorted/corner": {     "link": f"{_artifacts_base_url}/nerfonthego-undistorted/corner.zip" },
    },
    "implementation_status": {
        "phototourism": "reproducing",
    },
}

try:
    from nerfbaselines import register
    register(WildGaussiansMethodSpec)
except ImportError:
    pass
