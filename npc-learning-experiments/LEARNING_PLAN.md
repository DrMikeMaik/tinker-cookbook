# NPC Fine-Tuning Learning Plan

## Overview
This folder contains experiments and learning code for fine-tuning tiny LLMs to power NPC nodes in our LangGraph system.

## Current NPC Architecture
- **Main Flow**: Strong LLM (GPT-4, Claude, etc.)
- **Smaller Nodes**: Currently using smaller general-purpose LLMs for:
  - Validation
  - Routing
  - Retries
  - Controlling dynamic parameters
  - Sentiment analysis

**Goal**: Replace smaller LLMs with fine-tuned tiny models (or single model with multiple LoRA adapters) to reduce latency and cost.

---

## Learning Path

### Phase 1: Understanding the Basics ✓ (In Progress)
- [x] Explore repository structure
- [ ] Run first supervised learning example (`sl_basic.py`)
- [ ] Understand LoRA configuration and hyperparameters
- [ ] Learn data format (conversations → tokens)

### Phase 2: Simple Classification Tasks (Week 1-2)
- [ ] **Experiment 1**: Sentiment Classification
  - Train Llama-3.2-1B on sentiment analysis
  - Compare latency vs current LLM
  - Measure accuracy

- [ ] **Experiment 2**: Binary Routing
  - Train model to route between conversation types
  - Test on sample NPC dialogues

- [ ] **Experiment 3**: Validation Tasks
  - Train model to validate NPC response quality
  - Compare with rule-based validation

### Phase 3: Multi-LoRA Single Model (Week 3-4)
- [ ] Train single base model with multiple LoRA adapters
- [ ] Test adapter swapping for different node types
- [ ] Measure overhead of LoRA swapping
- [ ] Compare vs separate fine-tuned models

### Phase 4: Distillation from Current System (Week 5-6)
- [ ] Collect production data from current LangGraph nodes
- [ ] Use prompt_distillation approach to internalize prompts
- [ ] Distill knowledge from strong LLMs into tiny models
- [ ] A/B test against current system

### Phase 5: Production Integration (Week 7-8)
- [ ] Benchmark latency improvements
- [ ] Integration with LangGraph
- [ ] Fallback strategies
- [ ] Monitoring and evaluation

---

## Key Concepts to Learn

### LoRA (Low-Rank Adaptation)
- **Rank**: Default 32, higher for complex tasks (128 for distillation)
- **Learning Rate**: ~10x higher than full fine-tuning
- **Parameters**: Only trains ~1% of model parameters

### Model Sizes for NPC Nodes
- **Llama-3.2-1B**: Ultra-fast, good for simple classification
- **Llama-3.2-3B**: Balance of speed and capability
- **Qwen-2.5-0.5B**: Smallest option for very simple tasks

### Training Approaches
1. **Supervised Fine-Tuning (SFT)**: For classification, routing
2. **Distillation**: Transfer knowledge from your current strong LLMs
3. **RL (optional)**: For complex decision-making nodes

---

## Experiment Structure

Each experiment will follow this structure:
```
npc-learning-experiments/
├── 01-sentiment-classification/
│   ├── train.py
│   ├── data/
│   │   └── sentiment_examples.jsonl
│   ├── eval.py
│   └── results/
├── 02-routing/
├── 03-validation/
└── ...
```

---

## Success Metrics

For each fine-tuned node, we'll measure:
1. **Latency**: Target <100ms vs current LLM calls
2. **Accuracy**: Must match or exceed current system
3. **Cost**: Training cost + inference cost reduction
4. **Reliability**: Failure rate, edge case handling

---

## Next Steps

1. Run `sl_basic.py` to understand the training loop
2. Create synthetic sentiment analysis dataset
3. Train first tiny model
4. Benchmark and iterate

---

## Resources

- **Tinker Cookbook Docs**: `README.md` in root
- **Example Data**: `/example-data/conversations.jsonl`
- **Key Files**:
  - `tinker_cookbook/renderers.py`: Data formatting
  - `tinker_cookbook/supervised/train.py`: Training loop
  - `tinker_cookbook/recipes/prompt_distillation/`: Relevant for our use case
