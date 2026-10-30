# -*- coding: utf-8 -*-
"""
GenPark Wukong Enterprise Brain FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import GenParkWukongEnterpriseBrain

mcp = FastMCP("genpark-wukong-enterprise-brain")
brain = GenParkWukongEnterpriseBrain()

@mcp.tool()
def find_knowledge_graph_relation_path(
    triples_json: str,
    start_entity: str,
    target_entity: str,
    max_hops: int = 4
) -> str:
    """
    Executes Breadth-First Search (BFS) to discover relation paths between entities.
    """
    triples = json.loads(triples_json)
    res = brain.find_knowledge_graph_relation_path(triples, start_entity, target_entity, max_hops)
    return json.dumps(res, indent=2)

@mcp.tool()
def resolve_multihop_semantic_query(
    triples_json: str,
    entity_root: str,
    predicate_chain_json: str
) -> str:
    """
    Executes sequential relational join along a chain of predicates.
    """
    triples = json.loads(triples_json)
    chain = json.loads(predicate_chain_json)
    res = brain.resolve_multihop_semantic_query(triples, entity_root, chain)
    return json.dumps(res, indent=2)

@mcp.tool()
def reconcile_conflicting_fact_consensus(claims_json: str) -> str:
    """
    Reconciles contradictory facts using source reliability log-odds weights.
    """
    claims = json.loads(claims_json)
    res = brain.reconcile_conflicting_fact_consensus(claims)
    return json.dumps(res, indent=2)

def main():
    print("Testing Enterprise Brain:")
    t = [{"subject": "Alice", "predicate": "manager_of", "object": "Bob"}]
    print(find_knowledge_graph_relation_path(json.dumps(t), "Alice", "Bob"))

if __name__ == "__main__":
    main()
