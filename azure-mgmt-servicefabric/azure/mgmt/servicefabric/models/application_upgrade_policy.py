# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApplicationUpgradePolicy(Model):
    """Describes the policy for a monitored application upgrade.

    :param upgrade_replica_set_check_timeout: The maximum amount of time to
     block processing of an upgrade domain and prevent loss of availability
     when there are unexpected issues. When this timeout expires, processing of
     the upgrade domain will proceed regardless of availability loss issues.
     The timeout is reset at the start of each upgrade domain. Valid values are
     between 0 and 42949672925 inclusive. (unsigned 32-bit integer).
    :type upgrade_replica_set_check_timeout: long
    :param force_restart: If true, then processes are forcefully restarted
     during upgrade even when the code version has not changed (the upgrade
     only changes configuration or data).
    :type force_restart: bool
    :param rolling_upgrade_monitoring_policy: The policy used for monitoring
     the application upgrade
    :type rolling_upgrade_monitoring_policy:
     ~azure.mgmt.servicefabric.models.RollingUpgradeMonitoringPolicy
    :param application_health_policy: Defines a health policy used to evaluate
     the health of an application or one of its children entities.
    :type application_health_policy:
     ~azure.mgmt.servicefabric.models.ArmApplicationHealthPolicy
    """

    _attribute_map = {
        'upgrade_replica_set_check_timeout': {'key': 'upgradeReplicaSetCheckTimeout', 'type': 'long'},
        'force_restart': {'key': 'forceRestart', 'type': 'bool'},
        'rolling_upgrade_monitoring_policy': {'key': 'rollingUpgradeMonitoringPolicy', 'type': 'RollingUpgradeMonitoringPolicy'},
        'application_health_policy': {'key': 'applicationHealthPolicy', 'type': 'ArmApplicationHealthPolicy'},
    }

    def __init__(self, **kwargs):
        super(ApplicationUpgradePolicy, self).__init__(**kwargs)
        self.upgrade_replica_set_check_timeout = kwargs.get('upgrade_replica_set_check_timeout', None)
        self.force_restart = kwargs.get('force_restart', None)
        self.rolling_upgrade_monitoring_policy = kwargs.get('rolling_upgrade_monitoring_policy', None)
        self.application_health_policy = kwargs.get('application_health_policy', None)
