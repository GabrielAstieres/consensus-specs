      Exception: ['class Fork(Container):\n    previous_version: Version\n    current_version: Version\n    epoch: Epoch  # Epoch of latest fork', 'class ForkData(Container):\n    current_version:
      Version\n    genesis_validators_root: Root', 'class Checkpoint(Container):\n    epoch: Epoch\n    root: Root', 'class Validator(Container):\n    pubkey: BLSPubkey\n    withdrawal_credentials:
      Bytes32  # Commitment to pubkey for withdrawals\n    effective_balance: Gwei  # Balance at stake\n    slashed: boolean\n    # Status epochs\n    activation_eligibility_epoch: Epoch  # When
      criteria for activation were met\n    activation_epoch: Epoch\n    exit_epoch: Epoch\n    withdrawable_epoch: Epoch  # When validator can withdraw funds', 'class AttestationData(Container):\n
      slot: Slot\n    index: CommitteeIndex\n    # LMD GHOST vote\n    beacon_block_root: Root\n    # FFG vote\n    source: Checkpoint\n    target: Checkpoint', 'class IndexedAttestation(Container):\n
      attesting_indices: List[ValidatorIndex, MAX_VALIDATORS_PER_COMMITTEE]\n    data: AttestationData\n    signature: BLSSignature', 'class PendingAttestation(Container):\n    aggregation_bits:
      Bitlist[MAX_VALIDATORS_PER_COMMITTEE]\n    data: AttestationData\n    inclusion_delay: Slot\n    proposer_index: ValidatorIndex', 'class Eth1Data(Container):\n    deposit_root:
      Root\n    deposit_count: uint64\n    block_hash: Hash32', 'class HistoricalBatch(Container):\n    block_roots: Vector[Root, SLOTS_PER_HISTORICAL_ROOT]\n    state_roots: Vector[Root,
      SLOTS_PER_HISTORICAL_ROOT]', 'class DepositMessage(Container):\n    pubkey: BLSPubkey\n    withdrawal_credentials: Bytes32\n    amount: Gwei', 'class DepositData(Container):\n    pubkey:
      BLSPubkey\n    withdrawal_credentials: Bytes32\n    amount: Gwei\n    signature: BLSSignature  # Signing over DepositMessage', 'class BeaconBlockHeader(Container):\n    slot:
      Slot\n    proposer_index: ValidatorIndex\n    parent_root: Root\n    state_root: Root\n    body_root: Root', 'class SigningData(Container):\n    object_root: Root\n    domain: Domain',
      'class ProposerSlashing(Container):\n    signed_header_1: SignedBeaconBlockHeader\n    signed_header_2: SignedBeaconBlockHeader', 'class AttesterSlashing(Container):\n    attestation_1:
      IndexedAttestation\n    attestation_2: IndexedAttestation', 'class Attestation(Container):\n    aggregation_bits: Bitlist[MAX_VALIDATORS_PER_COMMITTEE]\n    data: AttestationData\n    signature:
      BLSSignature', 'class Deposit(Container):\n    proof: Vector[Bytes32, DEPOSIT_CONTRACT_TREE_DEPTH + 1]  # Merkle path to deposit root\n    data: DepositData', 'class VoluntaryExit(Container):\n
      epoch: Epoch  # Earliest epoch when voluntary exit can be processed\n    validator_index: ValidatorIndex', 'class BeaconBlockBody(Container):\n    randao_reveal: BLSSignature\n    eth1_data:
      Eth1Data  # Eth1 data vote\n    graffiti: Bytes32  # Arbitrary data\n    # Operations\n    proposer_slashings: List[ProposerSlashing, MAX_PROPOSER_SLASHINGS]\n    attester_slashings:
      List[AttesterSlashing, MAX_ATTESTER_SLASHINGS]\n    attestations: List[Attestation, MAX_ATTESTATIONS]\n    deposits: List[Deposit, MAX_DEPOSITS]\n    voluntary_exits: List[SignedVoluntaryExit,
      MAX_VOLUNTARY_EXITS]', 'class BeaconBlock(Container):\n    slot: Slot\n    proposer_index: ValidatorIndex\n    parent_root: Root\n    state_root: Root\n    body: BeaconBlockBody', 'class
      BeaconState(Container):\n    # Versioning\n    genesis_time: uint64\n    genesis_validators_root: Root\n    slot: Slot\n    fork: Fork\n    # History\n    latest_block_header: BeaconBlockHeader\n
      block_roots: Vector[Root, SLOTS_PER_HISTORICAL_ROOT]\n    state_roots: Vector[Root, SLOTS_PER_HISTORICAL_ROOT]\n    historical_roots: List[Root, HISTORICAL_ROOTS_LIMIT]\n    # Eth1\n
      eth1_data: Eth1Data\n    eth1_data_votes: List[Eth1Data, EPOCHS_PER_ETH1_VOTING_PERIOD * SLOTS_PER_EPOCH]\n    eth1_deposit_index: uint64\n    # Registry\n    validators: List[Validator,
      VALIDATOR_REGISTRY_LIMIT]\n    balances: List[Gwei, VALIDATOR_REGISTRY_LIMIT]\n    # Randomness\n    randao_mixes: Vector[Bytes32, EPOCHS_PER_HISTORICAL_VECTOR]\n    # Slashings\n    slashings:
      Vector[Gwei, EPOCHS_PER_SLASHINGS_VECTOR]  # Per-epoch sums of slashed effective balances\n    # Attestations\n    previous_epoch_attestations: List[PendingAttestation, MAX_ATTESTATIONS *
      SLOTS_PER_EPOCH]\n    current_epoch_attestations: List[PendingAttestation, MAX_ATTESTATIONS * SLOTS_PER_EPOCH]\n    # Finality\n    justification_bits: Bitvector[JUSTIFICATION_BITS_LENGTH]  #
      Bit set for every recent justified epoch\n    previous_justified_checkpoint: Checkpoint  # Previous epoch snapshot\n    current_justified_checkpoint: Checkpoint\n    finalized_checkpoint:
      Checkpoint', 'class SignedVoluntaryExit(Container):\n    message: VoluntaryExit\n    signature: BLSSignature', 'class SignedBeaconBlock(Container):\n    message: BeaconBlock\n    signature:
      BLSSignature', 'class SignedBeaconBlockHeader(Container):\n    message: BeaconBlockHeader\n    signature: BLSSignature', 'def integer_squareroot(n: uint64) -> uint64:\n    """\n    Return the
      largest integer ``x`` such that ``x**2 <= n``.\n    """\n    if n == UINT64_MAX:\n        return UINT64_MAX_SQRT\n    x = n\n    y = (x + 1) // 2\n    while y < x:\n        x = y\n        y
      = (x + n // x) // 2\n    return x', 'def xor(bytes_1: Bytes32, bytes_2: Bytes32) -> Bytes32:\n    """\n    Return the exclusive-or of two 32-byte strings.\n    """\n    return Bytes32(a
      ^ b for a, b in zip(bytes_1, bytes_2))', 'def bytes_to_uint64(data: bytes) -> uint64:\n    """\n    Return the integer deserialization of ``data`` interpreted as ``ENDIANNESS``-endian.\n
      """\n    return uint64(int.from_bytes(data, ENDIANNESS))', 'def saturating_sub(a: int, b: int) -> int:\n    """\n    Computes a - b, saturating at numeric bounds.\n    """\n    return a
      - b if a > b else 0', 'def is_active_validator(validator: Validator, epoch: Epoch) -> bool:\n    """\n    Check if ``validator`` is active.\n    """\n    return validator.activation_epoch
      <= epoch < validator.exit_epoch', 'def is_eligible_for_activation_queue(validator: Validator) -> bool:\n    """\n    Check if ``validator`` is eligible to be placed into the activation
      queue.\n    """\n    return (\n        validator.activation_eligibility_epoch == FAR_FUTURE_EPOCH\n        and validator.effective_balance == MAX_EFFECTIVE_BALANCE\n    )', 'def
      is_eligible_for_activation(state: BeaconState, validator: Validator) -> bool:\n    """\n    Check if ``validator`` is eligible for activation.\n    """\n    return (\n        # Placement
      in queue is finalized\n        validator.activation_eligibility_epoch <= state.finalized_checkpoint.epoch\n        # Has not yet been activated\n        and validator.activation_epoch ==
      FAR_FUTURE_EPOCH\n    )', 'def is_slashable_validator(validator: Validator, epoch: Epoch) -> bool:\n    """\n    Check if ``validator`` is slashable.\n    """\n    return (not validator.slashed)
      and (validator.activation_epoch <= epoch < validator.withdrawable_epoch)', 'def is_slashable_attestation_data(data_1: AttestationData, data_2: AttestationData) -> bool:\n    """\n    Check if
      ``data_1`` and ``data_2`` are slashable according to Casper FFG rules.\n    """\n    return (\n        # Double vote\n        (data_1 != data_2 and data_1.target.epoch == data_2.target.epoch)
      or\n        # Surround vote\n        (data_1.source.epoch < data_2.source.epoch and data_2.target.epoch < data_1.target.epoch)\n    )', 'def is_valid_indexed_attestation(state: BeaconState,
      indexed_attestation: IndexedAttestation) -> bool:\n    """\n    Check if ``indexed_attestation`` is not empty, has sorted and unique indices and has a valid aggregate signature.\n    """\n    #
      Verify indices are sorted and unique\n    indices = indexed_attestation.attesting_indices\n    if len(indices) == 0 or not indices == sorted(set(indices)):\n        return False\n    # Verify
      aggregate signature\n    pubkeys = [state.validators[i].pubkey for i in indices]\n    domain = get_domain(state, DOMAIN_BEACON_ATTESTER, indexed_attestation.data.target.epoch)\n    signing_root
      = compute_signing_root(indexed_attestation.data, domain)\n    return bls.FastAggregateVerify(pubkeys, signing_root, indexed_attestation.signature)', 'def is_valid_merkle_branch(leaf: Bytes32,
      branch: Sequence[Bytes32], depth: uint64, index: uint64, root: Root) -> bool:\n    """\n    Check if ``leaf`` at ``index`` verifies against the Merkle ``root`` and ``branch``.\n    """\n    value
      = leaf\n    for i in range(depth):\n        if index // (2**i) % 2:\n            value = hash(branch[i] + value)\n        else:\n            value = hash(value + branch[i])\n    return value ==
      root', 'def compute_shuffled_index(index: uint64, index_count: uint64, seed: Bytes32) -> uint64:\n    """\n    Return the shuffled index corresponding to ``seed`` (and ``index_count``).\n    """\n
      assert index < index_count\n\n    # Swap or not (https://link.springer.com/content/pdf/10.1007%2F978-3-642-32009-5_1.pdf)\n    # See the \'generalized domain\' algorithm on page 3\n    for
      current_round in range(SHUFFLE_ROUND_COUNT):\n        pivot = bytes_to_uint64(hash(seed + uint_to_bytes(uint8(current_round)))[0:8]) % index_count\n        flip = (pivot + index_count - index)
      % index_count\n        position = max(index, flip)\n        source = hash(\n            seed\n            + uint_to_bytes(uint8(current_round))\n            + uint_to_bytes(uint32(position
      // 256))\n        )\n        byte = uint8(source[(position % 256) // 8])\n        bit = (byte >> (position % 8)) % 2\n        index = flip if bit else index\n\n    return index', 'def
      compute_proposer_index(state: BeaconState, indices: Sequence[ValidatorIndex], seed: Bytes32) -> ValidatorIndex:\n    """\n    Return from ``indices`` a random index sampled by effective balance.\n
      """\n    assert len(indices) > 0\n    MAX_RANDOM_BYTE = 2**8 - 1\n    i = uint64(0)\n    total = uint64(len(indices))\n    while True:\n        candidate_index = indices[compute_shuffled_index(i
      % total, total, seed)]\n        random_byte = hash(seed + uint_to_bytes(uint64(i // 32)))[i % 32]\n        effective_balance = state.validators[candidate_index].effective_balance\n        if
      effective_balance * MAX_RANDOM_BYTE >= MAX_EFFECTIVE_BALANCE * random_byte:\n            return candidate_index\n        i += 1', 'def compute_committee(indices: Sequence[ValidatorIndex],\n
      seed: Bytes32,\n                      index: uint64,\n                      count: uint64) -> Sequence[ValidatorIndex]:\n    """\n    Return the committee corresponding to
      ``indices``, ``seed``, ``index``, and committee ``count``.\n    """\n    start = (len(indices) * index) // count\n    end = (len(indices) * uint64(index + 1)) // count\n    return
      [indices[compute_shuffled_index(uint64(i), uint64(len(indices)), seed)] for i in range(start, end)]', 'def compute_epoch_at_slot(slot: Slot) -> Epoch:\n    """\n    Return the epoch number at
      ``slot``.\n    """\n    return Epoch(slot // SLOTS_PER_EPOCH)', 'def compute_start_slot_at_epoch(epoch: Epoch) -> Slot:\n    """\n    Return the start slot of ``epoch``.\n    """\n    return
      Slot(epoch * SLOTS_PER_EPOCH)', 'def compute_activation_exit_epoch(epoch: Epoch) -> Epoch:\n    """\n    Return the epoch during which validator activations and exits initiated in ``epoch``
      take effect.\n    """\n    return Epoch(epoch + 1 + MAX_SEED_LOOKAHEAD)', 'def compute_fork_data_root(current_version: Version, genesis_validators_root: Root) -> Root:\n    """\n    Return
      the 32-byte fork data root for the ``current_version`` and ``genesis_validators_root``.\n    This is used primarily in signature domains to avoid collisions across forks/chains.\n    """\n
      return hash_tree_root(ForkData(\n        current_version=current_version,\n        genesis_validators_root=genesis_validators_root,\n    ))', 'def compute_fork_digest(current_version:
      Version, genesis_validators_root: Root) -> ForkDigest:\n    """\n    Return the 4-byte fork digest for the ``current_version`` and ``genesis_validators_root``.\n    This is a digest
      primarily used for domain separation on the p2p layer.\n    4-bytes suffices for practical separation of forks/chains.\n    """\n    return ForkDigest(compute_fork_data_root(current_version,
      genesis_validators_root)[:4])', 'def compute_domain(domain_type: DomainType, fork_version: Version=None, genesis_validators_root: Root=None) -> Domain:\n    """\n    Return the domain for the
      ``domain_type`` and ``fork_version``.\n    """\n    if fork_version is None:\n        fork_version = GENESIS_FORK_VERSION\n    if genesis_validators_root is None:\n        genesis_validators_root
      = Root()  # all bytes zero by default\n    fork_data_root = compute_fork_data_root(fork_version, genesis_validators_root)\n    return Domain(domain_type + fork_data_root[:28])', 'def
      compute_signing_root(ssz_object: SSZObject, domain: Domain) -> Root:\n    """\n    Return the signing root for the corresponding signing data.\n    """\n    return hash_tree_root(SigningData(\n
      object_root=hash_tree_root(ssz_object),\n        domain=domain,\n    ))', 'def get_current_epoch(state: BeaconState) -> Epoch:\n    """\n    Return the current epoch.\n    """\n    return
      compute_epoch_at_slot(state.slot)', 'def get_previous_epoch(state: BeaconState) -> Epoch:\n    """`\n    Return the previous epoch (unless the current epoch is ``GENESIS_EPOCH``).\n    """\n
      current_epoch = get_current_epoch(state)\n    return GENESIS_EPOCH if current_epoch == GENESIS_EPOCH else Epoch(current_epoch - 1)', 'def get_block_root(state: BeaconState, epoch: Epoch) -> Root:\n
      """\n    Return the block root at the start of a recent ``epoch``.\n    """\n    return get_block_root_at_slot(state, compute_start_slot_at_epoch(epoch))', 'def get_block_root_at_slot(state:
      BeaconState, slot: Slot) -> Root:\n    """\n    Return the block root at a recent ``slot``.\n    """\n    assert slot < state.slot <= slot + SLOTS_PER_HISTORICAL_ROOT\n    return
      state.block_roots[slot % SLOTS_PER_HISTORICAL_ROOT]', 'def get_randao_mix(state: BeaconState, epoch: Epoch) -> Bytes32:\n    """\n    Return the randao mix at a recent ``epoch``.\n    """\n
      return state.randao_mixes[epoch % EPOCHS_PER_HISTORICAL_VECTOR]', 'def get_active_validator_indices(state: BeaconState, epoch: Epoch) -> Sequence[ValidatorIndex]:\n    """\n    Return the sequence
      of active validator indices at ``epoch``.\n    """\n    return [ValidatorIndex(i) for i, v in enumerate(state.validators) if is_active_validator(v, epoch)]', 'def get_validator_churn_limit(state:
      BeaconState) -> uint64:\n    """\n    Return the validator churn limit for the current epoch.\n    """\n    active_validator_indices = get_active_validator_indices(state,
      get_current_epoch(state))\n    return max(MIN_PER_EPOCH_CHURN_LIMIT, uint64(len(active_validator_indices)) // CHURN_LIMIT_QUOTIENT)', 'def get_seed(state: BeaconState, epoch: Epoch,
      domain_type: DomainType) -> Bytes32:\n    """\n    Return the seed at ``epoch``.\n    """\n    mix = get_randao_mix(state, Epoch(epoch + EPOCHS_PER_HISTORICAL_VECTOR - MIN_SEED_LOOKAHEAD -
      1))  # Avoid underflow\n    return hash(domain_type + uint_to_bytes(epoch) + mix)', 'def get_committee_count_per_slot(state: BeaconState, epoch: Epoch) -> uint64:\n    """\n    Return the
      number of committees in each slot for the given ``epoch``.\n    """\n    return max(uint64(1), min(\n        MAX_COMMITTEES_PER_SLOT,\n        uint64(len(get_active_validator_indices(state,
      epoch))) // SLOTS_PER_EPOCH // TARGET_COMMITTEE_SIZE,\n    ))', 'def get_beacon_committee(state: BeaconState, slot: Slot, index: CommitteeIndex) -> Sequence[ValidatorIndex]:\n    """\n
      Return the beacon committee at ``slot`` for ``index``.\n    """\n    epoch = compute_epoch_at_slot(slot)\n    committees_per_slot = get_committee_count_per_slot(state, epoch)\n    return
      compute_committee(\n        indices=get_active_validator_indices(state, epoch),\n        seed=get_seed(state, epoch, DOMAIN_BEACON_ATTESTER),\n        index=(slot % SLOTS_PER_EPOCH) *
      committees_per_slot + index,\n        count=committees_per_slot * SLOTS_PER_EPOCH,\n    )', 'def get_beacon_proposer_index(state: BeaconState) -> ValidatorIndex:\n    """\n    Return the beacon
      proposer index at the current slot.\n    """\n    epoch = get_current_epoch(state)\n    seed = hash(get_seed(state, epoch, DOMAIN_BEACON_PROPOSER) + uint_to_bytes(state.slot))\n    indices
      = get_active_validator_indices(state, epoch)\n    return compute_proposer_index(state, indices, seed)', 'def get_total_balance(state: BeaconState, indices: Set[ValidatorIndex]) -> Gwei:\n
      """\n    Return the combined effective balance of the ``indices``.\n    ``EFFECTIVE_BALANCE_INCREMENT`` Gwei minimum to avoid divisions by zero.\n    Math safe up to ~10B ETH, after which
      this overflows uint64.\n    """\n    return Gwei(max(EFFECTIVE_BALANCE_INCREMENT, sum([state.validators[index].effective_balance for index in indices])))', 'def get_total_active_balance(state:
      BeaconState) -> Gwei:\n    """\n    Return the combined effective balance of the active validators.\n    Note: ``get_total_balance`` returns ``EFFECTIVE_BALANCE_INCREMENT`` Gwei minimum to
      avoid divisions by zero.\n    """\n    return get_total_balance(state, set(get_active_validator_indices(state, get_current_epoch(state))))', 'def get_domain(state: BeaconState, domain_type:
      DomainType, epoch: Epoch=None) -> Domain:\n    """\n    Return the signature domain (fork version concatenated with domain type) of a message.\n    """\n    epoch = get_current_epoch(state)
      if epoch is None else epoch\n    fork_version = state.fork.previous_version if epoch < state.fork.epoch else state.fork.current_version\n    return compute_domain(domain_type, fork_version,
      state.genesis_validators_root)', 'def get_indexed_attestation(state: BeaconState, attestation: Attestation) -> IndexedAttestation:\n    """\n    Return the indexed attestation corresponding
      to ``attestation``.\n    """\n    attesting_indices = get_attesting_indices(state, attestation)\n\n    return IndexedAttestation(\n        attesting_indices=sorted(attesting_indices),\n
      data=attestation.data,\n        signature=attestation.signature,\n    )', 'def get_attesting_indices(state: BeaconState, attestation: Attestation) -> Set[ValidatorIndex]:\n    """\n    Return
      the set of attesting indices corresponding to ``data`` and ``bits``.\n    """\n    committee = get_beacon_committee(state, attestation.data.slot, attestation.data.index)\n    return set(index
      for i, index in enumerate(committee) if attestation.aggregation_bits[i])', 'def increase_balance(state: BeaconState, index: ValidatorIndex, delta: Gwei) -> None:\n    """\n    Increase the
      validator balance at index ``index`` by ``delta``.\n    """\n    state.balances[index] += delta', 'def decrease_balance(state: BeaconState, index: ValidatorIndex, delta: Gwei) -> None:\n    """\n
      Decrease the validator balance at index ``index`` by ``delta``, with underflow protection.\n    """\n    state.balances[index] = 0 if delta > state.balances[index] else state.balances[index] -
      delta', 'def initiate_validator_exit(state: BeaconState, index: ValidatorIndex) -> None:\n    """\n    Initiate the exit of the validator with index ``index``.\n    """\n    # Return if validator
      already initiated exit\n    validator = state.validators[index]\n    if validator.exit_epoch != FAR_FUTURE_EPOCH:\n        return\n\n    # Compute exit queue epoch\n    exit_epochs = [v.exit_epoch
      for v in state.validators if v.exit_epoch != FAR_FUTURE_EPOCH]\n    exit_queue_epoch = max(exit_epochs + [compute_activation_exit_epoch(get_current_epoch(state))])\n    exit_queue_churn
      = len([v for v in state.validators if v.exit_epoch == exit_queue_epoch])\n    if exit_queue_churn >= get_validator_churn_limit(state):\n        exit_queue_epoch += Epoch(1)\n\n    # Set
      validator exit epoch and withdrawable epoch\n    validator.exit_epoch = exit_queue_epoch\n    validator.withdrawable_epoch = Epoch(validator.exit_epoch + MIN_VALIDATOR_WITHDRAWABILITY_DELAY)',
      'def slash_validator(state: BeaconState,\n                    slashed_index: ValidatorIndex,\n                    whistleblower_index: ValidatorIndex=None) -> None:\n    """\n    Slash the
      validator with index ``slashed_index``.\n    """\n    epoch = get_current_epoch(state)\n    initiate_validator_exit(state, slashed_index)\n    validator = state.validators[slashed_index]\n
      validator.slashed = True\n    validator.withdrawable_epoch = max(validator.withdrawable_epoch, Epoch(epoch + EPOCHS_PER_SLASHINGS_VECTOR))\n    state.slashings[epoch % EPOCHS_PER_SLASHINGS_VECTOR]
      += validator.effective_balance\n    decrease_balance(state, slashed_index, validator.effective_balance // MIN_SLASHING_PENALTY_QUOTIENT)\n\n    # Apply proposer and whistleblower
      rewards\n    proposer_index = get_beacon_proposer_index(state)\n    if whistleblower_index is None:\n        whistleblower_index = proposer_index\n    whistleblower_reward =
      Gwei(validator.effective_balance // WHISTLEBLOWER_REWARD_QUOTIENT)\n    proposer_reward = Gwei(whistleblower_reward // PROPOSER_REWARD_QUOTIENT)\n    increase_balance(state, proposer_index,
      proposer_reward)\n    increase_balance(state, whistleblower_index, Gwei(whistleblower_reward - proposer_reward))', 'def initialize_beacon_state_from_eth1(eth1_block_hash: Hash32,\n
      eth1_timestamp: uint64,\n                                      deposits: Sequence[Deposit]) -> BeaconState:\n    fork = Fork(\n        previous_version=GENESIS_FORK_VERSION,\n
      current_version=GENESIS_FORK_VERSION,\n        epoch=GENESIS_EPOCH,\n    )\n    state = BeaconState(\n        genesis_time=eth1_timestamp + GENESIS_DELAY,\n        fork=fork,\n
      eth1_data=Eth1Data(block_hash=eth1_block_hash, deposit_count=uint64(len(deposits))),\n        latest_block_header=BeaconBlockHeader(body_root=hash_tree_root(BeaconBlockBody())),\n
      randao_mixes=[eth1_block_hash] * EPOCHS_PER_HISTORICAL_VECTOR,  # Seed RANDAO with Eth1 entropy\n    )\n\n    # Process deposits\n    leaves = list(map(lambda deposit: deposit.data,
      deposits))\n    for index, deposit in enumerate(deposits):\n        deposit_data_list = List[DepositData, 2**DEPOSIT_CONTRACT_TREE_DEPTH](*leaves[:index + 1])\n        state.eth1_data.deposit_root
      = hash_tree_root(deposit_data_list)\n        process_deposit(state, deposit)\n\n    # Process activations\n    for index, validator in enumerate(state.validators):\n        balance
      = state.balances[index]\n        validator.effective_balance = min(balance - balance % EFFECTIVE_BALANCE_INCREMENT, MAX_EFFECTIVE_BALANCE)\n        if validator.effective_balance ==
      MAX_EFFECTIVE_BALANCE:\n            validator.activation_eligibility_epoch = GENESIS_EPOCH\n            validator.activation_epoch = GENESIS_EPOCH\n\n    # Set genesis validators root for domain
      separation and chain versioning\n    state.genesis_validators_root = hash_tree_root(state.validators)\n\n    return state', 'def is_valid_genesis_state(state: BeaconState) -> bool:\n    if
      state.genesis_time < MIN_GENESIS_TIME:\n        return False\n    if len(get_active_validator_indices(state, GENESIS_EPOCH)) < MIN_GENESIS_ACTIVE_VALIDATOR_COUNT:\n        return False\n
      return True', 'def state_transition(state: BeaconState, signed_block: SignedBeaconBlock, validate_result: bool=True) -> None:\n    block = signed_block.message\n    # Process slots (including
      those with no blocks) since block\n    process_slots(state, block.slot)\n    # Verify signature\n    if validate_result:\n        assert verify_block_signature(state, signed_block)\n    #
      Process block\n    process_block(state, block)\n    # Verify state root\n    if validate_result:\n        assert block.state_root == hash_tree_root(state)', 'def verify_block_signature(state:
      BeaconState, signed_block: SignedBeaconBlock) -> bool:\n    proposer = state.validators[signed_block.message.proposer_index]\n    signing_root = compute_signing_root(signed_block.message,
      get_domain(state, DOMAIN_BEACON_PROPOSER))\n    return bls.Verify(proposer.pubkey, signing_root, signed_block.signature)', 'def process_slots(state: BeaconState, slot: Slot) -> None:\n    assert
      state.slot < slot\n    while state.slot < slot:\n        process_slot(state)\n        # Process epoch on the start slot of the next epoch\n        if (state.slot + 1) % SLOTS_PER_EPOCH == 0:\n
      process_epoch(state)\n        state.slot = Slot(state.slot + 1)', 'def process_slot(state: BeaconState) -> None:\n    # Cache state root\n    previous_state_root = hash_tree_root(state)\n
      state.state_roots[state.slot % SLOTS_PER_HISTORICAL_ROOT] = previous_state_root\n    # Cache latest block header state root\n    if state.latest_block_header.state_root == Bytes32():\n
      state.latest_block_header.state_root = previous_state_root\n    # Cache block root\n    previous_block_root = hash_tree_root(state.latest_block_header)\n    state.block_roots[state.slot %
      SLOTS_PER_HISTORICAL_ROOT] = previous_block_root', 'def process_epoch(state: BeaconState) -> None:\n    process_justification_and_finalization(state)\n    process_rewards_and_penalties(state)\n
      process_registry_updates(state)\n    process_slashings(state)\n    process_eth1_data_reset(state)\n    process_effective_balance_updates(state)\n    process_slashings_reset(state)\n
      process_randao_mixes_reset(state)\n    process_historical_roots_update(state)\n    process_participation_record_updates(state)', 'def get_matching_source_attestations(state: BeaconState,
      epoch: Epoch) -> Sequence[PendingAttestation]:\n    assert epoch in (get_previous_epoch(state), get_current_epoch(state))\n    return state.current_epoch_attestations if epoch ==
      get_current_epoch(state) else state.previous_epoch_attestations', 'def get_matching_target_attestations(state: BeaconState, epoch: Epoch) -> Sequence[PendingAttestation]:\n    return
      [\n        a for a in get_matching_source_attestations(state, epoch)\n        if a.data.target.root == get_block_root(state, epoch)\n    ]', 'def get_matching_head_attestations(state:
      BeaconState, epoch: Epoch) -> Sequence[PendingAttestation]:\n    return [\n        a for a in get_matching_target_attestations(state, epoch)\n        if a.data.beacon_block_root ==
      get_block_root_at_slot(state, a.data.slot)\n    ]', 'def get_unslashed_attesting_indices(state: BeaconState,\n                                    attestations: Sequence[PendingAttestation]) ->
      Set[ValidatorIndex]:\n    output = set()  # type: Set[ValidatorIndex]\n    for a in attestations:\n        output = output.union(get_attesting_indices(state, a))\n    return set(filter(lambda
      index: not state.validators[index].slashed, output))', 'def get_attesting_balance(state: BeaconState, attestations: Sequence[PendingAttestation]) -> Gwei:\n    """\n    Return the combined
      effective balance of the set of unslashed validators participating in ``attestations``.\n    Note: ``get_total_balance`` returns ``EFFECTIVE_BALANCE_INCREMENT`` Gwei minimum to avoid
      divisions by zero.\n    """\n    return get_total_balance(state, get_unslashed_attesting_indices(state, attestations))', 'def process_justification_and_finalization(state: BeaconState) ->
      None:\n    # Initial FFG checkpoint values have a `0x00` stub for `root`.\n    # Skip FFG updates in the first two epochs to avoid corner cases that might result in modifying this stub.\n    if
      get_current_epoch(state) <= GENESIS_EPOCH + 1:\n        return\n    previous_attestations = get_matching_target_attestations(state, get_previous_epoch(state))\n    current_attestations =
      get_matching_target_attestations(state, get_current_epoch(state))\n    total_active_balance = get_total_active_balance(state)\n    previous_target_balance = get_attesting_balance(state,
      previous_attestations)\n    current_target_balance = get_attesting_balance(state, current_attestations)\n    weigh_justification_and_finalization(state, total_active_balance,
      previous_target_balance, current_target_balance)', 'def weigh_justification_and_finalization(state: BeaconState,\n                                         total_active_balance:
      Gwei,\n                                         previous_epoch_target_balance: Gwei,\n                                         current_epoch_target_balance: Gwei) -> None:\n    previous_epoch
      = get_previous_epoch(state)\n    current_epoch = get_current_epoch(state)\n    old_previous_justified_checkpoint = state.previous_justified_checkpoint\n    old_current_justified_checkpoint
      = state.current_justified_checkpoint\n\n    # Process justifications\n    state.previous_justified_checkpoint = state.current_justified_checkpoint\n    state.justification_bits[1:]
      = state.justification_bits[:JUSTIFICATION_BITS_LENGTH - 1]\n    state.justification_bits[0] = 0b0\n    if previous_epoch_target_balance * 3 >= total_active_balance *
      2:\n        state.current_justified_checkpoint = Checkpoint(epoch=previous_epoch,\n                                                        root=get_block_root(state, previous_epoch))\n
      state.justification_bits[1] = 0b1\n    if current_epoch_target_balance * 3 >= total_active_balance * 2:\n        state.current_justified_checkpoint = Checkpoint(epoch=current_epoch,\n
      root=get_block_root(state, current_epoch))\n        state.justification_bits[0] = 0b1\n\n    # Process finalizations\n    bits = state.justification_bits\n    # The 2nd/3rd/4th most
      recent epochs are justified, the 2nd using the 4th as source\n    if all(bits[1:4]) and old_previous_justified_checkpoint.epoch + 3 == current_epoch:\n        state.finalized_checkpoint =
      old_previous_justified_checkpoint\n    # The 2nd/3rd most recent epochs are justified, the 2nd using the 3rd as source\n    if all(bits[1:3]) and old_previous_justified_checkpoint.epoch +
      2 == current_epoch:\n        state.finalized_checkpoint = old_previous_justified_checkpoint\n    # The 1st/2nd/3rd most recent epochs are justified, the 1st using the 3rd as source\n    if
      all(bits[0:3]) and old_current_justified_checkpoint.epoch + 2 == current_epoch:\n        state.finalized_checkpoint = old_current_justified_checkpoint\n    # The 1st/2nd most recent
      epochs are justified, the 1st using the 2nd as source\n    if all(bits[0:2]) and old_current_justified_checkpoint.epoch + 1 == current_epoch:\n        state.finalized_checkpoint =
      old_current_justified_checkpoint', 'def get_base_reward(state: BeaconState, index: ValidatorIndex) -> Gwei:\n    total_balance = get_total_active_balance(state)\n    effective_balance =
      state.validators[index].effective_balance\n    return Gwei(effective_balance * BASE_REWARD_FACTOR // integer_squareroot(total_balance) // BASE_REWARDS_PER_EPOCH)', 'def get_proposer_reward(state:
      BeaconState, attesting_index: ValidatorIndex) -> Gwei:\n    return Gwei(get_base_reward(state, attesting_index) // PROPOSER_REWARD_QUOTIENT)', 'def get_finality_delay(state: BeaconState)
      -> uint64:\n    return get_previous_epoch(state) - state.finalized_checkpoint.epoch', 'def is_in_inactivity_leak(state: BeaconState) -> bool:\n    return get_finality_delay(state)
      > MIN_EPOCHS_TO_INACTIVITY_PENALTY', 'def get_eligible_validator_indices(state: BeaconState) -> Sequence[ValidatorIndex]:\n    previous_epoch = get_previous_epoch(state)\n    return
      [\n        ValidatorIndex(index) for index, v in enumerate(state.validators)\n        if is_active_validator(v, previous_epoch) or (v.slashed and previous_epoch + 1 < v.withdrawable_epoch)\n
      ]', 'def get_attestation_component_deltas(state: BeaconState,\n                                     attestations: Sequence[PendingAttestation]\n                                     ) ->
      Tuple[Sequence[Gwei], Sequence[Gwei]]:\n    """\n    Helper with shared logic for use by get source, target, and head deltas functions\n    """\n    rewards = [Gwei(0)] * len(state.validators)\n
      penalties = [Gwei(0)] * len(state.validators)\n    total_balance = get_total_active_balance(state)\n    unslashed_attesting_indices = get_unslashed_attesting_indices(state, attestations)\n
      attesting_balance = get_total_balance(state, unslashed_attesting_indices)\n    for index in get_eligible_validator_indices(state):\n        if index in unslashed_attesting_indices:\n
      increment = EFFECTIVE_BALANCE_INCREMENT  # Factored out from balance totals to avoid uint64 overflow\n            if is_in_inactivity_leak(state):\n                # Since full base
      reward will be canceled out by inactivity penalty deltas,\n                # optimal participation receives full base reward compensation here.\n                rewards[index] +=
      get_base_reward(state, index)\n            else:\n                reward_numerator = get_base_reward(state, index) * (attesting_balance // increment)\n                rewards[index] +=
      reward_numerator // (total_balance // increment)\n        else:\n            penalties[index] += get_base_reward(state, index)\n    return rewards, penalties', 'def get_source_deltas(state:
      BeaconState) -> Tuple[Sequence[Gwei], Sequence[Gwei]]:\n    """\n    Return attester micro-rewards/penalties for source-vote for each validator.\n    """\n    matching_source_attestations
      = get_matching_source_attestations(state, get_previous_epoch(state))\n    return get_attestation_component_deltas(state, matching_source_attestations)', 'def get_target_deltas(state:
      BeaconState) -> Tuple[Sequence[Gwei], Sequence[Gwei]]:\n    """\n    Return attester micro-rewards/penalties for target-vote for each validator.\n    """\n    matching_target_attestations
      = get_matching_target_attestations(state, get_previous_epoch(state))\n    return get_attestation_component_deltas(state, matching_target_attestations)', 'def get_head_deltas(state:
      BeaconState) -> Tuple[Sequence[Gwei], Sequence[Gwei]]:\n    """\n    Return attester micro-rewards/penalties for head-vote for each validator.\n    """\n    matching_head_attestations =
      get_matching_head_attestations(state, get_previous_epoch(state))\n    return get_attestation_component_deltas(state, matching_head_attestations)', 'def get_inclusion_delay_deltas(state:
      BeaconState) -> Tuple[Sequence[Gwei], Sequence[Gwei]]:\n    """\n    Return proposer and inclusion delay micro-rewards/penalties for each validator.\n    """\n    rewards = [Gwei(0) for _ in
      range(len(state.validators))]\n    matching_source_attestations = get_matching_source_attestations(state, get_previous_epoch(state))\n    for index in get_unslashed_attesting_indices(state,
      matching_source_attestations):\n        attestation = min([\n            a for a in matching_source_attestations\n            if index in get_attesting_indices(state, a)\n        ],
      key=lambda a: a.inclusion_delay)\n        rewards[attestation.proposer_index] += get_proposer_reward(state, index)\n        max_attester_reward = Gwei(get_base_reward(state, index) -
      get_proposer_reward(state, index))\n        rewards[index] += Gwei(max_attester_reward // attestation.inclusion_delay)\n\n    # No penalties associated with inclusion delay\n    penalties
      = [Gwei(0) for _ in range(len(state.validators))]\n    return rewards, penalties', 'def get_inactivity_penalty_deltas(state: BeaconState) -> Tuple[Sequence[Gwei], Sequence[Gwei]]:\n
      """\n    Return inactivity reward/penalty deltas for each validator.\n    """\n    penalties = [Gwei(0) for _ in range(len(state.validators))]\n    if is_in_inactivity_leak(state):\n
      matching_target_attestations = get_matching_target_attestations(state, get_previous_epoch(state))\n        matching_target_attesting_indices = get_unslashed_attesting_indices(state,
      matching_target_attestations)\n        for index in get_eligible_validator_indices(state):\n            # If validator is performing optimally this cancels all rewards for a neutral
      balance\n            base_reward = get_base_reward(state, index)\n            penalties[index] += Gwei(BASE_REWARDS_PER_EPOCH * base_reward - get_proposer_reward(state, index))\n            if
      index not in matching_target_attesting_indices:\n                effective_balance = state.validators[index].effective_balance\n                penalties[index] += Gwei(effective_balance *
      get_finality_delay(state) // INACTIVITY_PENALTY_QUOTIENT)\n\n    # No rewards associated with inactivity penalties\n    rewards = [Gwei(0) for _ in range(len(state.validators))]\n    return
      rewards, penalties', 'def get_attestation_deltas(state: BeaconState) -> Tuple[Sequence[Gwei], Sequence[Gwei]]:\n    """\n    Return attestation reward/penalty deltas for each validator.\n
      """\n    source_rewards, source_penalties = get_source_deltas(state)\n    target_rewards, target_penalties = get_target_deltas(state)\n    head_rewards, head_penalties = get_head_deltas(state)\n
      inclusion_delay_rewards, _ = get_inclusion_delay_deltas(state)\n    _, inactivity_penalties = get_inactivity_penalty_deltas(state)\n\n    rewards = [\n        source_rewards[i] +
      target_rewards[i] + head_rewards[i] + inclusion_delay_rewards[i]\n        for i in range(len(state.validators))\n    ]\n\n    penalties = [\n        source_penalties[i] + target_penalties[i]
      + head_penalties[i] + inactivity_penalties[i]\n        for i in range(len(state.validators))\n    ]\n\n    return rewards, penalties', 'def process_rewards_and_penalties(state:
      BeaconState) -> None:\n    # No rewards are applied at the end of `GENESIS_EPOCH` because rewards are for work done in the previous epoch\n    if get_current_epoch(state) ==
      GENESIS_EPOCH:\n        return\n\n    rewards, penalties = get_attestation_deltas(state)\n    for index in range(len(state.validators)):\n        increase_balance(state, ValidatorIndex(index),
      rewards[index])\n        decrease_balance(state, ValidatorIndex(index), penalties[index])', 'def process_registry_updates(state: BeaconState) -> None:\n    # Process activation eligibility
      and ejections\n    for index, validator in enumerate(state.validators):\n        if is_eligible_for_activation_queue(validator):\n            validator.activation_eligibility_epoch =
      get_current_epoch(state) + 1\n\n        if (\n            is_active_validator(validator, get_current_epoch(state))\n            and validator.effective_balance <= EJECTION_BALANCE\n        ):\n
      initiate_validator_exit(state, ValidatorIndex(index))\n\n    # Queue validators eligible for activation and not yet dequeued for activation\n    activation_queue = sorted([\n        index
      for index, validator in enumerate(state.validators)\n        if is_eligible_for_activation(state, validator)\n        # Order by the sequence of activation_eligibility_epoch setting
      and then index\n    ], key=lambda index: (state.validators[index].activation_eligibility_epoch, index))\n    # Dequeued validators for activation up to churn limit\n    for index in
      activation_queue[:get_validator_churn_limit(state)]:\n        validator = state.validators[index]\n        validator.activation_epoch = compute_activation_exit_epoch(get_current_epoch(state))',
      'def process_slashings(state: BeaconState) -> None:\n    epoch = get_current_epoch(state)\n    total_balance = get_total_active_balance(state)\n    adjusted_total_slashing_balance
      = min(sum(state.slashings) * PROPORTIONAL_SLASHING_MULTIPLIER, total_balance)\n    for index, validator in enumerate(state.validators):\n        if validator.slashed and epoch
      + EPOCHS_PER_SLASHINGS_VECTOR // 2 == validator.withdrawable_epoch:\n            increment = EFFECTIVE_BALANCE_INCREMENT  # Factored out from penalty numerator to avoid uint64
      overflow\n            penalty_numerator = validator.effective_balance // increment * adjusted_total_slashing_balance\n            penalty = penalty_numerator // total_balance *
      increment\n            decrease_balance(state, ValidatorIndex(index), penalty)', 'def process_eth1_data_reset(state: BeaconState) -> None:\n    next_epoch = Epoch(get_current_epoch(state)
      + 1)\n    # Reset eth1 data votes\n    if next_epoch % EPOCHS_PER_ETH1_VOTING_PERIOD == 0:\n        state.eth1_data_votes = []', 'def process_effective_balance_updates(state: BeaconState)
      -> None:\n    # Update effective balances with hysteresis\n    for index, validator in enumerate(state.validators):\n        balance = state.balances[index]\n        HYSTERESIS_INCREMENT =
      uint64(EFFECTIVE_BALANCE_INCREMENT // HYSTERESIS_QUOTIENT)\n        DOWNWARD_THRESHOLD = HYSTERESIS_INCREMENT * HYSTERESIS_DOWNWARD_MULTIPLIER\n        UPWARD_THRESHOLD = HYSTERESIS_INCREMENT
      * HYSTERESIS_UPWARD_MULTIPLIER\n        if (\n            balance + DOWNWARD_THRESHOLD < validator.effective_balance\n            or validator.effective_balance + UPWARD_THRESHOLD <
      balance\n        ):\n            validator.effective_balance = min(balance - balance % EFFECTIVE_BALANCE_INCREMENT, MAX_EFFECTIVE_BALANCE)', 'def process_slashings_reset(state: BeaconState) ->
      None:\n    next_epoch = Epoch(get_current_epoch(state) + 1)\n    # Reset slashings\n    state.slashings[next_epoch % EPOCHS_PER_SLASHINGS_VECTOR] = Gwei(0)', 'def process_randao_mixes_reset(state:
      BeaconState) -> None:\n    current_epoch = get_current_epoch(state)\n    next_epoch = Epoch(current_epoch + 1)\n    # Set randao mix\n    state.randao_mixes[next_epoch %
      EPOCHS_PER_HISTORICAL_VECTOR] = get_randao_mix(state, current_epoch)', 'def process_historical_roots_update(state: BeaconState) -> None:\n    # Set historical root accumulator\n    next_epoch
      = Epoch(get_current_epoch(state) + 1)\n    if next_epoch % (SLOTS_PER_HISTORICAL_ROOT // SLOTS_PER_EPOCH) == 0:\n        historical_batch = HistoricalBatch(block_roots=state.block_roots,
      state_roots=state.state_roots)\n        state.historical_roots.append(hash_tree_root(historical_batch))', 'def process_participation_record_updates(state: BeaconState) -> None:\n    # Rotate
      current/previous epoch attestations\n    state.previous_epoch_attestations = state.current_epoch_attestations\n    state.current_epoch_attestations = []', 'def process_block(state: BeaconState,
      block: BeaconBlock) -> None:\n    process_block_header(state, block)\n    process_randao(state, block.body)\n    process_eth1_data(state, block.body)\n    process_operations(state, block.body)',
      'def process_block_header(state: BeaconState, block: BeaconBlock) -> None:\n    # Verify that the slots match\n    assert block.slot == state.slot\n    # Verify that the block is newer than latest
      block header\n    assert block.slot > state.latest_block_header.slot\n    # Verify that proposer index is the correct index\n    assert block.proposer_index == get_beacon_proposer_index(state)\n
      # Verify that the parent matches\n    assert block.parent_root == hash_tree_root(state.latest_block_header)\n    # Cache current block as the new latest block\n    state.latest_block_header
      = BeaconBlockHeader(\n        slot=block.slot,\n        proposer_index=block.proposer_index,\n        parent_root=block.parent_root,\n        state_root=Bytes32(),  # Overwritten in the
      next process_slot call\n        body_root=hash_tree_root(block.body),\n    )\n\n    # Verify proposer is not slashed\n    proposer = state.validators[block.proposer_index]\n    assert
      not proposer.slashed', 'def process_randao(state: BeaconState, body: BeaconBlockBody) -> None:\n    epoch = get_current_epoch(state)\n    # Verify RANDAO reveal\n    proposer =
      state.validators[get_beacon_proposer_index(state)]\n    signing_root = compute_signing_root(epoch, get_domain(state, DOMAIN_RANDAO))\n    assert bls.Verify(proposer.pubkey, signing_root,
      body.randao_reveal)\n    # Mix in RANDAO reveal\n    mix = xor(get_randao_mix(state, epoch), hash(body.randao_reveal))\n    state.randao_mixes[epoch % EPOCHS_PER_HISTORICAL_VECTOR] =
      mix', 'def process_eth1_data(state: BeaconState, body: BeaconBlockBody) -> None:\n    state.eth1_data_votes.append(body.eth1_data)\n    if state.eth1_data_votes.count(body.eth1_data) * 2 >
      EPOCHS_PER_ETH1_VOTING_PERIOD * SLOTS_PER_EPOCH:\n        state.eth1_data = body.eth1_data', 'def process_operations(state: BeaconState, body: BeaconBlockBody) -> None:\n    # Verify that
      outstanding deposits are processed up to the maximum number of deposits\n    assert len(body.deposits) == min(MAX_DEPOSITS, state.eth1_data.deposit_count - state.eth1_deposit_index)\n\n    def
      for_ops(operations: Sequence[Any], fn: Callable[[BeaconState, Any], None]) -> None:\n        for operation in operations:\n            fn(state, operation)\n\n    for_ops(body.proposer_slashings,
      process_proposer_slashing)\n    for_ops(body.attester_slashings, process_attester_slashing)\n    for_ops(body.attestations, process_attestation)\n    for_ops(body.deposits,
      process_deposit)\n    for_ops(body.voluntary_exits, process_voluntary_exit)', 'def process_proposer_slashing(state: BeaconState, proposer_slashing: ProposerSlashing) -> None:\n    header_1 =
      proposer_slashing.signed_header_1.message\n    header_2 = proposer_slashing.signed_header_2.message\n\n    # Verify header slots match\n    assert header_1.slot == header_2.slot\n    # Verify
      header proposer indices match\n    assert header_1.proposer_index == header_2.proposer_index\n    # Verify the headers are different\n    assert header_1 != header_2\n    # Verify the proposer
      is slashable\n    proposer = state.validators[header_1.proposer_index]\n    assert is_slashable_validator(proposer, get_current_epoch(state))\n    # Verify signatures\n    for signed_header
      in (proposer_slashing.signed_header_1, proposer_slashing.signed_header_2):\n        domain = get_domain(state, DOMAIN_BEACON_PROPOSER, compute_epoch_at_slot(signed_header.message.slot))\n
      signing_root = compute_signing_root(signed_header.message, domain)\n        assert bls.Verify(proposer.pubkey, signing_root, signed_header.signature)\n\n    slash_validator(state,
      header_1.proposer_index)', 'def process_attester_slashing(state: BeaconState, attester_slashing: AttesterSlashing) -> None:\n    attestation_1 = attester_slashing.attestation_1\n    attestation_2
      = attester_slashing.attestation_2\n    assert is_slashable_attestation_data(attestation_1.data, attestation_2.data)\n    assert is_valid_indexed_attestation(state, attestation_1)\n    assert
      is_valid_indexed_attestation(state, attestation_2)\n\n    slashed_any = False\n    indices = set(attestation_1.attesting_indices).intersection(attestation_2.attesting_indices)\n    for
      index in sorted(indices):\n        if is_slashable_validator(state.validators[index], get_current_epoch(state)):\n            slash_validator(state, index)\n            slashed_any
      = True\n    assert slashed_any', 'def process_attestation(state: BeaconState, attestation: Attestation) -> None:\n    data = attestation.data\n    assert data.target.epoch in
      (get_previous_epoch(state), get_current_epoch(state))\n    assert data.target.epoch == compute_epoch_at_slot(data.slot)\n    assert data.slot + MIN_ATTESTATION_INCLUSION_DELAY <= state.slot
      <= data.slot + SLOTS_PER_EPOCH\n    assert data.index < get_committee_count_per_slot(state, data.target.epoch)\n\n    committee = get_beacon_committee(state, data.slot, data.index)\n
      assert len(attestation.aggregation_bits) == len(committee)\n\n    pending_attestation = PendingAttestation(\n        data=data,\n        aggregation_bits=attestation.aggregation_bits,\n
      inclusion_delay=state.slot - data.slot,\n        proposer_index=get_beacon_proposer_index(state),\n    )\n\n    if data.target.epoch == get_current_epoch(state):\n        assert
      data.source == state.current_justified_checkpoint\n        state.current_epoch_attestations.append(pending_attestation)\n    else:\n        assert data.source ==
      state.previous_justified_checkpoint\n        state.previous_epoch_attestations.append(pending_attestation)\n\n    # Verify signature\n    assert is_valid_indexed_attestation(state,
      get_indexed_attestation(state, attestation))', 'def get_validator_from_deposit(pubkey: BLSPubkey, withdrawal_credentials: Bytes32, amount: uint64) -> Validator:\n    effective_balance
      = min(amount - amount % EFFECTIVE_BALANCE_INCREMENT, MAX_EFFECTIVE_BALANCE)\n\n    return Validator(\n        pubkey=pubkey,\n        withdrawal_credentials=withdrawal_credentials,\n
      effective_balance=effective_balance,\n        slashed=False,\n        activation_eligibility_epoch=FAR_FUTURE_EPOCH,\n        activation_epoch=FAR_FUTURE_EPOCH,\n
      exit_epoch=FAR_FUTURE_EPOCH,\n        withdrawable_epoch=FAR_FUTURE_EPOCH,\n    )', 'def add_validator_to_registry(state: BeaconState,\n                              pubkey: BLSPubkey,\n
      withdrawal_credentials: Bytes32,\n                              amount: uint64) -> None:\n    state.validators.append(get_validator_from_deposit(pubkey, withdrawal_credentials, amount))\n
      state.balances.append(amount)', 'def apply_deposit(state: BeaconState,\n                  pubkey: BLSPubkey,\n                  withdrawal_credentials: Bytes32,\n                  amount:
      uint64,\n                  signature: BLSSignature) -> None:\n    validator_pubkeys = [v.pubkey for v in state.validators]\n    if pubkey not in validator_pubkeys:\n        #
      Verify the deposit signature (proof of possession) which is not checked by the deposit contract\n        deposit_message = DepositMessage(\n            pubkey=pubkey,\n
      withdrawal_credentials=withdrawal_credentials,\n            amount=amount,\n        )\n        domain = compute_domain(DOMAIN_DEPOSIT)  # Fork-agnostic domain since deposits are valid across
      forks\n        signing_root = compute_signing_root(deposit_message, domain)\n        if bls.Verify(pubkey, signing_root, signature):\n            add_validator_to_registry(state, pubkey,
      withdrawal_credentials, amount)\n    else:\n        # Increase balance by deposit amount\n        index = ValidatorIndex(validator_pubkeys.index(pubkey))\n        increase_balance(state, index,
      amount)', 'def process_deposit(state: BeaconState, deposit: Deposit) -> None:\n    # Verify the Merkle branch\n    assert is_valid_merkle_branch(\n        leaf=hash_tree_root(deposit.data),\n
      branch=deposit.proof,\n        depth=DEPOSIT_CONTRACT_TREE_DEPTH + 1,  # Add 1 for the List length mix-in\n        index=state.eth1_deposit_index,\n        root=state.eth1_data.deposit_root,\n
      )\n\n    # Deposits must be processed in order\n    state.eth1_deposit_index += 1\n\n    apply_deposit(\n        state=state,\n        pubkey=deposit.data.pubkey,\n
      withdrawal_credentials=deposit.data.withdrawal_credentials,\n        amount=deposit.data.amount,\n        signature=deposit.data.signature,\n    )', 'def process_voluntary_exit(state: BeaconState,
      signed_voluntary_exit: SignedVoluntaryExit) -> None:\n    voluntary_exit = signed_voluntary_exit.message\n    validator = state.validators[voluntary_exit.validator_index]\n    # Verify the
      validator is active\n    assert is_active_validator(validator, get_current_epoch(state))\n    # Verify exit has not been initiated\n    assert validator.exit_epoch == FAR_FUTURE_EPOCH\n    #
      Exits must specify an epoch when they become valid; they are not valid before then\n    assert get_current_epoch(state) >= voluntary_exit.epoch\n    # Verify the validator has been active
      long enough\n    assert get_current_epoch(state) >= validator.activation_epoch + SHARD_COMMITTEE_PERIOD\n    # Verify signature\n    domain = get_domain(state, DOMAIN_VOLUNTARY_EXIT,
      voluntary_exit.epoch)\n    signing_root = compute_signing_root(voluntary_exit, domain)\n    assert bls.Verify(validator.pubkey, signing_root, signed_voluntary_exit.signature)\n    # Initiate
      exit\n    initiate_validator_exit(state, voluntary_exit.validator_index)']
