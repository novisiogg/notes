# 🗺️ Master Learning Roadmap

---

## ✅ Phase 0: Python Mastery & Best Practices

*Focus: Technical fluency and professional standards for Python codebases.*

### 0.1 Python Language Deep Dive
* **Decorators**: Creating and applying, with and without arguments.
* **Context Managers**: Using `with`, and writing custom context managers (`__enter__`, `__exit__`).
* **Exceptions**: Catching, raising, creating custom exceptions, using `finally`, and robust error handling patterns.
* **Iterables, Generators & Comprehensions**: How generators save memory, generator expressions, custom iterators (`__iter__`, `__next__`).
* **Meta-programming & Reflection**: Inspecting objects with `inspect`, `getattr`, dynamic class creation.

### 0.2 Typing, Packaging & Testing
* **Type Hints & Static Analysis**: Using the `typing` module, `mypy` for static checks, runtime validation.
* **Packaging & Distribution**: Writing `pyproject.toml`, building wheels, publishing to PyPI.
* **Unit Testing & Mocking**: `unittest`, `pytest`, fixtures, mocking, code coverage.
* **Documentation**: Writing docstrings (PEP 257), generating reference docs (Sphinx/pdoc).
* **Linting & Formatting**: Enforcing with `flake8`, `black`, `isort`.

### 0.3 Performance, Concurrency, and Debugging
* **Profiling & Optimization**: `cProfile`, `timeit`, identifying bottlenecks.
* **Debugging Tools**: Using `pdb`, effective breakpoints, IDE debuggers.
* **Concurrency Patterns**: When to use threads, processes, asyncio, and `concurrent.futures`.
* **Environment Management**: Masking secrets with `.env` files.
* **Containerization**: Using **Docker** to isolate and reproduce execution environments.
* **Portability**: Building for Linux, Mac, and Windows.

---

## ✅ Phase 1 & 2: Core Infrastructure (Completed)
* **OOP Foundations**: Transitioned to Class-based architecture.
* **Data Persistence**: Implemented JSON-based state saving.
* **The Librarian Pattern**: Created a dedicated `MemoryManager` to handle Disk I/O.
* **System Control**: Mastered the `os` and `subprocess` modules to allow the agent to act on the computer.

---

## ✅ Phase 3: The Brain & Memory (Completed)
* **3.1 Local Inference**: Hooked up **Ollama (Llama 3.1)** via local socket communication.
* **3.2 Context Loops**: Implemented history-passing to allow the AI to "remember" previous turns.
* **3.3 Modular Persistence**: Decoupled storage logic from interface logic for scalability.
* **3.4 Factory Resets**: Created logic to clear `history` while preserving `metadata`.

---

## 💻 Phase 4: How Computers Really Work — From Silicon to Software

*Focus: The journey from transistors to running programs. Learn what the CPU actually does, how memory is managed, what happens when you run a binary, and how the OS coordinates everything. This is foundational knowledge that everything else builds on.*

### 4.0 From Transistors to Logic Gates
* **The Basics**: How transistors act as switches; NAND/NOR as universal gates.
* **Binary Arithmetic**: Addition, subtraction in binary; signed integers (two's complement); overflow and carry flags.
* **Boolean Algebra**: Simplifying logic circuits; how a 1-bit and then 4-bit ALU is built from gates.
* **Clock Cycles**: What a clock signal does; synchronous vs. asynchronous circuits; the fetch-decode-execute cycle at the hardware level.
* **Deeper**: Latches, flip-flops, and registers — how the CPU "remembers" a single bit.

### 4.1 CPU Architecture in Depth
* **Registers**: General-purpose (RAX, RBX...), the instruction pointer (RIP), stack pointer (RSP), and flags register.
* **The ALU & FPU**: Integer vs. floating-point operations; why 0.1 + 0.2 ≠ 0.3.
* **Pipelining**: How CPUs overlap fetch, decode, execute, write-back stages; hazards and stalls.
* **Cache Hierarchy**: L1/L2/L3 caches; cache lines, cache hits/misses, and why cache locality matters for performance.
* **Branch Prediction**: How CPUs guess the next instruction and what happens when they're wrong (Spectre/Meltdown as a real-world consequence).
* **SIMD & Vectorization**: How CPUs process multiple data points in parallel (SSE, AVX); why this matters enormously for ML.

### 4.2 Assembly Language — Reading the Machine
* **Why Assembly**: Understanding what the compiler actually produces; reading disassembly output.
* **x86-64 Basics**: MOV, ADD, SUB, CMP, JMP, CALL, RET — the essential instructions.
* **The Stack in Assembly**: How function calls push/pop stack frames; the calling convention (who saves which registers).
* **System Calls**: How assembly talks to the OS via `syscall`; writing a "Hello, World" without libc.
* **Tool**: Disassemble a compiled Python extension or C program with `objdump` or `Ghidra`; read and annotate the output.
* **Deeper**: Understanding how compilers translate `if`, `for`, and function calls into assembly.

### 4.3 How Compiling Works — From Code to Binary
* **The Full Pipeline**: Source → Preprocessor → Compiler (IR) → Assembler → Linker → Executable.
* **Intermediate Representations**: What LLVM IR looks like; how optimizations (dead code elimination, inlining) happen at this stage.
* **Object Files & Symbols**: What `.o` files contain; the symbol table; how `nm` and `readelf` reveal a binary's internals.
* **Linking**: Static vs. dynamic linking; shared libraries (`.so`, `.dll`); how the dynamic linker resolves symbols at runtime.
* **The ELF Format**: Sections (`.text`, `.data`, `.bss`, `.rodata`); how the OS loader maps an ELF binary into memory.
* **Interpreted vs. Compiled**: Where Python fits — bytecode, the CPython VM, and how `.pyc` files work.
* **Tool**: Compile a C program at different optimization levels (`-O0`, `-O2`, `-O3`) and compare the assembly output with `godbolt.org`.

### 4.4 Processes, Memory, and the OS Kernel
* **Virtual Memory**: Every process thinks it owns the whole address space; page tables, TLBs, and how the MMU translates virtual to physical.
* **Memory Layout of a Process**: Stack region, heap region, code segment, data segment, memory-mapped files — what lives where and why.
* **The Kernel / User Space Boundary**: Ring 0 vs. Ring 3; why user code can't directly touch hardware; the role of system calls as the gateway.
* **Process Creation**: `fork()` and `exec()` — how a shell spawns processes; copy-on-write pages.
* **Signals**: SIGKILL, SIGTERM, SIGSEGV — how the OS tells a process something happened.
* **File Descriptors**: Everything is a file; stdin/stdout/stderr; pipes; how `|` works at the OS level.
* **Scheduler**: Preemptive multitasking; time slices; priority and nice values; the run queue.
* **Deeper**: Context switching — exactly what the OS saves and restores when it swaps processes.

### 4.5 Compiled vs. Interpreted Languages — The Full Picture
* **JIT Compilation**: How PyPy, V8 (JavaScript), and the JVM compile hot code paths at runtime.
* **Garbage Collection Deep Dive**: Reference counting (CPython), mark-and-sweep, generational GC — trade-offs in latency and throughput.
* **Why C is Fast**: No GC, manual memory, direct pointer arithmetic, no boxing of primitives.
* **Why Python is Slow (and What to Do About It)**: The GIL, interpreter overhead, boxing; using Cython, Numba, or writing C extensions.

### 4.6 Operating Systems & Process Control
* **Understand**: Processes, threads vs. coroutines, scheduling, and memory management.
* **Mastery Upgrade**: **Stack vs. Heap Memory**; knowing exactly how the computer manages variable memory and garbage collection.
* **Tool**: Writing a script to monitor real-time process resource usage (CPU, RAM).

### 4.7 Computer Architecture
* **Understand**: Bits, bytes, binary/hex, floating point representations, and overflow.
* **Read**: Basics of assembly language (x86 or ARM) to understand the CPU's instruction set.

### 4.8 Networks, Encryption, and Protocols
* **Understand**: DNS, routing basics, and the differences between TCP and UDP.
* **Experiment**: Building a minimal Python chat server with sockets and adding SSL for encryption.

### 4.9 Mathematics for AI (First Principles)
* **Linear Algebra**: Vectors, matrices, and tensor operations.
* **Calculus**: Derivatives, gradients, and optimization via gradient descent.
* **Probability**: Bayesian reasoning, softmax functions, and entropy.


---

## 🌐 Phase 5: Networking & External Senses

*Focus: How computers ask the world for information and communicate at the bytes-and-bits level.*

### 5.0 The Request/Response Cycle
* **The Detail**: Anatomy of a **Packet**; learning HTTP Methods (`GET`, `POST`), **Headers**, and **Status Codes** (200, 404, 500).
* **Beyond the API**: **TCP/IP Sockets**, Handshakes, and connection teardown.
* **The Concept**: **Serialization vs. Deserialization**; turning Python Dicts into JSON ("suitcases").
* **Mastery Upgrade**: The **OSI Model** (Application to Physical layers) and **DNS Resolution** (the mechanics of turning names into IPs).
* **Deeper**: **Endianness** (Big-endian vs. Little-endian) and how data travels the wire.
* **Tools**: `requests` library, plus direct use of Python's `socket` and `asyncio` for bare-metal networking.

### 5.1 API Integration & Tooling
* **The Detail**: Building a `tools.py` module to fetch real-world data like Weather, News, or Stocks.
* **The Concept**: **The API Handshake**; learning to read documentation, handle authentication, rate limits, and failures.
* **Foundations**: Understanding REST vs. GraphQL, RPC, and WebSockets.
* **Deeper**: Implementing a simple local REST API **server**.
* **Tools**: `requests`, `FastAPI`, or `Flask`.

### 5.2 Asynchronous Execution (`asyncio`)
* **The Detail**: Moving from sequential to concurrent code execution.
* **The Concept**: Using `async/await` so the AI doesn't "freeze" during I/O operations.
* **Mastery Upgrade**: The **Python GIL (Global Interpreter Lock)**; understanding the trade-offs between Threading and Multiprocessing for true parallelism.
* **Beyond**: **Event loops** and the "reactor pattern".
* 
### 5.3 Physical & Data Link Layer (OSI Layers 1–2)
* **Layer 1 — Physical**: How bits become electrical signals, radio waves, or light pulses; encoding schemes (NRZ, Manchester); cables, fiber, Wi-Fi (802.11) basics.
* **Layer 2 — Data Link**: MAC addresses; Ethernet frames (header, payload, FCS); how switches build MAC tables and forward frames.
* **ARP (Address Resolution Protocol)**: How a machine discovers the MAC address for a given IP; the ARP table; why ARP has no authentication (and why that matters for security).
* **VLANs**: Logically segmenting a physical network; 802.1Q tagging; why VLANs aren't a security boundary by themselves.
* **Wireless Specifics**: SSID, BSSID, channels, 802.11 association process; WPA2/WPA3 handshake.

### 5.4 IP & Routing (OSI Layer 3)
* **IPv4 in Detail**: Packet header fields (TTL, TOS/DSCP, flags, fragment offset); what each field actually does.
* **Subnetting Mastery**: CIDR notation; calculating network address, broadcast, and host range; why `/30` exists; designing a subnet scheme.
* **IPv6**: Why it exists; address format; types (link-local, global unicast, multicast); dual-stack operation.
* **Routing**: How routers build forwarding tables; static routes vs. dynamic routing protocols.
* **Dynamic Routing Protocols**: RIP (distance vector), OSPF (link-state), BGP (path vector) — the protocol that holds the internet together.
* **NAT (Network Address Translation)**: How your home router maps many private IPs to one public IP; port address translation (PAT); why NAT breaks end-to-end connectivity.
* **ICMP**: Ping and traceroute under the hood; how TTL expiry reveals the path of a packet.

### 5.5 Transport Layer — TCP & UDP (OSI Layer 4)
* **TCP Deep Dive**: The three-way handshake (SYN, SYN-ACK, ACK) and four-way teardown in detail; sequence numbers and acknowledgement numbers; sliding window and flow control; congestion control (slow start, AIMD, CUBIC).
* **TCP States**: SYN_SENT, ESTABLISHED, TIME_WAIT, CLOSE_WAIT — reading a `netstat` or `ss` output and understanding what every state means.
* **UDP**: Why it exists; checksum only; use cases (DNS, DHCP, gaming, video streaming, QUIC).
* **Ports**: Well-known (0–1023), registered (1024–49151), ephemeral; how the OS demultiplexes incoming packets to the right process.
* **Deeper**: TCP segment retransmission; Nagle's algorithm; `SO_REUSEADDR` and what it does.

### 5.6 DNS — The Internet's Phone Book
* **Full Resolution Walk**: Recursive resolver → Root nameserver → TLD nameserver → Authoritative nameserver; what each hop does.
* **Record Types**: A, AAAA, CNAME, MX, TXT, NS, PTR, SOA — what each is used for and when.
* **TTL & Caching**: How long resolvers cache answers; why low TTL matters during a migration.
* **DNS Security**: DNSSEC (signing records); DNS over HTTPS (DoH) and DNS over TLS (DoT).
* **DNS as an Attack Vector**: Zone transfers (`AXFR`); DNS amplification DDoS; DNS tunneling (exfiltrating data through DNS queries).
* **Tool**: Use `dig`, `nslookup`, and `Wireshark` to trace every step of a DNS resolution.

### 5.7 Application Layer Protocols (OSI Layer 7)
* **HTTP/1.1 vs. HTTP/2 vs. HTTP/3**: Persistent connections; multiplexing; header compression (HPACK); QUIC (HTTP/3 over UDP).
* **HTTPS / TLS**: Full TLS 1.3 handshake step-by-step; cipher suites; certificate pinning; HSTS.
* **SMTP, IMAP, POP3**: How email actually moves between servers; STARTTLS; MIME encoding; why email is inherently insecure.
* **SSH**: Public key authentication; the Diffie-Hellman key exchange inside an SSH session; port forwarding and tunneling.
* **FTP vs. SFTP vs. SCP**: Active vs. passive FTP; why plain FTP is dangerous; secure alternatives.
* **DHCP**: The DORA process (Discover, Offer, Request, Acknowledge); lease times; DHCP starvation attacks.

### 5.8 Network Architecture & Design
* **LAN / WAN / MAN**: The physical and logical scope of networks.
* **Firewalls**: Packet filtering, stateful inspection, application-layer gateways; rule ordering and default-deny.
* **DMZ (Demilitarized Zone)**: Why public-facing servers live in their own segment.
* **Load Balancers**: Layer 4 vs. Layer 7; round-robin, least-connections; health checks; sticky sessions.
* **CDNs (Content Delivery Networks)**: Anycast routing; edge caching; how Cloudflare works.
* **Software-Defined Networking (SDN)**: Separating the control plane from the data plane; OpenFlow.
* **VPNs in Depth**: IPsec (IKEv2, ESP, AH); WireGuard (modern, minimal protocol); OpenVPN; split tunneling.

### 5.9 Network Monitoring & Troubleshooting
* **The Toolbox**: `ping`, `traceroute`/`tracert`, `mtr`, `netstat`/`ss`, `ip`, `tcpdump`, `Wireshark`, `nmap`.
* **Reading Packet Captures**: Filtering in Wireshark; identifying a TCP handshake, a DNS query, and a TLS hello in a pcap.
* **Network Performance**: Bandwidth vs. latency vs. throughput; `iperf3`; jitter and its impact on real-time protocols.
* **Logging & Alerting**: Syslog; how network devices export logs; basic SIEM concepts (Splunk, ELK stack).

---

## 🔊 Phase 6: The Physical Senses (Voice, Audio, and Beyond)

*Focus: Digital Signal Processing, Audio Buffering, and the first steps in perception.*

### 6.1 Text-to-Speech (TTS)
* **The Detail**: Bitrates, sample rates, and frequency.
* **The Concept**: **Multi-threading**; playing audio while the AI processes its next thought.
* **Mastery Upgrade**: **PCM (Pulse Code Modulation)** and **Sample Interleaving** (how stereo data is packed in memory).
* **Deeper**: **Waveform generation** and basic signal processing including Fourier transforms and filtering.
* **Tools**: `gTTS`, `edge-tts`, `Piper`, and exploration of `PyDub` or `librosa`.

### 6.2 Speech-to-Text (STT)
* **The Detail**: Turning analog sound into digital data; ADCs (Analog/Digital Converters) basics.
* **The Concept**: **VAD (Voice Activity Detection)** and setting silence thresholds.
* **Deeper**: **STFT** (Short-Time Fourier Transform), fundamentals of MFCCs, and spectrograms.
* **Tools**: `Whisper` (Local), `SpeechRecognition`, and visualizing audio waveforms.

### 6.3 Sensing Beyond Audio (Optional/Advanced)
* **Vision**: Understanding camera input, image matrices, and basics of computer vision with OpenCV.
* **Sensors**: Learning about basic analog/digital sensor interfacing for microphones, cameras, and IMUs.

---

## 🦾 Phase 7: AI Fundamentals & Machine Learning Foundations

*Focus: Classic ML, core math, hands-on with data, deep learning concepts, and evaluation.*

### 7.1 Data and ML Problem Types
* **Supervised & Unsupervised Learning**: Classification, regression, clustering.
* **Data Preparation**: Cleaning, splitting (train/test/validation), handling missing values, feature scaling.
* **Exploring Data**: `pandas` basics, statistical summaries, visualizations (`matplotlib`, `seaborn`).

### 7.2 Classic Algorithms & Evaluation
* **Core Algorithms**: Linear regression, logistic regression, k-NN, decision trees, k-means.
* **Evaluation Metrics**: Accuracy, precision, recall, F1, ROC/AUC, confusion matrices, cross-validation.
* **Overfitting / Underfitting**: Causes and cures.

### 7.3 Probability & Statistics for AI
* **Probability Distributions**: Gaussian, categorical, Bernoulli.
* **Bayesian Inference**: Basics and when to use.
* **Randomness and Reproducibility**: Seeding, random states, experiment tracking.

### 7.4 Mathematics for AI (First Principles)
* **Linear Algebra**: Vectors, matrices, and tensor operations.
* **Calculus**: Derivatives, gradients, and optimization via gradient descent.
* **Probability**: Bayesian reasoning, softmax functions, and entropy.

### 7.5 Neural Networks & Deep Learning Basics
* **NN Anatomy**: Layers, weights, activations (sigmoid, ReLU, softmax).
* **Backpropagation & Gradient Descent**: How models learn.
* **Regularization**: Dropout, L1/L2 penalties, batch normalization.
* **Training Routines**: SGD, Adam optimizers, learning curves.
* **Intro to Architectures**: CNN, RNN/LSTM/GRU (basic concepts, use cases).
* **Frameworks**: `PyTorch` or `TensorFlow` first models (from data to prediction).

### 7.6 Model Management & Reproducibility
* **Logging & Experiment Tracking**: Using MLflow, WandB, or manual strategies.
* **Versioning & Deployment**: Saving models, inference basics, environment capture.

### 7.7 AI Ethics, Bias, Explainability
* **Bias & Fairness**: Recognizing, quantifying, and mitigating.
* **Explainability**: Feature importances, SHAP, LIME basics.
* **Data Privacy**: Handling sensitive data, privacy-preserving approaches.

---

## 🔩 Phase 8: Transformer Architecture & How Modern LLMs Actually Work

*Focus: Understand the specific architecture that powers GPT, Claude, Llama, and every major modern AI — from the attention mechanism at the math level, to how tokens become predictions, to how training works at scale. This is the phase that turns "I use AI" into "I understand AI."*

### 8.1 The Attention Mechanism — The Core Idea
* **What Attention Solves**: Why RNNs struggled with long sequences; the vanishing gradient problem and why attention bypasses it.
* **Scaled Dot-Product Attention**: Q (Query), K (Key), V (Value) matrices — where they come from and what they represent geometrically.
* **The Math Step by Step**: `Attention(Q, K, V) = softmax(QKᵀ / √dₖ) · V` — work through this formula with small concrete numbers until it's intuitive.
* **Why Scaling by √dₖ**: The dot-product magnitude problem in high dimensions; what happens without scaling.
* **Attention as Soft Lookup**: Framing attention as a differentiable dictionary — every query gets a weighted blend of all values.

### 8.2 Multi-Head Attention
* **Why Multiple Heads**: Each head can attend to different aspects of the input simultaneously (syntax, semantics, coreference, etc.).
* **The Mechanics**: Splitting into heads, independent attention per head, concatenation, and the final projection matrix.
* **What Heads Learn**: Empirical findings — induction heads, positional heads, syntactic heads; how interpretability research probes them.
* **Computational Cost**: How attention scales O(n²) with sequence length; why this is the bottleneck for long contexts.

### 8.3 The Full Transformer Block
* **Layer Normalization**: Why LayerNorm instead of BatchNorm; Pre-LN vs. Post-LN and training stability.
* **Feed-Forward Sublayer**: The two-layer MLP inside every transformer block; the expansion ratio (4x); what it stores vs. what attention stores.
* **Residual (Skip) Connections**: Why they enable deep networks to train; the "residual stream" framing.
* **Putting It Together**: One full transformer block as a diagram and in code (`PyTorch`).

### 8.4 Positional Encoding
* **Why Transformers Are Position-Blind by Default**: Attention has no notion of order; why this matters.
* **Sinusoidal Encoding (Original)**: The sine/cosine formulas; why they generalize to unseen lengths.
* **Learned Positional Embeddings**: What GPT-2 uses; the trade-off vs. sinusoidal.
* **Rotary Positional Embedding (RoPE)**: The modern standard (used in Llama, Mistral, GPT-NeoX); how it encodes relative position directly into the attention computation.
* **ALiBi and Other Variants**: Length extrapolation and why it's hard.

### 8.5 Tokenization — From Text to Numbers
* **Why Tokenization Exists**: Models operate on integers, not characters or words.
* **Byte-Pair Encoding (BPE)**: The algorithm step-by-step; how a vocabulary is built from a corpus; merge rules.
* **WordPiece & SentencePiece**: Variants used by BERT and T5; key differences.
* **The Vocabulary and Embedding Matrix**: How token IDs map to vectors; why the embedding and unembedding matrices are sometimes tied.
* **Tokenization Quirks**: Why "1+1=2" tokenizes strangely; why some languages are far more "expensive" than English; the impact on model arithmetic.
* **Tool**: Use the `tiktoken` library or Hugging Face `tokenizers` to inspect tokenization of different inputs.

### 8.6 The Decoder-Only Architecture (GPT-Style)
* **Causal (Masked) Self-Attention**: The causal mask — why future tokens are hidden during training; the upper-triangular mask matrix.
* **Autoregressive Generation**: How a model generates one token at a time by feeding its own output back in.
* **The Full Forward Pass**: Embedding → N × Transformer Blocks → LayerNorm → Unembedding → Logits → Softmax → Probability distribution.
* **The Training Objective**: Next-token prediction (cross-entropy loss); why this simple objective produces surprisingly general capabilities.
* **KV Cache**: How inference is accelerated by caching Key and Value matrices; why it matters for latency and memory.

### 8.7 Encoder-Only & Encoder-Decoder Architectures
* **BERT (Encoder-Only)**: Bidirectional attention; masked language modeling; why it's better for classification/retrieval than generation.
* **T5 / BART (Encoder-Decoder)**: Cross-attention between encoder and decoder; use cases (translation, summarization).
* **When to Use Which**: The practical decision tree — generation → decoder-only; understanding/classification → encoder-only; seq2seq → encoder-decoder.

### 8.8 Training at Scale
* **Pre-training**: What it means to train on trillions of tokens; data pipelines, deduplication, quality filtering.
* **The Loss Landscape**: Why transformers are surprisingly trainable; the role of learning rate warmup and cosine decay.
* **Scaling Laws (Chinchilla)**: The relationship between model size, dataset size, and compute; what "compute-optimal" training means.
* **Mixed Precision Training**: FP16 / BF16 vs. FP32; gradient scaling; why BF16 became the standard.
* **Distributed Training**: Data parallelism, tensor parallelism, pipeline parallelism — how models too large to fit on one GPU are trained.

### 8.9 Fine-tuning & Alignment
* **Supervised Fine-Tuning (SFT)**: Training on instruction-response pairs to shift behavior; the risk of "catastrophic forgetting."
* **RLHF (Reinforcement Learning from Human Feedback)**: The reward model; PPO training loop; why alignment is non-trivial.
* **DPO (Direct Preference Optimization)**: The modern alternative to RLHF; why it's simpler and often equally effective.
* **LoRA (Low-Rank Adaptation)**: Fine-tuning large models cheaply by injecting small trainable matrices; why rank matters; `peft` library.
* **QLoRA**: Quantized LoRA — fine-tuning a 70B model on a single consumer GPU.

### 8.10 Inference Optimization & Quantization
* **Quantization Basics**: INT8, INT4, GGUF formats; the accuracy vs. size trade-off.
* **`llama.cpp` Under the Hood**: How it runs quantized models on CPU/GPU; the GGUF format; Q4_K_M vs. Q8_0.
* **Speculative Decoding**: Using a small draft model to propose tokens; the large model only verifies — large latency gains.
* **Flash Attention**: Reordering the attention computation to avoid materializing the full attention matrix; the memory and speed implications.
* **vLLM & PagedAttention**: How production serving systems manage KV cache memory like a virtual memory system.

### 8.11 Context, Memory & the Limits of the Architecture
* **Context Window**: What it is physically (the sequence the model can "see"); why extending it is hard.
* **Lost in the Middle**: Empirical finding that models attend poorly to information in the middle of long contexts.
* **Retrieval-Augmented Generation (RAG) Revisited**: Why RAG is an architectural workaround for finite context; its limits.
* **Long-Context Architectures**: Sparse attention, sliding window attention (Mistral), state-space models (Mamba) as an alternative paradigm.

### 8.12 Hands-On Projects
* **Attention from Scratch**: Implement scaled dot-product attention and multi-head attention in pure `numpy`; verify against a `PyTorch` reference.
* **Tiny GPT**: Build and train a character-level GPT (following Karpathy's nanoGPT) on a small text corpus; understand every line.
* **Tokenizer Inspector**: Write a script that tokenizes the same sentence in 5 different tokenizers (GPT-4, Llama 3, Mistral, BERT, T5) and visualizes the differences.
* **Attention Pattern Visualizer**: Run a small open-source model and visualize the attention weights across heads for a chosen input; identify what different heads appear to attend to.
* **LoRA Fine-Tune**: Use `peft` + `transformers` to LoRA fine-tune a small model (e.g., Phi-3-mini) on a custom Q&A dataset; evaluate before and after.

---

## 🧠 Phase 9: Deep Memory (RAG, Vector Math, and The Math Under the Hood)

*Focus: High-dimensional mathematics, information retrieval, and semantic search.*

### 9.1 Vector Embeddings
* **The Math**: Turning "meaning" into coordinates—introduction to **linear algebra** including vectors, dot products, and matrices.
* **The Concept**: Why "King - Man + Woman = Queen" works in vector math.
* **Deeper**: Norms, **cosine similarity**, and **distance metrics** in high-dimensional space.
* **Foundations**: **Dimensionality reduction** techniques like PCA and t-SNE.
* **Extra**: Basics of how embedding models are trained.

### 9.2 Vector Databases (RAG)
* **The Detail**: The Retrieval Augmented Generation pipeline—how search ties to generation.
* **The Concept**: "Semantic" vs. "keyword" search.
* **Deeper**: Custom search ranking, vector indexing methods (HNSW, IVFPQ), and ANN (Approximate Nearest Neighbor) search.
* **Tools**: `ChromaDB`, `FAISS`, and manual cosine similarity calculations with `numpy`.

---

## 🤖 Phase 10: Autonomous Agency & Decision Making

*Focus: Teaching the AI to reason, act, and coordinate—single- and multi-agent systems.*

### 10.1 Tool Schemas & Function Calling
* **The Detail**: Writing function specifications in JSON using OpenAI specs or JSON-schema.
* **The Concept**: Securely passing arguments and validating input/output types.
* **Mastery Upgrade**: **Idempotency**; designing tools so they can be called multiple times without unintended side effects.

### 10.2 The ReAct Pattern
* **The Concept**: **Reason + Act**; the loop where the AI decides its needs, reasons through them, and acts to fulfill them.
* **Deeper**: Chain-of-Thought prompting and self-reflection.
* **Foundations**: Knowledge of planning algorithms including Finite State Machines, Behavior Trees, and basics of Reinforcement Learning.

### 10.3 Multi-Agent Systems (MAS)
* **The Detail**: Orchestrating multiple AIs (e.g., Researcher and Writer) and solving coordination problems.
* **Deeper**: Understanding messaging, task allocation, blackboard architecture, and agent communication protocols.
* **Further**: Emergence and basics of self-organization.

---

## 🛡️ Phase 11: Hardening & Professionalism

*Focus: Security, performance, portability, ethical design, and safe deployment.*

* **Graceful Failure**: Implementing retry logic, circuit breakers, and robust error handling.
* **Security**: Threat modeling, input sanitization, and preventing code injection.
* **Ethics**: Data privacy, explainability, and responsible AI guidelines.

---

## 🔥 Phase 12: Building Your Own Local LLM (The "JARVIS Core")

*Focus: Pulling together all components to run a truly local, explainable, and extensible AI.*

* **Collect Models**: Comparing open-source models like Llama, Mistral, Gemma, or Phi-3.
* **Inference Engines**: Running models with `llama.cpp`, `llamafile`, or `ctransformers` while experimenting with quantization.
* **Fine-tuning**: Preparing a workflow for training or fine-tuning models on your own personal data.
* **UI/UX**: Building terminal UIs, web UIs (FastAPI + React), or voice interfaces.
* **Self-Reflection**: Implementing logging and prompt inspection to see the model's internal "thought" process.
* **Continual Learning**: Researching online learning and production memory updates.

---

## 🧩 Phase 13: Philosophy, AGI, and Next Frontiers

*Focus: Where science meets philosophy—mind, consciousness, and intelligence.*

* **Read**: Turing's "Computing Machinery and Intelligence," Searle's "Chinese Room," and modern AGI forecasts.
* **Question**: What does it mean for a machine to "understand"?
* **Explore**: Symbolic AI, hybrid models, and multi-modal perception.

---

## 🔐 Phase 14: Computer Security — Offense, Defense, and Everything Between

*Focus: Learn security the way professionals do — by understanding attacks deeply enough to build real defenses. This phase covers the full stack: from memory corruption at the byte level, to web exploitation, to social engineering.*

### 14.1 Security Mindset & Foundations
* **The Attacker's Mindset**: Thinking in terms of attack surfaces, threat models, and trust boundaries.
* **CIA Triad**: Confidentiality, Integrity, Availability — the three pillars every security decision maps to.
* **CVEs and the Vulnerability Lifecycle**: How bugs are discovered, disclosed, patched, and weaponized.
* **Defense in Depth**: Why no single layer is enough; layered controls.
* **Principle of Least Privilege**: Processes, users, and services should have the minimum permissions they need — nothing more.
* **Tools**: Set up a home lab with VMs (VirtualBox/VMware + Kali Linux + a vulnerable target like Metasploitable or DVWA).

### 14.2 Cryptography — The Engine of Security
* **Symmetric Encryption**: AES (modes: ECB, CBC, GCM); why ECB is broken; what an IV does.
* **Asymmetric Encryption**: RSA from first principles (modular arithmetic, Euler's theorem); how public/private key pairs work mathematically.
* **Hashing**: SHA-256, MD5 (and why MD5 is dead); collision resistance; what a hash is not.
* **Password Storage**: Why you never store plaintext; bcrypt, scrypt, Argon2; salts and why they exist.
* **TLS/SSL**: The full TLS handshake step-by-step; certificate chains; what HTTPS actually protects (and what it doesn't).
* **PKI**: Certificate Authorities, certificate revocation, how your browser decides to trust a site.
* **Deeper**: Diffie-Hellman key exchange; elliptic curve cryptography (ECC); why forward secrecy matters.
* **Tool**: Use `openssl` CLI to inspect certificates, generate keys, encrypt/decrypt files, and simulate a TLS handshake.

### 14.3 Web Security — How the Web Gets Hacked
* **HTTP in Depth**: Cookies (flags: Secure, HttpOnly, SameSite), sessions, tokens (JWTs); how authentication state is maintained.
* **SQL Injection**: How it works at the database level; UNION-based, blind, time-based; parameterized queries as the fix.
* **Cross-Site Scripting (XSS)**: Reflected, stored, DOM-based; the Same-Origin Policy; Content Security Policy (CSP).
* **Cross-Site Request Forgery (CSRF)**: How forged requests exploit session cookies; CSRF tokens; SameSite cookies as defense.
* **IDOR & Broken Access Control**: Insecure Direct Object References; privilege escalation through predictable resource IDs.
* **Command Injection / Shell Injection**: How unsanitized user input reaches `os.system()` or `subprocess`; never do it; always use argument arrays.
* **Server-Side Request Forgery (SSRF)**: Making the server fetch arbitrary URLs; attacking internal services; cloud metadata endpoint exploitation.
* **OWASP Top 10**: Know every entry, the attack, and the mitigation.
* **Tools**: Burp Suite (intercept, modify, replay HTTP); OWASP DVWA and WebGoat as practice targets.

### 14.4 Social Engineering & Phishing — The Human Attack Surface
* **Why It Works**: Cognitive biases exploited by attackers (urgency, authority, scarcity, social proof).
* **Phishing Anatomy**: How a convincing phishing email is constructed; spoofed headers, lookalike domains, link obfuscation.
* **Spear Phishing**: Targeted attacks using OSINT to personalize lures.
* **Vishing & Smishing**: Voice and SMS-based social engineering techniques.
* **Pretexting**: Constructing a false identity or scenario to extract information.
* **Phishing Infrastructure**: How attackers register lookalike domains, set up fake login pages, and harvest credentials.
* **Defense**: Email authentication (SPF, DKIM, DMARC) — how they work technically and why misconfigurations are dangerous.
* **Tool**: Analyze real phishing email headers; use `MXToolbox` to inspect SPF/DKIM records; examine URL patterns and redirects safely.

### 14.5 Binary Exploitation & Memory Corruption
* **Buffer Overflows**: Stack-based overflows from first principles; overwriting the return address; writing a simple exploit in C.
* **Stack Canaries**: How they detect overflows; how attackers bypass them (info leaks).
* **ASLR (Address Space Layout Randomization)**: How it randomizes memory layout; how information leaks defeat it.
* **DEP/NX (No-Execute)**: Marking memory non-executable; why shellcode directly on the stack no longer works.
* **Return-Oriented Programming (ROP)**: Chaining existing code "gadgets" to bypass NX; the concept of a ROP chain.
* **Heap Exploitation Basics**: Use-after-free, heap spraying, double-free — the class of bugs that power most modern exploits.
* **Format String Vulnerabilities**: How `printf(user_input)` leaks memory or writes arbitrary values.
* **Tools**: `pwndbg` (GDB extension), `pwntools` (Python exploit framework), `checksec` (inspect binary protections), `ROPgadget`.

### 14.6 Linux Privilege Escalation
* **SUID/SGID Binaries**: How set-user-ID bits let normal users run programs as root; common misconfigurations.
* **Sudo Misconfigurations**: `sudo -l` enumeration; exploiting overly permissive sudo rules.
* **Cron Jobs**: World-writable scripts run by root; path hijacking.
* **Writable `/etc/passwd`**: Adding a root user entry.
* **Kernel Exploits**: When all else fails; finding and using local privilege escalation CVEs.
* **Tool**: Practice on dedicated platforms — TryHackMe "Linux PrivEsc" rooms, HackTheBox retired machines.

### 14.7 Network Attacks & Defense
* **Packet Sniffing**: How passive eavesdropping works on shared networks; why switches largely defeated it and why ARP spoofing brings it back.
* **ARP Spoofing / Poisoning**: Tricking hosts into sending traffic through your machine (man-in-the-middle at Layer 2).
* **DNS Poisoning & Hijacking**: Injecting false DNS responses; BGP hijacking at a conceptual level.
* **Port Scanning & Enumeration**: How `nmap` works; TCP SYN scan vs. full connect; OS fingerprinting.
* **Firewalls & IDS/IPS**: How rules are evaluated; stateful vs. stateless firewalls; the difference between detection and prevention.
* **VPNs & Proxies**: How they mask traffic; where they help and where they don't.
* **Tools**: `Wireshark` (packet analysis), `nmap`, `Scapy` (craft arbitrary packets in Python), `Ettercap` (ARP spoofing lab).

### 14.8 Reverse Engineering & Malware Analysis
* **What Reverse Engineering Is**: Understanding a binary you don't have source for.
* **Static Analysis**: Reading disassembled code without running it; identifying strings, imports, and control flow.
* **Dynamic Analysis**: Running a sample in a sandbox and observing behavior (network calls, file writes, registry changes).
* **Malware Families**: Viruses, worms, trojans, ransomware, rootkits, keyloggers — how each achieves persistence and payload delivery.
* **Anti-Analysis Techniques**: Obfuscation, packing, anti-debugging tricks, VM detection — and how analysts defeat them.
* **Tools**: `Ghidra` (NSA's free disassembler/decompiler), `x64dbg` (Windows debugger), `Cutter` (Rizin GUI), `FLARE VM` (malware analysis environment), `Any.run` / `VirusTotal` sandbox.

### 14.9 Capture The Flag (CTF) Methodology
* **Categories**: Pwn (binary exploitation), Web, Crypto, Forensics, Reversing, Misc — know what each demands.
* **Forensics Skills**: Disk image analysis, steganography, file carving, memory dump analysis with `Volatility`.
* **CTF Toolbox**: `CyberChef` (data transformations), `binwalk` (firmware analysis), `strings`, `xxd`, `file`, `strace`.
* **Practice Platforms**: PicoCTF, CTFtime.org, HackTheBox, TryHackMe, OverTheWire (Bandit → Narnia → Exploit.Education).

---

## ☁️ Phase 15: Cloud Security — Where Real Attacks Happen

*Focus: The majority of real-world breaches today happen not through buffer overflows or phishing, but through misconfigured cloud infrastructure, overprivileged IAM roles, and exposed storage. This phase covers cloud security the way professionals do — by understanding how cloud environments are attacked and how to lock them down.*

### 15.1 Cloud Fundamentals for Security
* **The Shared Responsibility Model**: What AWS/GCP/Azure secure vs. what you secure; where the boundary sits and why misunderstanding it causes breaches.
* **Cloud Regions, Availability Zones, and the Attack Surface**: How geographic distribution creates security boundaries — and new attack vectors.
* **The Metadata Service (IMDS)**: Every EC2/GCE/Azure VM has an internal HTTP endpoint at `169.254.169.254`; why this is frequently the pivot point in cloud attacks (the SSRF → metadata → credentials chain).
* **Cloud vs. On-Prem Security Mindset**: Identity is the new perimeter; why "assume breach" thinking is standard in cloud.

### 15.2 IAM — Identity and Access Management
* **IAM Fundamentals**: Users, groups, roles, and policies; the difference between authentication and authorization in cloud.
* **AWS IAM Deep Dive**: Policy evaluation logic (explicit deny > explicit allow > implicit deny); understanding `Effect`, `Action`, `Resource`, and `Condition` in policy JSON.
* **The Principle of Least Privilege in IAM**: Why `*` in a policy is a red flag; how to scope permissions correctly.
* **IAM Roles for Services**: How EC2 instances, Lambda functions, and containers assume roles; the instance profile mechanism.
* **Privilege Escalation via IAM**: How an attacker with limited IAM permissions can chain actions to reach `AdministratorAccess`; classic escalation paths (e.g., `iam:PassRole` + `ec2:RunInstances`).
* **Cross-Account Access**: Role assumption across accounts; the trust policy; supply chain attack vectors.
* **Tools**: `Pacu` (AWS exploitation framework), `ScoutSuite` (multi-cloud auditing), `IAM Access Analyzer`, `Cloudsplaining` (IAM policy analyzer).

### 15.3 Storage Misconfigurations — The Most Common Breach Vector
* **S3 Bucket Security**: Public vs. private buckets; Block Public Access settings; bucket policies vs. ACLs; why ACLs are deprecated.
* **The S3 Breach Playbook**: How attackers enumerate and access misconfigured buckets; `aws s3 ls s3://bucket-name` without credentials; the "confused deputy" problem.
* **Bucket Enumeration Techniques**: Permutation-based enumeration (`grayhatwarfare.com`, `S3Scanner`); grepping source code and JS files for bucket names.
* **Other Storage Services**: GCS (Google Cloud Storage) bucket misconfigurations; Azure Blob Storage anonymous access; the common patterns across providers.
* **Sensitive Data in Storage**: Why S3 buckets frequently contain database dumps, private keys, `.env` files, and backup archives — and how attackers find them.
* **Defense**: Enabling `aws:SecureTransport`; S3 server-side encryption; versioning and MFA delete; CloudTrail logging for data events.

### 15.4 Compute Security (EC2, Lambda, Containers)
* **EC2 Security Groups**: Stateful firewall rules; why `0.0.0.0/0` on port 22 or 3389 is an immediate red flag; security group enumeration.
* **The SSRF → IMDS Attack Chain**: An SSRF vulnerability in a web app can hit `http://169.254.169.254/latest/meta-data/iam/security-credentials/` to steal the instance's IAM credentials — this is one of the most impactful cloud attack chains in practice.
* **IMDSv2**: The token-based defense against IMDS abuse; how to enforce it; why IMDSv1 is still dangerous.
* **Lambda Security**: Cold start vs. warm execution; environment variables as a secrets antipattern; the risk of over-permissive execution roles; injection via event payloads.
* **Container Security (ECS, EKS)**: Image scanning; the risk of running as root in a container; Kubernetes RBAC and common misconfigurations; the `kubectl exec` lateral movement path.
* **User Data Scripts**: How EC2 launch scripts are frequently used to bootstrap and how they leak secrets if logged or exposed.

### 15.5 Network Security in the Cloud
* **VPC Architecture**: Subnets (public vs. private); route tables; internet gateways vs. NAT gateways; why "public subnet" doesn't mean "publicly accessible."
* **Security Groups vs. NACLs**: Stateful (SGs) vs. stateless (NACLs); rule ordering; when to use each.
* **VPC Flow Logs**: What they capture; using them to detect port scans, unusual outbound connections, and data exfiltration.
* **Peering and Transit Gateways**: How VPCs connect; lateral movement opportunities if peering is misconfigured.
* **Private Endpoints**: Keeping S3/DynamoDB/etc. traffic inside the VPC; why routing to the public internet for AWS services is a risk.
* **AWS WAF, Shield, and CloudFront**: Layer 7 protection; DDoS mitigation; rate limiting rules.

### 15.6 Logging, Monitoring & Detection
* **CloudTrail**: The audit log of every AWS API call; what it captures; why disabling it is an attacker priority; detecting its disablement.
* **CloudWatch**: Metrics, logs, and alarms; how to build alerts for suspicious activity (new IAM user created, root login, S3 policy change).
* **GuardDuty**: AWS's managed threat detection; what it detects (credential exfiltration, crypto mining, port scanning, Tor usage); its limits.
* **SIEM Integration**: Forwarding CloudTrail to a SIEM (Splunk, ELK, Sentinel); building detection rules for common cloud TTPs.
* **AWS Config**: Continuous compliance checking; detecting drift from a secure baseline; managed rules (e.g., `s3-bucket-public-read-prohibited`).
* **The Attacker's Detection Evasion Playbook**: Deleting CloudTrail logs, using low-and-slow API calls, operating in regions with no GuardDuty enabled.

### 15.7 Secrets Management
* **The Secrets Antipattern**: Hardcoded credentials in source code, `.env` files committed to Git, secrets in environment variables — how each leaks and how attackers find them.
* **AWS Secrets Manager & Parameter Store**: Storing, rotating, and auditing secrets; how services retrieve secrets at runtime without hardcoding.
* **Git History Mining**: `truffleHog`, `gitleaks`, `git log -p` — how attackers and red teamers scan repos for accidentally committed secrets.
* **Leaked Credentials Response**: The runbook for when a key is exposed — immediate rotation, reviewing CloudTrail for unauthorized use, revoking sessions.
* **Vault (HashiCorp)**: Dynamic secrets; lease-based access; the agent pattern for injecting secrets into containers.

### 15.8 Cloud-Specific Attack Techniques (Red Team Perspective)
* **Enumeration Without Credentials**: Identifying cloud provider, enumerating public S3 buckets, identifying exposed services, finding metadata from WHOIS/DNS/certificates.
* **Credential Theft Vectors**: SSRF to IMDS, Lambda environment variable leakage, secrets in CloudFormation templates, EC2 user data, GitHub Actions secrets exposure.
* **Lateral Movement in Cloud**: From one compromised role to another via `sts:AssumeRole`; from EC2 to S3 to RDS via overprivileged roles; cross-service exploitation.
* **Persistence Mechanisms**: Creating backdoor IAM users, adding policies to existing users, Lambda backdoors, EC2 AMI persistence.
* **Data Exfiltration**: S3 replication to attacker-controlled bucket; RDS snapshot sharing; exfiltrating via DNS (using Route53 as a covert channel).
* **Tools**: `Pacu` (AWS exploitation), `CloudMapper` (visualizing AWS environments), `Prowler` (AWS security best practices auditor), `CloudFox` (attack surface enumeration).

### 15.9 Compliance, Governance & Hardening
* **CIS AWS Foundations Benchmark**: The industry-standard checklist; what each control does and why; automating compliance checks.
* **AWS Organizations & SCPs (Service Control Policies)**: Enforcing guardrails across accounts; preventing `us-east-1`-only deployments; blocking dangerous API calls organization-wide.
* **The Well-Architected Framework (Security Pillar)**: AWS's own security best practices; the five design principles.
* **Terraform for Secure Infrastructure**: Writing infrastructure-as-code with security built in; `tfsec` and `checkov` for static analysis of Terraform.
* **Incident Response in the Cloud**: Isolating a compromised EC2 instance; capturing memory and disk for forensics; the IR runbook.

### 15.10 Hands-On Projects
* **IAM Privilege Escalation Lab**: Set up a deliberately misconfigured AWS account (use a free-tier sandbox); start with a low-privilege IAM user; escalate to admin using at least 2 different paths; document each step.
* **S3 Bucket Auditor**: Build a Python tool using `boto3` that scans all S3 buckets in an account for public access, missing encryption, disabled logging, and missing versioning; output a prioritized risk report.
* **SSRF to IMDS Simulation**: Build a deliberately vulnerable Flask app that has an SSRF vulnerability; exploit it to retrieve simulated IMDS credentials; then patch the app and document the fix.
* **CloudTrail Anomaly Detector**: Write a Python script that reads CloudTrail logs and flags suspicious events: root account usage, IAM user creation, policy changes, access from new regions, and high-volume API calls.
* **Secrets Scanner**: Build a tool that clones a public GitHub repo and scans the entire git history for hardcoded AWS keys, passwords, and tokens using regex and entropy analysis; test it against repos known to have had leaked credentials.
* **Terraform Secure Baseline**: Write Terraform that deploys a VPC with public/private subnets, an EC2 instance with IMDSv2 enforced, an S3 bucket with all public access blocked, and CloudTrail enabled — run `tfsec` and fix every finding.

---

## 📚 Appendix: Resources & Learning Materials

* **Books**: "Artificial Intelligence: A Modern Approach" (Russell & Norvig); "Deep Learning" (Goodfellow); "Computer Systems: A Programmer's Perspective" (Bryant & O'Hallaron — the bible for Phase 4); "The Web Application Hacker's Handbook"; "Hacking: The Art of Exploitation" (Erickson).
* **Online**: 3Blue1Brown (mathematics & neural networks); MIT OpenCourseWare 6.004 (Computation Structures); LiveOverflow (binary exploitation); IppSec (HackTheBox walkthroughs); Julia Evans / "Wizard Zines" (networking & OS internals explained brilliantly).
* **Practice Labs**: HackTheBox, TryHackMe, OverTheWire, PicoCTF, pwn.college (pwn/binary), PortSwigger Web Security Academy (web).
* **Communities**: Reddit r/LocalLLaMA, r/netsec, r/ReverseEngineering; Hugging Face forums; GitHub; CTFtime.org.

---

# 🕹️ PROJECTS

---

## 🐍 Phase 0: Python Mastery

### 0.1 · Python Language Deep Dive
- **Decorator-powered Logging**
  Implement logging and timing decorators for AI function calls.
- **Custom Context Manager**
  Write a context manager that tracks resource usage (memory/CPU) during model inference.
- **Fault-Tolerant AI Service**
  Build an exception-resilient "mini agent" that never crashes, logging all errors to a file.
- **Data Streaming Generator**
  Create a generator that streams large datasets for ML, one batch at a time.

### 0.2 · Typing, Packaging & Testing
- **Typed AI API**
  Build a tiny inference API with full type annotations and enforce them with `mypy`.
- **Reusable AI Utility Package**
  Make a Python package (with tests and `setup.py`) for common tasks (e.g., text cleaning, tokenizing).
- **Test-Driven Model Evaluation**
  Write tests to verify correctness of preprocessing and model output.

### 0.3 · Performance, Concurrency, Debugging
- **Performance Profiler**
  Instrument a model inference pipeline to profile and optimize bottlenecks.
- **Concurrent Inference Server**
  Use threads/asyncio to allow your AI app to handle multiple requests simultaneously.
- **Debuggable Chatbot**
  Add live debugging (breakpoints, logging) to your console AI assistant.

---

## 🏗️ Phase 1 & 2: Core Infrastructure

- **OOP-Powered Agent**
  Refactor a chatbot or image classifier into a fully class-based architecture.
- **Persistent Memory Bot**
  Create a to-do assistant that remembers tasks (JSON on disk) even after restart.
- **MemoryManager Demo**
  Build a modular "library" class that supports swapping storage backends (file/cloud).
- **System-Aware AI**
  Agent can launch/terminate local programs based on user requests.

---

## 🧠 Phase 3: The Brain & Memory

- **History-Aware Chatbot**
  An AI assistant that maintains conversational context/history and summaries.
- **Factory Reset Logic**
  Add "memory wipe" and selective reset features to your bot UI.
- **Local Agent with Ollama**
  Connect to Llama locally for inference, expose via Python.
- **Memory-Scoped Notepad**
  AI app with temporary (history) and permanent (metadata) notes.

---

## 💻 Phase 4: How Computers Really Work

### 4.0 · From Transistors to Logic Gates
- **Logic Gate Simulator**
  Build AND, OR, NAND, XOR gates in Python; simulate a 1-bit adder and chain it to a 4-bit ALU.
- **Binary Calculator**
  CLI tool that performs addition and subtraction in binary, showing carry/overflow flags explicitly.

### 4.1 · CPU Architecture in Depth
- **Cache Miss Profiler**
  Write two memory access patterns (sequential vs. random) in C or Python/ctypes; measure and explain the timing difference using cache behavior.
- **Pipeline Hazard Demo**
  Annotate a snippet of assembly (from a real compiled program) and identify where data hazards would cause stalls.
- **SIMD Experiment**
  Use NumPy (which uses SIMD internally) and a pure Python loop to process a large array; compare and explain the speedup in terms of vectorization.

### 4.2 · Assembly Language
- **Hello World in Assembly**
  Write a Linux x86-64 "Hello, World" using only syscalls (no libc); assemble with `nasm`, link with `ld`, run it.
- **Disassembly Annotator**
  Compile a simple C function (e.g., a loop, an if-else) at `-O0` and `-O2`; annotate the disassembly output line by line using `objdump` or Godbolt.
- **Stack Frame Inspector**
  Use `gdb` to pause a program inside a function call; print the stack, identify the return address, saved registers, and local variables.

### 4.3 · How Compiling Works
- **Compiler Pipeline Explorer**
  Take a 20-line C program through each stage manually: `cpp` (preprocessor) → `cc1` (compiler) → `as` (assembler) → `ld` (linker). Inspect the output at each step.
- **ELF Dissector**
  Use `readelf` and `objdump` to map every section of a compiled binary; write a report explaining what `.text`, `.data`, `.bss`, and `.rodata` contain for your program.
- **Dynamic Linker Tracer**
  Use `LD_DEBUG=all` or `strace` to watch the dynamic linker resolve symbols at program startup; document which `.so` files are loaded and in what order.

### 4.4 · Processes, Memory, and the OS Kernel
- **Virtual Memory Mapper**
  Write a Python or C program that reads `/proc/self/maps` and produces a human-readable map of its own address space, annotating stack, heap, code, and shared libraries.
- **Fork & Exec Shell**
  Build a minimal Unix shell from scratch in C or Python that supports running commands, piping (`|`), and basic I/O redirection (`>`, `<`).
- **Syscall Tracer**
  Use `strace` on several programs (a Python script, `curl`, `ls`); count and categorize syscalls; write a brief analysis of what each program is doing at the OS level.

### 4.5 · OS & Process Control
- **Resource Monitor**
  Script logs AI CPU/memory usage live.
- **Controlled Forking**
  Run multiple agent subprocesses and aggregate outputs.

### 4.6 · Computer Architecture
- **Bit Visualizer**
  Binary/hex of weights or floating-point rounding.
- **Model Compression Lab**
  Quantize weights, compare performance.

### 4.7 · Networks & Protocols
- **AI Chat Server**
  Secure, minimal chat server with SSL and sockets.
- **DNS Explorer**
  AI logs domain→IP lookups made.

### 4.8 · Mathematics for AI
- **Matrix Playground**
  Visualize matrix operations; interactively demo linear algebra.
- **Gradient Descent Animator**
  Show each step of loss minimization.

---

## 🌐 Phase 5: Networking & External Senses

### 5.0 · The Request/Response Cycle
- **Mini HTTP Client**
  Python CLI for GET/POST requests and JSON API parsing.
- **Raw Socket Bot**
  Tiny TCP server/client for echo or Q&A.
- **OSI Visualizer**
  Log/draw the OSI layers involved in an AI web request.

### 5.1 · API Integration & Tooling
- **Weather/News Agent Tool**
  AI module for fetching real-world data via an external API.
- **Rate Limit Demo**
  App detects and adapts to API rate limits (retry/backoff).
- **DIY REST API**
  Serve inference or DB using FastAPI.

### 5.2 · Asynchronous Execution (asyncio)
- **Async Web Scraper**
  Fetch multiple web pages concurrently (AI "data gathering").
- **Async Task Scheduler**
  Handle long-running tasks using async (e.g., reminders).
- **Concurrency Benchmark**
  Compare threading, async, and multiprocessing for model inference.

  ### 5.3 · Physical & Data Link
- **Ethernet Frame Decoder**
  Use `Scapy` to capture live traffic and parse raw Ethernet frames; display source/dest MAC, EtherType, and payload for each frame.
- **ARP Table Inspector**
  Python tool that periodically reads the ARP table, detects new entries, and alerts if a MAC address changes for an existing IP (basic ARP spoofing detector).

### 5.4 · IP & Routing
- **Subnet Calculator**
  Build a Python CLI that takes any IP/prefix and outputs: network address, broadcast, first/last host, number of hosts, and whether a given IP is in the subnet.
- **Traceroute from Scratch**
  Implement `traceroute` in Python using raw ICMP sockets and TTL manipulation; compare output against the system `traceroute`.
- **Routing Table Visualizer**
  Parse the output of `ip route` or a router config file; draw the routing decision tree for a given destination packet.

### 5.5 · TCP & UDP
- **TCP State Machine**
  Build a Python visualization that animates the TCP three-way handshake and four-way teardown in real time, capturing a real connection with `Scapy`.
- **Reliable UDP**
  Implement a simple stop-and-wait ARQ protocol on top of UDP — add sequence numbers, acknowledgements, and retransmission on timeout.
- **TCP Congestion Monitor**
  Use `ss -i` and `tc` to observe TCP congestion window changes during a large file transfer; log and plot the cwnd over time.

### 5.6 · DNS
- **DNS Resolver from Scratch**
  Implement a recursive DNS resolver in Python using only UDP sockets (no `dnspython`); walk the delegation chain from the root all the way to the authoritative answer.
- **DNS Exfiltration Demo**
  Build a toy proof-of-concept that encodes a file into DNS query labels and "sends" it to a local listener; then build the detection rule that catches it.
- **DNSSEC Validator**
  Write a Python tool that validates the DNSSEC chain of trust for a given domain using `dnspython`; report which records are signed and whether the chain is valid.

### 5.7 · Application Layer Protocols
- **HTTP/1.1 Server from Scratch**
  Build a Python HTTP server using raw sockets (no `http.server`); support GET, HEAD, and POST; parse headers; serve static files and return correct status codes.
- **TLS Handshake Logger**
  Use `Wireshark` and a test HTTPS connection; capture and annotate every message in a TLS 1.3 handshake (ClientHello, ServerHello, Certificate, Finished).
- **SSH Tunnel Demo**
  Set up an SSH tunnel to forward a local port to a remote service; explain how it works; then implement a minimal SSH client concept using `paramiko`.

### 5.8 · Network Architecture & Defense
- **Firewall & DMZ Lab**
  Configure a three-interface VM setup (external, DMZ, internal) with `iptables` rules enforcing proper zone-based access control; document and justify every rule.
- **Load Balancer Simulation**
  Implement a simple Layer 4 TCP load balancer in Python that proxies connections to a pool of backend servers using round-robin; add health checks.
- **WireGuard VPN Setup**
  Set up a WireGuard VPN between two VMs; capture handshake traffic; explain each field in the WireGuard handshake packet; verify traffic is encrypted end-to-end.

### 5.9 · Monitoring & Troubleshooting
- **Network Baseline Monitor**
  Python daemon that continuously monitors latency, packet loss, and bandwidth to key hosts; logs anomalies and generates alerts.
- **Packet Capture Analyzer**
  Build a Python tool using `Scapy` or `pyshark` that reads a `.pcap` file and produces a summary report: top talkers, protocol breakdown, DNS queries made, HTTP hosts contacted.
- **Full Network Lab Capstone**
  Design and build a virtualized network with at least 3 subnets, a router, a firewall, a DNS server, and an HTTP server; document the full topology; test connectivity and security rules end-to-end.

---

## 🔊 Phase 6: Physical Senses (Voice, Audio, Beyond)

### 6.1 · Text-to-Speech (TTS)
- **Talking AI Assistant**
  Turn bot responses into speech (`gTTS`, `edge-tts`, etc.).
- **Audio Dashboard**
  Visualize waveforms, bitrates of AI-generated audio.
- **Custom Voice Filtering**
  Add echo, change speed, or basic DSP effects.

### 6.2 · Speech-to-Text (STT)
- **Voice-Controlled Agent**
  Control an agent with speech input (`SpeechRecognition`, `Whisper`).
- **Silence Detector**
  Implement VAD for start/stop recording.
- **Speech Analysis**
  Draw real-time audio spectrogram from mic input.

### 6.3 · Sensing Beyond Audio
- **Image Recognizer**
  AI vision agent with webcam, using `opencv`.
- **Sensor Dashboard**
  Simulate or connect basic sensors, feed live data to AI.

---

## 🦾 Phase 7: AI & Machine Learning Foundations

### 7.1 · Data & ML Problem Types
- **AI Data Explorer**
  Tool to load, clean, and visualize datasets.
- **Auto Splitter**
  Script to automate train/test splits.

### 7.2 · Classic Algorithms & Evaluation
- **Play with Classics**
  MNIST classifier (logistic regression, decision trees).
- **Confusion Matrix Dashboard**
  Visualize model errors & accuracy.

### 7.3 · Probability & Statistics
- **Bias Detector**
  Agent summarizes distributions and flags data bias.
- **Random Outcome Simulator**
  Use probability for outcome prediction (e.g., spam detection).

### 7.4 · NN & Deep Learning Basics
- **Build-Your-Own NN**
  Train a toy neural network (e.g., XOR) from scratch with no framework — just `numpy`.
- **NN Visualizer**
  Show activations/weights as the network learns.
- **Regularization Playground**
  Demo overfitting and dropout.

### 7.5 · Model Management & Reproducibility
- **Experiment Logger**
  Track all hyperparameters and results.
- **Simple Deployment**
  Serve a trained model (Flask/FastAPI).

### 7.6 · AI Ethics, Bias, Explainability
- **Bias Audit**
  Dashboard to show and mitigate model bias.
- **Explain-a-Prediction**
  SHAP or similar to explain model outputs.

---

## 🔩 Phase 8: Transformer Architecture

### 8.1–8.2 · Attention Mechanism
- **Attention from Scratch**
  Implement scaled dot-product attention and multi-head attention in pure `numpy`; verify against a `PyTorch` reference.
- **Attention Pattern Visualizer**
  Run a small open-source model and visualize the attention weights across heads for a chosen input; identify what different heads appear to attend to.

### 8.3–8.6 · The Full Architecture
- **Tiny GPT**
  Build and train a character-level GPT (following Karpathy's nanoGPT) on a small text corpus; understand every line of code.
- **Tokenizer Inspector**
  Write a script that tokenizes the same sentence in 5 different tokenizers (GPT-4, Llama 3, Mistral, BERT, T5) and visualizes the differences in token count and segmentation.

### 8.9 · Fine-tuning
- **LoRA Fine-Tune**
  Use `peft` + `transformers` to LoRA fine-tune a small model (e.g., Phi-3-mini) on a custom Q&A dataset; evaluate before and after.

### 8.10 · Inference Optimization
- **Quantization Comparison**
  Load the same model in Q4, Q5, and Q8 via `llama.cpp`; benchmark speed, memory usage, and output quality on the same prompt set.

---

## 🧠 Phase 9: Deep Memory (RAG, Vector Math)

- **Embeddings Explorer**
  Visualize and compare text/image embeddings; cosine similarity search.
- **Mini RAG Bot**
  Use vector search + LLM to answer from knowledge base.
- **Custom Vector DB**
  Make a mini FAISS/ChromaDB system for a toy dataset.

---

## 🤖 Phase 10: Autonomous Agency

- **Function Calling Demo**
  LLM calls Python tools defined with JSON schema.
- **ReAct Agent**
  Model reasons aloud and takes action in a loop.
- **Task Allocation Simulator**
  Multi-agent system (planner, worker, critic).

---

## 🛡️ Phase 11: Hardening & Professionalism

- **Dockerized AI Service**
  Containerize your agent with secrets management.
- **Resilient API**
  Add retry/circuit-breaker logic to model serving.
- **Security Scanner**
  Tool to analyze code for security issues.
- **Ethics Pledge Display**
  Add visible privacy/ethics policy to outputs.

---


## 🔥 Phase 12: Build Your Own Local LLM

- **Local LLM Interface**
  UI (terminal/web) to talk to Ollama/llama.cpp.
- **Mini Fine-Tuner**
  Script to (simulate) fine-tune on your data.
- **Prompt Inspector**
  UI displays prompt, completion, and LLM "thoughts."
- **Model Explorer**
  Compare Llama, Mistral, etc., side-by-side.

---

## 🧩 Phase 13: Philosophy & Next Frontiers

- **AI Thought Journal**
  Log and visualize: "What does my agent actually understand?"
- **Symbolic Reasoning Bot**
  Integrate rule-based logic with neural agent.
- **Chinese Room Simulator**
  Script/game simulating the famous philosophy thought experiment.
- **AGI Debate Club**
  Agent that debates definitions of intelligence.

---

## 🔐 Phase 14: Computer Security

### 14.1 · Security Foundations
- **Threat Model Document**
  Choose a real application (your AI agent); write a structured threat model identifying assets, trust boundaries, attack surfaces, and mitigations.
- **Home Lab Setup**
  Configure VirtualBox with Kali Linux + one vulnerable target (DVWA or Metasploitable 2); document your network topology.

### 14.2 · Cryptography
- **AES Modes Comparison**
  Encrypt the same image file with AES-ECB and AES-CBC; display both outputs visually to understand why ECB is broken.
- **TLS Inspector**
  Use `openssl s_client` to connect to several HTTPS sites; decode the certificate chain, identify the cipher suite, and document each field.
- **Password Cracker (Educational)**
  Build a Python script that cracks MD5 password hashes using a wordlist + salt; demonstrate why MD5 is unsuitable and why bcrypt/Argon2 is not; measure the time difference.

### 14.3 · Web Security
- **SQL Injection Lab**
  Set up DVWA; exploit a login form using manual SQL injection (no tools); document every step; then fix the vulnerability using parameterized queries.
- **XSS Payload Lab**
  Find and exploit a stored XSS vulnerability in DVWA; demonstrate cookie theft; implement CSP to block it.
- **Burp Suite Session Hijack Demo**
  Use Burp Suite to intercept and modify a request in DVWA; demonstrate IDOR by accessing another user's data; document the fix.
- **Command Injection Hunter**
  Find and exploit a command injection in DVWA; write a Python scanner that detects the pattern in source code.

### 14.4 · Social Engineering & Phishing
- **Phishing Email Analyzer**
  Collect 5 real-world phishing emails (from spam folders or public datasets); for each one, analyze and document the headers, domain spoofing technique, payload, and social engineering trigger used.
- **SPF/DKIM/DMARC Auditor**
  Build a Python tool using `dns.resolver` that checks a domain's SPF, DKIM, and DMARC records and produces a security report with pass/fail/misconfigured status.
- **Lookalike Domain Detector**
  Write a script that takes a brand name (e.g., "paypal") and generates a list of common typosquatting/homograph variants; check which ones are registered using `whois`.

### 14.5 · Binary Exploitation
- **Stack Overflow (Controlled)**
  Write a deliberately vulnerable C program; overflow the buffer to overwrite the return address and redirect execution to a different function — document every byte.
- **ROP Chain Builder**
  Disable ASLR on a VM; use `ROPgadget` to find gadgets in a binary; build a minimal ROP chain that calls `execve("/bin/sh")`.
- **CTF Pwn Challenge**
  Complete at least 3 binary exploitation challenges on pwn.college or PicoCTF; write up your solution methodology for each.

### 14.6 · Linux Privilege Escalation
- **PrivEsc Lab**
  Set up a deliberately misconfigured Linux VM (using a TryHackMe room or manual setup); escalate from a low-privileged user to root using at least 3 different techniques (SUID, sudo misconfiguration, cron job); document each path.
- **SUID Scanner**
  Write a Python or Bash script that finds all SUID/SGID binaries on a system and cross-references them against GTFOBins for known exploit paths.

### 14.7 · Network Attacks & Defense
- **ARP Spoof Lab**
  On an isolated VM network, perform an ARP spoofing attack using `Scapy`; capture traffic with `Wireshark`; implement dynamic ARP inspection as a defense.
- **Port Scanner from Scratch**
  Build a Python TCP SYN scanner using `Scapy` (raw sockets, no nmap); implement service detection by reading banners; compare results against nmap.
- **Firewall Rule Analyzer**
  Write `iptables` rules to implement a default-deny firewall with specific allow rules; then write a script that parses and explains each rule in plain English.

### 14.8 · Reverse Engineering & Malware Analysis
- **Static Malware Triage**
  Obtain a known-benign but obfuscated binary (e.g., a crackme from crackmes.one); perform static analysis with `Ghidra`; identify the expected password or key without running it.
- **Behavior Sandbox Report**
  Run a sample through Any.run or an offline sandbox; write a full IOC (Indicators of Compromise) report: file hashes, network connections, registry changes, dropped files.
- **Packer Detector**
  Write a Python script using `pefile` that detects whether a Windows PE binary is packed (high entropy sections, missing imports); test against UPX-packed and clean binaries.

### 14.9 · CTF Practice
- **OverTheWire Bandit (all levels)**
  Complete all Bandit levels; write a cheatsheet of every technique learned.
- **PicoCTF Season**
  Complete a full PicoCTF competition or past season; aim for at least one solve in each category (Pwn, Web, Crypto, Forensics, Reversing).
- **HackTheBox Easy Machine**
  Root at least 2 retired Easy-rated HTB machines; write a full walkthrough documenting enumeration, exploitation, and privilege escalation.

---

## ☁️ Phase 15: Cloud Security

### 15.2 · IAM & Privilege Escalation
- **IAM Privilege Escalation Lab**
  Set up a deliberately misconfigured AWS sandbox account; start with a low-privilege IAM user; escalate to admin using at least 2 different paths; document each step.
- **IAM Policy Analyzer**
  Build a Python tool using `boto3` that reads all IAM policies in an account and flags dangerous permissions (`*`, `iam:PassRole`, `sts:AssumeRole` with wildcard resources).

### 15.3 · Storage Misconfigurations
- **S3 Bucket Auditor**
  Build a Python tool using `boto3` that scans all S3 buckets in an account for public access, missing encryption, disabled logging, and missing versioning; output a prioritized risk report.
- **Secrets Scanner**
  Build a tool that clones a public GitHub repo and scans the entire git history for hardcoded AWS keys, passwords, and tokens using regex and entropy analysis; test it against repos known to have had leaked credentials.

### 15.4 · SSRF & Compute Security
- **SSRF to IMDS Simulation**
  Build a deliberately vulnerable Flask app that has an SSRF vulnerability; exploit it to retrieve simulated IMDS credentials; then patch the app and document the fix.

### 15.5 · Logging & Detection
- **CloudTrail Anomaly Detector**
  Write a Python script that reads CloudTrail logs and flags suspicious events: root account usage, IAM user creation, policy changes, access from new regions, and high-volume API calls.

### 15.6 · Hardening
- **Terraform Secure Baseline**
  Write Terraform that deploys a VPC with public/private subnets, an EC2 instance with IMDSv2 enforced, an S3 bucket with all public access blocked, and CloudTrail enabled — run `tfsec` and fix every finding.

## 🛠️ Professional & Deployment Projects

- **CI/CD Workflow**: Add and document a GitHub Actions workflow for one chosen project.
- **Production Monitoring**: Implement simple logging, health checks, or status endpoint in your API server(s).
- **Code Review / Open Source Contribution**: Participate in or simulate a code review; submit a PR to an open-source AI/Python project.
- **Web UI/UX Polish**: Build a minimal web frontend or CLI enhancement for an existing project.
- **Real-Time Dashboard**: Visualize metrics or model predictions live for any agent.
- **Async Benchmarking**: Measure and document sync vs. async API throughput for your ML inference service.
- **Cross-language Exploration**: (Optional) Replicate a core utility or agent prototype in Rust, Go, or C, then document comparison with Python.


---

## 📚 Resources

### Books
- **Computer Science**: *Computer Systems: A Programmer's Perspective* (Bryant & O'Hallaron) — the single best book for Phases 1 & 5
- **Networking**: *Computer Networking: A Top-Down Approach* (Kurose & Ross)
- **Security**: *The Web Application Hacker's Handbook*, *Hacking: The Art of Exploitation* (Erickson)
- **AI/ML**: *Deep Learning* (Goodfellow), *Neural Networks and Deep Learning* (Nielsen — free online)
- **C**: *The C Programming Language* (Kernighan & Ritchie)

### Online
- **Networking**: Julia Evans' networking zines (b0rk.ca), Beej's Guide to Network Programming
- **Security**: PortSwigger Web Security Academy (free, hands-on labs), picoCTF, HackTheBox
- **AI**: Andrej Karpathy's YouTube (neural nets from scratch), 3Blue1Brown (linear algebra, calculus, neural nets)
- **Systems**: *CS:APP* lab assignments, OSDev Wiki, xv6 (MIT teaching OS)

### Practice Platforms
- **Security CTFs**: picoCTF, CTFtime, HackTheBox, TryHackMe
- **Networking Labs**: GNS3, Packet Tracer, or a home router with OpenWrt
- **AI Experiments**: Kaggle, Hugging Face, Papers With Code

---

> **The Rule**: For every concept, ask "what is actually happening at the byte level?" Then verify by writing code that proves it.
