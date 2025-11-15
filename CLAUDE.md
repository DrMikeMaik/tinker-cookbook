# CLAUDE.md - Project Context & Memory

> **Purpose**: This file maintains context across different Claude Code sessions.
> Any Claude instance working on this repository should read this file first!

---

## 🎯 Project Goals

This is a **forked repository** of `tinker-cookbook` for learning purposes. The user wants to:

1. **Learn how to use tinker-cookbook** for fine-tuning small LLMs
2. **Apply this knowledge to a specific use case**: LLM-powered NPCs

### The User's Use Case: NPC System

The user has an **advanced LangGraph-based NPC system** with:
- **Main flow**: Powered by strong LLMs (GPT-4, Claude, etc.)
- **Smaller nodes**: Currently using smaller general-purpose LLMs for:
  - Validation
  - Routing
  - Retries
  - Controlling dynamic parameters
  - Sentiment analysis
  - Other auxiliary tasks

**The Hypothesis**: These smaller nodes can be replaced with fine-tuned tiny models (Llama-3.2-1B, Qwen-2.5-0.5B, etc.) or a single tiny model with **multiple LoRA adapters** to:
- ✅ Reduce latency (from seconds to milliseconds)
- ✅ Lower costs (tiny models are nearly free)
- ✅ Maintain or improve accuracy (specialized > general)

---

## 📂 Repository Organization

### Original Repository Code
- `/home/user/tinker-cookbook/tinker_cookbook/` - Original SDK and recipes
- `/home/user/tinker-cookbook/example-data/` - Sample datasets
- `/home/user/tinker-cookbook/README.md` - Original documentation

**IMPORTANT**: Do NOT modify the original repository code unless absolutely necessary!

### Learning Workspace
- `/home/user/tinker-cookbook/npc-learning-experiments/` - **All learning code goes here**

This separation ensures:
- No confusion between original code and experiments
- Clean workspace for iteration
- Easy to contribute improvements back upstream if desired

---

## ✅ What Has Been Accomplished

### Session 1: Initial Setup & Core Experiments (2025-11-13)

**Explored the Repository**:
- ✅ Understood tinker-cookbook structure and purpose
- ✅ Identified key files: `renderers.py`, `hyperparam_utils.py`, training loops
- ✅ Reviewed example recipes: `sl_basic.py`, `rl_basic.py`, `prompt_distillation/`
- ✅ Learned about LoRA configuration (rank, learning rates)

**Created Learning Workspace**:
- ✅ `/npc-learning-experiments/` folder structure
- ✅ `LEARNING_PLAN.md` - 8-week roadmap from basics to production
- ✅ `README.md` - Overview of experiments and NPC use case

**Built Three Core Experiments** (ready to run):

1. **Experiment 01: Sentiment Classification** (`01-sentiment-classification/`)
   - ✅ Training script (`train.py`) based on `sl_basic.py`
   - ✅ 30 NPC dialogue examples in JSONL format
   - ✅ 3-way classification: POSITIVE/NEGATIVE/NEUTRAL
   - ✅ Configured for Llama-3.2-1B with LoRA (rank=32, lr=2e-4)
   - **Note**: User preferred routing and jailbreak detection, but this remains as learning reference

2. **Experiment 02: Routing Node** (`02-routing-node/`) ⭐ **PRIORITY**
   - ✅ Training script for 4-way routing classification
   - ✅ 48 training examples (RAG / game_state / both / neither)
   - ✅ Structured JSON output format
   - ✅ Directly applicable to LangGraph flow
   - **Expected**: 20-40x faster than LLM API, perfect JSON compliance

3. **Experiment 03: Jailbreak Detection** (`03-jailbreak-detection/`) ⭐ **CRITICAL**
   - ✅ Training script for binary jailbreak classification
   - ✅ 48 training examples (24 safe, 24 jailbreak attempts)
   - ✅ First line of defense for production NPC safety
   - ✅ Detects prompt injection, role manipulation, command injection
   - **Expected**: 99%+ accuracy, <50ms detection time

**Git Operations**:
- ✅ Branch: `claude/learning-tool-exploration-011CV5jpQncxAkeGr6dLZ3tE`
- ✅ Committed all experiments separately
- ✅ Pushed to remote

---

## 🚧 Current Status

**Phase**: Learning & Experimentation (Week 1 of 8-week plan)

**Ready to Execute**:
- ✅ Three experiments fully set up and ready to run
- ✅ Training data created for all experiments
- ✅ Training scripts configured and documented
- ✅ Focus shifted from sentiment to routing + jailbreak (better production value)

**Recommended Execution Order**:
1. **Routing Node** (Experiment 02) - Most impactful for LangGraph
2. **Jailbreak Detection** (Experiment 03) - Critical for safety
3. **Sentiment** (Experiment 01) - Optional learning reference

**Next Immediate Steps**:
1. User will run experiments and observe training
2. Analyze training metrics (loss, accuracy)
3. Test inference latency and JSON format compliance
4. Compare results with current LLM approach
5. Iterate on training data based on results

---

## 📋 Next Steps & Roadmap

### Immediate (This Week)
- [ ] Run `02-routing-node/train.py` (priority experiment)
- [ ] Run `03-jailbreak-detection/train.py` (critical for safety)
- [ ] Analyze training results for both experiments
- [ ] Test inference latency and JSON format compliance
- [ ] Document findings and accuracy metrics

### Short-term (Weeks 2-3)
- [ ] Collect real routing decisions from user's LangGraph
- [ ] Collect real jailbreak attempts from production logs
- [ ] Retrain with real data
- [ ] Add reasoning output to routing (optional step 2)
- [ ] Compare different model sizes (1B vs 3B)
- [ ] Experiment 4: Language detection (English yes/no)

### Medium-term (Weeks 4-6)
- [ ] Multi-LoRA approach: Single base model with multiple adapters
- [ ] Measure LoRA swapping overhead
- [ ] Distillation from user's current strong LLMs
- [ ] Prompt internalization experiments

### Long-term (Weeks 7-8)
- [ ] Production integration with LangGraph
- [ ] Comprehensive benchmarking (latency, accuracy, cost)
- [ ] A/B testing against current system
- [ ] Fallback strategies and monitoring

---

## 🔑 Key Technical Insights

### About tinker-cookbook
- **Purpose**: SDK for fine-tuning LLMs via cloud training API
- **Core Feature**: LoRA-based efficient training
- **Data Format**: JSONL with `{"messages": [{"role": "...", "content": "..."}, ...]}`
- **Training**: Async-first, automatic checkpointing, distributed training handled by API

### LoRA Configuration Rules
- **Learning Rate**: ~10x higher than full fine-tuning (typically 1e-4 to 2e-4)
- **Rank**: Default 32, higher for complex tasks (128 for distillation)
- **Rank vs LR**: Independent! Changing rank doesn't require LR adjustment
- **Parameters**: Only trains ~1% of model parameters

### Model Recommendations for NPC Tasks
| Task Type | Recommended Model | Expected Latency | Difficulty |
|-----------|------------------|------------------|------------|
| Simple classification | Llama-3.2-1B | <100ms | Easy |
| Multi-class routing | Llama-3.2-3B | <200ms | Easy |
| Complex validation | Qwen-2.5-3B | <300ms | Medium |
| Multi-task (LoRA) | Llama-3.2-1B + adapters | <150ms | Medium |

### Important Files in Original Repo
- `tinker_cookbook/renderers.py` - Data formatting (chat → tokens)
- `tinker_cookbook/supervised/train.py` - SFT training loop
- `tinker_cookbook/hyperparam_utils.py` - LoRA hyperparameter calculation
- `tinker_cookbook/recipes/sl_basic.py` - **Start here for learning**
- `tinker_cookbook/recipes/prompt_distillation/` - Relevant for NPC use case

---

## 💡 Important Context & Decisions

### Why Separate Workspace?
The user explicitly requested keeping learning code separate from the original repository to avoid confusion. All experiments go in `/npc-learning-experiments/`.

### Why Focus on Routing & Jailbreak Detection?
**User feedback**: Sentiment was not the best first choice. Instead, focus on:

**Routing Node** (Experiment 02):
- 4-way classification directly applicable to LangGraph flow
- Structured JSON output teaches format compliance
- Most impactful for reducing latency in production
- Multi-class classification is better learning than binary

**Jailbreak Detection** (Experiment 03):
- Critical for production NPC safety
- Binary classification (easiest, highest accuracy)
- Prevents PR disasters and safety issues
- Can save costs by filtering bad requests early

**Sentiment Classification** (Experiment 01):
- Kept as reference for learning basics
- 3-way classification example
- Less critical for user's immediate needs

### Why LoRA?
- User wants to potentially use **single model with multiple LoRA adapters**
- Much more efficient than training multiple full models
- Fast adapter swapping at inference time
- Standard approach in tinker-cookbook

### Data Strategy
- Phase 1: Use synthetic/example data for learning
- Phase 2: Collect real NPC dialogue logs from user's production system
- Phase 3: Iterative improvement with real data

---

## 🤝 Working with This Repository

### For Future Claude Instances

**When starting a new session**:
1. Read this file first (`CLAUDE.md`)
2. Check `npc-learning-experiments/LEARNING_PLAN.md` for detailed roadmap
3. Review the most recent experiment folder for current work
4. Check git log to see latest progress

**When creating new experiments**:
1. Create new folder in `npc-learning-experiments/XX-experiment-name/`
2. Include: `train.py`, `data/`, `README.md`, (optionally) `eval.py`
3. Update this file's "What Has Been Accomplished" section
4. Commit with descriptive message

**When helping the user**:
1. Remember: They want to learn AND apply to NPC use case
2. Explain concepts clearly (they're learning fine-tuning)
3. Connect examples to their LangGraph nodes
4. Measure and compare latency/accuracy/cost

---

## 📊 Success Metrics

For each fine-tuned node replacement, we track:
1. **Latency**: Target <100ms (vs 1-2s for API calls)
2. **Accuracy**: Must match or exceed current system
3. **Cost**: Training cost + inference savings
4. **Reliability**: Failure rates, edge case handling

---

## 🐛 Known Issues & Limitations

None yet - project just started!

---

## 📝 Notes for Continuity

- **Branch**: `claude/learning-tool-exploration-011CV5jpQncxAkeGr6dLZ3tE`
- **Python Environment**: Assumes `tinker` package is installed
- **API Access**: User has access to Tinker training API
- **Data Privacy**: Use synthetic data for learning; real game data comes later

---

## 🔄 Update History

- **2025-11-13 (Session 1)**: Initial project setup
  - Created learning workspace structure
  - Built sentiment classification experiment (01)
  - User feedback: Routing and jailbreak detection more valuable
  - Built routing node experiment (02) - **PRIORITY**
  - Built jailbreak detection experiment (03) - **CRITICAL**
  - All three experiments ready to run
  - Updated focus to structured output and production-critical tasks

---

**Last Updated**: 2025-11-13
**Last Updated By**: Claude (Session 1)
**Next Review**: After user runs routing and jailbreak experiments
