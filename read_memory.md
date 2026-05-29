hello-agents/
├── hello_agents/
│   ├── memory/                   # 记忆系统模块
│   │   ├── base.py               # 基础数据结构（MemoryItem, MemoryConfig, BaseMemory）        #ok
│   │   ├── manager.py            # 记忆管理器（统一协调调度）                                   #ok
│   │   ├── embedding.py          # 统一嵌入服务（DashScope/Local/TFIDF）                       #ok
│   │   ├── types/                # 记忆类型实现
│   │   │   ├── working.py        # 工作记忆（TTL管理，纯内存）                                 #ok
│   │   │   ├── episodic.py       # 情景记忆（事件序列，SQLite+Qdrant）                         #ok
│   │   │   ├── semantic.py       # 语义记忆（知识图谱，Qdrant+Neo4j）                          #ok
│   │   │   └── perceptual.py     # 感知记忆（多模态，SQLite+Qdrant）                           #ok
│   │   ├── storage/              # 存储后端实现
│   │   │   ├── qdrant_store.py   # Qdrant向量存储（高性能向量检索）                            #ok
│   │   │   ├── neo4j_store.py    # Neo4j图存储（知识图谱管理）                                 #ok
│   │   │   └── document_store.py # SQLite文档存储（结构化持久化）                              #ok
│   │   └── rag/                  # RAG系统
│   │       ├── pipeline.py       # RAG管道（端到端处理）
│   │       └── document.py       # 文档处理器（多格式解析）
│   └── tools/builtin/            # 扩展内置工具
│       ├── memory_tool.py        # 记忆工具（Agent记忆能力）                                   #ok
│       └── rag_tool.py           # RAG工具（智能问答能力）
└──
