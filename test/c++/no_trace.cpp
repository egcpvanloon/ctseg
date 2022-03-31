#include <cmath>
#include <triqs/test_tools/gfs.hpp>
#include <triqs_ctseg/solver_core.hpp>

TEST(CtHybSpin, Anderson) {
  // Start the mpi
  mpi::communicator world;

  double beta         = 20.0;
  double U            = 0.0;
  double mu           = 0.0;
  double epsilon      = 0.2;
  int n_cycles        = 10000 / world.size();
  int n_warmup_cycles = 1000;
  int length_cycle    = 50;
  int random_seed     = 23488 + 28 * world.rank();
  int n_iw            = 1000;

  // Prepare the parameters
  constr_params_t param_constructor;
  solve_params_t param_solve;

  param_constructor.beta      = beta;
  param_constructor.gf_struct = {{"up", 1}, {"down", 1}};
  param_constructor.n_tau     = 10001;

  // Create solver instance
  solver_core ctqmc(param_constructor);

  param_solve.h_int           = U * n("up", 0) * n("down", 0);
  param_solve.hartree_shift   = {mu, mu};
  param_solve.n_cycles        = n_cycles;
  param_solve.n_warmup_cycles = n_warmup_cycles;
  param_solve.length_cycle    = length_cycle;
  param_solve.random_seed     = random_seed;
  // Measures
  param_solve.measure_gt  = true;
  param_solve.measure_nnt = false;
  // Moves
  param_solve.move_insert_segment  = true;
  param_solve.move_remove_segment  = true;
  param_solve.move_split_segment   = true;
  param_solve.move_regroup_segment = true;
  param_solve.move_move_segment    = true;
  // Moves for test purposes - do not use
  param_solve.move_insert_segment_v2  = false;
  param_solve.move_remove_segment_v2  = false;
  param_solve.move_split_segment_v2   = false;
  param_solve.move_regroup_segment_v2 = false;

  // Prepare delta
  nda::clef::placeholder<0> om_;
  auto delta_w   = gf<imfreq>({beta, Fermion, n_iw}, {1, 1});
  auto delta_tau = gf<imtime>({beta, Fermion, param_constructor.n_tau}, {1, 1});
  delta_w(om_) << 1.0 / (om_ - epsilon);
  delta_tau()          = fourier(delta_w);
  ctqmc.Delta_tau()[0] = delta_tau;
  ctqmc.Delta_tau()[1] = delta_tau;

  // Solve!!
  ctqmc.solve(param_solve);

  // Save the results
  if (world.rank() == 0) {
    h5::file G_file("no_trace.out.h5", 'w');
    h5_write(G_file, "(ctqmc.G_tau()[0])", ctqmc.results.G_tau()[0]);
  }
  if (world.rank() == 0) {
    h5::file G_file("no_trace.ref.h5", 'r');
    gf<imtime> g;
    h5_read(G_file, "(ctqmc.G_tau()[0])", g);
    EXPECT_GF_NEAR(g, ctqmc.results.G_tau()[0]);
  }
}
MAKE_MAIN;
