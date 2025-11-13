# NPC Learning Experiments

This folder contains experiments for learning how to fine-tune tiny LLMs for NPC-related tasks, separate from the original tinker-cookbook repository.

## Our Goal

Replace the smaller LLMs in our LangGraph NPC system with fine-tuned tiny models to:
- **Reduce latency** (from seconds to milliseconds)
- **Lower costs** (tiny models are nearly free)
- **Maintain accuracy** (specialized models can match or exceed general-purpose LLMs)

## Current NPC Architecture

```
┌─────────────────────────────────────┐
│         LangGraph NPC System        │
├─────────────────────────────────────┤
│                                     │
│  Main Flow: Strong LLM              │
│  (GPT-4, Claude, etc.)              │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ Smaller LLM Nodes:            │ │
│  │ • Validation                  │ │
│  │ • Routing                     │ │
│  │ • Retries                     │ │
│  │ • Dynamic parameters          │ │
│  │ • Sentiment analysis          │ │
│  └───────────────────────────────┘ │
│           ↓                         │
│  Replace with fine-tuned tiny      │
│  models or LoRA adapters!          │
└─────────────────────────────────────┘
```

## Experiments

### [01-sentiment-classification](./01-sentiment-classification/)
**Status**: Ready to run

Train a tiny model (Llama-3.2-1B) to classify player sentiment (POSITIVE/NEGATIVE/NEUTRAL).

**Key learnings**:
- JSONL data format
- LoRA configuration
- Model size vs capability trade-offs

**Next**: Run this first to understand the basics!

### 02-routing (Coming soon)
Train a model to route between different conversation types or NPC personalities.

### 03-validation (Coming soon)
Train a model to validate NPC response quality before sending to players.

### 04-multi-lora (Coming soon)
Single base model with multiple LoRA adapters for different tasks.

### 05-distillation (Coming soon)
Distill knowledge from your current strong LLMs into tiny models.

## Getting Started

1. **Read the learning plan**: See [LEARNING_PLAN.md](./LEARNING_PLAN.md)
2. **Run first experiment**: Start with sentiment classification
3. **Iterate**: Try different models, hyperparameters, datasets
4. **Measure**: Compare latency and accuracy with current system

## Prerequisites

```bash
# Install tinker SDK
pip install tinker

# Install this cookbook in editable mode
pip install -e /home/user/tinker-cookbook
```

## Resources

- **Original Repository**: `/home/user/tinker-cookbook/`
- **Examples**: `/home/user/tinker-cookbook/tinker_cookbook/recipes/`
- **Documentation**: `/home/user/tinker-cookbook/README.md`

## Separation from Original Repo

All code in this folder (`npc-learning-experiments/`) is separate from the forked repository. This keeps our learning experiments clean and prevents mixing with the original codebase.

When we're ready to contribute improvements back to tinker-cookbook, we'll do so through proper PRs!

## Questions & Iteration

As we work through these experiments, we'll:
- Document what works and what doesn't
- Measure concrete latency and accuracy improvements
- Build toward production integration with your LangGraph system
- Explore multi-LoRA approaches for maximum flexibility

Let's start with experiment 01! 🚀
