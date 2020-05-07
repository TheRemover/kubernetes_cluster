from cluster_power.cluster_power import Cluster

def main():
  cluster = Cluster()
  print(cluster.nodes)
  cluster.power_off()
  cluster.power_off(name="N1R")
#  cluster.power_on(name="N1L")
#  cluster.power_on(name="N3R")
#  cluster.get_state()

if __name__ == "__main__":
    main()

