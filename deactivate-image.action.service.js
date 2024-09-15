/**
 * (c) Copyright 2016 Hewlett-Packard Development Company, L.P.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may
 * not use this file except in compliance with the License. You may obtain
 * a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 */
(function () {
    'use strict';

    angular
        .module('horizon.app.core.images')
        .factory('horizon.app.core.images.actions.deactivate-image.service', deactivateImageService);

    deactivateImageService.$inject = [
        '$q',        
        'horizon.app.core.openstack-service-api.glance',
        'horizon.app.core.openstack-service-api.policy',
        'horizon.framework.util.q.extensions',
        'horizon.framework.widgets.modal.simple-modal.service',
    ];

    /**
     * @ngDoc factory
     * @name horizon.app.core.images.actions.deactivateImageService
     * @Description A service to open the user wizard.
     */
    function deactivateImageService(
        $q,        
        glance,
        policy,
        $qExtensions,
        simpleModalService,
    ) {

        var service = {
            allowed: allowed,
            perform: perform
        };

        return service;

        //////////////
        
        function allowed(image) {
            return $q.all([
                policy.ifAllowed({ rules: [['image', 'deactivate']] }),
                isActive(image)
            ]);
        }

        function perform(image) {
            var deferred = glance.getImage(image.id);
            deferred.then(onLoad);

            var data = {};
            data.imagePromise = deferred;
            function onLoad(response) {
                var localImage = response.data;
                data.image = localImage;
            }
            return simpleModalService.modal({
                data: data,                
            }).result;
        }
        
        function isActive(image) {
            return $qExtensions.booleanAsPromise(image.status === 'active');
        }
    } // end of deactivateService
})(); // end of IIFE
