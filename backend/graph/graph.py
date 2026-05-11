from langgraph.graph import StateGraph, END

from backend.graph.state import PaperState

from backend.graph.nodes.planner import planner_node
from backend.graph.nodes.github_search import github_search_node
from backend.graph.nodes.coder import coder_node
from backend.graph.nodes.summary import summary_node
from backend.graph.nodes.explanation import explanation_node
from backend.graph.nodes.packager import packager_node


workflow = StateGraph(PaperState)

workflow.add_node("planner", planner_node)
workflow.add_node("github_search", github_search_node)
workflow.add_node("coder", coder_node)
workflow.add_node("summary", summary_node)
workflow.add_node("explanation", explanation_node)
workflow.add_node("packager", packager_node)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "github_search")
workflow.add_edge("github_search", "coder")
workflow.add_edge("coder", "summary")
workflow.add_edge("summary", "explanation")
workflow.add_edge("explanation", "packager")
workflow.add_edge("packager", END)

graph = workflow.compile()