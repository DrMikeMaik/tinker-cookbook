"""
Train a tiny model for NPC sentiment classification.

This experiment demonstrates:
1. Fine-tuning a small model (Llama-3.2-1B) for a specific NPC task
2. Using LoRA for efficient training
3. Measuring latency improvements vs larger models

Usage:
    python train.py
    python train.py model_name="meta-llama/Llama-3.2-3B"  # Try a slightly larger model
"""

import chz
import sys
from pathlib import Path
from tinker_cookbook import cli_utils, model_info
from tinker_cookbook.renderers import TrainOnWhat
from tinker_cookbook.supervised import train
from tinker_cookbook.supervised.data import FromConversationFileBuilder
from tinker_cookbook.supervised.types import ChatDatasetBuilderCommonConfig
import asyncio


def build_config_blueprint() -> chz.Blueprint[train.Config]:
    # Use a tiny model - perfect for simple classification!
    model_name = "meta-llama/Llama-3.2-1B"
    renderer_name = model_info.get_recommended_renderer_name(model_name)

    # Path to our NPC sentiment training data
    current_dir = Path(__file__).parent
    data_path = current_dir / "data" / "npc_sentiment_training.jsonl"

    # Configuration for our dataset
    common_config = ChatDatasetBuilderCommonConfig(
        model_name_for_tokenizer=model_name,
        renderer_name=renderer_name,
        max_length=512,  # Sentiment classification is short!
        batch_size=32,   # Smaller batch size for faster iteration
        train_on_what=TrainOnWhat.ALL_ASSISTANT_MESSAGES,
    )

    # Build dataset from our JSONL file
    dataset = FromConversationFileBuilder(
        common_config=common_config,
        file_path=str(data_path),
    )

    return chz.Blueprint(train.Config).apply(
        {
            "log_path": str(current_dir / "results" / "sentiment-run"),
            "model_name": model_name,
            "dataset_builder": dataset,
            "learning_rate": 2e-4,  # LoRA uses ~10x higher LR
            "lr_schedule": "linear",
            "num_epochs": 3,  # More epochs for small dataset
            "eval_every": 2,
            "lora_rank": 32,  # Default LoRA rank
        }
    )


def main(config: train.Config):
    print("\n" + "="*60)
    print("NPC Sentiment Classification Training")
    print("="*60)
    print(f"Model: {config.model_name}")
    print(f"Log path: {config.log_path}")
    print(f"Epochs: {config.num_epochs}")
    print(f"Learning rate: {config.learning_rate}")
    print(f"LoRA rank: {config.lora_rank}")
    print("="*60 + "\n")

    # Avoid clobbering log dir from your previous run:
    cli_utils.check_log_dir(config.log_path, behavior_if_exists="ask")
    asyncio.run(train.main(config))


if __name__ == "__main__":
    blueprint = build_config_blueprint()
    blueprint.make_from_argv(sys.argv[1:])
    main(blueprint.make())
