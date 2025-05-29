from app import graph

if __name__ == "__main__":n    graph = graph_builder.compile()
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import StateGraph
from langgraph.types import StartEvent

# 初始化聊天机器人
graph = StateGraph(state_schema=GraphState)
graph.add_node("llm_node", llm_node)
graph.add_edge("llm_node", "llm_node")
graph.set_entry_point("llm_node")
graph.set_finish_point("llm_node")

# 启动本地服务器
if __name__ == "__main__":n    import uvicorn
    from langgraph.runtime import RunnableConfig
    
    # 创建可运行实例
    app = graph.compile()
    
    # 启动服务
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)