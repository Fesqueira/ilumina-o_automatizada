

import asyncio
import datetime
import random
import logging
from dataclasses import dataclass

# ==============================
# CONFIGURAÇÕES
# ==============================
@dataclass
class Config:
    light_threshold: int = 40       # abaixo disso = escuro
    timeout_no_motion: int = 20     # segundos sem movimento → desliga
    night_start: str = "19:00"      # início do modo noturno
    night_end: str = "06:00"        # fim do modo noturno
    manual_override: str | None = None  # "on", "off" ou None (automático)
    simulation_speed: float = 1.0   # tempo entre leituras (segundos)

config = Config()

# ==============================
# LOGS E ESTADO
# ==============================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%H:%M:%S"
)

class SystemState:
    is_on = False
    last_motion_time = None

state = SystemState()

# ==============================
# FUNÇÕES AUXILIARES
# ==============================
def time_in_range(start_str: str, end_str: str, now: datetime.time) -> bool:
    """Verifica se o horário atual está dentro de um intervalo."""
    start = datetime.time(*map(int, start_str.split(":")))
    end = datetime.time(*map(int, end_str.split(":")))

    if start <= end:
        return start <= now <= end
    else:  # atravessa a meia-noite
        return now >= start or now <= end

def is_night() -> bool:
    now = datetime.datetime.now().time()
    return time_in_range(config.night_start, config.night_end, now)

# ==============================
# AÇÕES DO SISTEMA
# ==============================
def turn_on(reason=""):
    if not state.is_on:
        state.is_on = True
        print("💡 Luz ACESA!", f"({reason})")
        logging.info(f"Luz ligada ({reason})")

def turn_off(reason=""):
    if state.is_on:
        state.is_on = False
        print("🌑 Luz APAGADA!", f"({reason})")
        logging.info(f"Luz desligada ({reason})")

# ==============================
# LÓGICA PRINCIPAL
# ==============================
def evaluate(light_level: int, motion: bool):
    """Decide se a luz deve ligar ou desligar."""

    # Controle manual (forçado)
    if config.manual_override == "on":
        turn_on("manual override")
        return
    elif config.manual_override == "off":
        turn_off("manual override")
        return

    dark = light_level < config.light_threshold
    night = is_night()

    if motion:
        state.last_motion_time = datetime.datetime.now()

    # Se estiver escuro e houver movimento → acende
    if dark and motion:
        turn_on("escuro + movimento")
        return

    # Se for de noite → acende (modo noturno)
    if night:
        turn_on("modo noturno")
        return

    # Se passou tempo sem movimento → apaga
    if state.last_motion_time:
        elapsed = (datetime.datetime.now() - state.last_motion_time).total_seconds()
        if elapsed >= config.timeout_no_motion:
            turn_off("sem movimento")
            return

    # Se estiver claro → apaga
    if not dark and not night:
        turn_off("ambiente claro")

# ==============================
# SIMULAÇÃO DE SENSORES
# ==============================
async def simulate_sensors():
    while True:
        light_level = random.randint(0, 100)  # luminosidade (0=escuro, 100=claro)
        motion = random.random() < (0.3 if light_level < 50 else 0.05)  # movimento aleatório

        print(f"\n[Sensores] Luz: {light_level} | Movimento: {motion}")
        evaluate(light_level, motion)

        await asyncio.sleep(config.simulation_speed)

# ==============================
# INTERFACE DE COMANDO
# ==============================
async def user_interface():
    loop = asyncio.get_event_loop()
    while True:
        cmd = await loop.run_in_executor(None, input, "\nComando (on/off/auto/status/quit): ")
        cmd = cmd.strip().lower()

        if cmd == "on":
            config.manual_override = "on"
            evaluate(0, False)
        elif cmd == "off":
            config.manual_override = "off"
            evaluate(100, False)
        elif cmd == "auto":
            config.manual_override = None
            print("🔄 Modo automático ativado.")
        elif cmd == "status":
            print(f"Luz: {'ACESa' if state.is_on else 'APAGADA'} | Modo: {config.manual_override or 'automático'}")
        elif cmd == "quit":
            print("👋 Encerrando simulação...")
            asyncio.get_event_loop().stop()
            return
        else:
            print("Comando inválido. Use: on / off / auto / status / quit")

# ==============================
# FUNÇÃO PRINCIPAL
# ==============================
async def main():
    print("🚀 SIMULADOR DE ILUMINAÇÃO AUTOMATIZADA INICIADO")
    print("O sistema alternará entre claro/escuro e detectará movimento aleatoriamente.\n")
    await asyncio.gather(simulate_sensors(), user_interface())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Simulação encerrada manualmente.")
contador = 0