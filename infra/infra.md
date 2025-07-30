# Infrastructure Setup – Idea Validator

This file documents how to build, deploy, and test the Idea Validator FastAPI app using Docker and Kubernetes via Minikube.

---

## 📁 Project Structure

```
idea-validator-ai/
├── app/
│   └── main.py
├── infra/
│   └── k8s/
│       ├── deployment.yaml
│       ├── service.yaml
│       ├── namespace.yaml
│       └── ingress.yaml
├── requirements.txt
├── Dockerfile
└── infra.md  👈 (this file)
```

---

## 🔧 Step-by-Step Setup

### 1. 🐳 Build Docker Image

```bash
docker build -t idea-validator:latest -f Dockerfile .
```

---

### 2. 🚀 Start Minikube

```bash
minikube start
```

To use Minikube's internal Docker daemon:

```powershell
& minikube -p minikube docker-env --shell powershell | Invoke-Expression
```

You **must rebuild** inside Minikube after this.

---

### 3. 🔁 Rebuild Docker Image (inside Minikube's Docker)

```bash
docker build -t idea-validator:latest -f Dockerfile .
```

---

### 4. 🧩 Apply Kubernetes Configs

Optional: Create namespace and set context

```bash
kubectl apply -f infra/k8s/namespace.yaml
kubectl config set-context --current --namespace=idea-validator
```

Apply all configs:

```bash
kubectl apply -f infra/k8s/deployment.yaml
kubectl apply -f infra/k8s/service.yaml
kubectl apply -f infra/k8s/ingress.yaml  # optional
```

---

### 5. 🔍 Verify Pod Status

```bash
kubectl get pods
kubectl logs <pod-name>
```

---

### 6. 🌐 Test Service via Minikube

Run this to get the local URL:

```bash
minikube service idea-validator-service --url
```

Then test it:

```bash
curl -X POST http://127.0.0.1:<port>/validate   -H "Content-Type: application/json"   -d "{"idea": "An AI co-pilot for teachers"}"
```

---

## 🔄 Notes

- Always rebuild the image inside Minikube's Docker daemon if the code changes.
- Use `kubectl logs <pod>` for debugging.
- You can expose the app using Ingress (optional) by updating DNS or local `hosts` file.

---

## 📈 Optional: Ingress and Namespace Files

### `infra/k8s/namespace.yaml`

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: idea-validator
```

### `infra/k8s/ingress.yaml`

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: idea-validator-ingress
  namespace: idea-validator
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
    - host: idea.local
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: idea-validator-service
                port:
                  number: 8080
```

To use this:

```bash
minikube addons enable ingress
```

Then edit your system's hosts file:

```
127.0.0.1 idea.local
```

---

✅ You're all set. This project now runs locally in Kubernetes with Docker-built microservice infra. 