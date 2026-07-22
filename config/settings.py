# config/settings.py

from pathlib import Path

# -----------------------------
# PROJECT ROOT
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# DATABASE
# -----------------------------
DATABASE_PATH = BASE_DIR / "data" / "packets.db"

# -----------------------------
# DATA FILES
# -----------------------------
CSV_PATH = BASE_DIR / "data" / "traffic.csv"

# -----------------------------
# MODEL PATHS
# -----------------------------
MODEL_DIR = BASE_DIR / "models"

ISOLATION_FOREST_MODEL = MODEL_DIR / "isolation_forest.pkl"
ONECLASS_MODEL = MODEL_DIR / "oneclass_svm.pkl"
SCALER_PATH = MODEL_DIR / "scaler.pkl"

# -----------------------------
# NETWORK SETTINGS
# -----------------------------
INTERFACE = None

CAPTURE_TIMEOUT = None

MAX_PACKETS = 0

# -----------------------------
# THREAT DETECTION
# -----------------------------
PORT_SCAN_THRESHOLD = 20

DDOS_PACKET_THRESHOLD = 500

BRUTE_FORCE_THRESHOLD = 10

DNS_QUERY_LENGTH_THRESHOLD = 50

# -----------------------------
# DASHBOARD SETTINGS
# -----------------------------
REFRESH_RATE = 3000

# -----------------------------
# REPORT SETTINGS
# -----------------------------
REPORT_DIR = BASE_DIR / "reports"

# -----------------------------
# LOGGING
# -----------------------------
LOG_DIR = BASE_DIR / "logs"

LOG_FILE = LOG_DIR / "netvision.log"