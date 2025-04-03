import argparse
from eth2spec.test.helpers.constants import PHASE0, ALTAIR, BELLATRIX, CAPELLA, DENEB, ELECTRA, FULU
from eth2spec.gen_helpers.gen_from_tests.gen import run_state_test_generators, combine_mods, check_mods

parser = argparse.ArgumentParser()
parser.add_argument('--test_name', type=str, required=False, help='Test desired')
args = parser.parse_args()
test_name = args.test_name


if __name__ == "__main__":

    if test_name == 'test_name':
        phase_0_mods = {key: 'eth2spec.test.phase0.sanity.test_' + key for key in [
            'blocks',
            'slots',
        ]}

        _new_altair_mods = {key: 'eth2spec.test.altair.sanity.test_' + key for key in [
            'blocks',
        ]}
        altair_mods = combine_mods(_new_altair_mods, phase_0_mods)

        _new_bellatrix_mods = {key: 'eth2spec.test.bellatrix.sanity.test_' + key for key in [
            'blocks',
        ]}
        bellatrix_mods = combine_mods(_new_bellatrix_mods, altair_mods)

        _new_capella_mods = {key: 'eth2spec.test.capella.sanity.test_' + key for key in [
            'blocks',
        ]}
        capella_mods = combine_mods(_new_capella_mods, bellatrix_mods)

        _new_deneb_mods = {key: 'eth2spec.test.deneb.sanity.test_' + key for key in [
            'blocks',
        ]}
        deneb_mods = combine_mods(_new_deneb_mods, capella_mods)

        # This is a "hack" which allows other test files (e.g., test_deposit_transition.py)
        # to reuse the sanity/block test format. If a new test file is added or removed,
        # do not forget to update sanity/block/__init__.py accordingly.
        _new_electra_mods_1 = {key: 'eth2spec.test.electra.sanity.' + key for key in [
            'blocks',
        ]}
        _new_electra_mods_2 = {key: 'eth2spec.test.electra.sanity.test_' + key for key in [
            'slots',
        ]}
        _new_electra_mods = {**_new_electra_mods_1, **_new_electra_mods_2}
        electra_mods = combine_mods(_new_electra_mods, deneb_mods)

        # No additional Fulu specific sanity tests
        fulu_mods = electra_mods

        all_mods = {
            PHASE0: phase_0_mods,
            ALTAIR: altair_mods,
            BELLATRIX: bellatrix_mods,
            CAPELLA: capella_mods,
            DENEB: deneb_mods,
            ELECTRA: electra_mods,
            FULU: fulu_mods,
        }
        check_mods(all_mods, "sanity")

        run_state_test_generators(runner_name="sanity", all_mods=all_mods)
    else:
        phase_0_mods = {'eth2spec.test.phase0.sanity.' + test_name}

        _new_altair_mods = {'eth2spec.test.altair.sanity.' + test_name}

        altair_mods = combine_mods(_new_altair_mods, phase_0_mods)

        _new_bellatrix_mods = {'eth2spec.test.bellatrix.sanity.' + test_name}

        bellatrix_mods = combine_mods(_new_bellatrix_mods, altair_mods)

        _new_capella_mods = {'eth2spec.test.capella.sanity.' + test_name}

        capella_mods = combine_mods(_new_capella_mods, bellatrix_mods)

        _new_deneb_mods = {'eth2spec.test.deneb.sanity.' + test_name}

        deneb_mods = combine_mods(_new_deneb_mods, capella_mods)

        _new_electra_mods = {'eth2spec.test.electra.sanity.' + test_name}

        electra_mods = combine_mods(_new_electra_mods, deneb_mods)

        # No additional Fulu specific sanity tests
        fulu_mods = electra_mods

        all_mods = {
            PHASE0: phase_0_mods,
            ALTAIR: altair_mods,
            BELLATRIX: bellatrix_mods,
            CAPELLA: capella_mods,
            DENEB: deneb_mods,
            ELECTRA: electra_mods,
            FULU: fulu_mods,
        }
        check_mods(all_mods, "sanity")

        run_state_test_generators(runner_name="sanity", all_mods=all_mods)
