# Sharpe Nova OS — Current State

**Effective date:** September 18, 2026  
**Reconciliation date:** September 18, 2026  
**Authority:** Architect  
**Coherence review:** Jarvis-Nova CCO  
**Repository role:** governed public current-state projection  
**Canonical corporate accepted-state authority:** `nova-infrastructure-systems/nova-core`

This file is the approved public projection of current Sharpe Nova OS state. It
is not the canonical corporate accepted-state store. Current corporate accepted
state is authoritative only in the private `nova-infrastructure-systems/nova-core`
registry after the exact-head Architect-authorized transfer completed on
August 28, 2026.

## What Nova is

Sharpe Nova OS preserves governed review context for agent-prepared financial
actions before local authority acts.

```text
Agent prepares an action.
Nova structures review context.
Local authority decides.
External systems execute.
Nova does not execute.
```

## Public projection update — September 18, 2026

The public projection now distinguishes Nova's bounded **retail agent plane**
from the separate **institutional target-v2 plane**.

```yaml
public_projection_current_state:
  retail_agent_plane:
    public_machine_commerce_surface: live
    network: Base_mainnet
    payment_asset: USDC
    payment_protocol: x402_v2
    public_resources: 4
    authority_effect: none
    approval_effect: none
    execution_effect: none
    access_effect: context_resource_access_only

  institutional_plane:
    canonical_direction: target_v2_non_authority_review_context
    target_v2_runtime_implemented: false
    target_v2_production_active: false
    institutional_pilot_started: false
    system_wide_production_readiness: not_established

  authority_boundary:
    local_authority_decides: true
    external_systems_execute: true
    Nova_executes: false
```

The retail public service does not create institutional identity, workflow
authorization, institutional production activation, or capital authority.
Payment buys bounded context access only.

The four public resources are:

| Resource | Price | Job |
|---|---:|---|
| State Ping | 0.002 USDC | What context exists? |
| Context Delta | 0.02 USDC | What materially changed? |
| Governed Review Context | 0.10 USDC | What review context belongs around this exact proposed action? |
| Decision Context Packet | 1.00 USDC | What portable integrity-bound review artifact should local authority receive? |

The permanent capital boundary remains:

> **NO SECOND PAYMENT without separate explicit capital authorization.**


## Public projection sanitization — September 18, 2026

The Architect separately authorized deletion-bearing sanitization of this public
repository after private-source continuity, stabilization observation, and CCO
completion review were satisfied. That authority is repository-scoped only.

```yaml
public_projection_sanitization:
  Architect_authorized: true
  authorized_at: 2026-09-18
  scope: public_repository_current_tree_only
  production_change_authorized: false
  deployment_authorized: false
  payment_or_settlement_authorized: false
  capital_movement_authorized: false
  retired_grant_program_material_current_tree_retention: false
```

Removed paths remain available through Git history. The canonical production
implementation and corporate accepted state remain private.

## Repository architecture transition

```yaml
repository_architecture:

  public_repository:
    repository: nova-infrastructure-systems/sharpe-nova-os
    role: NON_AUTHORITATIVE_GOVERNED_PROJECTION
    current_corporate_accepted_state_claims_permitted: false
    historical_governance_and_public_contracts_retained: true

  private_repository:
    repository: nova-infrastructure-systems/nova-core
    visibility: private
    role: CANONICAL_CORPORATE_ACCEPTED_STATE_AUTHORITY
    provisioned: true
    public_history_imported: true
    migration_parity_verified: true
    public_source_SHA: eeba729534088bdec705e84219188bb5aaaa14eb
    private_bootstrap_merged: true
    private_bootstrap_CI: passed
    current_production_implementation_source_observed: true
    future_production_development_surface: true

  accepted_state_authority:
    current: nova-infrastructure-systems/nova-core
    transfer_status: EFFECTIVE_REPOSITORY_VERIFIED
    authorization_reference: ARCHITECT-AUTH-CANONICAL-TRANSFER-2026-08-28-B3FB1A8-F50BC42
    authorized_starting_public_head: b3fb1a8fc0c395759c46e4cdc9c9fe4b07006317
    authorized_starting_private_head: f50bc4295b0463779f34c22219a64fc578656abd
    public_projection_merge_commit: 2b7c5361090f04de95b898f2bb8746ae86f305af
    private_effective_transfer_merge_commit: 037a24c68c0ecb4cb4a98354c5ec2667a1f75672
    private_completion_evidence_merge_commit: 052cdaf256c846489bc12b54a5b698411247fc90

  public_private_boundary:
    governance_accepted: true
    authority_transfer_complete: true
    production_source_cutover_observed_complete: true
    public_projection_hygiene: complete
    public_sanitization_complete: true
    public_sanitization_PR: 68
    public_sanitization_merge_commit: 738988184d5dcf545c66362ae402e0b604f8cf21

  private_main_protection:
    status: BLOCKED_BY_PLATFORM_POLICY
    privacy_weakened_to_enable_protection: false
    compensating_controls_required: true

deployment_reconciliation:
  public_repository_dependency_recorded_historically: true

  primary_continuity_service:
    service: nova-api
    source_repository: nova-infrastructure-systems/nova-core
    source_branch: main
    deployed_source_commit: d64e7523177f666a7d549a087fc763b5edc4e957
    source_main_match_at_observation: true
    manual_deploy_observed: true
    provider_live_observed: true
    existing_hostname_preserved: true
    auto_deploy: Off
    post_cutover_health_200_observed: true
    post_cutover_tested_containment_observed: true
    post_cutover_active_identity_count: 3
    post_cutover_credential_fingerprint_parity_observed: true
    post_cutover_authentication_3_of_3_observed: true
    evidence_level: operator_observed

  parallel_private_continuity_candidate:
    deployed: true
    private_source_alignment_observed: true
    health_and_tested_containment_parity_observed: true
    credential_state_parity_observed: true
    credential_authentication_3_of_3_observed: true
    rollback_mechanism_exercised: true
    rollback_auto_credential_preservation: false
    post_rollback_recovery_observed: true
    evidence_level: operator_observed

  provider_evidence_receipt_state: evidence_submitted_private
  private_repoint_required_before_runtime_removal: true
  private_repoint_completed: true
  intentional_cutover_completed: true
  public_repository_dependency_for_observed_active_production_runtime: false
  post_cutover_public_contract_validation: repository_verified_complete
  post_cutover_private_implementation_validation: repository_verified_complete
  removal_gate: SATISFIED_FOR_PR_68_REPOSITORY_SANITIZATION

repository_transition_effects:
  parallel_provider_continuity_candidate_effect: observed_live
  canonical_production_cutover_effect: operator_observed_private_source_live
  public_runtime_removal_effect: none
  accepted_state_authority_transfer_effect: effective_repository_verified
  canonical_corporate_state_changed: true
  cross_agent_current_use_set_changed: false
  retail_runtime_effect: none
  payment_effect: none
  institutional_Gate_5_effect: none
  institutional_data_effect: none
  chronology_effect: none
  institutional_Reflex_Memory_effect: none
```

The accepted-state authority transfer is complete at the repository-governance
layer. The private `nova-core` registry is the sole canonical corporate
accepted-state authority. This public repository is now a governed projection:
it may publish approved doctrine, contracts, schemas, interoperability material,
and externally supportable state, but its retained accepted-state registry is
historical projection only and must not be used for current corporate
accepted-state claims.

The transfer did not authorize deletion of the public runtime or any public
production-supporting surface. It did not create chronology, Reflex Memory
acceptance, payment or settlement authority, institutional Gate 5 authority,
production runtime changes, or capital authority.

The rollback exercise established that provider recovery and authenticated
continuity are separate controls: provider-held identity state was not
automatically preserved by rollback and required restoration plus revalidation.
The primary cutover therefore preserved a recovery rule that requires provider
identity-state verification after any future rollback.

## Current product state

```yaml
current_product_state:
  projection_role: governed_public_projection
  canonical_corporate_accepted_state_source: nova-infrastructure-systems/nova-core
  canonical_direction: target_v2_non_authority_review_context

  retail_agent_plane:
    public_service_live: true
    network: Base_mainnet
    payment_asset: USDC
    payment_protocol: x402_v2
    four_public_resources_live: true
    authority_effect: none
    approval_effect: none
    execution_effect: none
    access_effect: context_resource_access_only

  Legacy_v1:
    implemented: true
    canonical_future_external_model: false
    new_external_integrations_permitted: false
    consumer_dependency: conditional_pass_no_external_consumers_observed
    external_compatibility_window_required: false
    safe_to_retire: false

  production_custody:
    GitHub_corporate_repository: nova-infrastructure-systems/nova-core
    active_primary_service: nova-api
    active_primary_source_repository: nova-infrastructure-systems/nova-core
    active_primary_source_branch: main
    active_primary_source_commit: d64e7523177f666a7d549a087fc763b5edc4e957
    private_source_cutover: operator_observed_live
    primary_hostname_continuity: operator_observed
    primary_health_post_cutover: operator_observed_200
    primary_tested_containment_post_cutover: operator_observed
    active_credential_set_post_cutover: operator_observed_3_of_3
    active_credential_authentication_post_cutover: operator_observed_3_of_3
    parallel_private_continuity_candidate: operator_observed_live
    rollback_mechanism_exercised: true
    rollback_auto_credential_preservation: false
    post_rollback_recovery: operator_observed
    public_repository_dependency_for_observed_active_production_runtime: false
    post_cutover_repository_validation: repository_verified_complete
    CDP_custody: Architect_attested_Admin_Owner
    CDP_API_key_management: true
    CDP_active_API_keys: 1
    CDP_business_verification_status: pending
    CDP_x402_or_facilitator_enabled: false
    CDP_current_Nova_integration_present: false
    CDP_settlement_configuration_present: false
    linked_settlement_destination_present: false
    full_gate_status: conditional_pass

  readiness_baseline:
    status: closed
    production_incident_disposition: contained_historically_unattested
    historical_CDP_retention_complete: false

  target_v2:
    canonical_contract: design-v2.1
    Gate_3: complete

    private_synthetic_reference_adapter:
      implemented: true
      scope: private_synthetic_reference_only
      runtime_effect: none
      public_endpoint_effect: none
      production_effect: none
      canonicality_source: authoritative_repository_main
      canonicality_repository: nova-infrastructure-systems/nova-core

    Gate_4: complete

    Gate_5_Entry_Design_Review:
      status: COMPLETE
      artifact: institutional_exposure_contract_v0.1
      scope: institutional_exposure_contract_only
      canonicality_source: authoritative_repository_main
      canonicality_repository: nova-infrastructure-systems/nova-core

    Gate_5_authorization_preconditions:
      status: NOT_YET_SATISFIED
      preconditions_not_yet_evidenced: 18
      silently_resolved: false

    Gate_5:
      status: NOT_STARTED
      authority: false

    institutional_pilot:
      authorized: false
      started: false

    runtime_implemented: false
    production_active: false
    runtime_implementation_authority: false
    production_activation_authority: false
    system_wide_production_readiness: not_established

  Phase_1:
    offline_proof_chain: completed
    repository_validation: passed
    system_wide_production_readiness: not_established
    market_validation: not_established
    buyer_validation: not_established

  institutional_use:
    bounded_pilot: not_started
    operator_dependency: not_established
    adoption: not_established

  commercialization:
    retail_agent_plane:
      public_service_live: true
      Base_USDC_x402_v2_live: true
      fixed_resource_pricing_live: true
      Marketplace_submission_sent: true
      Marketplace_listing_independently_verified: false
      Marketplace_discovery_established: false
    institutional_plane:
      marketplace_activation: false
      x402_as_identity_or_authority: false
      production_activation: false
      capital_authority: false
    buyer_demand_established: false
    recurring_paid_usage_established: false
    product_market_fit_established: false
```

## What exists today

The repository and current evidence establish:

* a separately bounded live retail machine-commerce surface on Base mainnet using USDC and x402 v2;
* four independently priced public context resources: State Ping, Context Delta, Governed Review Context, and Decision Context Packet;
* explicit `authority_effect: none`, `approval_effect: none`, and `execution_effect: none` across those resources;
* payment isolation: access to one resource does not authorize purchase of another;

* the implemented Legacy v1 runtime;
* the approved non-authority target v2 contract;
* an offline Phase 1 proof chain;
* deterministic repository validation;
* governance, chronology, source, and authority specifications;
* a bounded stablecoin-treasury workflow definition;
* production-readiness and incident-control gates;
* a governed public projection repository at `nova-infrastructure-systems/sharpe-nova-os`;
* a private implementation and canonical corporate accepted-state repository at `nova-infrastructure-systems/nova-core`;
* an exact-head Architect-authorized accepted-state authority transfer from public starting head `b3fb1a8fc0c395759c46e4cdc9c9fe4b07006317` to private starting head `f50bc4295b0463779f34c22219a64fc578656abd`;
* GitHub-verified public projection merge `2b7c5361090f04de95b898f2bb8746ae86f305af`;
* GitHub-verified private effective-transfer merge `037a24c68c0ecb4cb4a98354c5ec2667a1f75672` and completion-evidence merge `052cdaf256c846489bc12b54a5b698411247fc90`;
* preservation of the accepted-state payload and historical provenance through the transfer;
* verified repository identity reconciliation through PR #38;
* merged readiness reconciliation through PR #39;
* an operator-observed in-place source repoint of the existing `nova-api` Render service to private `nova-core/main`;
* an operator-observed manual production deployment of private commit `d64e7523177f666a7d549a087fc763b5edc4e957` on the preserved primary hostname;
* operator-observed post-cutover `/health` HTTP 200 on the primary service;
* operator-observed post-cutover containment on `/openapi.json`, `/docs`, `/redoc`, `/services.json`, the tested constraint-pressure feed, and unauthenticated context/proof routes;
* operator-observed post-cutover parity of the complete three-identity active production credential set;
* operator-observed post-cutover three-of-three authenticated HTTP 200 behavior;
* a live parallel private continuity candidate retained as a comparison/fallback reference during stabilization;
* an exercised provider rollback on the private continuity candidate;
* a demonstrated rollback failure mode in which provider-held credential state was not automatically preserved;
* successful operator-observed restoration of credential state and three-of-three authenticated continuity after rollback;
* repository-verified completion of the post-cutover public-contract and private-implementation validation gate, with detailed operating evidence retained privately and in Git history;
* Architect-attested CDP Admin/Owner access with project-setting and API-key management authority;
* one active CDP API key classified founder/internal;
* Architect-attested current CDP x402/facilitator disabled state;
* Architect-attested absence of a current Nova CDP integration;
* Architect-attested absence of settlement configuration and linked settlement destination;
* a current visible CDP payment/settlement summary showing zero entries, zero successful settlements, and zero failed settlements;
* an Architect-attested Legacy v1 key and route-history review with no external consumers observed in the reviewed evidence;
* an external public-boundary check matching the repository-defined containment contract;
* Architect approval of the final production/discovery incident disposition as `CONTAINED_HISTORICALLY_UNATTESTED`;
* a closed Readiness Gate Baseline;
* a canonical private synthetic target-v2 reference adapter with no runtime,
  public-endpoint, production, or authority effect.

## What does not exist today

The available evidence does not establish:

* authorization to remove the public runtime or its production-supporting implementation surface;
* independently verified full provider-side cutover or rollback attestation;
* automatic provider-held credential preservation across rollback;
* a deployed target v2 runtime;
* a production-active target v2 endpoint;
* independently verified full provider-side production-custody attestation;
* independently verified Legacy v1 consumer history across all retention periods;
* complete historical CDP activity or settlement history;
* a provider-stated historical retention boundary for the observed x402 Payments surface;
* a live institutional pilot;
* demonstrated operator dependency;
* buyer pull;
* adoption;
* product-market fit;
* pricing power;
* institutional x402 as identity, workflow authorization, approval, or capital authority;
* live Arc production support;
* live Circle Gateway verification or settlement through Nova;
* authority to move, approve, sign, or settle capital.

## Current implementation priority

The accepted-state authority transfer, private-source continuity work, and
authorized public-repository sanitization are complete. The public repository is
now the bounded external contract/proof surface; canonical production machinery,
corporate accepted state, and internal operating evidence remain private.

PR #68 consumed the Architect's September 18, 2026 deletion authority for that
specific repository sanitization. Git history remains preserved. No standing
deletion authority or production authority is created by that completed action.

Gate 5 remains not started and has no implementation or production-activation
authority.

```yaml
current_readiness_priority:
  Gate_1_production_custody:
    status: conditional_pass
    limitations:
      - provider_control_planes_not_independently_verified
      - founder_concentration_remains
      - CDP_business_verification_pending
      - rollback_requires_provider_identity_state_revalidation

  Gate_2_Legacy_v1_dependency:
    status: conditional_pass
    limitations:
      - evidence_Architect_attested_not_independently_verified
      - historical_retention_not_proven_complete

  repository_transition:
    status: authority_transfer_complete_repository_validation_complete_stabilization_complete
    accepted_state_authority: nova-infrastructure-systems/nova-core
    public_repository_role: NON_AUTHORITATIVE_GOVERNED_PROJECTION
    provider_continuity_evidence: evidence_submitted
    intentional_cutover: operator_observed_complete
    primary_source_private: true
    public_repository_dependency_for_observed_active_production_runtime: false
    public_contract_validation: repository_verified_complete
    private_implementation_validation: repository_verified_complete
    public_current_tree_sanitization: complete_PR_68
    public_runtime_service_removal: not_performed
    production_effect_from_sanitization: none

  production_incident:
    status: contained_historically_unattested
    active_exposure_closed: true
    historical_retention_gap_preserved: true

  Readiness_Gate_Baseline:
    status: closed

  Gate_3_v2_field_derivation:
    status: complete
    implementation_authority: false
    production_activation_authority: false

  canonical_contract:
    status: design-v2.1

  Gate_4_private_synthetic_adapter:
    status: complete
    artifact: private_synthetic_reference_adapter
    scope: private_synthetic_reference_only
    canonicality_source: authoritative_repository_main
    canonicality_repository: nova-infrastructure-systems/nova-core
    runtime_effect: none
    public_endpoint_effect: none
    production_effect: none
    target_v2_runtime: not_implemented
    target_v2_production: not_active
    system_wide_production_readiness: not_established
    production_activation_authority: false

  Gate_5_Entry_Design_Review:
    status: COMPLETE
    artifact: institutional_exposure_contract_v0.1
    scope: institutional_exposure_contract_only
    canonicality_source: authoritative_repository_main
    canonicality_repository: nova-infrastructure-systems/nova-core

  Gate_5_authorization_preconditions:
    status: NOT_YET_SATISFIED
    preconditions_not_yet_evidenced: 18
    silently_resolved: false

  Gate_5_bounded_institutional_pilot:
    status: not_started
    authority: false
    institutional_pilot:
      authorized: false
      started: false
    implementation_authority: false
    production_activation_authority: false
```

A future production progression would remain one bounded private target v2
review context for an agent-prepared stablecoin treasury action. The Gate 4
reference implementation preserves the completed Gate 3 design:

* stable action identity;
* proposal-version identity;
* source authority and observation time;
* constraint context;
* missing, stale, conflicting, and unavailable state;
* the local-authority boundary;
* reconstructable review context;
* deterministic proof canonicalization.

It must not approve, authorize, sign, settle, or execute the action.

## Product generations

* [Legacy v1](docs/legacy-v1/README.md)
* [Target v2](docs/target-v2/README.md)

## Readiness detail

See:

* [Production Readiness Register](docs/operations/production-readiness-register.md)
* [Phase 1 Inspection Status](docs/inspection/phase-1-inspection-status.md)

Detailed production-readiness, incident, and post-cutover operating receipts are
retained in the private operating-evidence surface and Git history. They are not
part of the current public tree.

## Evidence boundary

Repository ownership, protected public merges, private transfer merges, the
canonical accepted-state authority transition, and the post-cutover repository
validation described above are independently verified through GitHub repository
evidence. Render, Legacy v1, private continuity, rollback, cutover, and CDP
control-plane observations remain Architect-attested or operator-observed unless
separately identified as independently verified.

The private continuity and immediate cutover proof establish submitted evidence
for tested private-source alignment, preserved hostname, containment, complete
credential parity, three-of-three authentication, rollback mechanics, and
recovery. They do not establish independent provider verification. Public-tree
sanitization authority was separately granted by the Architect and consumed by
PR #68; accepted-state authority transfer remains separately established by its
own exact-head authorization and verified public/private transfer chain.

The rollback exercise specifically demonstrated that provider-held credential
state may require restoration and revalidation even when the provider reports
the service Live and `/health` remains healthy.

The current CDP x402/facilitator and settlement configuration is attested as
disabled. The visible CDP payment summary shows zero activity, but the portal
does not expose a review window or retention boundary sufficient to establish
that no historical CDP verification or settlement activity ever occurred.

The approved disposition `CONTAINED_HISTORICALLY_UNATTESTED` closes the active
exposure while preserving that historical unknown. It must not be interpreted
as proof of zero historical activity.

Coinbase business verification for Nova Infrastructure Systems Corporation is
currently pending. That is a provider-onboarding state, not evidence of Nova
institutional adoption, buyer validation, or enterprise readiness.

## Claim rule

A generic repository artifact, passing test suite, design approval, offline
proof, Architect-attested provider observation, operator-observed continuity or
cutover test, closed readiness baseline, or contained incident does not
independently establish system-wide production readiness, institutional use,
buyer demand, adoption, pricing power, product-market fit, deletion authority,
or production authority. The completed public sanitization and accepted-state
transfer each relied on separate explicit Architect authorization and must not be
treated as standing authority for future actions.