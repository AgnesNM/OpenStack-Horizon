            <div class="form-field">
              <div class="btn-group" name="status">
                <label class="btn btn-default"
                       ng-repeat="option in ctrl.imageStatusOptions"
                       ng-model="ctrl.image.status"
                       uib-btn-radio="option.value">{$ ::option.label $}</label>
              </div>
            </div>
