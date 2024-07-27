from netbench.netbench import Netbench
from src.netbench.settings import Settings

settings = Settings()
settings.get_user_inputs()

netbench = Netbench(settings.settings)
netbench.start_test()
