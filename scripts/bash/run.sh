#!/usr/bin/env bash
set -e

cleanup() {
    echo "Shutting down both backend and frontend..."
    kill $BACKEND_PID $FRONTEND_PID
    wait $BACKEND_PID $FRONTEND_PID
}

trap cleanup SIGINT

ROOT_DIR="$(realpath "$(dirname "$0")/../..")"

cd "$ROOT_DIR/backend"

if [[ "$1" == "test" ]]; then
    echo "Running backend tests..."
    uv run python -m pytest -v tests/  # Run pytest if 'test' argument is passed
else
    echo "Starting backend server..."
    uv run --active uvicorn app.main:app --reload  # Start backend server normally
fi &
BACKEND_PID=$!

cd "$ROOT_DIR/frontend"

if [[ ! -d "node_modules" ]]; then
    echo "Installing frontend dependencies..."
    npm install
fi

echo "Starting frontend server..."
npm run dev &
FRONTEND_PID=$!

wait $BACKEND_PID $FRONTEND_PID
