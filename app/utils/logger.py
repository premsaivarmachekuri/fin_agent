import logging, sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
    format='{"time":"%(asctime)s","level":"%(levelname)s","msg":"%(message)s"}')
logger = logging.getLogger("fin_agent")
