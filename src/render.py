from pathlib import Path
from renderer.render import Renderer
from replay_parser import ReplayParser
from renderer.utils import LOGGER


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--replay", type=str, required=True)
    namespace = parser.parse_args()
    path = Path(namespace.replay)
    video_path = path.parent.joinpath(f"{path.stem}.mp4")
    with open(namespace.replay, "rb") as f:
        LOGGER.info("Parsing the replay file...")
        replay_info = ReplayParser(
            f, strict=True, raw_data_output=False
        ).get_info()
        LOGGER.info("Rendering the replay file...")
        renderer = Renderer(
            replay_info["hidden"]["replay_data"],
            logs=True,
            enable_chat=True,
            use_tqdm=True,
        )
        renderer.start(str(video_path))
        LOGGER.info("Done.")
