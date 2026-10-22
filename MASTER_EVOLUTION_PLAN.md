# MASTER EVOLUTION PLAN — UARS Sovereign Terminal

## Vision
To transform the UARS Sovereign Terminal from a keyword-reactive system into a semantically-aware autonomous interface that enforces absolute non-repetition and dynamic mutation of AI responses.

## Capability Levels
- **L0: Keyword Reactive** (Current) - Simple `strstr` and `in` checks for "repeat", "loop", etc.
- **L1: Semantic Awareness** - Use of embeddings or LLM-based intent analysis to detect repetition.
- **L2: Mutation Engine** - Implementation of the "AI must mutate" doctrine via dynamic prompt injection based on repetition depth.
- **L3: Sovereign Kernel** - Moving semantic detection into a hardened C-kernel shim with local embedding support.
- **L4: Self-Evolving Interface** - UI/UX that adapts based on the detected "mutation" state of the conversation.

## Evolutionary Roadmap

### Phase 1: Semantic Transition (L0 $\rightarrow$ L1)
- [ ] **Intent Analysis**: Replace keyword checks in `uars_internal.py` with a semantic similarity check against session history.
- [ ] **Repetition Buffer**: Implement a sliding window of recent user intents.
- [ ] **Mutation Trigger**: Formalize the trigger for "Mutation" based on a similarity threshold.

### Phase 2: Mutation Logic (L1 $\rightarrow$ L2)
- [ ] **Lexical Diversification**: Create a library of mutation strategies (e.g., changing persona, shifting perspective, increasing depth).
- [ ] **Dynamic Prompting**: Inject specific mutation instructions into the LLM prompt when repetition is detected.

### Phase 3: Kernel Hardening (L2 $\rightarrow$ L3)
- [ ] **C-Shim Integration**: Move the semantic trigger into `uars_kernel.c` using a lightweight C-based similarity library.
- [ ] **Secure Intent Store**: Implement a protected memory region for storing the intent buffer.

## Tracking
- **Current Level**: 0
- **Next Objective**: Phase 1 - Semantic Transition (Issue #11).
