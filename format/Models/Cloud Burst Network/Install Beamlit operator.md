# Install Beamlit operator

## Prerequisites

Before you begin, ensure that you have the following:

1. **Kubernetes Cluster**: A running Kubernetes cluster (version 1.18 or later is recommended). You can use managed services like [Amazon EKS](https://aws.amazon.com/eks/), [Google GKE](https://cloud.google.com/kubernetes-engine), [Azure AKS](https://azure.microsoft.com/services/kubernetes-service/), or set up your own cluster.
2. **kubectl**: Installed and configured to interact with your Kubernetes cluster. [Installation Guide](https://kubernetes.io/docs/tasks/tools/install-kubectl/).
3. **Helm**: Installed on your local machine. [Installation Guide](Install%20Beamlit%20operator.md).
4. **Access Permissions**: Sufficient permissions to install resources in the target Kubernetes cluster.

---

## Install Helm

If you haven't installed Helm yet, follow these steps:

1. **Download Helm**:
    
    Visit the [Helm Releases](https://github.com/helm/helm/releases) page and download the appropriate binary for your operating system.
    
2. **Install Helm**:
    
    For macOS using Homebrew:
    
    ```bash
    brew install helm
    
    ```
    
    For Linux:
    
    ```bash
    curl <https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3> | bash
    
    ```
    
    For Windows using Chocolatey:
    
    ```powershell
    choco install kubernetes-helm
    
    ```
    
3. **Verify Installation**:
    
    ```bash
    helm version
    
    ```
    
    You should see output similar to:
    
    ```
    version.BuildInfo{Version:"v3.10.0", GitCommit:"...", GitTreeState:"clean", GoVersion:"go1.20.5"}
    
    ```
    

---

## Add the Beamlit operator Helm Repository

1. **Add the Repository**:
    
    ```bash
    helm repo add ai-platform <https://charts.yourdomain.com/ai-platform>
    
    ```
    
2. **Update Helm Repositories**:
    
    Fetch the latest charts from all your configured repositories.
    
    ```bash
    helm repo update
    
    ```
    
3. **Verify the Repository is Added**:
    
    ```bash
    helm repo list
    
    ```
    
    You should see `[your-repo-name]` in the list.
    

---

## Create a Namespace (Optional)

It's a good practice to install the operator in a separate namespace. Replace `[namespace]` with your desired namespace name.

```bash
kubectl create namespace [namespace]

```

*Example:*

```bash
kubectl create namespace beamlit-operator

```

---

## Configure Custom Values (Optional)

The Helm chart comes with default configurations, but you can customize them as needed.

1. **Fetch Default `values.yaml`**:
    
    ```bash
    helm show values [your-repo-name]/[chart-name] > values.yaml
    
    ```
    
2. **Edit `values.yaml`**:
    
    Open `values.yaml` in your preferred text editor and modify the parameters as needed. Common configurations include:
    
    - **Control Plane Endpoint**: URL or IP address where the operator sends data.
    - **Authentication**: API keys or tokens for secure communication.
    - **Resource Limits**: CPU and memory allocations.
    - **Logging Level**: Adjust verbosity for logs.
    
    *Example:*
    
    ```yaml
    controlPlane:
      endpoint: "<https://controlplane.yourdomain.com>"
      apiKey: "your-api-key"
    
    resources:
      limits:
        cpu: "500m"
        memory: "256Mi"
    
    logging:
      level: "info"
    
    ```
    

---

## Install the Operator Using Helm

Once you have configured your settings, proceed to install the operator.

1. **Basic Installation**:
    
    ```bash
    helm install [release-name] [your-repo-name]/[chart-name] --namespace [namespace]
    
    ```
    
2. **Installation with Custom `values.yaml`**:
    
    If you've customized the `values.yaml`, use the `-f` flag to apply your configurations.
    
    ```bash
    helm install [release-name] [your-repo-name]/[chart-name] --namespace [namespace] -f values.yaml
    
    ```
    
3. **Verify Installation**:
    
    ```bash
    helm list --namespace [namespace]
    
    ```
    

---

## Verify the Installation

Ensure that all components of the operator are running correctly.

1. **Check Pods**:
    
    ```bash
    kubectl get pods --namespace [namespace]
    
    ```
    
    You should see pods related to your operator in the `Running` state.
    
2. **Check Services**:
    
    ```bash
    kubectl get services --namespace [namespace]
    
    ```
    
3. **Check Logs**:
    
    To troubleshoot or verify operations, view the logs of the operator pod.
    
    ```bash
    kubectl logs [pod-name] --namespace [namespace]
    
    ```
    

---

## Upgrading the Operator

To upgrade the operator to a newer version, follow these steps:

1. **Update Helm Repositories**:
    
    ```bash
    helm repo update
    
    ```
    
2. **Upgrade the Release**:
    
    ```bash
    helm upgrade [release-name] [your-repo-name]/[chart-name] --namespace [namespace]
    
    ```
    
    If you have a custom `values.yaml`, include the `-f` flag:
    
    ```bash
    helm upgrade ai-operator ai-platform/operator --namespace ai-operator -f values.yaml
    
    ```
    
3. **Verify the Upgrade**:
    
    Check the status of the release to ensure the upgrade was successful.
    
    ```bash
    helm status [release-name] --namespace [namespace]
    
    ```
    

---

## Uninstalling the Operator

If you need to remove the operator from your cluster, follow these steps:

1. **Uninstall the Helm Release**:
    
    ```bash
    helm uninstall [release-name] --namespace [namespace]
    
    ```
    
2. **Delete the Namespace (If Created)**:
    
    **⚠️ Warning**: This will delete all resources within the namespace.
    
    ```bash
    kubectl delete namespace [namespace]
    
    ```
    
3. **Remove Helm Repository (Optional)**:
    
    If you no longer need the Helm repository, you can remove it.
    
    ```bash
    helm repo remove [your-repo-name]
    
    ```
    

## Additional Resources

- **[Your Operator Name] Documentation**: [Link to comprehensive documentation]
- **Helm Documentation**: [https://helm.sh/docs/](https://helm.sh/docs/)
- **Kubernetes Documentation**: [https://kubernetes.io/docs/](https://kubernetes.io/docs/)
- **Support and Community**: Join our [Slack/Discord](Install%20Beamlit%20operator.md) or open an issue on [GitHub](Install%20Beamlit%20operator.md) for help.

## Troubleshooting Tips

- **Helm Not Found Error**: Ensure Helm is installed and added to your system's PATH.
- **Permission Denied**: Verify that your Kubernetes context has the necessary permissions to install resources in the target namespace.
- **Pod CrashLoopBackOff**: Check the pod logs for errors and ensure that all required configurations (e.g., API keys) are correctly set in `values.yaml`.
- **Network Issues**: Ensure that your cluster can reach the control plane endpoint specified in the configuration.