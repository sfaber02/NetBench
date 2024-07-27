from netbench.netbench import Netbench
from src.netbench.settings import Settings

settings = Settings().settings

netbench = Netbench(settings)
netbench.start_test()
