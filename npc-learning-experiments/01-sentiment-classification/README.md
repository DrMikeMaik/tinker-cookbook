# Experiment 01: NPC Sentiment Classification

## Goal
Train a tiny model (Llama-3.2-1B) to classify player sentiment in NPC dialogue as POSITIVE, NEGATIVE, or NEUTRAL.

## Why This Matters for NPCs
In your LangGraph system, you have smaller LLMs handling validation, routing, and other auxiliary tasks. **Sentiment analysis** is a perfect candidate for a fine-tuned tiny model because:

1. **Simple task** - 3-way classification (POSITIVE/NEGATIVE/NEUTRAL)
2. **Low latency** - Much faster than calling GPT-4 or Claude
3. **Consistent format** - Input/output is predictable
4. **Cost effective** - Tiny models are nearly free to run

## Dataset
We created 30 training examples in `data/npc_sentiment_training.jsonl` that simulate player interactions:
- Player compliments → POSITIVE
- Player complaints → NEGATIVE
- Player questions → NEUTRAL

In production, you'd collect real data from your game logs.

## Model Choice
**Llama-3.2-1B** - The smallest Llama model, perfect for simple classification:
- ~1 billion parameters
- Very fast inference (<100ms on CPU, <10ms on GPU)
- Still capable enough for sentiment analysis

## Training Configuration
```python
model_name = "meta-llama/Llama-3.2-1B"
max_length = 512           # Short inputs
batch_size = 32            # Small batch for quick iteration
learning_rate = 2e-4       # LoRA standard (10x higher than full fine-tuning)
lora_rank = 32             # Default LoRA rank
num_epochs = 3             # Multiple passes over small dataset
```

## How to Run

### Step 1: Install dependencies (if not already done)
```bash
pip install tinker
pip install -e /home/user/tinker-cookbook
```

### Step 2: Run training
```bash
cd /home/user/tinker-cookbook/npc-learning-experiments/01-sentiment-classification
python train.py
```

### Step 3: Monitor training
Training logs will be saved to `results/sentiment-run/`. Watch for:
- Training loss (should decrease)
- Validation accuracy (if implemented)
- Training time per step

### Step 4 (Optional): Try different models
```bash
# Try slightly larger model
python train.py model_name="meta-llama/Llama-3.2-3B"

# Try different LoRA rank
python train.py lora_rank=64

# Try different learning rate
python train.py learning_rate=1e-4
```

## Expected Results

After training, you should be able to:
1. Load the fine-tuned model
2. Send player messages and get sentiment labels instantly
3. Compare latency: <100ms (tiny model) vs 1-2s (GPT-4 API call)

## Next Steps

Once this works:
1. **Collect real data** - Export conversations from your game
2. **Evaluate accuracy** - Compare with your current sentiment classifier
3. **Benchmark latency** - Measure inference time
4. **Try LoRA swapping** - Train multiple LoRAs for different tasks

## Integration with LangGraph

In your LangGraph nodes, you'd replace:
```python
# Current approach
sentiment = await llm_call("Classify sentiment: {message}")
```

With:
```python
# Fine-tuned tiny model approach
sentiment = await tiny_model.predict(message)  # Much faster!
```

## Files
- `train.py` - Training script
- `data/npc_sentiment_training.jsonl` - Training dataset (30 examples)
- `results/` - Training logs and checkpoints (created during training)
- `README.md` - This file

## Key Learnings

This experiment teaches:
1. How to structure training data in JSONL format
2. How LoRA configuration works (rank, learning rate)
3. How to fine-tune for classification tasks
4. The trade-offs between model size and capability
