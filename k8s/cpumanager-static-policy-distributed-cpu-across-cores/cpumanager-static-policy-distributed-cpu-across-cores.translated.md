# Kubernetes v1.31: New Kubernetes CPUManager Static Policy: Distribute CPUs Across Cores

In Kubernetes v1.31, we are excited to announce a significant improvement to the CPU management capabilities: the `distribute-cpus-across-cores` option for the [CPUManager static policy](/docs/tasks/administer-cluster/cpu-management-policies/#static-policy-options). This feature is currently in alpha and is hidden by default, marking a strategic shift aimed at optimizing CPU utilization and enhancing performance on multi-core processor systems.

## Understanding the Feature

Traditionally, Kubernetes' CPUManager has tended to allocate CPUs as compactly as possible, often packing them onto the fewest physical cores. However, the allocation strategy matters, as CPUs on the same physical host still share certain resources of the physical core, such as cache and execution units, etc.

![cpu-cache-architecture](/blog/2024/08/22/cpumanager-static-policy-distributed-cpu-across-cores/cpu-cache-architecture.png)

While the default approach minimizes inter-core communication and can be beneficial in some cases, it also presents challenges. CPUs sharing a physical core can lead to resource contention, which in turn can cause performance bottlenecks, especially in CPU-intensive applications.

The new `distribute-cpus-across-cores` feature addresses this issue by modifying the allocation strategy. When enabled, this policy option instructs CPUManager to distribute CPUs (hardware threads) as evenly as possible across multiple physical cores. This distribution aims to minimize contention between CPUs sharing the same physical core, potentially improving application performance by providing them with dedicated core resources.

Technically, in this static policy, the free CPU list is reordered in the way shown in the picture, aiming to allocate CPUs from different physical cores.

![cpu-ordering](/blog/2024/08/22/cpumanager-static-policy-distributed-cpu-across-cores/cpu-ordering.png)

## Enabling the Feature

To enable this feature, users first need to add the `--cpu-manager-policy=static` kubelet flag or the `cpuManagerPolicy: static` field in KubeletConfiuration. Then users can add `--cpu-manager-policy-options distribute-cpus-across-cores=true` or `distribute-cpus-across-cores=true` to the CPUManager policy options in the Kubernetes configuration. This setting instructs CPUManager to adopt the new distributed strategy. It's important to note that this policy option currently cannot be used with the `full-pcpus-only` or `distribute-cpus-across-numa` options.

## Current Limitations and Future Directions

As with any new feature, especially those in alpha, there are limitations and areas for future improvement. One significant limitation currently is that `distribute-cpus-across-cores` cannot be combined with other policy options that might conflict with the CPU allocation strategy. This limitation affects compatibility with certain workloads and deployment scenarios that rely on more specialized resource management.

Looking ahead, we are committed to enhancing the compatibility and functionality of the `distribute-cpus-across-cores` option. Future updates will focus on addressing these compatibility issues, allowing this policy to seamlessly integrate with other CPUManager policies. Our goal is to provide a more flexible and robust CPU allocation framework capable of accommodating diverse workloads and performance requirements.

## Conclusion

The introduction of the `distribute-cpus-across-cores` policy in Kubernetes CPUManager is a step in our ongoing efforts to improve resource management and enhance application performance. By reducing contention for physical cores, this feature offers a more balanced approach to CPU resource allocation, particularly beneficial for environments running heterogeneous workloads. We encourage Kubernetes users to test this new feature and provide feedback, which is crucial in shaping its future development.

This draft aims to clearly explain the new feature while setting expectations for its current stage and future improvements.

## Further Reading

Please refer to the [Controlling CPU Management Policies on Nodes](/docs/tasks/administer-cluster/cpu-management-policies/) task page for more information about CPUManager and its relationship with other node-level resource managers.

## Get Involved

This feature is driven by [SIG Node](https://github.com/Kubernetes/community/blob/master/sig-node/README.md). If you are interested in helping develop this feature, sharing feedback, or participating in any other ongoing SIG Node projects, please attend the SIG Node meetings for more details.