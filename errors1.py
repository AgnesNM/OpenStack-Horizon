nduta@nduta-XPS-13-9370:~/horizon$ tox -e npm -- lint
.pkg: _optional_hooks> python /home/nduta/.local/lib/python3.10/site-packages/pyproject_api/_backend.py True setuptools.build_meta __legacy__
.pkg: get_requires_for_build_editable> python /home/nduta/.local/lib/python3.10/site-packages/pyproject_api/_backend.py True setuptools.build_meta __legacy__
.pkg: build_editable> python /home/nduta/.local/lib/python3.10/site-packages/pyproject_api/_backend.py True setuptools.build_meta __legacy__
npm: install_package> python -I -m pip install --force-reinstall --no-deps /home/nduta/horizon/.tox/.tmp/package/14/horizon-25.1.1.dev1-0.editable-py3-none-any.whl
npm: commands[0]> nodeenv -p
 * Install prebuilt node (22.9.0) ..... done.
npm: commands[1]> npm install
⠹
> horizon@0.0.0 postinstall
> if [ ! -d .tox/npm ]; then tox -e npm --notest; fi


up to date, audited 400 packages in 7s

33 packages are looking for funding
  run `npm fund` for details

16 vulnerabilities (4 low, 3 moderate, 9 high)

To address issues that do not require attention, run:
  npm audit fix

To address all issues possible (including breaking changes), run:
  npm audit fix --force

Some issues need review, and may require choosing
a different dependency.

Run `npm audit` for details.
npm: commands[2]> npm run lint

> horizon@0.0.0 lint
> eslint --no-color openstack_dashboard/static horizon/static openstack_dashboard/dashboards/*/static


/home/nduta/horizon/openstack_dashboard/static/app/app.module.js
  74:3  warning  Missing JSDoc @returns for function              valid-jsdoc
  74:3  warning  Missing JSDoc for parameter '$locationProvider'  valid-jsdoc
  74:3  warning  Missing JSDoc for parameter '$routeProvider'     valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/cloud-services/hz-if-cinder-extensions.directive.js
  27:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/cloud-services/hz-if-neutron-extensions.directive.js
  27:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/cloud-services/hz-if-policies.directive.js
  29:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/cloud-services/hz-if-services.directive.js
  29:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/cloud-services/hz-if-settings.directive.js
  29:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/cloud-services/hz-if-version.directive.js
  31:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/conf/conf.module.js
  35:3  warning  Missing JSDoc @returns for function  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/flavors/flavors.module.js
  115:7  warning  Missing JSDoc @returns for function  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/images/actions/create.action.service.js
  37:3  warning  Missing JSDoc @returns for function                valid-jsdoc
  37:3  warning  Missing JSDoc for parameter '$q'                   valid-jsdoc
  37:3  warning  Missing JSDoc for parameter 'events'               valid-jsdoc
  37:3  warning  Missing JSDoc for parameter 'resourceType'         valid-jsdoc
  37:3  warning  Missing JSDoc for parameter 'createWorkflow'       valid-jsdoc
  37:3  warning  Missing JSDoc for parameter 'metadataService'      valid-jsdoc
  37:3  warning  Missing JSDoc for parameter 'glance'               valid-jsdoc
  37:3  warning  Missing JSDoc for parameter 'policy'               valid-jsdoc
  37:3  warning  Missing JSDoc for parameter 'actionResultService'  valid-jsdoc
  37:3  warning  Missing JSDoc for parameter 'wizardModalService'   valid-jsdoc
  37:3  warning  Missing JSDoc for parameter 'toast'                valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/images/actions/create.action.service.spec.js
  39:9   warning  'deferredCreate' was used before it was defined  no-use-before-define
  39:26  warning  '$q' was used before it was defined              no-use-before-define
  40:9   warning  'deferredCreate' was used before it was defined  no-use-before-define
  41:16  warning  'deferredCreate' was used before it was defined  no-use-before-define

/home/nduta/horizon/openstack_dashboard/static/app/core/images/actions/create.workflow.service.js
  30:3  warning  Missing JSDoc @returns for function            valid-jsdoc
  30:3  warning  Missing JSDoc for parameter 'basePath'         valid-jsdoc
  30:3  warning  Missing JSDoc for parameter 'workflowService'  valid-jsdoc
  30:3  warning  Missing JSDoc for parameter 'gettext'          valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/images/actions/delete-image.service.spec.js
  22:9   warning  'deferredModal' was used before it was defined  no-use-before-define
  26:16  warning  'deferredModal' was used before it was defined  no-use-before-define

/home/nduta/horizon/openstack_dashboard/static/app/core/images/actions/edit.action.service.js
   37:3   warning  Missing JSDoc @returns for function                valid-jsdoc
   37:3   warning  Missing JSDoc for parameter '$q'                   valid-jsdoc
   37:3   warning  Missing JSDoc for parameter 'imageResourceType'    valid-jsdoc
   37:3   warning  Missing JSDoc for parameter 'editWorkflow'         valid-jsdoc
   37:3   warning  Missing JSDoc for parameter 'metadataService'      valid-jsdoc
   37:3   warning  Missing JSDoc for parameter 'glance'               valid-jsdoc
   37:3   warning  Missing JSDoc for parameter 'policy'               valid-jsdoc
   37:3   warning  Missing JSDoc for parameter 'actionResultService'  valid-jsdoc
   37:3   warning  Missing JSDoc for parameter '$qExtensions'         valid-jsdoc
   37:3   warning  Missing JSDoc for parameter 'wizardModalService'   valid-jsdoc
   37:3   warning  Missing JSDoc for parameter 'toast'                valid-jsdoc
  103:34  error    Missing space before opening brace                 space-before-blocks

/home/nduta/horizon/openstack_dashboard/static/app/core/images/actions/edit.workflow.service.js
  29:3  warning  Missing JSDoc @returns for function            valid-jsdoc
  29:3  warning  Missing JSDoc for parameter 'basePath'         valid-jsdoc
  29:3  warning  Missing JSDoc for parameter 'workflowService'  valid-jsdoc
  29:3  warning  Missing JSDoc for parameter 'gettext'          valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/images/actions/launch-instance.service.js
  31:3  warning  Expected JSDoc for 'policy' but found 'launchInstanceModal'        valid-jsdoc
  31:3  warning  Expected JSDoc for 'launchInstanceModal' but found '$qExtensions'  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/images/actions/update-metadata.action.service.js
  32:3  warning  Expected JSDoc for 'actionResultService' but found '$qExtensions'  valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'imageResourceType'                    valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/images/images.module.js
  200:3  warning  Missing JSDoc @returns for function          valid-jsdoc
  212:3  warning  Missing JSDoc @returns for function          valid-jsdoc
  234:3  warning  Missing JSDoc @returns for function          valid-jsdoc
  234:3  warning  Missing JSDoc for parameter 'imagesService'  valid-jsdoc
  234:3  warning  Missing JSDoc for parameter 'statuses'       valid-jsdoc
  285:3  warning  Missing JSDoc for parameter 'detailRoute'    valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/images/images.service.js
   96:5  warning  Missing JSDoc parameter type for 'item'  valid-jsdoc
   96:5  warning  Missing JSDoc return description         valid-jsdoc
  172:5  warning  Missing JSDoc @returns for function      valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/images/images.service.spec.js
  70:31  warning  Unexpected use of undefined  no-undefined
  75:31  warning  Unexpected use of undefined  no-undefined

/home/nduta/horizon/openstack_dashboard/static/app/core/images/steps/create-image/create-image.controller.js
   34:3   warning  Missing JSDoc @returns for function            valid-jsdoc
   34:3   warning  Missing JSDoc for parameter '$scope'           valid-jsdoc
   34:3   warning  Missing JSDoc for parameter 'glance'           valid-jsdoc
   34:3   warning  Missing JSDoc for parameter 'events'           valid-jsdoc
   34:3   warning  Missing JSDoc for parameter 'imageFormats'     valid-jsdoc
   34:3   warning  Missing JSDoc for parameter 'validationRules'  valid-jsdoc
   34:3   warning  Missing JSDoc for parameter 'settings'         valid-jsdoc
   34:3   warning  Missing JSDoc for parameter 'policyAPI'        valid-jsdoc
  145:14  warning  Gratuitous parentheses around expression       no-extra-parens

/home/nduta/horizon/openstack_dashboard/static/app/core/images/steps/create-volume/create-volume.controller.js
  34:3  warning  Missing JSDoc for parameter 'BYTE_TO_GIB'  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/images/steps/deactivate/deactivate.controller.js
  10:7   error  Expected indentation of 4 space characters but found 6   indent
  16:7   error  Expected indentation of 4 space characters but found 6   indent
  18:7   error  Expected indentation of 4 space characters but found 6   indent
  23:7   error  Expected indentation of 4 space characters but found 6   indent
  25:7   error  Expected indentation of 4 space characters but found 6   indent
  29:7   error  Expected indentation of 4 space characters but found 6   indent
  30:11  error  Expected indentation of 8 space characters but found 10  indent
  31:11  error  Expected indentation of 8 space characters but found 10  indent
  34:7   error  Expected indentation of 4 space characters but found 6   indent
  35:11  error  Expected indentation of 8 space characters but found 10  indent
  36:11  error  Expected indentation of 8 space characters but found 10  indent
  37:11  error  Expected indentation of 8 space characters but found 10  indent
  38:11  error  Expected indentation of 8 space characters but found 10  indent
  41:7   error  Expected indentation of 4 space characters but found 6   indent
  42:11  error  Expected indentation of 8 space characters but found 10  indent
  45:7   error  Expected indentation of 4 space characters but found 6   indent
  46:10  error  Expected indentation of 8 space characters but found 9   indent
  48:5   error  Expected indentation of 2 space characters but found 4   indent

/home/nduta/horizon/openstack_dashboard/static/app/core/images/steps/edit-image/edit-image.controller.js
  32:3  warning  Missing JSDoc @returns for function            valid-jsdoc
  32:3  warning  Missing JSDoc for parameter '$scope'           valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'imageFormats'     valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'validationRules'  valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'settings'         valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'policy'           valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/images/steps/update-metadata/update-metadata.controller.js
  31:3  warning  Missing JSDoc @returns for function                valid-jsdoc
  31:3  warning  Missing JSDoc for parameter '$scope'               valid-jsdoc
  31:3  warning  Missing JSDoc for parameter '$q'                   valid-jsdoc
  31:3  warning  Missing JSDoc for parameter 'events'               valid-jsdoc
  31:3  warning  Missing JSDoc for parameter 'metadataService'      valid-jsdoc
  31:3  warning  Missing JSDoc for parameter 'metadataTreeService'  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/keypairs/actions/create.service.js
   79:28  warning  Gratuitous parentheses around expression           no-extra-parens
  131:5   warning  Expected JSDoc for 'response' but found 'keypair'  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/keypairs/actions/import.service.js
  82:28  warning  Gratuitous parentheses around expression  no-extra-parens

/home/nduta/horizon/openstack_dashboard/static/app/core/keypairs/keypair.controller.js
  32:3  warning  Expected JSDoc for 'nova' but found '$uibModal'  valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'spinnerService'     valid-jsdoc
  32:3  warning  Missing JSDoc for parameter '$window'            valid-jsdoc
  77:5  warning  Missing JSDoc for parameter 'config'             valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/metadata/metadata.service.js
  29:3  warning  Missing JSDoc @returns for function   valid-jsdoc
  29:3  warning  Missing JSDoc for parameter 'nova'    valid-jsdoc
  29:3  warning  Missing JSDoc for parameter 'glance'  valid-jsdoc
  29:3  warning  Missing JSDoc for parameter 'cinder'  valid-jsdoc
  45:5  warning  Missing JSDoc @returns for function   valid-jsdoc
  63:5  warning  Missing JSDoc @returns for function   valid-jsdoc
  83:5  warning  Missing JSDoc @returns for function   valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/metadata/modal/modal-helper.controller.js
  29:3  warning  JSDoc syntax error                   valid-jsdoc
  41:5  warning  Missing JSDoc @returns for function  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/metadata/modal/modal.controller.js
  35:3  warning  Missing JSDoc @returns for function                valid-jsdoc
  35:3  warning  Missing JSDoc for parameter '$uibModalInstance'    valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'metadataService'      valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'metadataTreeService'  valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'toastService'         valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'available'            valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'existing'             valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'params'               valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/metadata/modal/modal.service.js
  30:3  warning  Missing JSDoc @returns for function            valid-jsdoc
  30:3  warning  Missing JSDoc for parameter '$uibModal'        valid-jsdoc
  30:3  warning  Missing JSDoc for parameter 'path'             valid-jsdoc
  30:3  warning  Missing JSDoc for parameter 'metadataService'  valid-jsdoc
  30:3  warning  Missing JSDoc for parameter 'modalConstants'   valid-jsdoc
  41:5  warning  Missing JSDoc @returns for function            valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/network_qos/actions/add-rule.action.service.js
  138:12  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style
  145:12  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style
  146:53  warning  Unexpected use of undefined                                                   no-undefined
  155:12  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style

/home/nduta/horizon/openstack_dashboard/static/app/core/network_qos/actions/add-rule.action.service.spec.js
  56:37  warning  Unexpected use of undefined  no-undefined

/home/nduta/horizon/openstack_dashboard/static/app/core/network_qos/actions/create.action.service.spec.js
  64:57  warning  Unexpected use of undefined  no-undefined
  70:36  warning  Unexpected use of undefined  no-undefined

/home/nduta/horizon/openstack_dashboard/static/app/core/network_qos/actions/delete-rule.action.service.js
   78:12  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style
   90:13  warning  Gratuitous parentheses around expression                                      no-extra-parens
   90:35  warning  Gratuitous parentheses around expression                                      no-extra-parens
   91:22  warning  Gratuitous parentheses around expression                                      no-extra-parens
   97:12  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style
  100:12  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style
  103:12  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style

/home/nduta/horizon/openstack_dashboard/static/app/core/network_qos/actions/delete.action.service.spec.js
  22:9   warning  'deferredModal' was used before it was defined  no-use-before-define
  26:16  warning  'deferredModal' was used before it was defined  no-use-before-define

/home/nduta/horizon/openstack_dashboard/static/app/core/network_qos/actions/edit-rule.action.service.js
  126:12  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style
  147:12  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style
  151:12  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style
  156:12  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style

/home/nduta/horizon/openstack_dashboard/static/app/core/network_qos/actions/edit-rule.controller.js
  58:12  warning  Closing curly brace does not appear on the same line as the subsequent block        brace-style
  69:12  warning  Closing curly brace does not appear on the same line as the subsequent block        brace-style
  81:12  warning  Closing curly brace does not appear on the same line as the subsequent block        brace-style
  93:8   warning  You should not use "this" directly. Instead, assign it to a variable called "ctrl"  angular/controller-as-vm

/home/nduta/horizon/openstack_dashboard/static/app/core/network_qos/actions/edit-rule.controller.spec.js
  91:24  warning  Unexpected use of undefined  no-undefined

/home/nduta/horizon/openstack_dashboard/static/app/core/network_qos/actions/workflow/delete-rule.workflow.service.js
   91:16  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style
   98:16  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style
  105:16  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style

/home/nduta/horizon/openstack_dashboard/static/app/core/network_qos/qos.module.js
   97:3  warning  Missing JSDoc @returns for function  valid-jsdoc
  123:3  warning  Missing JSDoc @returns for function  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/openstack-service-api/cinder.service.js
  359:5  warning  Missing JSDoc @returns for function   valid-jsdoc
  375:5  warning  Missing JSDoc @returns for function   valid-jsdoc
  375:5  warning  Missing JSDoc for parameter 'quotas'  valid-jsdoc
  390:5  warning  Missing JSDoc @returns for function   valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/openstack-service-api/keystone.service.js
  391:5  warning  Missing JSDoc for parameter 'type'  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/openstack-service-api/neutron.service.js
  331:5  warning  Missing JSDoc @returns for function                         valid-jsdoc
  349:5  warning  Missing JSDoc @returns for function                         valid-jsdoc
  368:5  warning  Missing JSDoc for parameter 'suppressError'                 valid-jsdoc
  388:5  warning  Missing JSDoc @returns for function                         valid-jsdoc
  388:5  warning  Missing JSDoc for parameter 'params'                        valid-jsdoc
  445:4  warning  Missing JSDoc @returns for function                         valid-jsdoc
  445:4  warning  Missing JSDoc for parameter 'suppressError'                 valid-jsdoc
  725:5  warning  Missing JSDoc @returns for function                         valid-jsdoc
  725:5  warning  Expected JSDoc for 'deleteRuleId' but found 'deleteruleId'  valid-jsdoc
  744:5  warning  Missing JSDoc @returns for function                         valid-jsdoc
  744:5  warning  Expected JSDoc for 'deleteRuleId' but found 'deleteruleId'  valid-jsdoc
  762:5  warning  Missing JSDoc @returns for function                         valid-jsdoc
  762:5  warning  Expected JSDoc for 'deleteRuleId' but found 'deleteruleId'  valid-jsdoc
  780:5  warning  Missing JSDoc @returns for function                         valid-jsdoc
  780:5  warning  Expected JSDoc for 'deleteRuleId' but found 'deleteruleId'  valid-jsdoc
  826:5  warning  Missing JSDoc for parameter 'params'                        valid-jsdoc
  847:5  warning  Missing JSDoc @returns for function                         valid-jsdoc
  847:5  warning  Missing JSDoc for parameter 'newTrunk'                      valid-jsdoc
  859:5  warning  Missing JSDoc @returns for function                         valid-jsdoc
  879:5  warning  Missing JSDoc @returns for function                         valid-jsdoc
  879:5  warning  Missing JSDoc for parameter 'oldTrunk'                      valid-jsdoc
  879:5  warning  Missing JSDoc for parameter 'newTrunk'                      valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/openstack-service-api/nova.service.js
   93:5  warning  Missing JSDoc for parameter 'feature'           valid-jsdoc
  224:5  warning  Missing JSDoc for parameter 'reserved'          valid-jsdoc
  424:5  warning  Missing JSDoc for parameter 'suppressError'     valid-jsdoc
  438:5  warning  Missing JSDoc for parameter 'suppressError'     valid-jsdoc
  452:5  warning  Missing JSDoc for parameter 'suppressError'     valid-jsdoc
  466:5  warning  Missing JSDoc for parameter 'suppressError'     valid-jsdoc
  480:5  warning  Missing JSDoc for parameter 'suppressError'     valid-jsdoc
  494:5  warning  Missing JSDoc for parameter 'suppressError'     valid-jsdoc
  508:5  warning  Missing JSDoc for parameter 'suppressError'     valid-jsdoc
  522:5  warning  Missing JSDoc for parameter 'suppressError'     valid-jsdoc
  766:5  warning  Missing JSDoc @returns for function             valid-jsdoc
  782:5  warning  Missing JSDoc @returns for function             valid-jsdoc
  782:5  warning  Missing JSDoc for parameter 'quotas'            valid-jsdoc
  797:5  warning  Missing JSDoc @returns for function             valid-jsdoc
  812:5  warning  Missing JSDoc @returns for function             valid-jsdoc
  848:5  warning  Expected JSDoc for 'instanceId' but found 'ID'  valid-jsdoc
  918:5  warning  Expected JSDoc for 'instanceId' but found 'ID'  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/openstack-service-api/nova.service.spec.js
  269:25  warning  Unexpected use of undefined  no-undefined

/home/nduta/horizon/openstack_dashboard/static/app/core/openstack-service-api/swift.service.js
  110:5  warning  Missing JSDoc for parameter 'params'       valid-jsdoc
  126:5  warning  Missing JSDoc for parameter 'ignoreError'  valid-jsdoc
  283:5  warning  Missing JSDoc for parameter 'ignoreError'  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/server_groups/actions/create.action.service.js
  33:3  warning  Missing JSDoc @returns for function                valid-jsdoc
  33:3  warning  Missing JSDoc for parameter 'novaAPI'              valid-jsdoc
  33:3  warning  Missing JSDoc for parameter 'policy'               valid-jsdoc
  33:3  warning  Missing JSDoc for parameter 'workflow'             valid-jsdoc
  33:3  warning  Missing JSDoc for parameter 'resourceType'         valid-jsdoc
  33:3  warning  Missing JSDoc for parameter 'modalFormService'     valid-jsdoc
  33:3  warning  Missing JSDoc for parameter 'toast'                valid-jsdoc
  33:3  warning  Missing JSDoc for parameter 'actionResultService'  valid-jsdoc
  33:3  warning  Missing JSDoc for parameter 'gettext'              valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/server_groups/server-groups.module.js
  89:3  warning  Missing JSDoc @returns for function  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/trunks/actions/create.action.service.js
  41:3   warning  Missing JSDoc @returns for function                valid-jsdoc
  41:3   warning  Missing JSDoc for parameter '$q'                   valid-jsdoc
  41:3   warning  Missing JSDoc for parameter 'neutron'              valid-jsdoc
  41:3   warning  Missing JSDoc for parameter 'policy'               valid-jsdoc
  41:3   warning  Missing JSDoc for parameter 'userSession'          valid-jsdoc
  41:3   warning  Missing JSDoc for parameter 'createWorkflow'       valid-jsdoc
  41:3   warning  Missing JSDoc for parameter 'portsExtra'           valid-jsdoc
  41:3   warning  Missing JSDoc for parameter 'resourceType'         valid-jsdoc
  41:3   warning  Missing JSDoc for parameter 'actionResultService'  valid-jsdoc
  41:3   warning  Missing JSDoc for parameter 'wizardModalService'   valid-jsdoc
  41:3   warning  Missing JSDoc for parameter 'toast'                valid-jsdoc
  41:3   warning  Missing JSDoc for parameter '$location'            valid-jsdoc
  70:7   warning  Unexpected 'todo' comment                          no-warning-comments
  71:29  warning  Gratuitous parentheses around expression           no-extra-parens
  98:18  warning  Unexpected use of undefined                        no-undefined

/home/nduta/horizon/openstack_dashboard/static/app/core/trunks/actions/create.action.service.spec.js
  39:19  warning  Unexpected use of undefined  no-undefined

/home/nduta/horizon/openstack_dashboard/static/app/core/trunks/actions/create.workflow.service.js
  30:3  warning  Missing JSDoc @returns for function            valid-jsdoc
  30:3  warning  Missing JSDoc for parameter 'basePath'         valid-jsdoc
  30:3  warning  Missing JSDoc for parameter 'workflowService'  valid-jsdoc
  30:3  warning  Missing JSDoc for parameter 'gettext'          valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/trunks/actions/delete.action.service.spec.js
  24:9   warning  'deferredModal' was used before it was defined  no-use-before-define
  28:16  warning  'deferredModal' was used before it was defined  no-use-before-define

/home/nduta/horizon/openstack_dashboard/static/app/core/trunks/actions/edit.action.service.js
  39:3   warning  Missing JSDoc @returns for function                valid-jsdoc
  39:3   warning  Missing JSDoc for parameter '$q'                   valid-jsdoc
  39:3   warning  Missing JSDoc for parameter '$location'            valid-jsdoc
  39:3   warning  Missing JSDoc for parameter 'neutron'              valid-jsdoc
  39:3   warning  Missing JSDoc for parameter 'policy'               valid-jsdoc
  39:3   warning  Missing JSDoc for parameter 'userSession'          valid-jsdoc
  39:3   warning  Missing JSDoc for parameter 'editWorkflow'         valid-jsdoc
  39:3   warning  Missing JSDoc for parameter 'portsExtra'           valid-jsdoc
  39:3   warning  Missing JSDoc for parameter 'resourceType'         valid-jsdoc
  39:3   warning  Missing JSDoc for parameter 'actionResultService'  valid-jsdoc
  39:3   warning  Missing JSDoc for parameter 'wizardModalService'   valid-jsdoc
  39:3   warning  Missing JSDoc for parameter 'toast'                valid-jsdoc
  39:3   warning  Missing JSDoc for parameter '$rootScope'           valid-jsdoc
  64:39  warning  Gratuitous parentheses around expression           no-extra-parens
  76:7   warning  Unexpected 'todo' comment                          no-warning-comments
  77:29  warning  Gratuitous parentheses around expression           no-extra-parens
  99:11  warning  Gratuitous parentheses around expression           no-extra-parens

/home/nduta/horizon/openstack_dashboard/static/app/core/trunks/actions/edit.action.service.spec.js
  39:19  warning  Unexpected use of undefined  no-undefined

/home/nduta/horizon/openstack_dashboard/static/app/core/trunks/actions/edit.workflow.service.js
  30:3  warning  Missing JSDoc @returns for function            valid-jsdoc
  30:3  warning  Missing JSDoc for parameter 'basePath'         valid-jsdoc
  30:3  warning  Missing JSDoc for parameter 'workflowService'  valid-jsdoc
  30:3  warning  Missing JSDoc for parameter 'gettext'          valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/trunks/actions/ports-extra.service.js
   24:3  warning  Missing JSDoc @returns for function       valid-jsdoc
  101:9  warning  Gratuitous parentheses around expression  no-extra-parens

/home/nduta/horizon/openstack_dashboard/static/app/core/trunks/trunks.module.js
  124:3  warning  Missing JSDoc @returns for function  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/app/core/trunks/trunks.service.js
  103:35  warning  Gratuitous parentheses around expression  no-extra-parens
  155:9   warning  Unexpected 'todo' comment                 no-warning-comments

/home/nduta/horizon/openstack_dashboard/static/app/redirect.controller.js
  28:3  warning  Missing JSDoc @returns for function               valid-jsdoc
  28:3  warning  Missing JSDoc for parameter '$window'             valid-jsdoc
  28:3  warning  Missing JSDoc for parameter '$location'           valid-jsdoc
  28:3  warning  Missing JSDoc for parameter 'gettext'             valid-jsdoc
  28:3  warning  Missing JSDoc for parameter 'waitSpinnerService'  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/static/js/horizon.flatnetworktopology.js
  106:60  warning  'vnc_window' was used before it was defined  no-use-before-define

/home/nduta/horizon/openstack_dashboard/static/js/horizon.networktopology.js
  130:73  warning  'vncWindow' was used before it was defined            no-use-before-define
  317:17  warning  Function 'convex_hulls' has a complexity of 11        complexity
  374:21  warning  Function 'anonymous' has a complexity of 13           complexity
  558:21  warning  Function 'collapse_network' has a complexity of 14    complexity
  655:18  warning  Function 'load_topology' has a complexity of 29       complexity
  906:23  warning  Function 'removePortOrSubnet' has a complexity of 11  complexity
  958:17  warning  Function 'show_balloon' has a complexity of 14        complexity

/home/nduta/horizon/openstack_dashboard/static/js/horizon.quota.js
  323:39  warning  Function 'anonymous' has a complexity of 16  complexity

/home/nduta/horizon/horizon/static/auth/login/login.module.js
  27:3  warning  Missing JSDoc @returns for function            valid-jsdoc
  27:3  warning  Missing JSDoc for parameter '$provide'         valid-jsdoc
  27:3  warning  Missing JSDoc for parameter '$windowProvider'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/conf/permissions.service.js
  25:3  warning  JSDoc syntax error                        valid-jsdoc
  60:5  warning  Missing JSDoc @returns for function       valid-jsdoc
  60:5  warning  Missing JSDoc for parameter 'configItem'  valid-jsdoc
  72:5  warning  Missing JSDoc @returns for function       valid-jsdoc
  72:5  warning  Missing JSDoc for parameter 'configItem'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/conf/resource-type-registry.service.js
  168:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  168:7  warning  Missing JSDoc for parameter 'name'        valid-jsdoc
  168:7  warning  Missing JSDoc for parameter 'prop'        valid-jsdoc
  202:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  202:7  warning  Missing JSDoc for parameter 'properties'  valid-jsdoc
  227:7  warning  Missing JSDoc return description          valid-jsdoc
  235:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  235:7  warning  Missing JSDoc for parameter 'func'        valid-jsdoc
  262:7  warning  Missing JSDoc return description          valid-jsdoc
  270:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  287:7  warning  Missing JSDoc return description          valid-jsdoc
  299:7  warning  Missing JSDoc parameter type for 'func'   valid-jsdoc
  321:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  357:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  357:7  warning  Missing JSDoc for parameter 'func'        valid-jsdoc
  384:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  384:7  warning  Missing JSDoc for parameter 'subpath'     valid-jsdoc
  405:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  405:7  warning  Missing JSDoc for parameter 'func'        valid-jsdoc
  427:7  warning  Missing JSDoc return description          valid-jsdoc
  435:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  435:7  warning  Missing JSDoc for parameter 'spec'        valid-jsdoc
  451:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  451:7  warning  Missing JSDoc for parameter 'func'        valid-jsdoc
  477:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  477:7  warning  Missing JSDoc for parameter 'item'        valid-jsdoc
  494:7  warning  Missing JSDoc parameter type for 'url'    valid-jsdoc
  494:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  510:7  warning  Missing JSDoc parameter type for 'url'    valid-jsdoc
  510:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  528:7  warning  Missing JSDoc parameter type for 'url'    valid-jsdoc
  528:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  539:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  539:7  warning  Missing JSDoc for parameter 'func'        valid-jsdoc
  551:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  551:7  warning  Missing JSDoc for parameter 'item'        valid-jsdoc
  564:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  564:7  warning  Missing JSDoc for parameter 'count'       valid-jsdoc
  609:7  warning  Missing JSDoc @returns for function       valid-jsdoc
  609:7  warning  Missing JSDoc for parameter 'name'        valid-jsdoc
  629:7  warning  Missing JSDoc return description          valid-jsdoc
  641:7  warning  Missing JSDoc parameter type for 'func'   valid-jsdoc
  641:7  warning  Missing JSDoc return description          valid-jsdoc

/home/nduta/horizon/horizon/static/framework/util/actions/action-result.service.js
  24:3  warning  Missing JSDoc @returns for function       valid-jsdoc
  94:5  warning  Missing JSDoc parameter type for 'items'  valid-jsdoc
  94:5  warning  Missing JSDoc parameter type for 'type'   valid-jsdoc
  94:5  warning  Missing JSDoc return type                 valid-jsdoc

/home/nduta/horizon/horizon/static/framework/util/extensible/extensible.service.js
   29:3  warning  JSDoc syntax error                    valid-jsdoc
   46:3  warning  Missing JSDoc @returns for function   valid-jsdoc
  194:5  warning  Missing JSDoc @returns for function   valid-jsdoc
  194:5  warning  Missing JSDoc for parameter '$scope'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/util/file/file-reader.service.js
  26:3  warning  Missing JSDoc @returns for function  valid-jsdoc
  26:3  warning  Missing JSDoc for parameter '$q'     valid-jsdoc

/home/nduta/horizon/horizon/static/framework/util/file/text-download.service.js
  24:3  warning  Missing JSDoc @returns for function     valid-jsdoc
  24:3  warning  Missing JSDoc for parameter '$q'        valid-jsdoc
  24:3  warning  Missing JSDoc for parameter '$timeout'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/util/filters/filters.js
  100:3  warning  Missing JSDoc @returns for function  valid-jsdoc
  123:3  warning  Missing JSDoc @returns for function  valid-jsdoc
  146:3  warning  Missing JSDoc @returns for function  valid-jsdoc
  163:3  warning  Missing JSDoc @returns for function  valid-jsdoc
  178:3  warning  Missing JSDoc @returns for function  valid-jsdoc
  196:3  warning  Missing JSDoc @returns for function  valid-jsdoc
  208:3  warning  Missing JSDoc @returns for function  valid-jsdoc
  223:3  warning  Missing JSDoc @returns for function  valid-jsdoc
  252:3  warning  Missing JSDoc @returns for function  valid-jsdoc
  282:3  warning  Missing JSDoc @returns for function  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/util/filters/filters.spec.js
   49:28  warning  Unexpected use of undefined  no-undefined
  184:28  warning  Unexpected use of undefined  no-undefined
  184:45  warning  Unexpected use of undefined  no-undefined
  242:30  warning  Unexpected use of undefined  no-undefined
  333:34  warning  Unexpected use of undefined  no-undefined

/home/nduta/horizon/horizon/static/framework/util/filters/helpers.borrowed-from-underscore.js
  23:3  warning  Missing JSDoc @returns for function  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/util/http/http.js
  94:14  warning  Unexpected use of undefined  no-undefined

/home/nduta/horizon/horizon/static/framework/util/http/http.spec.js
  48:43  warning  Unexpected use of undefined  no-undefined
  61:43  warning  Unexpected use of undefined  no-undefined

/home/nduta/horizon/horizon/static/framework/util/i18n/i18n.js
  26:3  warning  Missing JSDoc @returns for function    valid-jsdoc
  26:3  warning  Missing JSDoc for parameter '$window'  valid-jsdoc
  59:3  warning  Missing JSDoc @returns for function    valid-jsdoc
  59:3  warning  Missing JSDoc for parameter '$window'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/util/navigations/navigations.service.js
  123:80  warning  Unnecessary use of boolean literals in conditional expression  no-unneeded-ternary

/home/nduta/horizon/horizon/static/framework/util/promise-toggle/hz-promise-toggle.directive.mock.js
  29:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/util/q/q.extensions.js
  23:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/util/uuid/uuid.js
  23:3  warning  Missing JSDoc @returns for function  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/util/workflow/workflow.service.js
  29:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/action-list/actions.controller.js
  24:3   warning  JSDoc syntax error           valid-jsdoc
  94:37  warning  Unexpected use of undefined  no-undefined

/home/nduta/horizon/horizon/static/framework/widgets/action-list/actions.directive.js
  26:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/action-list/actions.directive.spec.js
  72:45  warning  Unexpected use of undefined  no-undefined

/home/nduta/horizon/horizon/static/framework/widgets/action-list/actions.service.js
   80:7  warning  Missing JSDoc @returns for function                valid-jsdoc
   80:7  warning  Missing JSDoc for parameter 'permittedActions'     valid-jsdoc
  109:7  warning  Missing JSDoc @returns for function                valid-jsdoc
  109:7  warning  Missing JSDoc for parameter 'templates'            valid-jsdoc
  116:7  warning  Missing JSDoc @returns for function                valid-jsdoc
  116:7  warning  Missing JSDoc for parameter 'template'             valid-jsdoc
  123:7  warning  Missing JSDoc @returns for function                valid-jsdoc
  123:7  warning  Missing JSDoc for parameter 'templates'            valid-jsdoc
  138:7  warning  Missing JSDoc @returns for function                valid-jsdoc
  138:7  warning  Missing JSDoc for parameter 'actionTemplate'       valid-jsdoc
  138:7  warning  Missing JSDoc for parameter 'scope'                valid-jsdoc
  152:7  warning  Missing JSDoc @returns for function                valid-jsdoc
  152:7  warning  Missing JSDoc for parameter 'actionList'           valid-jsdoc
  152:7  warning  Missing JSDoc for parameter 'splitButton'          valid-jsdoc
  152:7  warning  Missing JSDoc for parameter 'scope'                valid-jsdoc
  165:7  warning  Missing JSDoc @returns for function                valid-jsdoc
  165:7  warning  Missing JSDoc for parameter 'actionTemplate'       valid-jsdoc
  176:7  warning  Missing JSDoc @returns for function                valid-jsdoc
  176:7  warning  Missing JSDoc for parameter 'actionList'           valid-jsdoc
  185:7  warning  Missing JSDoc @returns for function                valid-jsdoc
  185:7  warning  Missing JSDoc for parameter 'actionTemplate'       valid-jsdoc
  195:7  warning  Missing JSDoc @returns for function                valid-jsdoc
  195:7  warning  Missing JSDoc for parameter 'permittedAction'      valid-jsdoc
  195:7  warning  Missing JSDoc for parameter 'index'                valid-jsdoc
  195:7  warning  Missing JSDoc for parameter 'permittedActions'     valid-jsdoc
  226:7  warning  Missing JSDoc @returns for function                valid-jsdoc
  226:7  warning  Missing JSDoc for parameter 'action'               valid-jsdoc
  226:7  warning  Missing JSDoc for parameter 'index'                valid-jsdoc
  226:7  warning  Missing JSDoc for parameter 'numPermittedActions'  valid-jsdoc
  266:7  warning  Missing JSDoc @returns for function                valid-jsdoc
  266:7  warning  Missing JSDoc for parameter 'action'               valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/action-list/button-tooltip.row-warning.service.js
  29:3  warning  Missing JSDoc @returns for function     valid-jsdoc
  29:3  warning  Missing JSDoc for parameter '$timeout'  valid-jsdoc
  29:3  warning  Missing JSDoc for parameter 'path'      valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/charts/chart-tooltip.directive.js
  25:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/charts/charts.module.js
  116:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/charts/pie-chart.directive.js
  179:22  warning  'totalWithUnit' used outside of binding context  block-scoped-var

/home/nduta/horizon/horizon/static/framework/widgets/details/details.directive.js
  25:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/details/routed-details-view.controller.js
  127:11  warning  Gratuitous parentheses around expression  no-extra-parens
  127:44  warning  Gratuitous parentheses around expression  no-extra-parens

/home/nduta/horizon/horizon/static/framework/widgets/form/builders.provider.js
  24:3  warning  Missing JSDoc @returns for function  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/form/modal-form.service.js
  30:3  warning  Missing JSDoc @returns for function            valid-jsdoc
  30:3  warning  Missing JSDoc for parameter '$uibModal'        valid-jsdoc
  30:3  warning  Missing JSDoc for parameter 'widgetsBasePath'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/headers/hz-page-header.directive.js
  26:3  warning  Missing JSDoc @returns for function     valid-jsdoc
  26:3  warning  Missing JSDoc for parameter 'basePath'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/help-panel/help-panel.directive.js
  27:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/load-edit/load-edit.directive.js
  147:26  warning  Unexpected use of undefined  no-undefined

/home/nduta/horizon/horizon/static/framework/widgets/magic-search/hz-magic-search-bar.directive.js
  23:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/magic-search/hz-magic-search-context.directive.js
  28:3  warning  Missing JSDoc @returns for function                               valid-jsdoc
  28:3  warning  Expected JSDoc for '$parse' but found 'filterFacets'              valid-jsdoc
  28:3  warning  Expected JSDoc for 'magicSearchEvents' but found 'filterStrings'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/magic-search/magic-search.controller.js
  87:10  warning  There should be no spaces inside this paren  space-in-parens
  87:17  warning  There should be no spaces inside this paren  space-in-parens
  88:12  warning  There should be no spaces inside this paren  space-in-parens
  88:30  warning  There should be no spaces inside this paren  space-in-parens
  93:29  warning  Unexpected use of undefined                  no-undefined

/home/nduta/horizon/horizon/static/framework/widgets/magic-search/magic-search.controller.spec.js
  517:88  warning  Unexpected use of undefined                  no-undefined
  610:23  warning  Unexpected use of undefined                  no-undefined
  645:53  warning  There should be no spaces inside this paren  space-in-parens
  666:53  warning  There should be no spaces inside this paren  space-in-parens

/home/nduta/horizon/horizon/static/framework/widgets/magic-search/magic-search.service.js
   52:3  warning  Missing JSDoc return type  valid-jsdoc
  142:5  warning  Unexpected 'todo' comment  no-warning-comments

/home/nduta/horizon/horizon/static/framework/widgets/magic-search/st-magic-search.directive.js
  27:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/metadata/display/metadata-display.controller.js
  27:3  warning  Missing JSDoc @returns for function                                                 valid-jsdoc
  27:3  warning  Missing JSDoc for parameter 'metadataTreeService'                                   valid-jsdoc
  54:5  warning  You should not use "this" directly. Instead, assign it to a variable called "ctrl"  angular/controller-as-vm

/home/nduta/horizon/horizon/static/framework/widgets/metadata/display/metadata-display.directive.js
  25:3  warning  Missing JSDoc @returns for function              valid-jsdoc
  25:3  warning  Expected JSDoc for 'path' but found 'available'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/metadata/tree/metadata-tree-item.controller.js
  26:3  warning  Missing JSDoc @returns for function                                                 valid-jsdoc
  38:5  warning  You should not use "this" directly. Instead, assign it to a variable called "ctrl"  angular/controller-as-vm

/home/nduta/horizon/horizon/static/framework/widgets/metadata/tree/metadata-tree-item.directive.js
  25:3  warning  Missing JSDoc @returns for function           valid-jsdoc
  25:3  warning  Expected JSDoc for 'path' but found 'action'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/metadata/tree/metadata-tree.controller.js
  28:3  warning  Missing JSDoc @returns for function                                                 valid-jsdoc
  28:3  warning  Missing JSDoc for parameter 'metadataTreeService'                                   valid-jsdoc
  28:3  warning  Missing JSDoc for parameter 'defaults'                                              valid-jsdoc
  42:5  warning  You should not use "this" directly. Instead, assign it to a variable called "ctrl"  angular/controller-as-vm
  79:5  warning  Missing JSDoc @returns for function                                                 valid-jsdoc
  79:5  warning  Missing JSDoc for parameter 'name'                                                  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/metadata/tree/metadata-tree.directive.js
  25:3  warning  Missing JSDoc @returns for function          valid-jsdoc
  25:3  warning  Expected JSDoc for 'path' but found 'model'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/metadata/tree/tree.service.js
   23:3  warning  Missing JSDoc @returns for function  valid-jsdoc
   66:5  warning  Missing JSDoc @returns for function  valid-jsdoc
  106:5  warning  Missing JSDoc return description     valid-jsdoc
  149:5  warning  Missing JSDoc return description     valid-jsdoc
  176:5  warning  Missing JSDoc return description     valid-jsdoc
  197:5  warning  Missing JSDoc return description     valid-jsdoc
  212:5  warning  Missing JSDoc return description     valid-jsdoc
  226:5  warning  Missing JSDoc @returns for function  valid-jsdoc
  241:5  warning  Missing JSDoc @returns for function  valid-jsdoc
  252:5  warning  Missing JSDoc @returns for function  valid-jsdoc
  261:5  warning  JSDoc syntax error                   valid-jsdoc
  281:5  warning  JSDoc syntax error                   valid-jsdoc
  305:5  warning  Missing JSDoc return description     valid-jsdoc
  320:5  warning  Missing JSDoc return description     valid-jsdoc
  331:5  warning  Missing JSDoc @returns for function  valid-jsdoc
  342:5  warning  Missing JSDoc return description     valid-jsdoc
  372:5  warning  Missing JSDoc return description     valid-jsdoc
  392:5  warning  Missing JSDoc return description     valid-jsdoc
  410:5  warning  Missing JSDoc @returns for function  valid-jsdoc
  442:5  warning  Missing JSDoc return description     valid-jsdoc
  461:5  warning  Missing JSDoc @returns for function  valid-jsdoc
  475:5  warning  Missing JSDoc @returns for function  valid-jsdoc
  485:5  warning  Missing JSDoc @returns for function  valid-jsdoc
  503:5  warning  Missing JSDoc @returns for function  valid-jsdoc
  515:5  warning  Missing JSDoc return description     valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/modal/delete-modal.service.js
   29:3  warning  Missing JSDoc @returns for function               valid-jsdoc
   29:3  warning  Missing JSDoc for parameter '$q'                  valid-jsdoc
   29:3  warning  Missing JSDoc for parameter 'simpleModalService'  valid-jsdoc
   29:3  warning  Missing JSDoc for parameter 'toast'               valid-jsdoc
   29:3  warning  Missing JSDoc for parameter '$qExtensions'        valid-jsdoc
   56:5  warning  Expected JSDoc for 'scope' but found 'entities'   valid-jsdoc
   56:5  warning  Missing JSDoc for parameter 'context'             valid-jsdoc
  128:5  warning  Missing JSDoc @returns for function               valid-jsdoc
  128:5  warning  Missing JSDoc for parameter 'message'             valid-jsdoc
  128:5  warning  Missing JSDoc for parameter 'entities'            valid-jsdoc
  135:5  warning  Missing JSDoc @returns for function               valid-jsdoc
  135:5  warning  Missing JSDoc for parameter 'entity'              valid-jsdoc
  142:5  warning  Missing JSDoc @returns for function               valid-jsdoc
  142:5  warning  Missing JSDoc for parameter 'entity'              valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/modal/delete-modal.service.spec.js
  29:24  warning  '$q' was used before it was defined  no-use-before-define

/home/nduta/horizon/horizon/static/framework/widgets/modal/wizard.controller.js
  32:3  warning  Missing JSDoc @returns for function              valid-jsdoc
  32:3  warning  Missing JSDoc for parameter '$uibModalInstance'  valid-jsdoc
  32:3  warning  Missing JSDoc for parameter '$scope'             valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'workflow'           valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'submit'             valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'data'               valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/panel/hz-resource-panel.controller.js
  30:5  warning  You should not use "this" directly. Instead, assign it to a variable called "ctrl"  angular/controller-as-vm

/home/nduta/horizon/horizon/static/framework/widgets/panel/hz-resource-panel.directive.js
  25:3  warning  Missing JSDoc @returns for function     valid-jsdoc
  25:3  warning  Missing JSDoc for parameter 'basePath'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/property/hz-field.directive.js
  27:3  warning  Missing JSDoc parameter type for 'config'        valid-jsdoc
  27:3  warning  Missing JSDoc parameter type for 'item'          valid-jsdoc
  27:3  warning  Missing JSDoc @returns for function              valid-jsdoc
  27:3  warning  Expected JSDoc for '$filter' but found 'config'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/property/hz-resource-property-list.directive.js
  27:3  warning  Missing JSDoc @returns for function     valid-jsdoc
  27:3  warning  Missing JSDoc for parameter 'basePath'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/property/hz-resource-property.controller.js
  34:5  warning  You should not use "this" directly. Instead, assign it to a variable called "ctrl"  angular/controller-as-vm

/home/nduta/horizon/horizon/static/framework/widgets/property/hz-resource-property.directive.js
  28:3  warning  Missing JSDoc @returns for function     valid-jsdoc
  28:3  warning  Missing JSDoc for parameter '$log'      valid-jsdoc
  28:3  warning  Missing JSDoc for parameter 'basePath'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/table/hz-cell.directive.js
  25:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/table/hz-detail-row.directive.js
  28:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/table/hz-dynamic-table.controller.js
  44:5  warning  Missing JSDoc parameter type for 'newValue'          valid-jsdoc
  44:5  warning  Missing JSDoc @returns for function                  valid-jsdoc
  44:5  warning  Expected JSDoc for 'newConfig' but found 'newValue'  valid-jsdoc
  79:5  warning  Missing JSDoc parameter type for 'column'            valid-jsdoc
  79:5  warning  Missing JSDoc return description                     valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/table/hz-dynamic-table.directive.js
   27:3  warning  JSDoc syntax error         valid-jsdoc
  115:5  warning  Unexpected 'todo' comment  no-warning-comments

/home/nduta/horizon/horizon/static/framework/widgets/table/hz-expand-detail.directive.js
  24:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/table/hz-no-items.directive.js
  25:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/table/hz-resource-table.controller.js
   80:5   warning  Missing JSDoc parameter type for 'newValue'                                   valid-jsdoc
   80:5   warning  Missing JSDoc @returns for function                                           valid-jsdoc
  104:5   warning  Missing JSDoc parameter type for 'newValue'                                   valid-jsdoc
  104:5   warning  Missing JSDoc @returns for function                                           valid-jsdoc
  116:5   warning  Missing JSDoc @returns for function                                           valid-jsdoc
  132:16  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style
  137:14  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style
  153:5   warning  Missing JSDoc @returns for function                                           valid-jsdoc
  221:11  warning  Unexpected 'todo' comment                                                     no-warning-comments

/home/nduta/horizon/horizon/static/framework/widgets/table/hz-resource-table.controller.spec.js
  164:33  warning  Unexpected use of undefined  no-undefined
  180:40  warning  Unexpected use of undefined  no-undefined

/home/nduta/horizon/horizon/static/framework/widgets/table/hz-search-bar.directive.js
  27:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/table/hz-select-all.directive.js
  26:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/table/hz-select.directive.js
  22:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/table/hz-table-footer.directive.js
  26:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/table/hz-table.directive.js
  22:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/table/table.controller.js
  27:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/table/table.module.js
  18:3  warning  Missing JSDoc @returns for function            valid-jsdoc
  18:3  warning  Missing JSDoc for parameter 'stConfig'         valid-jsdoc
  18:3  warning  Missing JSDoc for parameter '$windowProvider'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/toast/toast.service.js
   70:5   warning  Missing JSDoc @returns for function       valid-jsdoc
   70:5   warning  Missing JSDoc for parameter 'type'        valid-jsdoc
   94:5   warning  Missing JSDoc @returns for function       valid-jsdoc
   94:5   warning  Missing JSDoc for parameter 'index'       valid-jsdoc
  101:5   warning  Missing JSDoc @returns for function       valid-jsdoc
  101:5   warning  Missing JSDoc for parameter 'type'        valid-jsdoc
  101:5   warning  Missing JSDoc for parameter 'msg'         valid-jsdoc
  115:5   warning  Missing JSDoc @returns for function       valid-jsdoc
  122:5   warning  Missing JSDoc parameter type for 'type'   valid-jsdoc
  122:5   warning  Missing JSDoc parameter type for 'msg'    valid-jsdoc
  131:25  warning  Gratuitous parentheses around expression  no-extra-parens
  132:16  warning  Gratuitous parentheses around expression  no-extra-parens
  136:5   warning  Missing JSDoc @returns for function       valid-jsdoc
  143:5   warning  Missing JSDoc @returns for function       valid-jsdoc
  150:5   warning  Missing JSDoc @returns for function       valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/transfer-table/filter-available.js
  25:3  warning  Expected JSDoc for '$memoize' but found 'available'  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/transfer-table/filter-available.spec.js
  52:30  warning  Unexpected use of undefined  no-undefined

/home/nduta/horizon/horizon/static/framework/widgets/transfer-table/transfer-table.controller.js
  37:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/transfer-table/transfer-table.module.js
  78:5  warning  Missing JSDoc @returns for function  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/wizard/modal-container.controller.js
  26:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/wizard/wizard.controller.js
  34:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/framework/widgets/wizard/wizard.directive.js
  25:3  warning  JSDoc syntax error  valid-jsdoc

/home/nduta/horizon/horizon/static/horizon/js/horizon.communication.js
  43:9  warning  Unexpected 'todo' comment  no-warning-comments

/home/nduta/horizon/horizon/static/horizon/js/horizon.d3barchart.js
   99:17  warning  Function 'anonymous' has a complexity of 13  complexity
  256:11  warning  Unexpected 'fixme' comment                   no-warning-comments
  384:5   warning  Unexpected 'fixme' comment                   no-warning-comments
  490:5   warning  Unexpected 'fixme' comment                   no-warning-comments
  578:5   warning  Unexpected 'fixme' comment                   no-warning-comments

/home/nduta/horizon/horizon/static/horizon/js/horizon.d3linechart.js
  235:7   warning  Unexpected 'todo' comment                   no-warning-comments
  401:7   warning  Unexpected 'fixme' comment                  no-warning-comments
  487:7   warning  Unexpected 'todo' comment                   no-warning-comments
  510:7   warning  Unexpected 'todo' comment                   no-warning-comments
  631:7   warning  Unexpected 'todo' comment                   no-warning-comments
  677:22  warning  'resizeend' was used before it was defined  no-use-before-define
  704:5   warning  Unexpected 'fixme' comment                  no-warning-comments

/home/nduta/horizon/horizon/static/horizon/js/horizon.d3piechart.js
  137:7  warning  Unexpected 'todo' comment  no-warning-comments

/home/nduta/horizon/horizon/static/horizon/js/horizon.forms.js
  153:37  warning  'endDate' was used before it was defined  no-use-before-define
  156:11  warning  'endDate' was used before it was defined  no-use-before-define
  160:9   warning  'endDate' was used before it was defined  no-use-before-define
  161:9   warning  'endDate' was used before it was defined  no-use-before-define

/home/nduta/horizon/horizon/static/horizon/js/horizon.tables.js
  118:15  warning  Unexpected 'todo' comment                    no-warning-comments
  250:30  warning  Function 'anonymous' has a complexity of 13  complexity
  629:7   warning  Unexpected 'todo' comment                    no-warning-comments

/home/nduta/horizon/openstack_dashboard/dashboards/identity/static/dashboard/identity/groups/actions/create.action.service.js
  35:3  warning  Missing JSDoc @returns for function                valid-jsdoc
  35:3  warning  Missing JSDoc for parameter '$q'                   valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'resourceType'         valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'keystoneAPI'          valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'policy'               valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'modalFormService'     valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'actionResultService'  valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'gettext'              valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'toast'                valid-jsdoc

/home/nduta/horizon/openstack_dashboard/dashboards/identity/static/dashboard/identity/groups/actions/edit.action.service.js
  32:3  warning  Missing JSDoc @returns for function                valid-jsdoc
  32:3  warning  Missing JSDoc for parameter '$q'                   valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'resourceType'         valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'keystoneAPI'          valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'policy'               valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'modalFormService'     valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'actionResultService'  valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'toast'                valid-jsdoc

/home/nduta/horizon/openstack_dashboard/dashboards/identity/static/dashboard/identity/groups/groups.module.js
  89:5  warning  Missing JSDoc @returns for function  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/dashboards/identity/static/dashboard/identity/roles/actions/create.action.service.js
  37:3   warning  Missing JSDoc @returns for function                valid-jsdoc
  37:3   warning  Missing JSDoc for parameter '$q'                   valid-jsdoc
  37:3   warning  Missing JSDoc for parameter 'basePath'             valid-jsdoc
  37:3   warning  Missing JSDoc for parameter 'resourceType'         valid-jsdoc
  37:3   warning  Missing JSDoc for parameter 'schema'               valid-jsdoc
  37:3   warning  Missing JSDoc for parameter 'keystoneAPI'          valid-jsdoc
  37:3   warning  Missing JSDoc for parameter 'policy'               valid-jsdoc
  37:3   warning  Missing JSDoc for parameter 'modalFormService'     valid-jsdoc
  37:3   warning  Missing JSDoc for parameter 'actionResultService'  valid-jsdoc
  37:3   warning  Missing JSDoc for parameter 'gettext'              valid-jsdoc
  37:3   warning  Missing JSDoc for parameter 'toast'                valid-jsdoc
  64:20  warning  Gratuitous parentheses around expression           no-extra-parens

/home/nduta/horizon/openstack_dashboard/dashboards/identity/static/dashboard/identity/roles/actions/edit.action.service.js
  36:3  warning  Missing JSDoc @returns for function                valid-jsdoc
  36:3  warning  Missing JSDoc for parameter '$q'                   valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'basePath'             valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'resourceType'         valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'schema'               valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'keystoneAPI'          valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'policy'               valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'modalFormService'     valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'actionResultService'  valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'toast'                valid-jsdoc

/home/nduta/horizon/openstack_dashboard/dashboards/identity/static/dashboard/identity/users/actions/create.action.service.js
  36:3  warning  Missing JSDoc @returns for function                valid-jsdoc
  36:3  warning  Missing JSDoc for parameter '$q'                   valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'resourceType'         valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'basePath'             valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'workflow'             valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'keystone'             valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'policy'               valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'actionResultService'  valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'modal'                valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'toast'                valid-jsdoc

/home/nduta/horizon/openstack_dashboard/dashboards/identity/static/dashboard/identity/users/actions/disable.action.service.js
  32:3  warning  Missing JSDoc @returns for function                valid-jsdoc
  32:3  warning  Missing JSDoc for parameter '$q'                   valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'resourceType'         valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'keystone'             valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'policy'               valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'actionResultService'  valid-jsdoc
  32:3  warning  Missing JSDoc for parameter '$qExtensions'         valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'toast'                valid-jsdoc

/home/nduta/horizon/openstack_dashboard/dashboards/identity/static/dashboard/identity/users/actions/enable.action.service.js
  32:3  warning  Missing JSDoc @returns for function                valid-jsdoc
  32:3  warning  Missing JSDoc for parameter '$q'                   valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'resourceType'         valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'keystone'             valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'policy'               valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'actionResultService'  valid-jsdoc
  32:3  warning  Missing JSDoc for parameter '$qExtensions'         valid-jsdoc
  32:3  warning  Missing JSDoc for parameter 'toast'                valid-jsdoc

/home/nduta/horizon/openstack_dashboard/dashboards/identity/static/dashboard/identity/users/actions/password.action.service.js
  35:3  warning  Missing JSDoc @returns for function                valid-jsdoc
  35:3  warning  Missing JSDoc for parameter '$q'                   valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'resourceType'         valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'basePath'             valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'workflow'             valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'keystone'             valid-jsdoc
(node:26847) [DEP0044] DeprecationWarning: The `util.isArray` API is deprecated. Please use `Array.isArray()` instead.
(Use `node --trace-deprecation ...` to show where the warning was created)
  35:3  warning  Missing JSDoc for parameter 'policy'               valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'settings'             valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'actionResultService'  valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'modal'                valid-jsdoc
  35:3  warning  Missing JSDoc for parameter 'toast'                valid-jsdoc

/home/nduta/horizon/openstack_dashboard/dashboards/identity/static/dashboard/identity/users/actions/update.action.service.js
  34:3  warning  Missing JSDoc @returns for function                valid-jsdoc
  34:3  warning  Missing JSDoc for parameter '$q'                   valid-jsdoc
  34:3  warning  Missing JSDoc for parameter 'resourceType'         valid-jsdoc
  34:3  warning  Missing JSDoc for parameter 'basePath'             valid-jsdoc
  34:3  warning  Missing JSDoc for parameter 'workflow'             valid-jsdoc
  34:3  warning  Missing JSDoc for parameter 'keystone'             valid-jsdoc
  34:3  warning  Missing JSDoc for parameter 'policy'               valid-jsdoc
  34:3  warning  Missing JSDoc for parameter 'actionResultService'  valid-jsdoc
  34:3  warning  Missing JSDoc for parameter 'modal'                valid-jsdoc
  34:3  warning  Missing JSDoc for parameter 'toast'                valid-jsdoc

/home/nduta/horizon/openstack_dashboard/dashboards/identity/static/dashboard/identity/users/users.module.js
  107:5  warning  Missing JSDoc @returns for function  valid-jsdoc
  126:3  warning  Missing JSDoc @returns for function  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/dashboards/identity/static/dashboard/identity/users/users.service.js
   53:5  warning  Missing JSDoc parameter type for 'params'  valid-jsdoc
   53:5  warning  Missing JSDoc @returns for function        valid-jsdoc
  128:5  warning  Missing JSDoc @returns for function        valid-jsdoc

/home/nduta/horizon/openstack_dashboard/dashboards/project/static/dashboard/project/containers/check-copy-destination.directive.js
  42:5   warning  Missing JSDoc @returns for function       valid-jsdoc
  42:5   warning  Missing JSDoc for parameter 'container'   valid-jsdoc
  77:31  warning  Gratuitous parentheses around expression  no-extra-parens
  77:62  warning  Unexpected use of undefined               no-undefined
  79:26  warning  Gratuitous parentheses around expression  no-extra-parens
  79:52  warning  Unexpected use of undefined               no-undefined

/home/nduta/horizon/openstack_dashboard/dashboards/project/static/dashboard/project/containers/containers-model.service.js
   39:3   warning  Missing JSDoc @returns for function       valid-jsdoc
   39:3   warning  Missing JSDoc for parameter 'swiftAPI'    valid-jsdoc
   39:3   warning  Missing JSDoc for parameter 'apiService'  valid-jsdoc
   39:3   warning  Missing JSDoc for parameter '$q'          valid-jsdoc
   56:26  warning  Unexpected 'todo' comment                 no-warning-comments
   80:5   warning  Missing JSDoc return description          valid-jsdoc
  102:5   warning  Missing JSDoc return description          valid-jsdoc
  102:5   warning  Missing JSDoc for parameter 'name'        valid-jsdoc
  102:5   warning  Missing JSDoc for parameter 'folder'      valid-jsdoc
  142:5   warning  Missing JSDoc return type                 valid-jsdoc
  142:5   warning  Missing JSDoc for parameter 'name'        valid-jsdoc
  158:5   warning  Missing JSDoc return description          valid-jsdoc
  171:5   warning  Missing JSDoc return description          valid-jsdoc
  171:5   warning  Missing JSDoc for parameter 'container'   valid-jsdoc
  171:5   warning  Missing JSDoc for parameter 'force'       valid-jsdoc
  209:5   warning  Missing JSDoc return description          valid-jsdoc
  209:5   warning  Missing JSDoc for parameter 'object'      valid-jsdoc
  232:5   warning  Missing JSDoc return description          valid-jsdoc
  232:5   warning  Missing JSDoc for parameter 'state'       valid-jsdoc
  232:5   warning  Missing JSDoc for parameter 'items'       valid-jsdoc
  232:5   warning  Missing JSDoc for parameter 'result'      valid-jsdoc
  295:5   warning  Missing JSDoc return description          valid-jsdoc
  295:5   warning  Missing JSDoc for parameter 'state'       valid-jsdoc
  295:5   warning  Missing JSDoc for parameter 'node'        valid-jsdoc
  377:5   warning  Missing JSDoc @returns for function       valid-jsdoc

/home/nduta/horizon/openstack_dashboard/dashboards/project/static/dashboard/project/containers/containers.controller.js
   77:5   warning  Unexpected 'todo' comment                                                     no-warning-comments
  300:12  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style

/home/nduta/horizon/openstack_dashboard/dashboards/project/static/dashboard/project/containers/containers.module.js
  46:3  warning  Missing JSDoc @returns for function            valid-jsdoc
  46:3  warning  Missing JSDoc for parameter '$provide'         valid-jsdoc
  46:3  warning  Missing JSDoc for parameter '$routeProvider'   valid-jsdoc
  46:3  warning  Missing JSDoc for parameter '$windowProvider'  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/dashboards/project/static/dashboard/project/containers/objects-batch-actions.service.js
  36:3  warning  Missing JSDoc @returns for function                valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'registryService'      valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'objectResCode'        valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'createFolderService'  valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'deleteService'        valid-jsdoc
  36:3  warning  Missing JSDoc for parameter 'uploadService'        valid-jsdoc

/home/nduta/horizon/openstack_dashboard/dashboards/project/static/dashboard/project/containers/objects-row-actions.service.js
   39:3   warning  Missing JSDoc @returns for function            valid-jsdoc
   39:3   warning  Missing JSDoc for parameter 'registryService'  valid-jsdoc
   39:3   warning  Missing JSDoc for parameter 'objectResCode'    valid-jsdoc
   39:3   warning  Missing JSDoc for parameter 'deleteService'    valid-jsdoc
   39:3   warning  Missing JSDoc for parameter 'downloadService'  valid-jsdoc
   39:3   warning  Missing JSDoc for parameter 'editService'      valid-jsdoc
   39:3   warning  Missing JSDoc for parameter 'viewService'      valid-jsdoc
   39:3   warning  Missing JSDoc for parameter 'copyService'      valid-jsdoc
   39:3   warning  Missing JSDoc for parameter 'gettext'          valid-jsdoc
  268:27  warning  Gratuitous parentheses around expression       no-extra-parens
  269:20  warning  Gratuitous parentheses around expression       no-extra-parens

/home/nduta/horizon/openstack_dashboard/dashboards/project/static/dashboard/project/containers/objects.controller.spec.js
   25:7   warning  '$routeParams' was used before it was defined  no-use-before-define
   26:38  warning  '$routeParams' was used before it was defined  no-use-before-define
   66:66  warning  Unexpected use of undefined                    no-undefined
  131:66  warning  Unexpected use of undefined                    no-undefined

/home/nduta/horizon/openstack_dashboard/dashboards/project/static/dashboard/project/workflow/launch-instance/flavor/flavor.controller.js
  346:28  warning  Gratuitous parentheses around expression  no-extra-parens

/home/nduta/horizon/openstack_dashboard/dashboards/project/static/dashboard/project/workflow/launch-instance/keypair/create-keypair.controller.spec.js
  33:16  warning  'createKeypairPromise' was used before it was defined  no-use-before-define

/home/nduta/horizon/openstack_dashboard/dashboards/project/static/dashboard/project/workflow/launch-instance/keypair/keypair.controller.js
  198:5  warning  Missing JSDoc @returns for function  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/dashboards/project/static/dashboard/project/workflow/launch-instance/launch-instance-model.service.js
  885:5  warning  Missing JSDoc @returns for function  valid-jsdoc

/home/nduta/horizon/openstack_dashboard/dashboards/project/static/dashboard/project/workflow/launch-instance/launch-instance.module.js
  48:7  warning  Unexpected 'todo' comment  no-warning-comments

/home/nduta/horizon/openstack_dashboard/dashboards/project/static/dashboard/project/workflow/launch-instance/networkports/ports.controller.js
   97:7   warning  The body of a for-in should be wrapped in an if statement to filter unwanted properties from the prototype  guard-for-in
  166:12  warning  Closing curly brace does not appear on the same line as the subsequent block                                brace-style

/home/nduta/horizon/openstack_dashboard/dashboards/project/static/dashboard/project/workflow/launch-instance/source/source.controller.js
  422:62  warning  There should be no spaces inside this paren                                   space-in-parens
  442:21  warning  Gratuitous parentheses around expression                                      no-extra-parens
  494:16  warning  Closing curly brace does not appear on the same line as the subsequent block  brace-style
  541:82  warning  There should be no spaces inside this paren                                   space-in-parens

✖ 755 problems (19 errors, 736 warnings)

npm: exit 1 (3.95 seconds) /home/nduta/horizon> npm run lint pid=26830
  npm: FAIL code 1 (58.71=setup[9.89]+cmd[38.23,6.64,3.95] seconds)
  evaluation failed :( (58.88 seconds)
