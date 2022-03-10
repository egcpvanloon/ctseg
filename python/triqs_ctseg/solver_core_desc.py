# Generated automatically using the command :
# c++2py ../../c++/triqs_ctseg/solver_core.hpp -p --members_read_only -a triqs_ctseg -m solver_core -o solver_core --moduledoc="The python module for triqs_ctseg" -C triqs -C nda_py --includes=../../c++ --includes=/usr/local/include/ --cxxflags="-std=c++20" --target_file_only
from cpp2py.wrap_generator import *

# The module
module = module_(full_name = "solver_core", doc = r"The python module for triqs_ctseg", app_name = "triqs_ctseg")

# Imports
module.add_imports(*['triqs.gf', 'triqs.gf.meshes', 'triqs.operators'])

# Add here all includes
module.add_include("triqs_ctseg/solver_core.hpp")

# Add here anything to add in the C++ code at the start, e.g. namespace using
module.add_preamble("""
#include <cpp2py/converters/pair.hpp>
#include <cpp2py/converters/string.hpp>
#include <cpp2py/converters/vector.hpp>
#include <nda_py/cpp2py_converters.hpp>
#include <triqs/cpp2py_converters/gf.hpp>
#include <triqs/cpp2py_converters/operators_real_complex.hpp>
#include <triqs/cpp2py_converters/real_or_complex.hpp>

""")


# The class solver_core
c = class_(
        py_type = "SolverCore",  # name of the python class
        c_type = "solver_core",   # name of the C++ class
        doc = r"""Main solver class""",   # doc of the C++ class
        hdf5 = False,
)

c.add_constructor("""(**constr_params_t)""", doc = r"""



+----------------+-------------------------+---------+----------------------------------------------------------------------------------------------------------+
| Parameter Name | Type                    | Default | Documentation                                                                                            |
+================+=========================+=========+==========================================================================================================+
| beta           | double                  | --      | Inverse temperature                                                                                      |
+----------------+-------------------------+---------+----------------------------------------------------------------------------------------------------------+
| gf_struct      | triqs::gfs::gf_struct_t | --      | Structure of the GF (names, sizes of blocks)                                                             |
+----------------+-------------------------+---------+----------------------------------------------------------------------------------------------------------+
| n_tau          | int                     | 10001   | Number of time slices for $Delta(\tau)$/$G(\tau)$/$F(\tau)$                                              |
+----------------+-------------------------+---------+----------------------------------------------------------------------------------------------------------+
| n_tau_k        | int                     | 10001   | Number of time slices for $K(\tau)$                                                                      |
+----------------+-------------------------+---------+----------------------------------------------------------------------------------------------------------+
| n_tau_jperp    | int                     | 10001   | Number of time slices for $J_\perp(\tau)$                                                                |
+----------------+-------------------------+---------+----------------------------------------------------------------------------------------------------------+
| n_tau_nn       | int                     | 101     | Number of Legendre coefficients for G(l)                                                                 |
+----------------+-------------------------+---------+----------------------------------------------------------------------------------------------------------+
| n_w_b_nn       | int                     | 32      | Number of bosonic Matsubara frequencies for $nn(i\omega)$, $\mathcal{D}_0(i\omega)$, $J_\perp(i\omega)$  |
+----------------+-------------------------+---------+----------------------------------------------------------------------------------------------------------+
| n_iw           | int                     | 1025    | Number of fermionic Matsubara frequencies for $G_0(i\omega)$, $G$, $F$, $\Sigma$                         |
+----------------+-------------------------+---------+----------------------------------------------------------------------------------------------------------+
""")

c.add_method("""void solve (**solve_params_t)""",
             doc = r"""



+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Parameter Name                | Type                | Default                                 | Documentation                                                                                                              |
+===============================+=====================+=========================================+============================================================================================================================+
| h_int                         | Op                  | --                                      | local Hamiltonian                                                                                                          |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| n_cycles                      | int                 | --                                      | Number of QMC cycles                                                                                                       |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| length_cycle                  | int                 | 50                                      | Length of a single QMC cycle                                                                                               |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| n_warmup_cycles               | int                 | 5000                                    | Number of cycles for thermalization                                                                                        |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| random_seed                   | int                 | 34788+928374*mpi::communicator().rank() | Seed for random number generator                                                                                           |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| random_name                   | std::string         | ""                                      | Name of random number generator                                                                                            |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| max_time                      | int                 | -1                                      | Maximum runtime in seconds, use -1 to set infinite                                                                         |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| verbosity                     | int                 | mpi::communicator().rank()==0?3:0       | Verbosity level                                                                                                            |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| move_insert_segment           | bool                | true                                    | Whether to perform the move insert segment (see [[move_insert_segment]])                                                   |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| move_remove_segment           | bool                | true                                    | Whether to perform the move remove segment (see [[move_remove_segment]])                                                   |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| move_move                     | bool                | false                                   | Whether to perform the move move segment (see [[move_move]])                                                               |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| move_swap_empty_lines         | bool                | false                                   | Whether to perform the move swap empty lines (see [[move_swap_empty_lines]])                                               |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| move_group_into_spin_segment  | bool                | false                                   | Whether to perform the move group into spin segment (see [[move_group_into_spin_segment]])                                 |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| move_split_spin_segment       | bool                | false                                   | Whether to perform the move split spin segment (see [[move_split_spin_segment]])                                           |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| move_group_into_spin_segment2 | bool                | false                                   | Whether to perform the move group into spin segment (see [[move_group_into_spin_segment2]])                                |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| move_split_spin_segment2      | bool                | false                                   | Whether to perform the move split spin segment (see [[move_split_spin_segment2]])                                          |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| keep_Jperp_negative           | bool                | true                                    | Whether to keep Jperp negative                                                                                             |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| measure_gt                    | bool                | true                                    | Whether to measure G(tau) (see [[measure_gt]])                                                                             |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| measure_sign                  | bool                | true                                    | Whether to measure MC sign (see [[measure_sign]])                                                                          |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| measure_ft                    | bool                | false                                   | Whether to measure improved estimator F(tau) (see [[measure_gt]]) (only isotropic spin-spin interactions if any)           |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| measure_gl                    | bool                | false                                   | Whether to measure G(l) (Legendre) (see [[measure_gl]])                                                                    |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| measure_fl                    | bool                | false                                   | Whether to measure improved estimator F(l) (Legendre) (see [[measure_gl]]) (only isotropic spin-spin interactions if any)  |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| measure_gw                    | bool                | false                                   | Whether to measure G(iomega) (see [[measure_gw]])                                                                          |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| measure_fw                    | bool                | false                                   | Whether to measure improved estimator F(iomega) (see [[measure_gw]])(only isotropic spin-spin interactions if any)         |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| measure_chipmt                | bool                | false                                   | Whether to measure chi_{+-}(tau) (see [[measure_chipmt]])                                                                  |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| measure_nn                    | bool                | false                                   | Whether to measure <nn> (see [[measure_nn]])                                                                               |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| measure_nnt                   | bool                | false                                   | Whether to measure langle n(tau)n(0)rangle (see [[measure_nnt]])                                                           |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| measure_nnw                   | bool                | false                                   | Whether to measure chi(iomega) (see [[measure_nnw]])                                                                       |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| hartree_shift                 | nda::vector<double> | nda::vector<double>{}                   | Hartree shift of the chem pot                                                                                              |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| det_init_size                 | int                 | 100                                     | The maximum size of the determinant matrix before a resize                                                                 |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| det_n_operations_before_check | int                 | 100                                     | Max number of ops before the test of deviation of the det, M^-1 is performed.                                              |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| det_precision_warning         | double              | 1.e-8                                   | Threshold for determinant precision warnings                                                                               |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| det_precision_error           | double              | 1.e-5                                   | Threshold for determinant precision error                                                                                  |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| det_singular_threshold        | double              | -1                                      | Bound for the determinant matrix being singular, abs(det) > singular_threshold. If <0, it is !isnormal(abs(det))           |
+-------------------------------+---------------------+-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
""")

c.add_property(name = "Delta_tau",
               getter = cfunction("block_gf_view<triqs::mesh::imtime> Delta_tau ()"),
               doc = r"""Hybridization function $\Delta^\sigma_{ab}(\tau)$""")

c.add_property(name = "Jperp_tau",
               getter = cfunction("gf_view<triqs::mesh::imtime> Jperp_tau ()"),
               doc = r"""Dynamical spin-spin interactions $\mathcal{J}_\perp(\tau)$""")

c.add_property(name = "D0_tau",
               getter = cfunction("gf_view<triqs::mesh::imtime> D0_tau ()"),
               doc = r"""Dynamical spin-spin interactions $\mathcal{J}_\perp(\tau)$""")

module.add_class(c)


# Converter for solve_params_t
c = converter_(
        c_type = "solve_params_t",
        doc = r"""""",
)
c.add_member(c_name = "h_int",
             c_type = "Op",
             initializer = """  """,
             doc = r"""local Hamiltonian""")

c.add_member(c_name = "n_cycles",
             c_type = "int",
             initializer = """  """,
             doc = r"""Number of QMC cycles""")

c.add_member(c_name = "length_cycle",
             c_type = "int",
             initializer = """ 50 """,
             doc = r"""Length of a single QMC cycle""")

c.add_member(c_name = "n_warmup_cycles",
             c_type = "int",
             initializer = """ 5000 """,
             doc = r"""Number of cycles for thermalization""")

c.add_member(c_name = "random_seed",
             c_type = "int",
             initializer = """ 34788+928374*mpi::communicator().rank() """,
             doc = r"""Seed for random number generator""")

c.add_member(c_name = "random_name",
             c_type = "std::string",
             initializer = """ "" """,
             doc = r"""Name of random number generator""")

c.add_member(c_name = "max_time",
             c_type = "int",
             initializer = """ -1 """,
             doc = r"""Maximum runtime in seconds, use -1 to set infinite""")

c.add_member(c_name = "verbosity",
             c_type = "int",
             initializer = """ mpi::communicator().rank()==0?3:0 """,
             doc = r"""Verbosity level""")

c.add_member(c_name = "move_insert_segment",
             c_type = "bool",
             initializer = """ true """,
             doc = r"""Whether to perform the move insert segment (see [[move_insert_segment]])""")

c.add_member(c_name = "move_remove_segment",
             c_type = "bool",
             initializer = """ true """,
             doc = r"""Whether to perform the move remove segment (see [[move_remove_segment]])""")

c.add_member(c_name = "move_move",
             c_type = "bool",
             initializer = """ false """,
             doc = r"""Whether to perform the move move segment (see [[move_move]])""")

c.add_member(c_name = "move_swap_empty_lines",
             c_type = "bool",
             initializer = """ false """,
             doc = r"""Whether to perform the move swap empty lines (see
   [[move_swap_empty_lines]])""")

c.add_member(c_name = "move_group_into_spin_segment",
             c_type = "bool",
             initializer = """ false """,
             doc = r"""Whether to perform the move group into spin segment (see
   [[move_group_into_spin_segment]])""")

c.add_member(c_name = "move_split_spin_segment",
             c_type = "bool",
             initializer = """ false """,
             doc = r"""Whether to perform the move split spin segment (see
   [[move_split_spin_segment]])""")

c.add_member(c_name = "move_group_into_spin_segment2",
             c_type = "bool",
             initializer = """ false """,
             doc = r"""Whether to perform the move group into spin segment (see
   [[move_group_into_spin_segment2]])""")

c.add_member(c_name = "move_split_spin_segment2",
             c_type = "bool",
             initializer = """ false """,
             doc = r"""Whether to perform the move split spin segment (see
   [[move_split_spin_segment2]])""")

c.add_member(c_name = "keep_Jperp_negative",
             c_type = "bool",
             initializer = """ true """,
             doc = r"""Whether to keep Jperp negative""")

c.add_member(c_name = "measure_gt",
             c_type = "bool",
             initializer = """ true """,
             doc = r"""Whether to measure G(tau) (see [[measure_gt]])""")

c.add_member(c_name = "measure_sign",
             c_type = "bool",
             initializer = """ true """,
             doc = r"""Whether to measure MC sign (see [[measure_sign]])""")

c.add_member(c_name = "measure_ft",
             c_type = "bool",
             initializer = """ false """,
             doc = r"""Whether to measure improved estimator F(tau) (see [[measure_gt]]) (only
   isotropic spin-spin interactions if any)""")

c.add_member(c_name = "measure_gl",
             c_type = "bool",
             initializer = """ false """,
             doc = r"""Whether to measure G(l) (Legendre) (see [[measure_gl]])""")

c.add_member(c_name = "measure_fl",
             c_type = "bool",
             initializer = """ false """,
             doc = r"""Whether to measure improved estimator F(l) (Legendre) (see [[measure_gl]])
   (only isotropic spin-spin interactions if any)""")

c.add_member(c_name = "measure_gw",
             c_type = "bool",
             initializer = """ false """,
             doc = r"""Whether to measure G(iomega) (see [[measure_gw]])""")

c.add_member(c_name = "measure_fw",
             c_type = "bool",
             initializer = """ false """,
             doc = r"""Whether to measure improved estimator F(iomega) (see [[measure_gw]])(only
   isotropic spin-spin interactions if any)""")

c.add_member(c_name = "measure_chipmt",
             c_type = "bool",
             initializer = """ false """,
             doc = r"""Whether to measure chi_{+-}(tau) (see [[measure_chipmt]])""")

c.add_member(c_name = "measure_nn",
             c_type = "bool",
             initializer = """ false """,
             doc = r"""Whether to measure <nn> (see [[measure_nn]])""")

c.add_member(c_name = "measure_nnt",
             c_type = "bool",
             initializer = """ false """,
             doc = r"""Whether to measure langle n(tau)n(0)rangle (see [[measure_nnt]])""")

c.add_member(c_name = "measure_nnw",
             c_type = "bool",
             initializer = """ false """,
             doc = r"""Whether to measure chi(iomega) (see [[measure_nnw]])""")

c.add_member(c_name = "hartree_shift",
             c_type = "nda::vector<double>",
             initializer = """ nda::vector<double>{} """,
             doc = r"""Hartree shift of the chem pot""")

c.add_member(c_name = "det_init_size",
             c_type = "int",
             initializer = """ 100 """,
             doc = r"""The maximum size of the determinant matrix before a resize""")

c.add_member(c_name = "det_n_operations_before_check",
             c_type = "int",
             initializer = """ 100 """,
             doc = r"""Max number of ops before the test of deviation of the det, M^-1 is performed.""")

c.add_member(c_name = "det_precision_warning",
             c_type = "double",
             initializer = """ 1.e-8 """,
             doc = r"""Threshold for determinant precision warnings""")

c.add_member(c_name = "det_precision_error",
             c_type = "double",
             initializer = """ 1.e-5 """,
             doc = r"""Threshold for determinant precision error""")

c.add_member(c_name = "det_singular_threshold",
             c_type = "double",
             initializer = """ -1 """,
             doc = r"""Bound for the determinant matrix being singular, abs(det) > singular_threshold. If <0, it is !isnormal(abs(det))""")

module.add_converter(c)

# Converter for constr_params_t
c = converter_(
        c_type = "constr_params_t",
        doc = r"""""",
)
c.add_member(c_name = "beta",
             c_type = "double",
             initializer = """  """,
             doc = r"""Inverse temperature""")

c.add_member(c_name = "gf_struct",
             c_type = "triqs::gfs::gf_struct_t",
             initializer = """  """,
             doc = r"""Structure of the GF (names, sizes of blocks)""")

c.add_member(c_name = "n_tau",
             c_type = "int",
             initializer = """ 10001 """,
             doc = r"""Number of time slices for $Delta(\tau)$/$G(\tau)$/$F(\tau)$""")

c.add_member(c_name = "n_tau_k",
             c_type = "int",
             initializer = """ 10001 """,
             doc = r"""Number of time slices for $K(\tau)$""")

c.add_member(c_name = "n_tau_jperp",
             c_type = "int",
             initializer = """ 10001 """,
             doc = r"""Number of time slices for $J_\perp(\tau)$""")

c.add_member(c_name = "n_tau_nn",
             c_type = "int",
             initializer = """ 101 """,
             doc = r"""Number of Legendre coefficients for G(l)""")

c.add_member(c_name = "n_w_b_nn",
             c_type = "int",
             initializer = """ 32 """,
             doc = r"""Number of bosonic Matsubara frequencies for $nn(i\omega)$,
   $\mathcal{D}_0(i\omega)$, $J_\perp(i\omega)$""")

c.add_member(c_name = "n_iw",
             c_type = "int",
             initializer = """ 1025 """,
             doc = r"""Number of fermionic Matsubara frequencies for $G_0(i\omega)$, $G$, $F$,
   $\Sigma$""")

module.add_converter(c)


module.generate_code()