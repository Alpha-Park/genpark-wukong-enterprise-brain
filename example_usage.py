# -*- coding: utf-8 -*-
import json
from client import GenParkWukongEnterpriseBrain

brain = GenParkWukongEnterpriseBrain()

# 1. Knowledge Graph Transitive Path Deduction
kg = [
    {"subject": "Engineering_Dept", "predicate": "controls_budget", "object": "Cloud_Infra_Budget"},
    {"subject": "Cloud_Infra_Budget", "predicate": "funds_contract", "object": "Vendor_AWS"},
    {"subject": "Alice_VP", "predicate": "leads_department", "object": "Engineering_Dept"}
]
path = brain.find_knowledge_graph_relation_path(kg, start_entity="Alice_VP", target_entity="Vendor_AWS")
print(f"Knowledge Graph Path Discovery: Connected={path['connected']} ({path['shortest_path_hops']} hops)")
for step in path["shortest_path"]:
    print(f"  {step['from']} --[{step['relation']}]--> {step['to']}")

# 2. Multi-Hop Semantic Query Join
chain = ["leads_department", "controls_budget", "funds_contract"]
query = brain.resolve_multihop_semantic_query(kg, entity_root="Alice_VP", predicate_chain=chain)
print()
print(f"Multi-Hop Query: Root 'Alice_VP' -> Chain {chain}")
print(f"  Terminal Entities: {query['resolved_terminal_entities']}")

# 3. Contradictory Fact Consensus Resolution
conflicting_claims = [
    {"source_id": "Legacy_CRM", "source_reliability": 0.65, "value": "Tier_Midmarket"},
    {"source_id": "Primary_Stripe", "source_reliability": 0.95, "value": "Tier_Enterprise"},
    {"source_id": "Hubspot_API", "source_reliability": 0.70, "value": "Tier_Enterprise"}
]
consensus = brain.reconcile_conflicting_fact_consensus(conflicting_claims)
print()
print(f"Fact Consensus: Winner='{consensus['consensus_value']}' (Confidence: {consensus['consensus_confidence']})")
print(f"  Scores: {consensus['voting_scores']}")
