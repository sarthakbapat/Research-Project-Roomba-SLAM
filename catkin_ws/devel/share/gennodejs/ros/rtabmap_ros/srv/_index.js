
"use strict";

let SetGoal = require('./SetGoal.js')
let ResetPose = require('./ResetPose.js')
let GetPlan = require('./GetPlan.js')
let PublishMap = require('./PublishMap.js')
let SetLabel = require('./SetLabel.js')
let GetMap = require('./GetMap.js')
let ListLabels = require('./ListLabels.js')

module.exports = {
  SetGoal: SetGoal,
  ResetPose: ResetPose,
  GetPlan: GetPlan,
  PublishMap: PublishMap,
  SetLabel: SetLabel,
  GetMap: GetMap,
  ListLabels: ListLabels,
};
