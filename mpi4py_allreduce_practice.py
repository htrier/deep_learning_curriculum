from mpi4py import MPI
comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
p = comm.Get_size()

if my_rank == 0:
    data = sum([1, 2, 3])
    all_data_sum = comm.allreduce(data, op=MPI.SUM)
    print("process ", my_rank, "has computed sum =", all_data_sum)
else:
    data = sum([4, 5, 6])
    all_data_sum = comm.allreduce(data, op=MPI.SUM)
    print("process ", my_rank, "has computed sum =", all_data_sum)
