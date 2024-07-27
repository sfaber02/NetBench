from netbench.netbench import NetBench
from src.netbench.settings import Settings

settings = Settings().settings

netbench = NetBench(settings)
netbench.start_test()
