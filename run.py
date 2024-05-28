import sys
import os
import asyncio
from core.main import main

# Add the core directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'core')))

# Import the main function and run it
if __name__ == "__main__":
    asyncio.run(main())
