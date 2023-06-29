import pytest
import numpy as np
from utils import check_q


@pytest.mark.kuka
def test_kuka_iiwa14(n_attempts):
    from ikfast_kuka_iiwa import get_fk, get_ik, get_dof, get_free_dof
    n_jts = get_dof()
    n_free_jts = get_free_dof()
    assert (n_jts, n_free_jts) == (7, 1)

    feasible_ranges = {
        'iiwa_joint_1': {'lower': -2.96705972839, 'upper': 2.96705972839},
        'iiwa_joint_2': {'lower': -2.09439510239, 'upper': 2.09439510239},
        'iiwa_joint_3': {'lower': -2.96705972839, 'upper': 2.96705972839},
        'iiwa_joint_4': {'lower': -2.09439510239, 'upper': 2.09439510239},
        'iiwa_joint_5': {'lower': -2.96705972839, 'upper': 2.96705972839},
        'iiwa_joint_6': {'lower': -2.09439510239, 'upper': 2.09439510239},
        'iiwa_joint_7': {'lower': -3.05432619099, 'upper': 3.05432619099},
    }

    pos, rot = get_fk([0] * n_jts)
    assert not get_ik(pos, rot, [])
    assert not get_ik(pos, rot, [1, 1])
    assert not get_ik(pos, rot, [1, 1, 1, 1])

    print("Testing random configurations...")
    for _ in range(n_attempts):
        q = np.random.rand(n_jts)
        for i, jt_name in enumerate(feasible_ranges.keys()):
            q[i] = q[i] * (feasible_ranges[jt_name]['upper'] - feasible_ranges[jt_name]['lower']) + \
                   feasible_ranges[jt_name]['lower']
        check_q(get_fk, get_ik, q, feasible_ranges, free_joint_ids=[2])
    print("Done!")
