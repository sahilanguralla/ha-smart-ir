import asyncio
import selectors
import sys

from commitizen.cli import main

if sys.platform == "darwin":
    # Define a custom policy to force SelectSelector
    # This ensures that even if asyncio.run() or new_event_loop() is called,
    # it uses the compatible selector.
    class SelectSelectorEventLoopPolicy(asyncio.DefaultEventLoopPolicy):
        def _loop_factory(self):
            return asyncio.SelectorEventLoop(selectors.SelectSelector())

    asyncio.set_event_loop_policy(SelectSelectorEventLoopPolicy())

if __name__ == "__main__":
    sys.exit(main())
