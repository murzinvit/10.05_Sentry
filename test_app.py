#!/usr/bin/env python3

import sentry_sdk
sentry_sdk.init(
    "https://a5a18eb62a524a8890d17fa56ad46e0b@o1019220.ingest.sentry.io/5985271",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)