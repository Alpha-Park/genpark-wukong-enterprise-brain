# -*- coding: utf-8 -*-
"""
GenPark Wukong Enterprise Brain Client
Zero-dependency knowledge graph relation path finder (BFS transitive closure),
multi-hop semantic query resolver, and contradictory fact consensus arbiter.
"""

import math
from typing import Dict, List, Any, Optional

class GenParkWukongEnterpriseBrain:
    """
    Resolves multi-hop enterprise knowledge graph relationships, executes path deductions,
    and reconciles contradictory facts across distributed data sources.
    """

    def find_knowledge_graph_relation_path(
        self,
        triples: List[Dict[str, str]],
        start_entity: str,
        target_entity: str,
        max_hops: int = 4
    ) -> Dict[str, Any]:
        """
        Executes Breadth-First Search (BFS) to discover transitive relation paths between two entities.
        Triple format: {"subject": "A", "predicate": "reports_to", "object": "B"}
        """
        if not triples or not start_entity or not target_entity:
            raise ValueError("Triples, start entity, and target entity must not be empty.")

        # Build adjacency graph: subject -> list of (predicate, object)
        adj = {}
        for t in triples:
            s = t.get("subject", "")
            p = t.get("predicate", "related_to")
            o = t.get("object", "")
            adj.setdefault(s, []).append((p, o))

        # BFS queue: (current_node, path_of_edges)
        queue = [(start_entity, [])]
        visited = set([start_entity])
        found_paths = []

        while queue:
            curr, path = queue.pop(0)

            if curr == target_entity and path:
                found_paths.append(path)
                continue

            if len(path) >= max_hops:
                continue

            for pred, nxt in adj.get(curr, []):
                if nxt not in visited or nxt == target_entity:
                    visited.add(nxt)
                    queue.append((nxt, path + [{"from": curr, "relation": pred, "to": nxt}]))

        shortest_path = min(found_paths, key=len) if found_paths else None

        return {
            "start_entity": start_entity,
            "target_entity": target_entity,
            "paths_found_count": len(found_paths),
            "shortest_path_hops": len(shortest_path) if shortest_path else None,
            "shortest_path": shortest_path,
            "connected": len(found_paths) > 0
        }

    def resolve_multihop_semantic_query(
        self,
        triples: List[Dict[str, str]],
        entity_root: str,
        predicate_chain: List[str]
    ) -> Dict[str, Any]:
        """
        Executes sequential relational join along a chain of predicates: (Root, p1, ?x) -> (?x, p2, ?y) -> ...
        """
        if not triples or not entity_root or not predicate_chain:
            raise ValueError("Triples, root entity, and predicate chain cannot be empty.")

        current_candidates = set([entity_root])
        step_traces = []

        for p in predicate_chain:
            next_candidates = set()
            matches = []
            for t in triples:
                if t.get("predicate", "") == p and t.get("subject", "") in current_candidates:
                    next_candidates.add(t.get("object", ""))
                    matches.append(t)
            
            step_traces.append({
                "predicate": p,
                "input_entities": list(current_candidates),
                "matched_triples": len(matches),
                "output_entities": list(next_candidates)
            })
            current_candidates = next_candidates
            if not current_candidates:
                break

        return {
            "root_entity": entity_root,
            "predicate_chain": predicate_chain,
            "resolved_terminal_entities": list(current_candidates),
            "step_traces": step_traces,
            "is_resolved": len(current_candidates) > 0
        }

    def reconcile_conflicting_fact_consensus(
        self,
        claims: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Reconciles contradictory facts using source reliability log-odds weights:
        W_s = ln(p_s / (1 - p_s))
        Claim format: {"source_id": "erp_1", "source_reliability": 0.90, "value": "Contract_Active"}
        """
        if not claims:
            raise ValueError("Claims list cannot be empty.")

        value_weights = {}
        for c in claims:
            val = str(c.get("value", ""))
            rel = max(0.51, min(0.99, c.get("source_reliability", 0.70)))
            # Log-odds reliability weight
            w = math.log(rel / (1.0 - rel))
            value_weights[val] = value_weights.get(val, 0.0) + w

        # Consensus winner is value with highest accumulated weight
        best_val = max(value_weights, key=value_weights.get)
        total_w = sum(value_weights.values())
        confidence = round(value_weights[best_val] / max(1e-9, total_w), 3)

        return {
            "total_claims_audited": len(claims),
            "unique_values_contested": len(value_weights),
            "consensus_value": best_val,
            "consensus_confidence": confidence,
            "voting_scores": {k: round(v, 3) for k, v in value_weights.items()},
            "is_unanimous": len(value_weights) == 1
        }
