#!/usr/bin/env python3
"""Minimal OpenAI-compatible API smoke test."""

import argparse
import os
import sys
import time

from dotenv import load_dotenv
from openai import APIConnectionError, APIStatusError, APITimeoutError, OpenAI


def mask_secret(value: str) -> str:
    if not value:
        return "<empty>"
    if len(value) <= 10:
        return value[:2] + "***"
    return f"{value[:6]}...{value[-4:]}"


def main() -> int:
    load_dotenv()

    parser = argparse.ArgumentParser(description="Test an OpenAI-compatible chat completions endpoint.")
    parser.add_argument("--model", default=None)
    parser.add_argument("--base-url", default=None)
    parser.add_argument("--api-key", default=None)
    parser.add_argument("--stream", action="store_true", help="Also test stream=True.")
    parser.add_argument("--timeout", type=float, default=30.0)
    args = parser.parse_args()

    api_key = args.api_key or os.getenv("OPENAI_API_KEY")
    base_url = args.base_url or os.getenv("OPENAI_BASE_URL")
    model = args.model or os.getenv("LLM_MODEL", "moonshot-v1-8k")

    print("OpenAI-compatible endpoint smoke test")
    print(f"base_url: {base_url}")
    print(f"model: {model}")
    print(f"api_key: {mask_secret(api_key)}")

    if not api_key or not base_url or not model:
        print("ERROR: OPENAI_API_KEY, OPENAI_BASE_URL, and model are required.", file=sys.stderr)
        return 2

    client = OpenAI(api_key=api_key, base_url=base_url, timeout=args.timeout)
    messages = [{"role": "user", "content": "请只回复两个字：成功"}]

    try:
        start = time.time()
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0,
            max_tokens=20,
        )
        elapsed = time.time() - start
        content = response.choices[0].message.content
        print(f"non_stream: OK in {elapsed:.2f}s")
        print(f"response: {content}")
    except APIStatusError as exc:
        print(f"non_stream: HTTP {exc.status_code}", file=sys.stderr)
        print(f"error: {exc.message}", file=sys.stderr)
        return 1
    except (APIConnectionError, APITimeoutError) as exc:
        print(f"non_stream: connection/timeout error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"non_stream: unexpected error: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1

    if args.stream:
        try:
            start = time.time()
            chunks = []
            stream = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0,
                max_tokens=20,
                stream=True,
            )
            for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    chunks.append(delta)
            elapsed = time.time() - start
            print(f"stream: OK in {elapsed:.2f}s")
            print(f"stream_response: {''.join(chunks)}")
        except APIStatusError as exc:
            print(f"stream: HTTP {exc.status_code}", file=sys.stderr)
            print(f"error: {exc.message}", file=sys.stderr)
            return 1
        except (APIConnectionError, APITimeoutError) as exc:
            print(f"stream: connection/timeout error: {exc}", file=sys.stderr)
            return 1
        except Exception as exc:
            print(f"stream: unexpected error: {type(exc).__name__}: {exc}", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
