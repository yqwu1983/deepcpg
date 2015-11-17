import h5py as h5
import numpy as np
import numpy.testing as npt


def test_data():
    f = h5.File('./data.h5', 'r')
    d = {x:f[x].value for x in f.keys()}
    f.close()

    delta = 5
    pos = 3037343
    i = np.nonzero(d['pos'] == pos)[0]

    # Targets sample 1
    o = d['u0_y'][i - delta: i + delta + 1]
    e = np.array([1, -1,  0,  0,  1,  1, -1, -1, -1,  0, -1])
    npt.assert_array_equal(o, e)

    # CpG neightbors sample 1
    c = d['c_x'][i,:, 0, :][0]
    o = c[:, c.shape[1] // 2 - delta:c.shape[1] // 2 + delta + 4]
    e = np.array([[0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
               [ 1266, 1231, 42, 26, 7, 6127, 13551, 26418, 27492, 27495, 27497, 27503, 27519,
                27534]])
    npt.assert_array_equal(o, e)

    # CpG neightbors sample 2
    c = d['c_x'][i,:, 1, :][0]
    o = c[:, c.shape[1] // 2 - delta:c.shape[1] // 2 + delta + 4]
    e = np.array([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
               [ 8969, 8959, 8954, 7703, 5996, 9140, 10796, 14266, 26177, 26204, 26638, 26681, 26715,
                26767]])
    npt.assert_array_equal(o, e)

    # Sequence
    s = d['s_x'][i][0]
    o = s[s.shape[0] // 2 - delta: s.shape[0] // 2 + delta + 1]
    e = np.array([[ 0., 0., 0., 1.],
               [ 1., 0., 0., 0.],
               [ 0., 1., 0., 0.],
               [ 0., 1., 0., 0.],
               [ 0., 0., 0., 1.],
               [ 0., 0., 0., 1.],
               [ 0., 1., 0., 0.],
               [ 0., 1., 0., 0.],
               [ 0., 0., 0., 1.],
               [ 0., 0., 0., 1.],
               [ 0., 0., 0., 1.]])
    npt.assert_array_equal(o, e)
