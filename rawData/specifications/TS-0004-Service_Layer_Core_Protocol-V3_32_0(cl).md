Source Document: TS-0004-Service_Layer_Core_Protocol-V3_32_0(cl).docx

The present document is provided for future development work within oneM2M only. The Partners accept no liability for any use of this specification.

The present document has not been subject to any approval process by the oneM2M Partners Type 1.  Published oneM2M specifications and reports for implementation should be obtained via the oneM2M Partners' Publications Offices.

About oneM2M

The purpose and goal of oneM2M is to develop technical specifications which address the need for a common M2M Service Layer that can be readily embedded within various hardware and software, and relied upon to connect the myriad of devices in the field with M2M application servers worldwide.

More information about oneM2M may be found at:  http//www.oneM2M.org

Copyright Notification

No part of this document may be reproduced, in an electronic retrieval system or otherwise, except as authorized by written permission.

The copyright and the foregoing restriction extend to reproduction in all media.

© 2024, oneM2M Partners Type 1 (ARIB, ATIS, CCSA, ETSI, TIA, TSDSI, TTA, TTC).

All rights reserved.

Notice of Disclaimer & Limitation of Liability

The information provided in this document is directed solely to professionals who have the appropriate degree of experience to understand and interpret its contents in accordance with generally accepted engineering or other professional standards and applicable regulations. No recommendation as to products or vendors is made or should be implied.

NO REPRESENTATION OR WARRANTY IS MADE THAT THE INFORMATION IS TECHNICALLY ACCURATE OR SUFFICIENT OR CONFORMS TO ANY STATUTE, GOVERNMENTAL RULE OR REGULATION, AND FURTHER, NO REPRESENTATION OR WARRANTY IS MADE OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR AGAINST INFRINGEMENT OF INTELLECTUAL PROPERTY RIGHTS. NO oneM2M PARTNER TYPE 1 SHALL BE LIABLE, BEYOND THE AMOUNT OF ANY SUM RECEIVED IN PAYMENT BY THAT PARTNER FOR THIS DOCUMENT, WITH RESPECT TO ANY CLAIM, AND IN NO EVENT SHALL oneM2M BE LIABLE FOR LOST PROFITS OR OTHER INCIDENTAL OR CONSEQUENTIAL DAMAGES. oneM2M EXPRESSLY ADVISES ANY AND ALL USE OF OR RELIANCE UPON THIS INFORMATION PROVIDED IN THIS DOCUMENT IS AT THE RISK OF THE USER.

Contents

1	Scope	35

2	References	35

2.1	Normative references	35

2.2	Informative references	37

3	Definitions and abbreviations	38

3.1	Definitions	38

3.2	Abbreviations	38

4	Conventions	40

5	Protocol design principles and requirements	40

5.1	General introduction	40

5.2	Introduction	40

5.2.0	Overview	40

5.2.1	Interfaces to the underlying networks	41

5.3	API design guidelines	41

5.4	Primitives	41

5.4.1	Introduction	41

5.4.2	Primitives modelling	42

5.4.3	Primitive principles	43

5.4.4	Serialization of primitives	43

5.5	Design principles	43

5.5.1	Introduction	43

5.5.2	Extensibility	43

5.5.3	Scalability	44

5.5.4	Fault tolerance and robustness	44

5.5.5	Efficiency	44

5.5.6	Inter-operability	44

5.5.7	Self-operation and self-management	44

6	oneM2M protocols/API overview	44

6.1	Introduction	44

6.2	Addressing	46

6.2.1	Introduction	46

6.2.2	Summary of oneM2M Identifiers	46

6.2.3	oneM2M Entity Addressing	46

6.2.4	oneM2M Resource Addressing	47

6.3	Common data types	48

6.3.1	Introduction	48

6.3.2	Simple data types incorporated from XML schema	48

6.3.3	oneM2M simple data types	50

6.3.4	oneM2M enumerated data types	57

6.3.4.1	Introduction	57

6.3.4.2	Enumeration type definitions	57

6.3.4.2.1	m2m:resourceType	57

6.3.4.2.2	m2m:cseTypeID	59

6.3.4.2.3	m2m:locationSource	59

6.3.4.2.4	m2m:stdEventCats	59

6.3.4.2.5	m2m:operation	59

6.3.4.2.6	m2m:responseType	60

6.3.4.2.7	m2m:resultContent	60

6.3.4.2.8	m2m:desIdResType	60

6.3.4.2.9	m2m:responseStatusCode	60

6.3.4.2.10	m2m:requestStatus	61

6.3.4.2.11	m2m:memberType	61

6.3.4.2.12	m2m:consistencyStrategy	62

6.3.4.2.13	m2m:cmdType	63

6.3.4.2.14	m2m:execModeType	63

6.3.4.2.15	m2m:execStatusType	63

6.3.4.2.16	m2m:execResultType	64

6.3.4.2.17	m2m:pendingNotification	64

6.3.4.2.18	m2m:notificationContentType	64

6.3.4.2.19	m2m:notificationEventType	65

6.3.4.2.20	m2m:status	65

6.3.4.2.21	m2m:batteryStatus	65

6.3.4.2.22	m2m:mgmtDefinition	66

6.3.4.2.23	m2m:logTypeId	66

6.3.4.2.24	m2m:logStatus	66

6.3.4.2.25	m2m:eventType	67

6.3.4.2.26	m2m:statsRuleStatusType	67

6.3.4.2.27	m2m:statModelType	67

6.3.4.2.28	m2m:encodingType	67

6.3.4.2.29	m2m:accessControlOperations	68

6.3.4.2.30	Void	68

6.3.4.2.31	m2m:filterUsage	68

6.3.4.2.32	m2m:notificationTargetPolicyAction	68

6.3.4.2.33	m2m:logicalOperator	68

6.3.4.2.34	m2m:filterOperation	69

6.3.4.2.35	m2m:securityInfoType	69

6.3.4.2.36	m2m:allJoynDirection	69

6.3.4.2.37	m2m:contentFilterSyntax	69

6.3.4.2.38	m2m:contentSecurity	70

6.3.4.2.39	m2m:suid	70

6.3.4.2.40	m2m:esprimKeyGenAlgID	71

6.3.4.2.41	m2m:esprimProtocolAndAlgID	71

6.3.4.2.42	Void	72

6.3.4.2.43	m2m:stationaryIndication	72

6.3.4.2.44	m2m:contentStatus	72

6.3.4.2.45	m2m:networkAction	72

6.3.4.2.46	m2m:locationInformationType	72

6.3.4.2.47	m2m:geofenceEventCriteria	73

6.3.4.2.48	m2m:semanticFormat	73

6.3.4.2.49	m2m:triggerPurpose	73

6.3.4.2.50	Void	73

6.3.4.2.51	m2m:authorizationDecision	73

6.3.4.2.52	m2m:authorizationStatus	74

6.3.4.2.53	m2m:acpCombiningAlgorithm	74

6.3.4.2.54	m2m:mashupMemberStoreType	74

6.3.4.2.55	m2m:mashupResultGenType	74

6.3.4.2.56	m2m:locationUpdateEventCriteria	75

6.3.4.2.57	m2m:AERegistrationStatus	75

6.3.4.2.58	m2m:multicastCapability	75

6.3.4.2.59	m2m:sessionState	75

6.3.4.2.60	m2m:triggerStatus	75

6.3.4.2.61	m2m:timeWindowType	76

6.3.4.2.62	m2m:transferSelectionGuidance	76

6.3.4.2.63	m2m:transactionMode	76

6.3.4.2.64	m2m:transactionControl	76

6.3.4.2.65	m2m:transactionState	77

6.3.4.2.66	m2m:transactionLockType	77

6.3.4.2.67	m2m:transactionMgmtHandling	77

6.3.5	Complex data types	77

6.3.5.1	Introduction	77

6.3.5.2	m2m:deliveryMetaData	78

6.3.5.3	m2m:aggregatedRequest	78

6.3.5.4	m2m:metaInformation	78

6.3.5.5	m2m:primitiveContent	79

6.3.5.6	m2m:batchNotify	79

6.3.5.7	m2m:eventNotificationCriteria	79

6.3.5.8	m2m:filterCriteria	79

6.3.5.9	m2m:attribute	80

6.3.5.10	Void	80

6.3.5.11	m2m:scheduleEntries	80

6.3.5.12	m2m:aggregatedNotification	80

6.3.5.13	m2m:notification	81

6.3.5.14	m2m:actionStatus	82

6.3.5.15	m2m:anyArgType	82

6.3.5.16	m2m:resetArgsType	82

6.3.5.17	m2m:rebootArgsType	82

6.3.5.18	m2m:uploadArgsType	82

6.3.5.19	m2m:downloadArgsType	83

6.3.5.20	m2m:softwareInstallArgsType	83

6.3.5.21	m2m:softwareUpdateArgsType	83

6.3.5.22	m2m:softwareUninstallArgsType	83

6.3.5.23	m2m:execReqArgsListType	84

6.3.5.24	m2m:mgmtLinkRef	84

6.3.5.25	m2m:resourceWrapper	84

6.3.5.26	m2m:setOfAcrs	84

6.3.5.27	m2m:accessControlRule	85

6.3.5.28	m2m:locationRegion	85

6.3.5.29	m2m:childResourceRef	86

6.3.5.30	m2m:responseTypeInfo	86

6.3.5.31	m2m:rateLimit	86

6.3.5.32	m2m:operationResult	86

6.3.5.33	m2m:aggregatedResponse	87

6.3.5.34	m2m:mgmtResource	87

6.3.5.35	m2m:announcedMgmtResource	88

6.3.5.36	m2m:contentRef	88

6.3.5.37	m2m:deletionContexts	88

6.3.5.38	m2m:flexContainerResource	89

6.3.5.39	m2m:announcedFlexContainerResource	89

6.3.5.40	m2m:missingData	90

6.3.5.41	m2m:tokenPermission	90

6.3.5.42	m2m:tokenClaimSet	90

6.3.5.43	m2m:dynAuthLocalTokenIdAssignments	90

6.3.5.44	m2m:dynAuthTokenSummary	91

6.3.5.45	m2m:dynAuthTokenReqInfo	91

6.3.5.46	m2m:dynAuthDasRequest	91

6.3.5.47	m2m:dynAuthDasResponse	92

6.3.5.48	m2m:securityInfo	92

6.3.5.49	m2m:listOfChildResourceRef	92

6.3.5.50	m2m:originatorESPrimRandObject	93

6.3.5.51	m2m:receiverESPrimRandObject	93

6.3.5.52	m2m:e2eSecInfo	93

6.3.5.53	m2m:tokenPermissions	93

6.3.5.54	m2m:backOffParameters	93

6.3.5.55	m2m:listOfDataLinks	94

6.3.5.56	m2m:dataLink	94

6.3.5.57	m2m:operationMonitor	94

6.3.5.58	m2m:dynAuthRelMapRequest	95

6.3.5.59	m2m:dynAuthRelMapResponse	95

6.3.5.60	m2m:ipAddress	95

6.3.5.61	m2m:setOfPermissions	95

6.3.5.62	m2m:representation	95

6.3.5.63	m2m:sessionDescriptions	96

6.3.5.64	m2m:activityPatternElements	96

6.3.5.65	m2m:activityPattern	96

6.3.5.66	m2m:eventNotificationCriteriaSet	96

6.3.5.67	m2m:specializationType	97

6.3.5.68	m2m:mashupMembers	97

6.3.6	Universal and Common attributes	98

6.4	Message parameter data types	100

6.4.1	Request primitive parameter data types	100

6.4.2	Response primitive parameter data types	101

6.5	Resource data types	102

6.5.1	Description	102

6.5.2	resource	103

6.5.2.1	Description	103

6.5.2.2	Reference	103

6.5.2.3	Usage	103

6.5.3	regularResource	103

6.5.3.1	Description	103

6.5.3.2	Reference	103

6.5.3.3	Usage	104

6.5.4	announceableResource	104

6.5.4.1	Description	104

6.5.4.2	Reference	104

6.5.4.3	Usage	104

6.5.5	announcedResource	104

6.5.5.1	Description	104

6.5.5.2	Reference	104

6.5.5.3	Usage	104

6.5.6	announceableSubordinateResource	105

6.5.6.1	Description	105

6.5.6.2	Reference	105

6.5.6.3	Usage	105

6.5.7	announcedSubordinateResource	105

6.5.7.1	Description	105

6.5.7.2	Reference	105

6.5.7.3	Usage	105

6.5.8	subordinateResource	105

6.5.8.1	Description	105

6.5.8.2	Reference	105

6.5.8.3	Usage	105

6.6	Response status codes	106

6.6.1	Introduction	106

6.6.2	RSC framework overview	106

6.6.3	Definition of Response Status Codes	106

6.6.3.1	Overview	106

6.6.3.2	Informational response class	106

6.6.3.3	Successful response class	106

6.6.3.4	Redirection response class	107

6.6.3.5	Originator error response class	107

6.6.3.6	Receiver error response class	107

6.6.3.7	Network system error response class	108

6.7	oneM2M specific MIME media types	108

6.8	Virtual Resources	109

7	oneM2M procedures	110

7.1	Introduction	110

7.2	Primitive format and generic procedure	110

7.2.1	Primitive format	110

7.2.1.1	Request primitive format	110

7.2.1.2	Response primitive format	112

7.2.2	Description of generic procedures	113

7.2.2.1	Generic resource request procedure for originator	113

7.2.2.2	Generic procedure for handling a Request at a receiver	114

7.3	Common operations	117

7.3.1	Originator actions	117

7.3.1.1	Compose request primitive	117

7.3.1.2	Send a request to the receiver CSE	118

7.3.1.3	Wait for response primitive	118

7.3.1.4	Retrieve the <request> resource	118

7.3.2	Receiver CSE actions	119

7.3.2.1	Check the validity of received request primitive	119

7.3.2.2	Create <request> resource locally	120

7.3.2.3	Create a success response (acknowledgement)	121

7.3.2.4	Send response primitive (acknowledgement)	122

7.3.2.5	Update <request> resource	122

7.3.2.6	Forwarding	122

7.3.2.7	Check Service Subscription Profile	123

7.3.2.8	Check Hosting CSE of the targeted resource	123

7.3.2.9	Blocking Subscription Notification Failure Handling	124

7.3.3	Hosting CSE actions	124

7.3.3.1	Check existence of the addressed resource	124

7.3.3.2	Check for duplicate group requests	125

7.3.3.3	Check validity of resource representation for CREATE	125

7.3.3.4	Check validity of resource representation for UPDATE	126

7.3.3.5	Create the resource	127

7.3.3.6	Retrieve the resource	128

7.3.3.7	Update the resource	128

7.3.3.8	Delete the resource	129

7.3.3.9	Notify processing	129

7.3.3.9.1	Notify processing when To parameter is an <AE> resource	129

7.3.3.9.2	Notify processing when To parameter is the <CSEBase> resource	129

7.3.3.10	Announce the resource or attribute	130

7.3.3.11	De-announce the resource or attribute	131

7.3.3.12	Create a success response	132

7.3.3.13	Create an error response	133

7.3.3.14	Resource discovery procedure	133

7.3.3.15	Check authorization of the originator	134

7.3.3.16	Send response primitive	135

7.3.3.17	Using Filter Criteria for identification of target resources	135

7.3.3.17.0	Introduction	135

7.3.3.17.1	Conditions on the creationTime attribute	136

7.3.3.17.2	Conditions on the lastModifiedTime attribute	137

7.3.3.17.3	Conditions on stateTag attribute	137

7.3.3.17.4	Conditions on expirationTime attribute	137

7.3.3.17.5	Conditions on labels attribute	137

7.3.3.17.6	Conditions on resourceType attribute	138

7.3.3.17.7	Conditions on contentSize attribute	138

7.3.3.17.8	Conditions on typeOfContent of contentInfo attribute	138

7.3.3.17.9	Conditions on attribute name and value pairs	138

7.3.3.17.10	Constraint on number of retrieved resources by limit element	139

7.3.3.17.11	Filter Usage request parameter	139

7.3.3.17.12	Filter Operation request attribute	139

7.3.3.17.13	Conditions on content-based discovery	139

7.3.3.17.14	Constraint on number of applicable levels in resource tree	139

7.3.3.17.15	Constraint on number of resources to skip over in retrieve response	140

7.3.3.17.16	Conditions on labelsQuery attribute	140

7.3.3.17.17	Applying a relative path	140

7.3.3.18	Semantic resource discovery	141

7.3.3.18.0	Introduction	141

7.3.3.18.1	Annotation-based method	141

7.3.3.18.2	Resource link-based method	142

7.3.3.19	Semantic query	142

7.3.3.19.0	Introduction	142

7.3.3.19.1	Approach-1: Semantic query with implicit scope	142

7.3.3.19.2	Approach-2: Semantic query with explicit scope	143

7.3.4	Management common operations	143

7.3.4.1	Identify the managed entity and the technology specific protocol	143

7.3.4.2	Locate the technology specific data model objects to be managed on the managed entity	143

7.3.4.3	Establish a management session with the managed entity or management server	144

7.3.4.4	Send the management request(s) to the managed entity corresponding to the received Request primitive	144

7.4	Resource type-specific procedures and definitions	144

7.4.0	Introduction	144

7.4.1	Resource type specification conventions	145

7.4.1.1	Resource type definition conventions	145

7.4.1.2	Resource type-specific procedure conventions	146

7.4.2	Resource type <accessControlPolicy>	146

7.4.2.1	Introduction	146

7.4.2.2	accessControlPolicy resource specific procedures for CRUD operations	147

7.4.2.2.0	Introduction	147

7.4.2.2.1	Create	147

7.4.2.2.2	Retrieve	147

7.4.2.2.3	Update	147

7.4.2.2.4	Delete	147

7.4.3	Resource Type <CSEBase>	148

7.4.3.1	Introduction	148

7.4.3.2	<CSEBase> resource specific procedures for CRUD+N operations	149

7.4.3.2.1	Create	149

7.4.3.2.2	Retrieve	149

7.4.3.2.3	Update	150

7.4.3.2.4	Delete	150

7.4.3.2.5	Notify	150

7.4.4	Resource Type <remoteCSE>	150

7.4.4.1	Introduction	150

7.4.4.2	<remoteCSE> resource specific procedures for CRUD operations	152

7.4.4.2.0	Introduction	152

7.4.4.2.1	Create	152

7.4.4.2.2	Retrieve	153

7.4.4.2.3	Update	153

7.4.4.2.4	Delete	153

7.4.5	Resource Type <AE>	154

7.4.5.1	Introduction	154

7.4.5.2	<AE> resource specific procedures for CRUD+N operations	155

7.4.5.2.0	Introduction	155

7.4.5.2.1	Create	155

7.4.5.2.2	Retrieve	157

7.4.5.2.3	Update	157

7.4.5.2.4	Delete	157

7.4.5.2.5	Notify	158

7.4.6	Resource Type <container>	158

7.4.6.1	Introduction	158

7.4.6.2	<container> resource specific procedures for CRUD operations	159

7.4.6.2.0	Introduction	159

7.4.6.2.1	Create	159

7.4.6.2.2	Retrieve	160

7.4.6.2.3	Update	160

7.4.6.2.4	Delete	160

7.4.7	Resource Type <contentInstance>	160

7.4.7.1	Introduction	160

7.4.7.2	<contentInstance> resource specific procedures for CRUD operations	161

7.4.7.2.1	Create	161

7.4.7.2.2	Retrieve	162

7.4.7.2.3	Update	162

7.4.7.2.4	Delete	163

7.4.8	Resource Type <subscription>	163

7.4.8.1	Introduction	163

7.4.8.2	<subscription> resource specific procedures for CRUD operations	164

7.4.8.2.1	Create	164

7.4.8.2.2	Retrieve	166

7.4.8.2.3	Update	166

7.4.8.2.4	Delete	167

7.4.9	Resource Type <schedule>	167

7.4.9.1	Introduction	167

7.4.9.2	<schedule> resource specific procedures for CRUD operations	169

7.4.9.2.0	Introduction	169

7.4.9.2.1	Create	169

7.4.9.2.2	Retrieve	170

7.4.9.2.3	Update	170

7.4.9.2.4	Delete	170

7.4.10	Resource Type <locationPolicy>	170

7.4.10.1	Introduction	170

7.4.10.2	<locationPolicy> resource specific procedures for CRUD Operations	171

7.4.10.2.0	Introduction	171

7.4.10.2.1	Create	171

7.4.10.2.2	Retrieve	173

7.4.10.2.3	Update	173

7.4.10.2.4	Delete	173

7.4.11	Resource Type <delivery>	174

7.4.11.1	Introduction	174

7.4.11.2	<delivery> resource specific procedures for CRUD operations	174

7.4.11.2.0	Introduction	174

7.4.11.2.1	Create	175

7.4.11.2.2	Retrieve	175

7.4.11.2.3	Update	175

7.4.11.2.4	Delete	176

7.4.12	Resource Type <request>	176

7.4.12.1	Introduction	176

7.4.12.2	<request> resource specific procedures for CRUD operations	177

7.4.12.2.0	Introduction	177

7.4.12.2.1	Create	177

7.4.12.2.2	Retrieve	177

7.4.12.2.3	Update	178

7.4.12.2.4	Delete	178

7.4.13	Resource Type <group>	179

7.4.13.1	Introduction	179

7.4.13.2	<group> resource specific procedures for CRUD operations	180

7.4.13.2.0	Introduction	180

7.4.13.2.1	Create	180

7.4.13.2.2	Retrieve	181

7.4.13.2.3	Update	181

7.4.13.2.4	Delete	182

7.4.14	Resource Type <fanOutPoint>	182

7.4.14.1	Introduction	182

7.4.14.2	<fanOutPoint> operations	183

7.4.14.2.1	Validate the type of resource to be created	183

7.4.14.2.2	Sub-group creation for members residing on the same CSE	183

7.4.14.2.3	Assign URI for aggregation of notification	183

7.4.14.2.4	Fan out Request to each member	183

7.4.14.2.5	Aggregation of member responses	184

7.4.14.2.6	Multicast fan out procedure	185

7.4.14.2.7	3GPPTM MBMS fan out procedure	188

7.4.14.3	<fanOutPoint> resource specific procedures for CRUD operations	188

7.4.14.3.1	Introduction	188

7.4.14.3.2	Create	188

7.4.14.3.3	Retrieve	189

7.4.14.3.4	Update	190

7.4.14.3.5	Delete	190

7.4.15	Resource Type <mgmtObj>	191

7.4.15.1	Introduction	191

7.4.15.2	<mgmtObj> resource specific procedures for CRUD operations	192

7.4.15.2.1	Introduction	192

7.4.15.2.2	Create	192

7.4.15.2.3	Retrieve	193

7.4.15.2.4	Update	193

7.4.15.2.5	Delete	193

7.4.16	Resource Type <mgmtCmd>	193

7.4.16.1	Introduction	193

7.4.16.2	<mgmtCmd> resource specific procedures for CRUD operations	195

7.4.16.2.0	Introduction	195

7.4.16.2.1	Create	195

7.4.16.2.2	Retrieve	195

7.4.16.2.3	Update	195

7.4.16.2.4	Delete	196

7.4.17	Resource Type <execInstance>	197

7.4.17.1	Introduction	197

7.4.17.2	<execInstance> resource specific procedures for CRUD operations	198

7.4.17.2.0	Create	198

7.4.17.2.1	Update (Cancel)	198

7.4.17.2.2	Retrieve	199

7.4.17.2.3	Delete	199

7.4.18	Resource Type <node>	199

7.4.18.1	Introduction	199

7.4.18.2	<node> resource specific procedures for CRUD operations	200

7.4.18.2.1	Create	200

7.4.18.2.2	Retrieve	201

7.4.18.2.3	Update	201

7.4.18.2.4	Delete	201

7.4.19	Resource Type <m2mServiceSubscriptionProfile>	201

7.4.19.1	Introduction	201

7.4.19.2	<m2mServiceSubscriptionProfile> resource specific procedures for CRUD operations	202

7.4.19.2.0	Introduction	202

7.4.19.2.1	Create	202

7.4.19.2.2	Retrieve	202

7.4.19.2.3	Update	202

7.4.19.2.4	Delete	203

7.4.20	Resource Type <serviceSubscribedNode>	203

7.4.20.1	Introduction	203

7.4.20.2	<serviceSubscribedNode> resource specific procedures for CRUD operations	204

7.4.20.2.0	Introduction	204

7.4.20.2.1	Create	204

7.4.20.2.2	Retrieve	204

7.4.20.2.3	Update	204

7.4.20.2.4	Delete	204

7.4.21	Resource Type <pollingChannel>	205

7.4.21.1	Introduction	205

7.4.21.2	<pollingChannel> resource specific procedures for CRUD operations	205

7.4.21.2.0	Introduction	205

7.4.21.2.1	Create	205

7.4.21.2.2	Retrieve	206

7.4.21.2.3	Update	206

7.4.21.2.4	Delete	206

7.4.22	Resource Type <pollingChannelURI>	206

7.4.22.1	Introduction	206

7.4.22.2	<pollingChannelURI> resource specific procedures for CRUD operations	207

7.4.22.2.0	Introduction	207

7.4.22.2.1	Create	207

7.4.22.2.2	Retrieve	207

7.4.22.2.3	Update	207

7.4.22.2.4	Delete	208

7.4.22.2.5	Notify	208

7.4.23	Resource Type <statsConfig>	208

7.4.23.1	Introduction	208

7.4.23.2	<statsConfig> resource-specific procedures for CRUD operations	209

7.4.23.2.1	Create	209

7.4.23.2.2	Retrieve	209

7.4.23.2.3	Update	209

7.4.23.2.4	Delete	210

7.4.24	Resource Type <eventConfig>	210

7.4.24.1	Introduction	210

7.4.24.2	<eventConfig> resource-specific procedures for CRUD operations	211

7.4.24.2.1	Create	211

7.4.24.2.2	Retrieve	212

7.4.24.2.3	Update	212

7.4.24.2.4	Delete	212

7.4.25	Resource Type <statsCollect>	212

7.4.25.1	Introduction	212

7.4.25.2	<statsCollect> resource-specific procedures for CRUD operations	214

7.4.25.2.1	Create	214

7.4.25.2.2	Retrieve	214

7.4.25.2.3	Update	214

7.4.25.2.4	Delete	215

7.4.26	Announced resource types	215

7.4.26.1	Introduction	215

7.4.26.2	Resource specific procedures for CRUD operations	216

7.4.26.2.1	Introduction	216

7.4.26.2.2	Create	216

7.4.26.2.3	Retrieve	216

7.4.26.2.4	Update	217

7.4.26.2.5	Delete	217

7.4.27	Resource Type <latest>	217

7.4.27.1	Introduction	217

7.4.27.2	<latest> Resource Specific Procedures for CRUD Operations	217

7.4.27.2.0	Introduction	217

7.4.27.2.1	Create	217

7.4.27.2.2	Retrieve	217

7.4.27.2.3	Update	218

7.4.27.2.4	Delete	219

7.4.28	Resource Type <oldest>	219

7.4.28.1	Introduction	219

7.4.28.2	<oldest> Resource Specific Procedures for CRUD Operations	219

7.4.28.2.0	Introduction	219

7.4.28.2.1	Create	219

7.4.28.2.2	Retrieve	219

7.4.28.2.3	Update	220

7.4.28.2.4	Delete	220

7.4.29	Resource Type <serviceSubscribedAppRule>	220

7.4.29.1	Introduction	220

7.4.29.2	<serviceSubscribedAppRule> resource specific procedures for CRUD operations	221

7.4.29.2.0	Introduction	221

7.4.29.2.1	Create	221

7.4.29.2.2	Retrieve	221

7.4.29.2.3	Update	222

7.4.29.2.4	Delete	222

7.4.30	Resource Type <notificationTargetMgmtPolicyRef>	222

7.4.30.1	Introduction	222

7.4.30.2	<notificationTargetMgmtPolicyRef> resource specific procedures for CRUD operations	223

7.4.30.2.0	Introduction	223

7.4.30.2.1	Create	223

7.4.30.2.2	Retrieve	223

7.4.30.2.3	Update	223

7.4.30.2.4	Delete	223

7.4.31	Resource Type <notificationTargetPolicy>	224

7.4.31.1	Introduction	224

7.4.31.2	<notificationTargetPolicy> resource specific procedures for CRUD operations	224

7.4.31.2.0	Introduction	224

7.4.31.2.1	Create	225

7.4.31.2.2	Retrieve	225

7.4.31.2.3	Update	225

7.4.31.2.4	Delete	225

7.4.32	Resource Type <policyDeletionRules>	225

7.4.32.1	Introduction	225

7.4.32.2	<policyDeletionRules> resource specific procedures for CRUD operations	226

7.4.32.2.0	Introduction	226

7.4.32.2.1	Create	226

7.4.32.2.2	Retrieve	226

7.4.32.2.3	Update	227

7.4.32.2.4	Delete	227

7.4.33	Resource Type <notificationTargetSelfReference>	227

7.4.33.1	Introduction	227

7.4.33.2	<notificationTargetSelfReference> resource specific procedures for CRUD operations	227

7.4.33.2.0	Introduction	227

7.4.33.2.1	Create	227

7.4.33.2.2	Retrieve	227

7.4.33.2.3	Update	228

7.4.33.2.4	Delete	228

7.4.34	Resource Type <semanticDescriptor>	229

7.4.34.1	Introduction	229

7.4.34.2	<semanticDescriptor> resource specific procedures for CRUD operations	230

7.4.34.2.0	Introduction	230

7.4.34.2.1	Create	230

7.4.34.2.2	Retrieve	231

7.4.34.2.3	Update	232

7.4.34.2.4	Delete	233

7.4.35	Resource Type <semanticFanOutPoint>	233

7.4.35.1	Introduction	233

7.4.35.2	<semanticFanOutPoint> resource specific procedures for CRUD operations	233

7.4.35.2.0	Introduction	233

7.4.35.2.1	Create	233

7.4.35.2.2	Retrieve	234

7.4.35.2.3	Update	234

7.4.35.2.4	Delete	235

7.4.36	Resource Type <dynamicAuthorizationConsultation>	235

7.4.36.1	Introduction	235

7.4.36.2	<dynamicAuthorizationConsultation> resource specific procedures for CRUD operations	236

7.4.36.2.0	Introduction	236

7.4.36.2.1	Create	236

7.4.36.2.2	Retrieve	236

7.4.36.2.3	Update	236

7.4.36.2.4	Delete	236

7.4.37	Resource Type <flexContainer>	237

7.4.37.1	Introduction	237

7.4.37.2	<flexContainer> resource specific procedures for CRUD operations	238

7.4.37.2.0	Introduction	238

7.4.37.2.1	Create	238

7.4.37.2.2	Retrieve	238

7.4.37.2.3	Update	238

7.4.37.2.4	Delete	239

7.4.38	Resource Type <timeSeries>	239

7.4.38.1	Introduction	239

7.4.38.2	<timeSeries> resource specific procedures for CRUD operations	240

7.4.38.2.0	Introduction	240

7.4.38.2.1	Create	240

7.4.38.2.2	Retrieve	241

7.4.38.2.3	Update	241

7.4.38.2.4	Delete	242

7.4.39	Resource Type <timeSeriesInstance>	242

7.4.39.1	Introduction	242

7.4.39.2	<timeSeriesInstance> resource specific procedures for CRUD operations	243

7.4.39.2.0	Introduction	243

7.4.39.2.1	Create	243

7.4.39.2.2	Retrieve	243

7.4.39.2.3	Update	243

7.4.39.2.4	Delete	244

7.4.40	Resource Type <role>	244

7.4.40.1	Introduction	244

7.4.40.2	<role> resource specific procedures for CRUD operations	245

7.4.40.2.0	Introduction	245

7.4.40.2.1	Create	245

7.4.40.2.2	Retrieve	245

7.4.40.2.3	Update	245

7.4.40.2.4	Delete	245

7.4.41	Resource Type <token>	246

7.4.41.1	Introduction	246

7.4.41.2	<token> resource specific procedures for CRUD operations	247

7.4.41.2.0	Introduction	247

7.4.41.2.1	Create	247

7.4.41.2.2	Retrieve	247

7.4.41.2.3	Update	247

7.4.41.2.4	Delete	247

7.4.42	Void	247

7.4.43	Resource Type <authorizationDecision>	247

7.4.43.1	Introduction	247

7.4.43.2	<authorizationDecision> resource specific procedures for CRUD operations	248

7.4.43.2.1	Create	248

7.4.43.2.2	Retrieve	248

7.4.43.2.3	Update	249

7.4.43.2.4	Delete	250

7.4.44	Resource Type <authorizationPolicy>	250

7.4.44.1	Introduction	250

7.4.44.2	<authorizationPolicy> resource specific procedures for CRUD operations	251

7.4.44.2.1	Create	251

7.4.44.2.2	Retrieve	251

7.4.44.2.3	Update	251

7.4.44.2.4	Delete	252

7.4.45	Resource Type <authorizationInformation>	252

7.4.45.1	Introduction	252

7.4.45.2	<authorizationInformation> resource specific procedures for CRUD operations	253

7.4.45.2.1	Create	253

7.4.45.2.2	Retrieve	253

7.4.45.2.3	Update	253

7.4.45.2.4	Delete	254

7.4.46	Resource Type <ontologyRepository>	254

7.4.46.1	Introduction	254

7.4.46.2	<ontologyRepository> resource specific procedures for CRUD operations	255

7.4.46.2.0	Introduction	255

7.4.46.2.1	Create	255

7.4.46.2.2	Retrieve	255

7.4.46.2.3	Update	255

7.4.46.2.4	Delete	255

7.4.47	Resource Type <ontology>	256

7.4.47.1	Introduction	256

7.4.47.2	<ontology> resource specific procedures for CRUD operations	257

7.4.47.2.0	Introduction	257

7.4.47.2.1	Create	257

7.4.47.2.2	Retrieve	257

7.4.47.2.3	Update	257

7.4.47.2.4	Delete	258

7.4.48	Resource Type <semanticValidation>	258

7.4.48.1	Introduction	258

7.4.48.2	<semanticValidation> resource specific procedures for CRUD operations	258

7.4.48.2.0	Introduction	258

7.4.48.2.1	Create	258

7.4.48.2.2	Retrieve	258

7.4.48.2.3	Update	259

7.4.48.2.4	Delete	260

7.4.49	Resource Type <semanticMashupJobProfile>	260

7.4.49.1	Introduction	260

7.4.49.2	<semanticMashupJobProfile> resource specific procedures for CRUD operations	261

7.4.49.2.0	Introduction	261

7.4.49.2.1	Create	261

7.4.49.2.2	Retrieve	262

7.4.49.2.3	Update	262

7.4.49.2.4	Delete	262

7.4.50	Resource Type <semanticMashupInstance>	263

7.4.50.1	Introduction	263

7.4.50.2	<semanticMashupInstance> resource specific procedures for CRUD operations	264

7.4.50.2.0	Introduction	264

7.4.50.2.1	Create	264

7.4.50.2.2	Retrieve	264

7.4.50.2.3	Update	265

7.4.50.2.4	Delete	265

7.4.51	Resource Type <mashup>	265

7.4.51.1	Introduction	265

7.4.51.2	<mashup> resource specific procedures for CRUD operations	265

7.4.51.2.0	Introduction	265

7.4.51.2.1	Create	265

7.4.51.2.2	Retrieve	266

7.4.51.2.3	Update	266

7.4.51.2.4	Delete	266

7.4.52	Resource Type <semanticMashupResult>	267

7.4.52.1	Introduction	267

7.4.52.2	<semanticMashupResult> resource specific procedures for CRUD operations	268

7.4.52.2.0	Introduction	268

7.4.52.2.1	Create	268

7.4.52.2.2	Retrieve	268

7.4.52.2.3	Update	268

7.4.52.2.4	Delete	268

7.4.53	Resource Type <AEContactList>	269

7.4.53.1	Introduction	269

7.4.53.2	<AEContactList> resource specific procedures for CRUD operations	269

7.4.53.2.0	Introduction	269

7.4.53.2.1	Create	269

7.4.53.2.2	Retrieve	270

7.4.53.2.3	Update	270

7.4.53.2.4	Delete	270

7.4.54	Resource Type <AEContactListPerCSE>	270

7.4.54.1	Introduction	270

7.4.54.2	<AEContactListPerCSE> resource specific procedures for CRUD operations	271

7.4.54.2.0	Introduction	271

7.4.54.2.1	Create	271

7.4.54.2.2	Retrieve	271

7.4.54.2.3	Update	272

7.4.54.2.4	Delete	272

7.4.55	Resource Type <localMulticastGroup>	272

7.4.55.1	Introduction	272

7.4.55.2	<localMulticastGroup> resource specific procedures for CRUD operations	273

7.4.55.2.0	Introduction	273

7.4.55.2.1	Create	273

7.4.55.2.2	Retrieve	274

7.4.55.2.3	Update	274

7.4.55.2.4	Delete	274

7.4.56	Resource Type <multimediaSession>	274

7.4.56.1	Introduction	274

7.4.56.2	<multimediaSession> resource specific procedures for CRUD operations	275

7.4.56.2.0	Introduction	275

7.4.56.2.1	Create	275

7.4.56.2.2	Retrieve	276

7.4.56.2.3	Update	276

7.4.56.2.4	Delete	276

7.4.57	Resource Type <triggerRequest>	276

7.4.57.1	Introduction	276

7.4.57.2	<triggerRequest> resource specific procedures for CRUD operations	277

7.4.57.2.0	Introduction	277

7.4.57.2.1	Create	277

7.4.57.2.2	Retrieve	278

7.4.57.2.3	Update	278

7.4.57.2.4	Delete	279

7.4.58	Resource Type <crossResourceSubscription>	279

7.4.58.1	Introduction	279

7.4.58.2	<crossResourceSubscription> resource specific procedures for CRUD operations	280

7.4.58.2.0	Introduction	280

7.4.58.2.1	Create	281

7.4.58.2.2	Retrieve	282

7.4.58.2.3	Update	282

7.4.58.2.4	Delete	282

7.4.59	Resource Type <backgroundDataTransfer>	283

7.4.59.1	Introduction	283

7.4.59.2	<backgroundDataTransfer> resource specific procedures for CRUD operations	284

7.4.59.2.0	Introduction	284

7.4.59.2.1	Create	284

7.4.59.2.2	Retrieve	284

7.4.59.2.3	Update	284

7.4.59.2.4	Delete	285

7.4.60	Resource Type <transactionMgmt>	285

7.4.60.1	Introduction	285

7.4.60.2	<transactionMgmt> resource specific procedures for CRUD operations	286

7.4.60.2.0	Introduction	286

7.4.60.2.1	Create	286

7.4.60.2.2	Retrieve	287

7.4.60.2.3	Update	287

7.4.60.2.4	Delete	287

7.4.61	Resource Type <transaction>	288

7.4.61.1	Introduction	288

7.4.61.2	<transaction> resource specific procedures for CRUD operations	289

7.4.61.2.0	Introduction	289

7.4.61.2.1	Create	289

7.4.61.2.2	Retrieve	290

7.4.61.2.3	Update	290

7.4.61.2.4	Delete	290

7.5	Primitive-specific procedures and definitions	291

7.5.1	Notification data object and procedures	291

7.5.1.1	Notification data object	291

7.5.1.2	Notification procedures	291

7.5.1.2.1	Introduction	291

7.5.1.2.2	Notification for <subscription> resources	292

7.5.1.2.3	Subscription Verification during Subscription Creation	295

7.5.1.2.4	Notification of Subscription Deletion	295

7.5.1.2.5	Notification for Asynchronous Non-blocking Request	296

7.5.1.2.6	Notification for subscription via group	296

7.5.1.2.7	Notification for service layer long polling	297

7.5.1.2.8	Notification for on-demand discovery request	297

7.5.1.2.9	Notification for missing Time Series Data	297

7.5.1.2.10	Notification for Dynamic Authorization	298

7.5.1.2.11	Notification for receiverESPrimRandObject Generation	299

7.5.1.2.12	Notification for End-to-End Security Certificate-based Key Establishment (ESCertKE)	300

7.5.1.2.13	Using Notify for transport of ESPrim Objects	301

7.5.1.2.14	Notification for Authorization Relationship Mapping Record creation	302

7.5.1.2.15	Notification for Authorization Relationship Mapping Record Request	303

7.5.1.2.16	Notification of a Change in AE Registration Point	303

7.5.1.2.17	Notification of a Reference to Application Entity Resource identifier	304

7.5.1.2.18	Cross-Resource Notification	305

7.5.1.2.19	Notification for Subscription Blocking Triggered update	305

7.5.1.2.20	Notification of Cross Resource Subscription Deletion	306

7.5.2	Elements contained in the Content primitive parameter	306

7.5.3	Multicast group procedures	307

7.5.3.1	Multicast group CREATE procedure	307

7.5.3.1.1	Common procedure	307

7.5.3.1.2	3GPPTM  MBMS group creation procedure	308

7.5.3.1.3	IP multicast group creation procedure	309

7.5.3.2	Multicast group Update procedure	309

7.5.3.3	Multicast group Delete procedure	311

7.6	Security Procedures	312

7.6.1	Introduction	312

7.6.2	Procedure for applying End-to-End Security of Primitives (ESPrim)	312

8	Representation of primitives in data transfer	316

8.1	Introduction	316

8.2	Short names	317

8.2.1	Introduction	317

8.2.2	Primitive parameters	317

8.2.3	Resource attributes	318

8.2.4	Resource types	324

8.2.5	Complex data types members	327

8.2.6	Trigger payload fields	330

8.3	XML serialization	331

8.3.1	Method	331

8.3.2	Examples	331

8.4	JSON serialization	332

8.4.1	Terminology	332

8.4.2	Method	332

8.4.3	Examples	333

8.5	CBOR serialization	335

8.5.1	Method	335

8.5.2	Examples	335

9	Mcn procedure	336

9.1	Introduction	336

9.2	Triggering	336

9.2.1	Introduction	336

Annex A (normative): Binding Mch to Diameter for Charging	340

A.1	Introduction	340

A.2	Diameter Commands on Mch	340

A.2.1	Accounting Request Command	340

A.2.2	Accounting Answer Command	340

A.3	Mapping of M2M Recorded Information Elements to AVPs	341

A.4	Summary of AVPs used	341

A.5	oneM2M Specific AVP Usage	344

A.5.1	Access-Network-Identifier AVP	344

A.5.2	Acct-Application-Id AVP	344

A.5.3	Accounting-Record-Type AVP	344

A.5.4	Application-Entity-ID AVP	344

A.5.5	Control-Memory-Size AVP	344

A.5.6	Current-Number-Members AVP	344

A.5.7	Data-Memory-Size AVP	344

A.5.8	External-ID AVP	344

A.5.9	Group-Name AVP	344

A.5.10	Hosting-CSE-ID AVP	345

A.5.11	Originator AVP	345

A.5.12	Maximum-Number-Members AVP	345

A.5.13	M2M-Event-Record-Timestamp AVP	345

A.5.14	M2M-Information AVP	345

A.5.15	Node-ID AVP	345

A.5.16	Occupancy AVP	346

A.5.17	Protocol-Type AVP	346

A.5.18	Rating-Group AVP	346

A.5.19	Receiver AVP	346

A.5.20	Request-Body-Size AVP	346

A.5.21	Request-Headers-Size AVP	346

A.5.22	Request-Operation AVP	346

A.5.23	Response-Body-Size AVP	346

A.5.24	Response-Headers-Size AVP	347

A.5.25	Response-Status-Code AVP	347

A.5.26	Service-Context-Id AVP	347

A.5.27	Service-Information AVP	347

A.5.28	Subgroup-Name AVP	347

A.5.29	Subscription-Id AVP	347

A.5.30	Subscription-Id-Data AVP	348

A.5.31	Subscription-Id-Type AVP	348

A.5.32	Target-ID AVP	348

Annex B (normative): 3GPPTM  MTC Interworking Device triggering	349

Annex C (informative): XML examples	350

C.1	XML schema for container resource type	350

C.2	Container resource that conforms to the Schema given above (see clause C.1)	352

Annex D (normative): <mgmtObj> Resource specializations	353

D.1	Introduction	353

D.2	Resource [firmware]	353

D.2.1	Introduction	353

D.2.2	Resource specific procedures for CRUD operations	353

D.2.2.0	Introduction	353

D.2.2.1	Create	354

D.2.2.2	Update	354

D.2.2.3	Retrieve	354

D.2.2.4	Delete	354

D.3	Resource [software]	354

D.3.1	Introduction	354

D.3.2	Resource specific procedures for CRUD operations	355

D.3.2.0	Introduction	355

D.3.2.1	Create	355

D.3.2.2	Update	355

D.3.2.3	Retrieve	356

D.3.2.4	Delete	356

D.4	Resource [memory]	356

D.4.1	Introduction	356

D.4.2	Resource specific procedures for CRUD operations	357

D.4.2.0	Introduction	357

D.4.2.1	Create	357

D.4.2.2	Update	357

D.4.2.3	Retrieve	357

D.4.2.4	Delete	357

D.5	Resource [areaNwkInfo]	357

D.5.1	Introduction	357

D.5.2	Resource specific procedures for CRUD operations	358

D.5.2.0	Introduction	358

D.5.2.1	Create	358

D.5.2.2	Update	358

D.5.2.3	Retrieve	358

D.5.2.4	Delete	359

D.6	Resource [areaNwkDeviceInfo]	359

D.6.1	Introduction	359

D.6.2	Resource specific procedures for CRUD operations	359

D.6.2.0	Introduction	359

D.6.2.1	Create	359

D.6.2.2	Update	360

D.6.2.3	Retrieve	360

D.6.2.4	Delete	360

D.7	Resource [battery]	360

D.7.1	Introduction	360

D.7.2	Resource specific procedures for CRUD operations	361

D.7.2.0	Introduction	361

D.7.2.1	Create	361

D.7.2.2	Update	361

D.7.2.3	Retrieve	361

D.7.2.4	Delete	361

D.8	Resource [deviceInfo]	362

D.8.1	Introduction	362

D.8.2	Resource specific procedures for CRUD operations	362

D.8.2.0	Introduction	362

D.8.2.1	Create	362

D.8.2.2	Update	363

D.8.2.3	Retrieve	363

D.8.2.4	Delete	363

D.9	Resource [deviceCapability]	363

D.9.1	Introduction	363

D.9.2	Resource specific procedures for CRUD operations	364

D.9.2.1	Introduction	364

D.9.2.2	Create	364

D.9.2.3	Update	364

D.9.2.4	Retrieve	365

D.9.2.5	Delete	365

D.10	Resource [reboot]	365

D.10.1	Introduction	365

D.10.2	Resource specific procedures for CRUD operations	365

D.10.2.0	Introduction	365

D.10.2.1	Create	366

D.10.2.2	Update	366

D.10.2.3	Retrieve	366

D.10.2.4	Delete	366

D.11	Resource [eventLog]	366

D.11.1	Introduction	366

D.11.2	Resource specific procedures for CRUD operations	367

D.11.2.0	Introduction	367

D.11.2.1	Create	367

D.11.2.2	Update	367

D.11.2.3	Retrieve	368

D.11.2.4	Delete	368

D.12	Resource [cmdhPolicy]	368

D.12.1	Introduction	368

D.12.2	Resource [activeCmdhPolicy]	369

D.12.3	Resource [cmdhDefaults]	369

D.12.4	Resource [cmdhDefEcValue]	370

D.12.5	Resource [cmdhEcDefParamValues]	370

D.12.6	Resource [cmdhLimits]	371

D.12.7	Resource [cmdhNetworkAccessRules]	372

D.12.8	Resource [cmdhNwAccessRule]	372

D.12.9	Resource [cmdhBuffer]	373

Annex E (informative): Procedures for accessing resources	374

E.1	Accessing resources in CSEs – blocking requests	374

E.2	Accessing Resources in CSEs - non-blocking requests	375

E.2.1	Non-blocking models	375

E.2.2	Synchronous case	375

Annex F (informative): Guidelines for oneM2M resource type XSD	380

Annex G (normative): Location request	382

G.1	Introduction	382

G.2	Location request by means of OMA-REST-NetAPI-TerminalLocation interface	382

G.2.1	Introduction	382

G.2.2	Resource structure of OMA NetAPI for terminal location	382

G.2.3	Procedures for terminal location	385

G.2.3.1	Request in a single query toward a location server	385

G.2.4	Subscribe to notifications for periodic location updates	385

G.2.5	Subscribe to notifications for area updates	386

G.3	Location request by means of 3GPPTM  MonitoringEvent API	387

G.3.1	Introduction	387

Annex H (normative): CMDH message processing	388

H.1	Pre-requisites	388

H.2	CMDH processing: processing request or response messages requiring the receiver CSE to forward information to another CSE	389

H.2.1	Applicability of CMDH processing	389

H.2.2	Partitioning of CMDH processing	389

H.2.3	CMDH message validation procedure	391

H.2.4	CMDH message forwarding procedure	395

H.2.5	Establishment of Mcc communication connection to another CSE	402

Annex I (informative): Guidelines for using XSD files in AE and CSE code	404

I.1	Usage of the oneM2M developed XSD files	404

I.2	Example AE/CSE implementation featuring mapping between short and long names for XML serialization	404

I.3	Example AE/CSE implementation featuring mapping between short and long names for JSON serialization	406

Annex J (normative): Specializations of <flexContainer> resource	408

J.1	Introduction	408

J.2	Void	408

J.3	Void	408

J.4	Resource type [svcObjWrapper]	408

J.5	Resource type [svcFwWrapper]	408

J.6	Resource type [allJoynApp]	409

J.7	Resource type [allJoynSvcObject]	409

J.8	Resource type [allJoynInterface]	410

J.9	Resource type [allJoynMethod]	410

J.10	Resource type [allJoynMethodCall]	411

J.11	Resource type [allJoynProperty]	412

Annex K (Informative): Optionality of resource attributes in requests	413

K.1	Introduction	413

K.2	Possible values of Create/Update request optionality with respect to WO/RO/RW attributes	413

History	414

List of figures

Figure 5.4.1-1: Communication model using Request and Response primitives over an IP-based Underlying Network	42

Figure 5.4.2-1: Primitive structure	43

Table 6.2.2-1: M2M Identifiers	46

Table 6.3.2-1: Data Types incorporated from XML Schema	49

Table 6.3.3-1: oneM2M Simple Data Types	51

Table 6.3.4.1-1: Example of oneM2M Enumeration Type Definition	57

Figure 6.3.4.1-1: Example of XSD version of oneM2M Enumeration Type	57

Table 6.3.4.2.1-1: Interpretation of m2m:resourceType	57

Table 6.3.4.2.2-1: Interpretation of m2m:cseTypeID	59

Table 6.3.4.2.3-1: Interpretation of m2m:locationSource	59

Table 6.3.4.2.4-1: Interpretation of m2m:stdEventCats	59

Table 6.3.4.2.5-1: Interpretation of m2m:operation	59

Table 6.3.4.2.6-1: Interpretation of m2m:responseType	60

Table 6.3.4.2.7-1: Interpretation of m2m:resultContent	60

Table 6.3.4.2.8-1: Interpretation of m2m:desIdResType	60

Table 6.3.4.2.9-1: Interpretation of m2m:responseStatusCode	60

Table 6.3.4.2.10-1: Interpretation of m2m:requestStatus	61

Table 6.3.4.2.11-1: Interpretation of m2m:memberType	61

Table 6.3.4.2.12-1: Interpretation of m2m:consistencyStrategy	62

Table 6.3.4.2.13-1: Interpretation of m2m:cmdType	63

Table 6.3.4.2.14-1: Interpretation of m2m:execModeType	63

Table 6.3.4.2.15-1: Interpretation of m2m:execStatusType	63

Table 6.3.4.2.16-1: Interpretation of m2m:execResultType	64

Table 6.3.4.2.17-1: Interpretation of m2m:pendingNotification	64

Table 6.3.4.2.18-1: Interpretation of m2m:notificationContentType	64

Table 6.3.4.2.19-1: Interpretation of m2m:notificationEventType	65

Table 6.3.4.2.20-1: Interpretation of m2m:status	65

Table 6.3.4.2.21-1: Interpretation of m2m:batteryStatus	65

Table 6.3.4.2.22-1: Interpretation of m2m:mgmtDefinition	66

Table 6.3.4.2.23-1: Interpretation of m2m:logTypeId	66

Table 6.3.4.2.24-1: Interpretation of m2m:logStatus	67

Table 6.3.4.2.25-1: Interpretation of m2m:eventType	67

Table 6.3.4.2.26-1: Interpretation of m2m:statsRuleStatusType	67

Table 6.3.4.2.27-1: Interpretation of m2m:statModelType	67

Table 6.3.4.2.28-1: Interpretation of m2m:encodingType	67

Table 6.3.4.2.29-1: Interpretation of m2m:accessControlOperations	68

Table 6.3.4.2.31-1: Interpretation of m2m:filterUsage	68

Table 6.3.4.2.32-1: Interpretation of m2m:notificationTargetPolicyAction	68

Table 6.3.4.2.33-1: Interpretation of m2m:logicalOperator	68

Table 6.3.4.2.34-1: Interpretation of m2m:filterOperation	69

Table 6.3.4.2.35-1: Interpretation of m2m:securityInfoType	69

Table 6.3.4.2.36-1: Interpretation of m2m:allJoynDirection	69

Table 6.3.4.2.37-1: Interpretation of m2m:contentFilterSyntax	69

Table 6.3.4.2.38-1: Interpretation of m2m:contentSecurity	70

Table 6.3.4.2.39-1: Interpretation of m2m:suid	71

Table 6.3.4.2.40-1: Interpretation of m2m:esprimKeyGenAlgID	71

Table 6.3.4.2.41-1: Interpretation of m2m:esprimProtocolAndAlgID	72

Table 6.3.4.2.43-1: Interpretation of m2m:stationaryIndication	72

Table 6.3.4.2.44-1: Interpretation of m2m:contentStatus	72

Table 6.3.4.2.45-1: Interpretation of m2m:networkAction	72

Table 6.3.4.2.46-1: Interpretation of m2m:locationInformationType	72

Table 6.3.4.2.47-1: Interpretation of m2m:geofenceEventCriteria	73

Table 6.3.4.2.48-1: Interpretation of m2m:semanticFormat	73

Table 6.3.4.2.49-1: Interpretation of m2m:triggerPurpose	73

Table 6.3.4.2.51-1: Interpretation of m2m:authorizationDecision	73

Table 6.3.4.2.52-1: Interpretation of m2m:authorizationStatus	74

Table 6.3.4.2.53-1: Interpretation of m2m:acpCombiningAlgorithm	74

Table 6.3.4.2.54-1: Interpretation of m2m:mashupMemberStoreType	74

Table 6.3.4.2.55-1: Interpretation of m2m:mashupResultGenType	75

Table 6.3.4.2.56-1: Interpretation of m2m:locationUpdateEventCriteria	75

Table 6.3.4.2.57-1: Interpretation of m2m:AERegistrationStatus	75

Table 6.3.4.2.58-1: Interpretation of m2m:multicastCapability	75

Table 6.3.4.2.59-1: Interpretation of m2m:sessionState	75

Table 6.3.4.2.60-1: Interpretation of m2m:triggerStatus	76

Table 6.3.4.2.61-1: Interpretation of m2m:timeWindowType	76

Table 6.3.4.2.62-1: Interpretation of m2m:transferSelectionGuidance	76

Table 6.3.4.2.63-1: Interpretation of m2m:transactionMode	76

Table 6.3.4.2.64-1: Interpretation of m2m:transactionControl	77

Table 6.3.4.2.65-1: Interpretation of m2m:transactionState	77

Table 6.3.4.2.66-1: Interpretation of m2m:transactionLockType	77

Table 6.3.4.2.67-1: Interpretation of m2m:transactionMgmtHandling	77

Table 6.3.5.2-1: Type Definition of m2m:deliveryMetadata	78

Table 6.3.5.3-1: Type Definition of m2m:aggregatedRequest	78

Table 6.3.5.4-1: Type Definition of m2m:metaInformation	78

Table 6.3.5.6-1: Type Definition of m2m:batchNotify	79

Table 6.3.5.7-1: Type Definition of m2m:eventNotificationCriteria	79

Table 6.3.5.8-1: Type Definition of m2m:filterCriteria	80

Table 6.3.5.9-1: Type Definition of m2m:attribute	80

Table 6.3.5.11-1: Type Definition of m2m:scheduleEntries	80

Table 6.3.5.12-1: Type Definition of m2m:aggregatedNotification	81

Table 6.3.5.13-1: Type Definition of m2m:notification	81

Table 6.3.5.14-1: Type Definition of m2m:actionStatus	82

Table 6.3.5.15-1: Type Definition of m2m:anyArgType	82

Table 6.3.5.16-1: Type Definition of m2m:resetArgsType	82

Table 6.3.5.17-1: Type Definition of m2m:rebootArgsType	82

Table 6.3.5.18-1: Type Definition of m2m:uploadArgsType	82

Table 6.3.5.19-1: Type Definition of m2m:downloadArgsType	83

Table 6.3.5.20-1: Type Definition of m2m:softwareInstallArgsType	83

Table 6.3.5.21-1: Type Definition of m2m:softwareUpdateArgsType	83

Table 6.3.5.22-1: Type Definition of m2m:softwareUninstallArgsType	83

Table 6.3.5.23-1: Type Definition of m2m:execReqArgsListType	84

Table 6.3.5.24-1: Type Definition of m2m:mgmtLinkRef	84

Table 6.3.5.25-1: Type Definition of m2m:resourceWrapper	84

Table 6.3.5.26-1: Type Definition of m2m:setOfAcrs	84

Table 6.3.5.27-1: Type Definition of m2m:accessControlRule	85

Table 6.3.5.28-1: Type Definition of m2m:locationRegion	85

Table 6.3.5.29-1: Type Definition of m2m:childResourceRef	86

Table 6.3.5.30-1: Type Definition of m2m:responseTypeInfo	86

Table 6.3.5.31-1: Type Definition of m2m:rateLimit	86

Table 6.3.5.32-1: Type Definition of m2m:operationResult	87

Table 6.3.5.33-1: Type Definition of m2m:aggregatedResponse	87

Table 6.3.5.34-1: Type Definition of m2m:mgmtResource	87

Table 6.3.5.35-1: Type Definition of m2m:announcedMgmtResource	88

Table 6.3.5.36-1: Type Definition of m2m:contentRef	88

Table 6.3.5.37-1: Type Definition of m2m:deletionContexts	88

Table 6.3.5.38-1: Type Definition of m2m:flexContainerResource	89

Table 6.3.5.39-1: Type Definition of m2m:announcedFlexContainerResource	89

Table 6.3.5.40-1: Type Definition of m2m:missingData	90

Table 6.3.5.41-1: Type Definition of m2m:tokenPermission	90

Table 6.3.5.42-1: Type Definition of m2m:tokenClaimSet	90

Table 6.3.5.43-1: Type Definition of m2m:dynAuthLocalTokenIdAssignments	90

Table 6.3.5.44-1: Type Definition of m2m:dynAuthTokenSummary	91

Table 6.3.5.45-1: Type Definition of m2m:dynAuthTokenReqInfo	91

Table 6.3.5.46-1: Type Definition of m2m:dynAuthDasRequest	91

Table 6.3.5.47-1: Type Definition of m2m:dynAuthDasResponse	92

Table 6.3.5.48-1: Type Definition of m2m:securityInfo	92

Table 6.3.5.49-1: Type Definition of m2m:listOfChildResourceRef	92

Table 6.3.5.50-1: Type Definition of m2m:originatorESPrimRandObject	93

Table 6.3.5.51-1: Type Definition of m2m:receiverESPrimRandObject	93

Table 6.3.5.52-1: Type Definition of m2m:e2eSecInfo	93

Table 6.3.5.53-1: Type Definition of m2m:tokenPermissions	93

Table 6.3.5.54-1: Type Definition of m2m:backOffParameters	94

Table 6.3.5.55-1: Type Definition of m2m:listOfDataLinks	94

Table 6.3.5.56-1: Type Definition of m2m:dataLink	94

Table 6.3.5.57-1: Type Definition of m2m:operationMonitor	94

Table 6.3.5.58-1: Type Definition of m2m:dynAuthRelMapRequest	95

Table 6.3.5.59-1: Type Definition of m2m:dynAuthRelMapResponse	95

Table 6.3.5.60-1: Type Definition of m2m:ipAddress	95

Table 6.3.5.61-1: Type Definition of m2m:setOfPermissions	95

Table 6.3.5.62-1: Elements used for representation element	96

Table 6.3.5.63-1: Type Definition of m2m:sessionDescriptions	96

Table 6.3.5.64-1: Type Definition of m2m:activityPatternElements	96

Table 6.3.5.65-1: Type Definition of m2m:activityPattern	96

Table 6.3.5.66-1: Type Definition of m2m:eventNotificationCriteriaSet	97

Table 6.3.5.68-1: Type Definition of m2m:mashupMembers	97

Table 6.3.6-1: Universal and Common Attributes	98

Table 6.3.6-2: Complex Data Types declaring groups of resource common attributes	98

Table 6.4.1-1: Data Types for Request primitive parameters	100

Table 6.4.2-1: Data Types for Response primitive parameters	102

Figure 6.5.1-1: Resource Types	103

Table 6.6.2-1: Definition of Response Status Code class	106

Table 6.6.3.2-1: Informational response class	106

Table 6.6.3.3-1: RSCs for successful response class	106

Table 6.6.3.4-1: RSCs for redirection response class	107

Table 6.6.3.5-1: RSCs for Originator error response class	107

Table 6.6.3.6-1: RSCs for Receiver error response class	108

Table 6.6.3.7-1: RSCs for Network system error response class	108

Table 6.7-1: oneM2M specific MIME media types	109

Table 6.8-1: Virtual Resources	109

Table 7.2.1.1-1: Request Primitive Parameters	111

Table 7.2.1.2-1: Response Primitive Parameters	112

Figure 7.2.2.1-1: Generic procedure of Originator	113

Figure 7.2.2.2-1: Generic procedure of Receiver	115

Figure 7.2.2.2-2: Resource handling procedure	116

Table 7.3.1.4-1: Request primitive parameter settings	118

Table 7.3.2.2-1: Common attributes settings for <request> resource	121

Table 7.3.2.2-2: Resource-specific attributes settings for <request> resource	121

Table 7.3.2.3-1: Response primitive parameter settings	122

Table 7.3.2.5-1: Common attributes settings for <request> resource	122

Table 7.3.2.5-2: Resource-specific attributes settings for <request> resource	122

Table 7.3.3.15-1: Types of Parameters in accessControlOriginators	134

Table 7.3.3.17.0-1: Summary on Filter conditions	135

Table 7.4.1.1-1: Data type definition of <resourceType>	145

Table 7.4.1.1-2: Universal/Common Attributes of <resourceType> resource	145

Table 7.4.1.1-3: Resource Specific Attributes of <resourceType> resource	145

Table 7.4.1.1-4: Child resources of <resourceType> resource	145

Table 7.4.2.1-1: Data type definition of <accessControlPolicy> resource	146

Table 7.4.2.1-2: Universal/Common Attributes of <accessControlPolicy> resource	146

Table 7.4.2.1-3: Resource Specific Attributes of <accessControlPolicy> resource	146

Table 7.4.2.1-4: Child Resources of <accessControlPolicy> resource	147

Table 7.4.3.1-1: Data type definition of <CSEBase> resource	148

Table 7.4.3.1-2: Universal/Common Attributes of <CSEBase> resource	148

Table 7.4.3.1-3: Resource Specific Attributes of <CSEBase> resource	148

Table 7.4.3.1-4: Child resources of <CSEBase> resource	149

Table 7.4.4.1-1: Data type definition of <remoteCSE> resource	150

Table 7.4.4.1-2: Universal/Common Attributes of <remoteCSE> resource	151

Table 7.4.4.1-3: Resource Specific Attributes of <remoteCSE> resource	151

Table 7.4.4.1-4: Child resources of <remoteCSE> resource	152

Table 7.4.5.1-1: Data type definition of <AE> resource	154

Table 7.4.5.1-2: Universal/Common Attributes of <AE> resource	154

Table 7.4.5.1-3: Resource Specific Attributes of <AE> resource	154

Table 7.4.5.1-4: Child resources of <AE> resource	155

Table 7.4.6.1-1: Data type definition of <container> resource	158

Table 7.4.6.1-2: Universal/Common Attributes of <container> resource	158

Table 7.4.6.1-3: Resource Specific Attributes of <container> resource	159

Table 7.4.7.1-1: Data type definition of <contentInstance> resource	160

Table 7.4.7.1-2: Universal/Common Attributes of <contentInstance> resource	161

Table 7.4.7.1-3: Resource Specific Attributes of <contentInstance> resource	161

Table 7.4.7.1-4: Child resources of <contentInstance> resource	161

Table 7.4.8.1-1: Data type definition of <subscription> resource	163

Table 7.4.8.1-2: Universal/Common Attributes of <subscription> resource	163

Table 7.4.8.1-3: Resource Specific Attributes of <subscription> resource	164

Table 7.4.8.1-4: Child resources of <subscription> resource	164

Table 7.4.9.1-1: Data type definition of <schedule> resource	167

Table 7.4.9.1-2: Universal/Common Attributes of <schedule> resource	168

Table 7.4.9.1-3: Resource Specific Attributes of <schedule> resource	168

Table 7.4.9.1-6: Child resources of <schedule > resource	169

Table 7.4.10.1-1: Data type definition of <locationPolicy> resource	170

Table 7.4.10.1-2: Universal/Common Attributes of <locationPolicy> resource	171

Table 7.4.10.1-3: Resource Specific Attributes of <locationPolicy> resource	171

Table 7.4.10.1-4: Child resources of <locationPolicy> resource	171

Table 7.4.11.1-1: Data type definition of <delivery> resource	174

Table 7.4.11.1-2: Universal/Common Attributes of <delivery> resource	174

Table 7.4.11.1-3: Resource Specific Attributes of <delivery> resource	174

Table 7.4.11.1-4: Child resources of <delivery> resource	174

Table 7.4.12.1-1: Data type definition of <request> resource	176

Table 7.4.12.1-2: Universal/Common Attributes of <request> resource	177

Table 7.4.12.1-3: Resource Specific Attributes of <request> resource	177

Table 7.4.12.1-4: Reference of child resources	177

Table 7.4.13.1-1: Data type definition of <group> resource	179

Table 7.4.13.1-2: Universal/Common Attributes of <group> resource	179

Table 7.4.13.1-3: Resource Specific Attributes of <group> resource	179

Table 7.4.13.1-4: Child resources of <group> resource	180

Figure 7.4.14.2.6-1: Generic procedure of Group-Hosting CSE	186

Table 7.4.15.1-1: Universal/Common Attributes of <mgmtObj> resource	191

Table 7.4.15.1-2: Resource Specific Attributes of <mgmtObj> resource	191

Table 7.4.15.1-3: Child resources of <mgmtObj> resource	192

Table 7.4.16.1-1: Data type definition of <mgmtCmd> resource	194

Table 7.4.16.1-2: Universal/Common Attributes of <mgmtCmd> resource	194

Table 7.4.16.1-3: Resource Specific Attributes of <mgmtCmd> resource	194

Table 7.4.16.1-4: Child resources of <mgmtCmd> resource	195

Table 7.4.17.1-1: Data type definition of <execInstance> resource	197

Table 7.4.17.1-2: Universal/Common Attributes of <execInstance> resource	197

Table 7.4.17.1-3: Resource Specific Attributes of <execInstance> resource	198

Table 7.4.17.1-4: Child Resources of <execInstance> resource	198

Table 7.4.18.1-1: Data type definition of <node> resource	200

Table 7.4.18.1-2: Universal/Common Attributes of <node> resource	200

Table 7.4.18.1-3: Resource Specific Attributes of <node> resource	200

Table 7.4.18.1-4: Child resources of <node> resource	200

Table 7.4.19.1-1: Data type definition of <m2mServiceSubscriptionProfile> resource	201

Table 7.4.19.1-2: Universal/Common Attributes of <m2mServiceSubscriptionProfile>	202

Table 7.4.19.1-3: Child resources of <m2mServiceSubscriptionProfile>	202

Table 7.4.20.1-1: Data type definition of <serviceSubscribedNode> resource	203

Table 7.4.20.1-2: Universal/Common Attributes of <serviceSubscribedNode> resource	203

Table 7.4.20.1-3: Resource Specific Attributes of <serviceSubscribedNode> resource	203

Table 7.4.20.1-4: Child resources of <serviceSubscribedNode> resource	203

Table 7.4.21.1-1: Data type definition of <pollingChannel> resource	205

Table 7.4.21.1-2: Universal/Common Attributes of <pollingChannel> resource	205

Table 7.4.21.1-3: Child resources of <pollingChannel> resource	205

Table 7.4.23.1-1: Data type definition of <statsConfig>	208

Table 7.4.23.1-2: Universal/Common Attributes of <statsConfig> resource	209

Table 7.4.23.1-3: Child resources of <statsConfig> resource	209

Table 7.4.24.1-1: Data type definition of <eventConfig>	210

Table 7.4.24.1-2: Universal/Common Attributes of <eventConfig> resource	210

Table 7.4.24.1-3: Resource Specific Attributes of <eventConfig> resource	211

Table 7.4.24.1-4: Child Resources of <eventConfig> resource	211

Table 7.4.25.1-1: Data type definition of <statsCollect>	212

Table 7.4.25.1-2: Universal/Common Attributes of <statsCollect> resource	213

Table 7.4.25.1-3: Resource Specific Attributes of <statsCollect> resource	213

Table 7.4.25.1-4: Child Resources of <statsCollect> resource	214

Table 7.4.26.1-1: Data type definition of announced Resource types	215

Table 7.4.26.1-2: Universal/Common Attributes of announcedResource	216

Table 7.4.26.1-3: Resource Specific Attributes of announcedResource	216

Table 7.4.29.1-1: Data type definition of <serviceSubscribedAppRule> resource	220

Table 7.4.29.1-2: Universal/Common Attributes of <serviceSubscribedAppRule> resource	221

Table 7.4.29.1-3: Resource Specific Attributes of <serviceSubscribedAppRule> resource	221

Table 7.4.29.1-4: Child resources of <serviceSubscribedAppRule> resource	221

Table 7.4.30.1-1: Data type definition of <notificationTargetMgmtPolicyRef> resource	222

Table 7.4.30.1-2: Universal/Common Attributes of <notificationTargetMgmtPolicyRef> resource	222

Table 7.4.30.1-3: Resource Specific Attributes of <notificationTargetMgmtPolicyRef> resource	222

Table 7.4.30.1-4: Child resources of <notificationTargetMgmtPolicyRef> resource	223

Table 7.4.31.1-1: Data type definition of <notificationTargetPolicy> resource	224

Table 7.4.31.1-2: Universal/Common Attributes of <notificationTargetPolicy> resource	224

Table 7.4.31.1-3: Resource Specific Attributes of <notificationTargetPolicy> resource	224

Table 7.4.31.1-4: Child resources of <notificationTargetPolicy> resource	224

Table 7.4.32.1-1: Data type definition of <policyDeletionRules> resource	225

Table 7.4.32.1-2: Universal/Common Attributes of <policyDeletionRules> resource	226

Table 7.4.32.1-3: Resource Specific Attributes of <policyDeletionRules> resource	226

Table 7.4.32.1-4: Child resources of <policyDeletionRules> resource	226

Table 7.4.34.1-1: Data type definition of <semanticDescriptor> resource	229

Table 7.4.34.1-2: Universal/Common Attributes of <semanticDescriptor> resource	229

Table 7.4.34.1-3: Resource Specific Attributes of <semanticDescriptor> resource	229

Table 7.4.34.1-4: Child resources of <semanticDescriptor> resource	230

Table 7.4.36.1-1: Data type definition of <dynamicAuthorizationConsultation> resource	235

Table 7.4.36.1-2: Universal/Common Attributes of <dynamicAuthorizationConsultation > resource	235

Table 7.4.36.1-3: Resource Specific Attributes of <dynamicAuthorizationConsultation> resource	236

Table 7.4.36.1-4: Child resources of <dynamicAuthorizationConsultation> resource	236

Table 7.4.37.1-1: Universal/Common Attributes of <flexContainer> resource	237

Table 7.4.37.1-2: Resource Specific Attributes of <flexContainer> resource	237

Table 7.4.37.1-3: Child Resources of <flexContainer> resource	238

Table 7.4.38.1-1: Data type definition of <timeSeries> resource	239

Table 7.4.38.1-2: Universal/Common Attributes of <timeSeries> resource	239

Table 7.4.38.1-3: Resource Specific Attributes of <timeSeries> resource	240

Table 7.4.38.1-4: Child Resources of <timeSeries> resource	240

Table 7.4.39.1-1: Data type definition of <timeSeriesInstance> resource	242

Table 7.4.39.1-2: Universal/Common Attributes of <timeSeriesInstance> resource	242

Table 7.4.39.1-3: Resource Specific Attributes of <timeSeriesInstance> resource	243

Table 7.4.39.1-4: Child resources of <timeSeriesInstance> resource	243

Table 7.4.40.1-1: Data type definition of <role> resource	244

Table 7.4.40.1-2: Universal/Common Attributes of <role> resource	244

Table 7.4.40.1-3: Resource Specific Attributes of <role> resource	245

Table 7.4.40.1-4: Child Resources of <role> resource	245

Table 7.4.41.1-1: Data type definition of <token> resource	246

Table 7.4.41.1-2: Universal/Common Attributes of <token> resource	246

Table 7.4.41.1-3: Resource Specific Attributes of <token> resource	246

Table 7.4.41.1-4: Child Resources of <token> resource	246

Table 7.4.43.1-1: Data type definition of <authorizationDecision> resource	247

Table 7.4.43.1-2: Universal/Common Attributes of <authorizationDecision> resource	248

Table 7.4.43.1-3: Resource Specific Attributes of <authorizationDecision> resource	248

Table 7.4.43.1-4: Child Resources of <authorizationDecision> resource	248

Table 7.4.44.1-1: Data type definition of <authorizationPolicy> resource	250

Table 7.4.44.1-2: Universal/Common Attributes of <authorizationPolicy> resource	250

Table 7.4.44.1-3: Resource Specific Attributes of <authorizationPolicy> resource	250

Table 7.4.44.1-4: Child Resources of <authorizationPolicy> resource	250

Table 7.4.45.1-1: Data type definition of <authorizationInformation> resource	252

Table 7.4.45.1-2: Universal/Common Attributes of <authorizationInformation> resource	252

Table 7.4.45.1-3: Resource Specific Attributes of <authorizationInformation> resource	252

Table 7.4.45.1-4: Child Resources of <authorizationInformation> resource	253

Table 7.4.46.1-1: Data type definition of <ontologyRepository> resource	254

Table 7.4.46.1-2: Universal/Common Attributes of <ontologyRepository> resource	254

Table 7.4.46.1-3: Child Resources of <ontologyRepository> resource	255

Table 7.4.47.1-1: Data type definition of <ontology> resource	256

Table 7.4.47.1-2: Universal/Common Attributes of <ontology> resource	256

Table 7.4.47.1-3: Resource Specific Attributes of <ontology> resource	256

Table 7.4.47.1-4: Child Resources of <ontology> resource	257

Table 7.4.49.1-1: Data type definition of <semanticMashupJobProfile> resource	260

Table 7.4.49.1-2: Universal/Common Attributes of <semanticMashupJobProfile> resource	261

Table 7.4.49.1-3: Resource Specific Attributes of <semanticMashupJobProfile> resource	261

Table 7.4.49.1-4: Child Resources of <semanticMashupJobProfile> resource	261

Table 7.4.50.1-1: Data type definition of <semanticMashupInstance> resource	263

Table 7.4.50.1-2: Universal/Common Attributes of <semanticMashupInstance> resource	263

Table 7.4.50.1-3: Resource Specific Attributes of <semanticMashupInstance> resource	263

Table 7.4.50.1-4: Child Resources of <semanticMashupInstance> resource	263

Table 7.4.52.1-1: Data type definition of <semanticMashupResult> resource	267

Table 7.4.52.1-2: Universal/Common Attributes of <semanticMashupResult> resource	267

Table 7.4.52.1-3: Resource Specific Attributes of <semanticMashupResult> resource	267

Table 7.4.52.1-4: Child Resources of <semanticMashupResult> resource	267

Table 7.4.53.1-1: Data type definition of <AEContactList> resource	269

Table 7.4.53.1-2: Universal/Common Attributes of <AEContactList> resource	269

Table 7.4.53.1-3: Resource Specific Attributes of <AEContactList> resource	269

Table 7.4.53.1-4: Child Resources of <AEContactList> resource	269

Table 7.4.54.1-1: Data type definition of <AEContactListPerCSE> resource	271

Table 7.4.54.1-2: Universal/Common Attributes of <AEContactListPerCSE> resource	271

Table 7.4.54.1-3: Resource Specific Attributes of <AEContactListPerCSE> resource	271

Table 7.4.55.1-1: Data type definition of <localMulticastGroup> resource	272

Table 7.4.55.1-2: Universal/Common Attributes of <localMulticastGroup> resource	273

Table 7.4.55.1-3: Resource Specific Attributes of <localMulticastGroup> resource	273

Table 7.4.56.1-1: Data type definition of <multimediaSession> resource	274

Table 7.4.56.1-2: Universal/Common Attributes of <multimediaSession> resource	275

Table 7.4.56.1-3: Resource Specific Attributes of <multimediaSession> resource	275

Table 7.4.56.1-4: Child Resources of <multimediaSession> resource	275

Table 7.4.57.1-1: Data type definition of <triggerRequest> resource	276

Table 7.4.57.1-2: Universal/Common Attributes of <triggerRequest> resource	277

Table 7.4.57.1-3: Resource Specific Attributes of <triggerRequest> resource	277

Table 7.4.57.1-4: Child Resources of <triggerRequest> resource	277

Table 7.4.58.1-1: Data type definition of <crossResourceSubscription> resource	280

Table 7.4.58.1-2: Universal/Common Attributes of <crossResourceSubscription> resource	280

Table 7.4.58.1-3: Resource Specific Attributes of <crossResourceSubscription> resource	280

Table 7.4.58.1-4: Child Resources of <crossResourceSubscription> resource	280

Table 7.4.59.1-1: Data type definition of <backgroundDataTransfer> resource	283

Table 7.4.59.1-2: Universal/Common Attributes of <backgroundDataTransfer> resource	283

Table 7.4.59.1-3: Resource Specific Attributes of <backgroundDataTransfer> resource	284

Table 7.4.59.1-4: Child Resources of <backgroundDataTransfer> resource	284

Table 7.4.60.1-1: Data type definition of <transactionMgmt> resource	285

Table 7.4.60.1-2: Universal/Common Attributes of <transactionMgmt> resource	285

Table 7.4.60.1-3: Resource Specific Attributes of <transactionMgmt> resource	285

Table 7.4.60.1-4: Child Resources of <transactionMgmt> resource	286

Table 7.4.61.1-1: Data type definition of <transaction> resource	288

Table 7.4.61.1-2: Universal/Common Attributes of <transaction> resource	288

Table 7.4.61.1-3: Resource Specific Attributes of <transaction> resource	289

Table 7.4.61.1-4: Child Resources of <transaction> resource	289

Table 7.5.1.1-1: Data Type Definition of notification data object	291

Table 7.5.1.1-2: Data Types for notification data objects	291

Table 7.5.2-1: Elements used for request content	306

Table 7.5.2-2: Elements used for response content	307

Table 7.5.3.1.1-1: Elements of Multicast Group Information Data Object	308

Table 7.5.3.2-1: memberIDs in the example <group> resource	310

Table 7.5.3.2-2: Old Multicast Group Information Data Objects	310

Table 7.5.3.2-3: New Multicast Group Information Data Object Example of <group> resource	310

Table 7.5.3.2-4: <localMulticastGroup> Operation for Member-Hosting CSEs Example	311

Table 7.5.3.2-5: <localMulticastGroup> Operation Result for Member-Hosting CSEs Example	311

Table 7.5.3.2-6: Multicast Group Information Data Object Example of <group> resource	311

Figure 7.6.2-1: Procedure for applying End-to-End Security of Primitives (ESPrim) to protect an exchange of inner primitives	313

Table 7.6.2-1: End-to-End security of Primitives (ESPrim) processing error cases with corresponding error message	316

Table 8.2.2-1: Primitive parameter short names	317

Table 8.2.2-2: Primitive root element short names	318

Table 8.2.3-1: Resource attribute short names (1/6)	318

Table 8.2.3-2: Resource attribute short names (2/6)	319

Table 8.2.3-3: Resource attribute short names (3/6)	320

Table 8.2.3-4: Resource attribute short names (4/6)	321

Table 8.2.3-5: Resource attribute short names (5/6)	322

Table 8.2.3-6: Resource attribute short names (6/6)	323

Table 8.2.4-1: Resource and specialization type short names	325

Table 8.2.5-1: Complex data type member short names	327

Table 8.2.6-1: Trigger payload field short names	330

Table 9.2.1-1: Trigger payload short names and field descriptions	337

Table A.3-1: Mapping of Recorded M2M Information Elements to Diameter AVPs	341

Table A.4-1: Use Of Diameter AVPs	343

Table D.2.1-1: Data Type Definition of [firmware]	353

Table D.2.1-2: Resource specific attributes of [firmware]	353

Table D.3.1-1: Data Type Definition of [software]	354

Table D.3.1-2: Resource specific attributes of [software]	355

Table D.4.1-1: Data Type Definition of [memory]	356

Table D.4.1-2: Resource specific attributes of [memory]	356

Table D.5.1-1: Data Type Definition of [areaNwkInfo]	358

Table D.5.1-2: Resource specific attributes of [areaNwkInfo]	358

Table D.6.1-1: Data Type Definition of [areaNwkDeviceInfo]	359

Table D.6.1-2: Resource specific attributes of [areaNwkDeviceInfo]	359

Table D.7.1-1: Data Type Definition of [battery]	360

Table D.7.1-2: Resource specific attributes of [battery]	361

Table D.8.1-1: Data Type Definition of [deviceInfo]	362

Table D.8.1-2: Resource specific attributes of [deviceInfo]	362

Table D.9.1-1: Data Type Definition of [deviceCapability]	363

Table D.9.1-2: Resource specific attributes of [deviceCapability]	364

Table D.10.1-1: Data Type Definition of [reboot]	365

Table D.10.1-2: Resource specific attributes of [reboot]	365

Table D.11.1-1: Data Type Definition of [eventLog]	367

Table D.11.1-2: Resource specific attributes of [eventLog]	367

Table D.12.1-1: Data Type Definition of [cmdhPolicy]	368

Table D.12.1-2: Resource specific attributes of [cmdhPolicy]	368

Table D.12.2-1: Data Type Definition of [activeCmdhPolicy]	369

Table D.12.2-2: Resource specific attributes of [activeCmdhPolicy]	369

Table D.12.3-1: Data Type Definition of [cmdhDefaults]	369

Table D.12.3-2: Resource specific attributes of [cmdhDefaults]	369

Table D.12.4-1: Data Type Definition of [cmdhDefEcValue]	370

Table D.12.4-2: Resource specific attributes of [cmdhDefEcValue]	370

Table D.12.5-1: Data Type Definition of [cmdhEcDefParamValues]	370

Table D.12.5-2: Resource specific attributes of [cmdhEcDefParamValues]	371

Table D.12.6-1: Data Type Definition of [cmdhLimits]	371

Table D.12.6-2: Resource specific attributes of [cmdhLimits]	371

Table D.12.7-1: Type Definition of [cmdhNetworkAccessRules]	372

Table D.12.7-2: Resource specific attributes of [cmdhNetworkAccessRules]	372

Table D.12.8-1: Data Type Definition of [cmdhNwAccessRule]	372

Table D.12.8-2: Resource specific attributes of [cmdhNwAccessRule]	373

Table D.12.9-1: Data Type Definition of [cmdhBuffer]	373

Table D.12.9-2: Resource specific attributes of [cmdhBuffer]	373

Figure E.1-1: Blocking access to resource	374

Figure E.2.2-1: Non-Blocking access to resource in synchronous mode (no hop)	376

Figure E.2.2-2: Non-Blocking access to resource in synchronous mode (one hop)	378

Figure G.2.2-1: Resource Structure defined by NetAPI for Terminal Location	383

Table G.2.2-1: Applicable NetAPI for Terminal Location	383

Table G.2.2-2: Resource Type Definition - TerminalLocation	383

Table G.2.2-3: Resource Type Definition - PeriodicNotificationSubscription	384

Table G.2.2-4: Resource Type Definition – CircleNotificationSubscription	384

Figure G.2.3.1-1: Single Query Toward Location Server	385

Figure G.2.4-1: Subscribe to Notification for Periodic Location Updates	385

Figure G.2.5-1: Subscribe to Notification for Area Updates	386

Figure H.2.2-1: CMDH Processing	391

Figure H.2.3-1: CMDH message validation procedure	395

Figure H.2.4-1: CMDH message forwarding procedure	396

Table J.4-1: Data type definition of [svcObjWrapper] resource	408

Table J.4-2: Resource Specific Attributes of [svcObjWrapper] resource	408

Table J.4-3: Child Resources of [svcObjWrapper] resource	408

Table J.5-1: Data type definition of [svcFwWrapper] resource	409

Table J.5-2: Resource Specific Attributes of [svcFwWrapper] resource	409

Table J.5-3: Child Resources of [svcFwWrapper] resource	409

Table J.6-1: Data type definition of [allJoynApp] resource	409

Table J.6-2: Resource Specific Attributes of [allJoynApp] resource	409

Table J.6-3: Child Resources of [allJoynApp] resource	409

Table J.7-1: Data type definition of [allJoynSvcObject] resource	410

Table J.7-2: Resource Specific Attributes of [allJoynSvcObject] resource	410

Table J.7-3: Child Resources of [allJoynSvcObject] resource	410

Table J.8-1: Data type definition of [allJoynInterface] resource	410

Table J.8-2: Resource Specific Attributes of [allJoynInterface] resource	410

Table J.8-3: Child Resources of [allJoynInterface] resource	410

Table J.9-1: Data type definition of [allJoynMethod] resource	411

Table J.9-2: Resource Specific Attributes of [allJoynMethod] resource	411

Table J.9-3: Child Resources of [allJoynMethod] resource	411

Table J.10-1: Data type definition of [allJoynMethodCall] resource	411

Table J.10-2: Resource Specific Attributes of [allJoynMethodCall] resource	411

Table J.10-3: Child Resources of [allJoynMethodCall] resource	411

Table J.11-1: Data type definition of [allJoynProperty] resource	412

Table J.11-2: Resource Specific Attributes of [allJoynProperty] resource	412

Table J.11-3: Child Resources of [allJoynProperty] resource	412

Table K.2-1: Request Optionality of Attributes in Content	413


# 1	Scope


The present document specifies the communication protocol(s) for oneM2M compliant Systems, M2M Applications, and/or other M2M systems.

The present document also specifies the common data formats, interfaces and message sequences to support reference points(s) defined by oneM2M.


# 2	References



## 2.1	Normative references


References are either specific (identified by date of publication and/or edition number or version number) or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies.

The following referenced documents are necessary for the application of the present document.

[1]	W3C Recommendation (26 November 2008): "Extensible Markup Language (XML) 1.0 (Fifth Edition)".

[2]	IETF RFC 3986: "Uniform Resource Identifier (URI): Generic Syntax".

[3]	W3C Recommendation (2004): "XML Schema Part 2: Datatypes Second Edition".

[4]	Void.

[5]	Void.

[6]	oneM2M TS-0001: "Functional Architecture".

[7]	oneM2M TS-0003: "Security Solutions".

[8]	IEEE 754-2008: "IEEE Standard for Floating-Point Arithmetic".

NOTE:	Available at http://ieeexplore.ieee.org/servlet/opac?punumber=4610933.

[9]	IETF RFC 4648: "The Base16, Base32, and Base64 Data Encodings".

[10]	IETF RFC 2045: "Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet Message Bodies".

[11]	IETF RFC 3987: "Internationalized Resource Identifiers (IRIs)".

[12]	Void.

[13]	Void.

[14]	IETF RFC 6733: "Diameter Base Protocol".

[15]	3GPP TS 23.682: "Architecture enhancements to facilitate communications with packet data networks and applications".

[16]	Void.

[17]	3GPP TS 23.003: "Numbering, addressing and identification".

[18]	Void.

[19]	IETF RFC 8259: "The JavaScript Object Notation (JSON) Data Interchange Format".

[20]	IETF RFC 5234: "Augmented BNF for Syntax Specifications: ABNF".

[21]	IETF RFC 3629: "UTF-8, a transformation format of ISO 10646".

[22]	oneM2M TS-0008: "CoAP Protocol Binding".

[23]	oneM2M TS-0009: "HTTP Protocol Binding".

[24]	oneM2M TS-0010: "MQTT Protocol Binding".

[25]	oneM2M TS-0011: "Common Terminology".

[26]	IETF RFC 6838: "Media Type Specifications and Registration Procedures".

[27]	ISO 8601:2004: "Data elements and interchange formats -- Information interchange -- Representation of dates and times".

[28]	OMA-TS-REST_NetAPI_TerminalLocation: "Open Mobile Alliance; RESTful Network API for Terminal Location", Version 1.0.

[29]	IETF RFC 4632: "Classless Inter-domain Routing (CIDR): The Internet Address Assignment and Aggregation Plan".

[30]	IETF RFC 5952: "A Recommendation for IPv6 Address Text Representation".

[31]	3GPP TS 32.299: "Telecommunication management; Charging management; Diameter charging applications".

[32]	IETF RFC 4006: "Diameter Credit-Control Application".

[33]	W3C Recommendation: "SPARQL 1.1 Query Language".

[34]	W3C Recommendation: "RDF 1.1 XML Syntax".

[35]	IETF RFC 4122: "A Universally Unique IDentifier (UUID) URN Namespace".

[36]	oneM2M TS-0012: "oneM2M Base Ontology".

[37]	oneM2M TS-0021: "oneM2M and AllJoyn Interworking".

[38]	oneM2M TS-0022: "Field Device Configuration".

[39]	IETF RFC 7049 (October 2013): "Concise Binary Object Representation (CBOR)".

[40]	oneM2M TS-0023: "Home Appliances Information Model and Mapping".

[41]	ISO 3166-1:2013: "Codes for the representation of names of countries and their subdivisions -- Part 1: Country codes".

[42]	oneM2M TS-0020: "WebSocket Protocol Binding".

[43]	oneM2M TS-0026: "3GPP Interworking".

[44]	W3C Recommendation: "OWL 2 Web Ontology Language: Structural Specification and Functional-Style Syntax (Second Edition)".

[45]	W3C Recommendation: "OWL 2 Web Ontology Language XML Serialization (Second Edition)".

[46]	W3C Recommendation: "OWL 2 Web Ontology Language: Mapping to RDF Graphs (Second Edition)".

[47]	W3C Recommendation: "RDF 1.1 Turtle: Terse RDF Triple Language".

[48]	W3C Note: "OWL 2 Web Ontology Language Manchester Syntax (Second Edition)".

[49]	W3C Recommendation:  "JSON-LD 1.1: A JSON-based Serialization for Linked Data".

[50]	oneM2M TS-0034: "Semantics Support".

[51]	3GPP TS 29.122: "T8 reference point for Northbound Application Programming Interfaces (APIs)".

[52]	IETF RFC 4566: "SDP: Session Description Protocol".

[53]	Void.

[54]	Void.

[55]	Void.

[56]	Void.

[57]	SPARQL Query Results XML Format (Second Edition)
https://www.w3.org/TR/rdf-sparql-XMLres

[58]	SPARQL 1.1 Query Results JSON Format
https://www.w3.org/TR/sparql11-results-json


## 2.2	Informative references


References are either specific (identified by date of publication and/or edition number or version number) or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies.

The following referenced documents are not necessary for the application of the present document but they assist the user with regard to a particular subject area.

[i.1]	oneM2M Drafting Rules.

NOTE:	Available at http://www.onem2m.org/images/files/oneM2M-Drafting-Rules.pdf.

[i.2]	Fielding, Roy Thomas (2000): "Architectural Styles and the Design of Network-based Software Architectures", Doctoral dissertation, University of California, Irvine.

[i.3]	OMA-TS-REST-NetAPI-NotificationChannel: "Open Mobile Alliance; RESTful Network API for Notification Channel", OMA-TS-REST-NetAPI-NotificationChannel-V1-0.

[i.4]	OMA-TS-MLP: "Open Mobile Alliance; Mobile Location Protocol",
OMA-TS-MLP-V3-4-20130226-C Version 3.4.

[i.5]	W3C Resource Description Framework.

NOTE:	Available at https://www.w3.org/RDF/.

[i.6]	W3C Recommendation: "SPARQL Query Language for RDF".

NOTE:	Available at https://www.w3.org/TR/rdf-sparql-query/.

[i.7]	IETF RFC 7515 (2015): "JSON Web Signature (JWS)".

[i.8]	IETF RFC 7516 (2015): "JSON Web Encryption (JWE)".

[i.9]	IETF RFC 7518 (2015): "JSON Web Algorithms (JWA)".

[i.10]	IETF RFC 5771 (2010): "IANA Guidelines for IPv4 Multicast Address Assignments".

[i.11]	IETF RFC 4291 (2006): "IP Version 6 Addressing Architecture".


# 3	Definitions and abbreviations



## 3.1	Definitions


For the purposes of the present document, the terms and definitions given in oneM2M TS-0011 Common Terminology [25] and the following apply:

Complex Data Type: data type that has a child element

Enumeration Type: data type that defines a variable to be one of a set of predefined constants

Group-Hosting CSE: CSE where the addressed group resource resides

Hosting CSE: CSE where the addressed resource is hosted

Location Server: server offering location capabilities

M2M Area Network: network providing connectivity between Application Service Nodes or Application Dedicated Nodes and Middle Nodes in the field domain

Mca: Reference Point for M2M Communication with AE

Mcc: Reference Point for M2M Communication with CSE

Mcc': Reference Point for M2M Communication with CSE of different M2M Service Provider

NULL: null value

NOTE:	The representation of null for different serialization types like xml and json can be found in clauses 8.3 and 8.4 respectively.

Originator: the AE/CSE that sends a Request

NOTE:	In case of a request that traverses multiple reference points, the Originator is the AE/CSE that sends the first request in the sequence.

Receiver: entity that receives the Request

Receiver CSE: any CSE that receives a request

Registrar CSE: CSE where an Application or another CSE has registered

Registree/Registrar CSE: CSE that registers with another CSE

Request: message sent from the Originator to the Receiver

Response: message replying to the Request, sent from the Receiver to the Originator


## 3.2	Abbreviations


For the purposes of the present document, the abbreviations given in oneM2M TS-0011 Common Terminology [25] and the following apply:

3GPP2	3rd Generation Partnership Project 2

ACP	AccessControlPolicy

AD	Anno Domini

AE-ID	Application Entity Identifier

ARC	Architecture

ASN-CSE	Application Entity that is registered with the CSE at Application Service Node

BCP	Best Current Practices

CDT	Common Data Type

CIDR	Classless Inter-Domain Routing

CMDH	Communication Management and Delivery Handling

CoAP	Constrained Application Protocol

CRUD	Create Retrieve Update Delete

CRUD+N	Create Retrieve Update Delete Notification

CSE-ID	Common Service Entity Identifier

CUDN	Create Update Delete Notify

DAA	Device Action Answer

DAR	Device-Action-Request

DNA	Device Notification Answer

DNR	Device Notification Request

DTLS	Datagram Transport Layer Security

FFS	For Further Study

FQDN	Fully Qualified Domain Name

GPS	Global Positioning System

HTTP	HyperText Transfer Protocol

IANA	Internet Assigned Numbers Authority

ID	IDentifier

IEEE	Institute of Electrical and Electronics Engineers

IETF	Internet Engineering Task Force

IN-AE	Application Entity that is registered with the CSE in the Infrastructure Node

IN-CSE	CSE which resides in the Infrastructure Node

IRI	Internationalized Resource Identifier

ISO	International Organization for Standardization

JSON	JavaScript Object Notation

MA	Mandatory Announced

MIME	Multipurpose Internet Mail Extension

MN-CSE	Reference Point for M2M Communication with CSE of different M2M Service Provider

MR	Mashup Requestor

MQTT	Message Queue Telemetry Transport

MTC-IWF	Machine Type Communications - InterWorking Function

NP	Not Present

NSE	Network Service Entity

OA	Optional Announced

OMA-DM	Open Mobile Alliance Device Management

RD	Retrieve Delete

RDF		Resource Description Framework

RFC	Request For Comment

RH	Resource Host

RPC	Remote Procedure Call

RSC	Response Status Codes

RUD	Retrieve Update Delete

SCS	Services Capability Server

SMF	Semantic Mashup Function

SMI	Semantic Mashup Instance

SMJP	Semantic Mashup Job Profile

SP	Service Provider

SPARQL	SPARQL Protocol and RDF Query Language

SP-ID	Service Provider Identifier

TBD	To Be Determined

TCP	Transmission Control Protocol

TLS	Transport Layer Security

UDP	User Datagram Protocol

UE	User Equipment

URI	Uniform Resource Identifier

URL	Uniform Resource Locator

UTC	Coordinated Universal Time

UTF	UCS Transformation Format

UUID	Universally Unique Identifier

WLAN	Wireless Local Area Network

XML	eXtensible Markup Language

XSD	XML Schema Definition


# 4	Conventions


The key words "Shall", "Shall not", "May", "Need not", "Should", "Should not" in the present document are to be interpreted as described in the oneM2M Drafting Rules [i.1].

To improve readability:

The information elements of oneM2M Request/Response messages will be referred to as parameters. Parameter names will be written in bold italic.

The information elements of resources will be referred to as attributes and child resources. Attributes will be written in italics.

Abbreviated short names for information elements (see clause 8) will be written in bold italic.


# 5	Protocol design principles and requirements



## 5.1	General introduction


Clause 5 contains the design principles and requirements for the oneM2M protocol.


## 5.2	Introduction



### 5.2.0	Overview


The oneM2M architecture is resource-based (oneM2M TS-0001 [6]). The functionality of the system is exposed by means of APIs over all reference points specified in oneM2M TS-0001 [6]. Operations upon resources hosted by a CSE are carried over an established channel that constitutes the communication on the reference points Mca and Mcc. All resource operations could be fulfilled with the considerations in terms of scalability, extensibility, fault tolerance and robustness, energy efficiency, and self-operation.

Offline Charging using the Mch reference point is described in [6] and specified in Annex A.

Each resource operation comprises a pair of primitives: Request and Response. The Request and Response primitives can be represented as XML documents or JSON texts. This process of representing a primitive as XML documents, JSON texts or CBOR data format is denoted serialization in the present document. Serialization translates primitives into a format that can be stored or exchanged between network entities. This is exploited when transmitting primitives over communication protocols such as HTTP, CoAP, MQTT or WebSocket.

In order to provide a well-defined interface for the reference points in oneM2M TS-0001 [6], the following aspects need to be provided:

the collection of primitives carried over a specific reference point; and

the definitions and procedures of resource types in relation to the underlying protocols and reference points involved.

The present document provides:

protocol design principles and requirements;

data type definitions and representations;

primitive format and generic procedures;

common operations of originators and receivers;

resource type-specific procedures; and

XML definitions and schema.

NOTE:	The actual binding of the interface to a specific protocol is not part of the present document, but is specified in a separate Technical Specifications [22], [23], [24], [42].

In accordance with the oneM2M architecture, each reference point is applicable to a wide range of underlying network technologies and transport protocols. oneM2M defines a set of bindings for specific underlying network technologies and transport protocols, these bindings are not limiting the applicability of the interfaces when used in other underlying networks and transport protocols. However, the behaviour of the interface needs to be respected in accordance to the present document and oneM2M TS-0001 [6].


### 5.2.1	Interfaces to the underlying networks


The CSEs access the network service functions provided by the underlying networks such as 3GPP, 3GPP2 and WLAN via Mcn reference point. Protocol bindings to the Mcn reference point are described in clause 9. The following services are provided by the underlying networks:

Device triggering (see oneM2M TS-0026 [43])

Location request (see Annex G)

Device Management (see clause 7.3.4)


## 5.3	API design guidelines


The following are the guidelines for designing APIs:

APIs shall follow the principle of RESTful architecture, as described in [i.2].

APIs shall indicate which features are supported and not supported over the reference points specified in oneM2M TS-0001 [6].

APIs shall define how to address resources and how to manipulate resources, in accordance with oneM2M TS-0001 [6]; the resource is identified by a Universal Resource Identifier (URI) [2].

APIs shall provide the format and syntax of the operation primitives for all resources defined in oneM2M TS-0001 [6]. In case that for a particular protocol binding an operation cannot be supported it has to be clearly stated in the specific protocol binding technical specification.

Each Resource has a representation (see [i.2]) that shall be transferred and manipulated with the verbs. These verbs are identified as operations in oneM2M TS-0001 [6]: CREATE. RETRIEVE, UPDATE, DELETE and NOTIFY.

All primitives as well as the way that those primitives are sent shall be defined. The functionality of the primitives shall be compliant to the resource type specific procedure as specified in oneM2M TS-0001 [6], clause 10.2.

Primitives shall include attributes in accordance with oneM2M TS-0001 [6] for a specific resource.

Primitives shall be self-descriptive and contain all the information needed for the receiver of the primitives to handle the primitives.

Primitives should be idempotent operations which means no matter how many times the primitive is sent, the result does not change, in accordance to [i.2].

Primitives shall be mapped on the transport layer protocols.


## 5.4	Primitives



### 5.4.1	Introduction


Primitives are common service layer messages exchanged over the Mca, Mcc and Mcc' reference points.

There are two use cases:

communication between an Originator and a Receiver which are collocated on the same M2M Node (e.g. ASN or MN) in the Common Service layer;

communication between an Originator and a remote Receiver via an Underlying Network.

In the first use case the primitives may be exchanged directly between the Originator and Receiver processes.

In case of using an IP-based Underlying Network as illustrated in Figure 5.4.1-1, the primitives are mapped to application layer communication protocols such as HTTP, CoAP, MQTT or WebSocket which use TCP or UDP on the transport layer. The specification of primitives, however, is independent of underlying communication protocols and allows introduction of bindings to other communication protocols.

Figure 5.4.1-1: Communication model using Request and
Response primitives over an IP-based Underlying Network

A single primitive in the common service layer may be mapped to zero or more transport messages by the communication protocol.

The Originators shall send requests to Receivers through primitives. The Originator and Receiver may be represented by either an AE or a CSE. The CRUD request primitive addresses a resource residing in a CSE. The Notify request primitive may address an AE or CSE.

Each CRUD+N operation consists of request and response primitives.


### 5.4.2	Primitives modelling


Primitives are modelled as follows.

A primitive is represented in the form of a data structure which defines, with appropriate parameters, specific procedures to be executed by both originator and receiver entities.

The data structure of a primitive consists of two parts:

a control part, which contains parameters specifying the processing of the primitive; and

an optional content part, which represents resource data, either the complete resource or only part of the resource (i.e. values of one or more resource attributes) in the partial addressing case.

Figure 5.4.2-1: Primitive structure


### 5.4.3	Primitive principles


Execution of one primitive shall finish completely before execution of a subsequent primitive starts that affects the same resource.

When creating or updating the resource, its representation (full or partial) shall be contained in the content part of the primitive. Based on the representation of the resource, the Hosting CSE can create or update the entire resource without need for further information.

The operations on resources triggered by primitives shall be idempotent. This means no matter how many times the same primitive is targeted to the same resource, the resource does not change after the first execution of this primitive, with the exception of the creation of child resources.


### 5.4.4	Serialization of primitives


When transferred over a oneM2M reference point while using a communication protocol such as HTTP, CoAP, MQTT or WebSocket, the way oneM2M Request and Response primitives are represented shall be defined by a specific oneM2M protocol binding that is being used for the message transfer. The originator and receiver of each primitive use the same binding, and thus they will be using compatible serialization and deserialization techniques. Clause 8 of the present document defines canonical approaches for serializing primitives as JSON objects, XML documents or CBOR data format used by oneM2M protocol bindings.


## 5.5	Design principles



### 5.5.1	Introduction


The following clauses (5.5.2 to 5.5.7) present the design principles which wrap up the perspectives and ways in terms of definitions and procedures of APIs and resources for the oneM2M core protocol specified in the present document. These design principles shall cover all characteristics and advantages of oneM2M protocols including specifications of bindings to transport protocols such as HTTP, CoAP, MQTT and WebSocket.

The design of oneM2M protocols consider and mitigate the risk of unintended consequences, such as extensibility and interoperability issues, operational problems, or efficiency.


### 5.5.2	Extensibility


The oneM2M protocols are designed to allow continued development and to facilitate changes by means of standardized extensions.

The impact of the extensibility on the existing oneM2M protocol functions shall be minimized.

Extensibility can be related to one or more of the following aspects:

handling a wide range of transport protocols as well as a different number of devices;

adding, removing or modifying oneM2M protocol functionality;

new oneM2M protocol routines;

new primitives and data types.


### 5.5.3	Scalability


For provisioning scalability as a requirement in the design of oneM2M protocols, one or several of the following mechanisms are used:

Ensuring direct addressability to the CSEs hosting target resources, to minimize network hops.

Asynchrony in terms of data processing, with the objective of minimizing the number of discarded packets.

Caching mechanisms that allow all the received packets to be processed.

Efficient load distribution to avoid bottlenecks and data loss.

Data compression and/or aggregation, in order to reduce the amount of data sent through the network.


### 5.5.4	Fault tolerance and robustness


One or more of the following mechanisms in terms of link availability can be exploited in the design of oneM2M protocols to account for a variety of exception conditions.

To provide reliable transmission of data packets, packet recovery will be dealt with by using mechanisms appropriate for the operating environment (e.g. constrained devices, unreliable networks).

When oneM2M protocols are employed over unreliable links, multiple data dissemination paths can be provided and maintained.


### 5.5.5	Efficiency


oneM2M protocols are designed with consideration of efficiency for networking involved resource-constrained devices.

As energy consumption directly affects the overall system performance, oneM2M protocols should consider energy efficiency, especially in resource constrained environments with battery-powered oneM2M devices.

Energy efficient oneM2M protocols aims at reducing the overall energy consumption while maintaining the performance required by the oneM2M Applications.


### 5.5.6	Inter-operability


API inter-operability between different protocol stacks is expected. For example, oneM2M API over HTTP/TCP/IP needs to inter-operate with CoAP/UDP in a local network using oneM2M API. oneM2M protocols are specified to provision the API inter-operability.


### 5.5.7	Self-operation and self-management


Devices employing the oneM2M API inter-work with established management protocols (e.g. security, discovery, bootstrapping, etc.). The inter-working with legacy management protocols via the oneM2M API shall be carried out in self-operation methods.


# 6	oneM2M protocols/API overview



## 6.1	Introduction


The present document describes message formats and procedures to communicate with a oneM2M-compliant M2M Platform System.

The present document describes:

Data representation for communication protocol messages.

Normal and exceptional procedure.

Status codes.

Guidelines for drafting APIs.

For wide acceptance by industrial markets, the present document describes structured and non-structured data for oneM2M Protocol using XML Schema Definition (XSD) language [3].

The actual format of data in request and response messages partially depends on the applied protocol binding. Mapping rules between the data formats defined in the present document types and protocol-specific native data formats are specified in the protocol binding specifications oneM2M TS-0008 [22], TS-0009 [23], TS-0010 [24] and TS-0020 [42].

The core data types of XML elements defined in the present document for use in oneM2M protocols shall use the namespace:

http://www.onem2m.org/xml/protocols.

The present document, and any XML or XML Schema Documents produced by oneM2M shall use the prefix m2m: to refer to that namespace.

Specializations of the <flexContainer> resource type (see clause 7.4.37) may employ a different target namespace.

The XSD files referenced in the present document shall serve the following purposes:

Provide an unambiguous definition of XML element names and data types used for:

resource representations;

resource attributes;

Request and Response primitives (including Notification primitive);

parameters used in Request and Response primitives.

Help to identify and avoid multiple definition of equivalent data types with different names.

Provide a testable definition of the value range of data elements (e.g. allowed number range, allowed characters or character patterns, allowed enumeration values).

NOTE 1:	The XML schemas do not fully check the value ranges of all data elements. This particularly applies to XML elements which represent string patterns (see Table 6.3.2-1). For full compliance with the present document, an implementation respects both the schema definition and any additional constraints given in the tables of data types defined in the present document.

Provide a testable definition of the presence of mandatory elements (minOccurs="1") and of cardinality of data elements (e.g. maxOccurs="2") in XML representations of data objects (i.e. resource instantiations and primitive parameters).

NOTE 2:	The XSD files referenced in the present document are intended to validate instantiations of complete resources at the Hosting CSE. When requesting a CRUD operation and receiving the response, the Content primitive parameter however typically includes partial representations of a resource. Implementations compliant with the present document may employ modified versions of the XSD for schema-validation of partial resource representations.

Provide a testable definition of the correct sequence of occurrence of each element of a data object (where correct sequence is required).

Enable the use of development tools that generate executable code for data object processing from the XSD.

Enable the use of XML development tools which allow automatic generation of valid templates for XML and JSON objects, and validation of the compliance of any XML or JSON objects with the XSD.

Parameters and resource representations exchanged in primitives between oneM2M entities shall comply with data formats defined in the present document based on the referred XSD documents. The present document defines procedures for validation of received messages and the error handling in case of reception of non-compliant message content.

NOTE 3:	M2M implementations are required to validate the data received in incoming primitives in accordance with the present document, but the present document does not intend to impose restrictions on implementation of the validation procedures. In particular the validation procedure is not required to use the XSD documents directly.


## 6.2	Addressing



### 6.2.1	Introduction


This clause describes the method of addressing oneM2M entities (e.g. AE or CSE) and oneM2M resources using identifiers described in the oneM2M TS-0001 [6].


### 6.2.2	Summary of oneM2M Identifiers


Table 6.2.2-1 shows the summary of M2M Identifiers defined in oneM2M TS-0001 [6].

Table 6.2.2-1: M2M Identifiers


### 6.2.3	oneM2M Entity Addressing


The oneM2M entities (e.g. AE or CSE) are identified and addressable using M2M Identifiers. Since an M2M Identifier is protocol independent, an IN-CSE shall accommodate address resolution functionality to get actual PoA addresses for communicating with other M2M entities using a specific protocol binding.

The present document assumes each oneM2M entity has the CSE-PoA address of its Registrar CSE in advance.

The CSE-ID shall be assigned by M2M Service Provider. The syntax of a CSE-ID is defined by the following ABNF notation [20]:

CSE-ID =  absolute-CSE-ID / SP-relative-CSE-ID

absolute-CSE-ID = M2M-SP-ID  SP-relative-CSE-ID

M2M-SP-ID = "//" FQDN

SP-relative-CSE-ID = "/" 1*unreserved

unreserved = (ALPHA / DIGIT) *(ALPHA / DIGIT / "-" / "." / "_")

FQDN = LABEL / (FQDN "." LABEL)

LABEL = LC-ALPHA [ *(LC_ALPHANUM / "-" ) LC-ALPHANUM ]

LC-ALPHANUM = %x61-7A / DIGIT

LC-ALPHA = %x61-7A

EXAMPLE 1 Starts:

EXAMPLE: //myoperator.com/cse1

This is an example of an absolute-CSE-ID

"//myoperator.com" is the M2M-SP-ID and "/cse1" is the SP-relative CSE-ID.

EXAMPLE 1 Ends.

The AE-ID is either assigned by the M2M Service Provider (S-type AE-ID Stem), or by the AE's Registrar CSE (C-Type Stem). The syntax of AE-ID in ABNF notation [20] is as follows:

AE-ID = absolute-AE-ID / SP-relative-AE-ID / S-AE-ID-Stem

absolute-AE-ID = M2M-SP-ID SP-relative-AE-ID

SP-relative-AE-ID = (SP-relative-CSE-ID "/" C-AE-ID-Stem ) / ("/" S-AE-ID-Stem )

S-AE-ID-Stem = "S" SP-assigned-AE-ID-Stem

C-AE-ID-Stem = "C" CSE-assigned-AE-ID-Stem

SP-assigned-AE-ID-Stem = 1*unreserved

CSE-assigned-AE-ID-Stem = 1*unreserved

EXAMPLE 2 Starts:

EXAMPLE: //myoperator.com/S563423

This is an example of an absolute-AE-ID that was assigned by the M2M-SP (//myoperator.com).

EXAMPLE: //myoperator.com/cse2/C3532ea3

This is an example of an absolute AE-ID, which registered on the Registrar CSE //myoperator.com/cse2. 'C3532ea3' is the AE-ID-Stem which is assigned by //myoperator.com/cse2.

EXAMPLE: /cse2/C3532ea3

This is the SP-relative version of the absolute AE-ID that is shown above.

EXAMPLE 2 Ends.

All M2M Identifiers are case-sensitive, so for example there could be two distinct CSEs one called //myoperator.com/cse1 and the other one called //myoperator.com/Cse1.

Note that the M2M-SP-ID portion of an identifier contains the FQDN of the service provider. In general Domain Names are case-insensitive, but the FQDN component of an M2M Identifier shall always use lowercase characters as required by the ABNF and as shown in the examples given above.


### 6.2.4	oneM2M Resource Addressing


Authorized oneM2M entities can operate on a oneM2M resource by addressing the resource identifier as the target address (i.e. To parameter) in a request primitive. There are two resource addressing methods:

Structured resource identifier (used in Hierarchical Addressing): the identifier is constructed as a relative path from the <CSEBase> resource via parent resources.

Unstructured resource identifier (used in Non-hierarchical Addressing): the identifier uniquely identifies the resource in the domain of its Hosting CSE.

Virtual resource addressing is specified in clause 6.8.

Furthermore each resource identifier can be expressed in either

CSE-relative format, or

SP-relative format, or

Absolute format

A single attribute of the targeted oneM2M resource shall be addressable adding the sub-address, (targeted-attribute-name) following a "#" character after the resource address. This sub-address representing an attribute name shall be the short name (clause 8.2).

The syntax of the resource identifier in ABNF notion [20] is as follows:

resource-identifier = (structured-resource-identifier / unstructured-resource-identifier) [ "#" targeted-attribute-name ]

structured-resource-identifier = [CSE-ID "/"] first-segment *("/" resource-name)

first-segment = resource-name / "-" / unstructured-CSE-relative-resource-identifier

unstructured-resource-identifier = [CSE-ID "/"] unstructured-CSE-relative-resource-identifier

unstructured-CSE-relative-resource-identifier = 1*unreserved

resource-name = 1*unreserved

If the resource-name is used in the first-segment production rule, it shall be the resourceName of the <CSEBase> resource. The character "-" (dash) can be used in the first-segment as a shortcut for the resourceName of the <CSEBase> resource.

When including resource identifiers into the Content parameter of response primitives (clause 7.5.2), the resource Hosting CSE shall use the CSE-relative format since the Originator knows the Hosting CSE ID.

All resource identifiers are case sensitive, so for example there could be two distinct resources one with identifier cin00856 and the other one with identifier CIN00856.


## 6.3	Common data types



### 6.3.1	Introduction


The following clauses (6.3.2 to 6.3.6) define the data format of resource attributes and parameters used in primitives.

All strings in oneM2M are case sensitive. Any primitive parameter or resource attribute name (or the name of any element contained therein) that has a datatype of xs:string or has a datatype derived from xs:string shall be treated as case-sensitive. In particular:

An AE or CSE shall preserve the case of the characters in any strings that it processes.

Any comparison of strings (for example the comparison made when evaluating a Filter Operation) shall take account of the case of the characters involved.


### 6.3.2	Simple data types incorporated from XML schema


The following "built-in data types" defined in Table 6.3.2-1 are incorporated from XML Schema definition [3].

Note that name space identifier for "http://www.w3.org/2001/XMLSchema" shall be referred to using the prefix xs: in the present document.

Table 6.3.2-1: Data Types incorporated from XML Schema


### 6.3.3	oneM2M simple data types


Table 6.3.3-1 describes oneM2M-specific simple data type definitions. XML Schema data type definitions for these data types can be found in the XSD file called CDT-commonTypes-v3_32_0.xsd.

The types in Table 6.3.3-1 are either:

Atomic data types derived from XML Schema data types by restrictions (other than enumeration) or union.

List data types constructed from other XML Schema or oneM2M-defined atomic data types.

The oneM2M-defined enumeration data types are defined in clause 6.3.4.

Table 6.3.3-1: oneM2M Simple Data Types

The m2m:timestamp datatype uses ISO 8601 [27] Complete Representation using the Basic Format as described here:

The timestamp shall be a string containing Year, Month, Day, Hours, Minutes and Seconds components using the format YYYYMMDDThhmmss as defined in [27]. In this representation the character "T" is to indicate the start of the time of day portion.

All these components shall appear in the string; reduced representations are not permitted.

The Seconds component may optionally contain a decimal fraction. In this case the string shall contain two integer digits, followed by a comma and then one or more fractional digits, up to a maximum of six. For example YYYYMMDDThhmmss,ssssss

The timestamp string shall not contain Timezone information. All timestamps shall be interpreted as being in UTC.

A receiving or Hosting CSE shall accept a timestamp that contains fractional seconds, but it need not act on a timestamp with the level of precision that is implied by its fractional part. For example, it is acceptable for a Hosting CSE to round up an expiration time when interpreting it.

NOTE 1:	Care should be taken when developing an application that compares timestamps. This is because AEs and CSEs are not required to have their clocks synchronized.

NOTE 2:	As the m2m:timestamp is expressed in UTC, an AE has to be aware of the Timezone in which it is operating if it is to be able to relate the timestamp to its local time.


### 6.3.4	oneM2M enumerated data types


6.3.4.1	Introduction

The oneM2M Enumeration Types are defined as extension from "enumeration type" which is defined in XML Schema definition [3]. The oneM2M Enumeration Types are based on xs:integer, and the numeric values are interpreted as specified in clause 6.3.4.2. Table 6.3.4.1-1 shows the example Enumeration Type definition for m2m:enumFooType.

Table 6.3.4.1-1: Example of oneM2M Enumeration Type Definition

The oneM2M Enumeration Type definition shall be implemented as part of 
CDT-enumeration-v3_32_0.xsd. Figure 6.3.4.1-1 shows the example XSD representation of "m2m:enumFooType".

Figure 6.3.4.1-1: Example of XSD version of oneM2M Enumeration Type

6.3.4.2	Enumeration type definitions

6.3.4.2.1	m2m:resourceType

Table 6.3.4.2.1-1: Interpretation of m2m:resourceType

6.3.4.2.2	m2m:cseTypeID

Used for the cseType attribute of the <CSEBase> resource.

Table 6.3.4.2.2-1: Interpretation of m2m:cseTypeID

6.3.4.2.3	m2m:locationSource

Used for the locationSource attribute of the <locationPolicy> resource.

Table 6.3.4.2.3-1: Interpretation of m2m:locationSource

6.3.4.2.4	m2m:stdEventCats

Used for the Event Category parameter in the request primitive and the eventCat attribute of the <delivery> resource and the cmdh policy resource types.

Table 6.3.4.2.4-1: Interpretation of m2m:stdEventCats

6.3.4.2.5	m2m:operation

Used for the Operation parameter in request and the operation attribute of the <request> resource.

Table 6.3.4.2.5-1: Interpretation of m2m:operation

6.3.4.2.6	m2m:responseType

Used for Response Type parameter (as a part of responseTypeInfo, see clause 6.3.5.30) in the request primitive.

Table 6.3.4.2.6-1: Interpretation of m2m:responseType

6.3.4.2.7	m2m:resultContent

Used for Result Content parameter in the request primitive.

Table 6.3.4.2.7-1: Interpretation of m2m:resultContent

6.3.4.2.8	m2m:desIdResType

Used in the metainformation attribute of the <request> resource.

Table 6.3.4.2.8-1: Interpretation of m2m:desIdResType

6.3.4.2.9	m2m:responseStatusCode

The values for this data type are defined in clause 6.6.3 "Definition of Response Status Codes".

Table 6.3.4.2.9-1: Interpretation of m2m:responseStatusCode

6.3.4.2.10	m2m:requestStatus

Used for the requestStatus attribute of the <request> resource.

Table 6.3.4.2.10-1: Interpretation of m2m:requestStatus

6.3.4.2.11	m2m:memberType

Used for the memberType attribute of the <group> resource.

Table 6.3.4.2.11-1: Interpretation of m2m:memberType

6.3.4.2.12	m2m:consistencyStrategy

Used for the consistencyStrategy attribute of the <group> resource.

Table 6.3.4.2.12-1: Interpretation of m2m:consistencyStrategy

6.3.4.2.13	m2m:cmdType

Used for the cmdType attribute of the <mgmtCmd> resource.

Table 6.3.4.2.13-1: Interpretation of m2m:cmdType

6.3.4.2.14	m2m:execModeType

Used for the execModeType attribute of <mgmtCmd> and <execInstance> resources.

Table 6.3.4.2.14-1: Interpretation of m2m:execModeType

6.3.4.2.15	m2m:execStatusType

Used for the execStatusType attribute of the <execInstance> resource.

Table 6.3.4.2.15-1: Interpretation of m2m:execStatusType

6.3.4.2.16	m2m:execResultType

Used for the execResult attribute of the <execInstance> resource.

Table 6.3.4.2.16-1: Interpretation of m2m:execResultType

6.3.4.2.17	m2m:pendingNotification

This is used for the pendingNotification attribute of the <subscription> resource.

Table 6.3.4.2.17-1: Interpretation of m2m:pendingNotification

6.3.4.2.18	m2m:notificationContentType

Table 6.3.4.2.18-1: Interpretation of m2m:notificationContentType

6.3.4.2.19	m2m:notificationEventType

Used for eventNotificationCriteria conditions and in the notificationEvent element.

Table 6.3.4.2.19-1: Interpretation of m2m:notificationEventType

6.3.4.2.20	m2m:status

This is used in [software], [firmware] resources.

Table 6.3.4.2.20-1: Interpretation of m2m:status

6.3.4.2.21	m2m:batteryStatus

This is used in the [battery] resource.

Table 6.3.4.2.21-1: Interpretation of m2m:batteryStatus

6.3.4.2.22	m2m:mgmtDefinition

This is used in the <mgmtObj> resource.

Table 6.3.4.2.22-1: Interpretation of m2m:mgmtDefinition

6.3.4.2.23	m2m:logTypeId

Used for the logTypeId attribute of the [eventLog] Management Resource.

Table 6.3.4.2.23-1: Interpretation of m2m:logTypeId

6.3.4.2.24	m2m:logStatus

Used for the logStatus attribute of the [eventLog] Management Resource.

Table 6.3.4.2.24-1: Interpretation of m2m:logStatus

6.3.4.2.25	m2m:eventType

Used for the eventType attribute of the <eventConfig> resource.

Table 6.3.4.2.25-1: Interpretation of m2m:eventType

6.3.4.2.26	m2m:statsRuleStatusType

Used for the statsRuleStatusType attribute of the <statsCollect> resource.

Table 6.3.4.2.26-1: Interpretation of m2m:statsRuleStatusType

6.3.4.2.27	m2m:statModelType

Used for the statModelType attribute of the <statsCollect> resource.

Table 6.3.4.2.27-1: Interpretation of m2m:statModelType

6.3.4.2.28	m2m:encodingType

Used to describe the encoding type that applies to the content attribute of the <contentInstance> resource.

Table 6.3.4.2.28-1: Interpretation of m2m:encodingType

6.3.4.2.29	m2m:accessControlOperations

Used in <accessControlPolicy>.

Table 6.3.4.2.29-1: Interpretation of m2m:accessControlOperations

6.3.4.2.30	Void

6.3.4.2.31	m2m:filterUsage

Used in m2m:filterCriteria.

Table 6.3.4.2.31-1: Interpretation of m2m:filterUsage

6.3.4.2.32	m2m:notificationTargetPolicyAction

Table 6.3.4.2.32-1: Interpretation of m2m:notificationTargetPolicyAction

6.3.4.2.33	m2m:logicalOperator

Table 6.3.4.2.33-1: Interpretation of m2m:logicalOperator

6.3.4.2.34	m2m:filterOperation

Used in m2m:filterCriteria.

Table 6.3.4.2.34-1: Interpretation of m2m:filterOperation

6.3.4.2.35	m2m:securityInfoType

Used in m2m:securityInfo.

Table 6.3.4.2.35-1: Interpretation of m2m:securityInfoType

6.3.4.2.36	m2m:allJoynDirection

Used for the direction attribute of the [allJoynApp] resource.

Table 6.3.4.2.36-1: Interpretation of m2m:allJoynDirection

6.3.4.2.37	m2m:contentFilterSyntax

Used for the contentFilterSyntax element in the Filter Criteria primitive parameter.

Table 6.3.4.2.37-1: Interpretation of m2m:contentFilterSyntax

6.3.4.2.38	m2m:contentSecurity

Used in m2m:contentInfo.

Table 6.3.4.2.38-1: Interpretation of m2m:contentSecurity

6.3.4.2.39	m2m:suid

Used in m2m:e2eSecInfo and other security features in oneM2M TS-0003 [7].

NOTE:	This enumeration is the concatenation of two identifiers. The first identifier identifies the type of credential (such as pre-provisioned symmetric key, symmetric key provisioned via a RSPF, or symmetric key distributed via MAF and certificate) and the intended scope within which the credential is to be used (such as shared with an MEF, shared with an MAF, use in SAEF, use in ESPrim, use in authentication encryption in ESData, or use in signature only in ESData).

Table 6.3.4.2.39-1: Interpretation of m2m:suid

6.3.4.2.40	m2m:esprimKeyGenAlgID

Used in m2m:receiverESPrimRandObject and m2m:originatorESPrimRandObject.

Table 6.3.4.2.40-1: Interpretation of m2m:esprimKeyGenAlgID

6.3.4.2.41	m2m:esprimProtocolAndAlgID

Used in m2m:receiveESPrimRandObject and m2m:originatorESPrimRandObject.

NOTE:	This enumeration is the concatenation of two identifiers. The most significant numeral identifies an object security technology (that is, a protocol) such as JSON Web Encryption (JWE) Compact Representation [i.8]. Further protocols can be supported in the future. The least significant numeral identifies an Authenticated Encryption option for that object security technology.

Table 6.3.4.2.41-1: Interpretation of m2m:esprimProtocolAndAlgID

6.3.4.2.42	Void

6.3.4.2.43	m2m:stationaryIndication

Used for the stationaryIndication element of m2m:activityPattern.

Table 6.3.4.2.43-1: Interpretation of m2m:stationaryIndication

6.3.4.2.44	m2m:contentStatus

Used for the Content Status response primitive parameter.

Table 6.3.4.2.44-1: Interpretation of m2m:contentStatus

6.3.4.2.45	m2m:networkAction

Used for the networkAction element in the m2m:backOffParameters.

Table 6.3.4.2.45-1: Interpretation of m2m:networkAction

6.3.4.2.46	m2m:locationInformationType

Used for the locationInformationType attribute of the <locationPolicy> resource.

Table 6.3.4.2.46-1: Interpretation of m2m:locationInformationType

6.3.4.2.47	m2m:geofenceEventCriteria

Used for the geofenceEventCriteria attribute of the <locationPolicy> resource.

Table 6.3.4.2.47-1: Interpretation of m2m:geofenceEventCriteria

6.3.4.2.48	m2m:semanticFormat

Used in the <semanticDescriptor> and <ontology> resources.

Table 6.3.4.2.48-1: Interpretation of m2m:semanticFormat

6.3.4.2.49	m2m:triggerPurpose

Used in defining trigger purpose in a trigger payload.

Table 6.3.4.2.49-1: Interpretation of m2m:triggerPurpose

6.3.4.2.50	Void

6.3.4.2.51	m2m:authorizationDecision

Used for the decision attribute of the <authorizationDecision> resource.

Table 6.3.4.2.51-1: Interpretation of m2m:authorizationDecision

6.3.4.2.52	m2m:authorizationStatus

Used for the status attribute of the <authorizationDecision> resource.

Table 6.3.4.2.52-1: Interpretation of m2m:authorizationStatus

6.3.4.2.53	m2m:acpCombiningAlgorithm

Used for the combiningAlgorithm attribute of the <authorizationPolicy> resource.

Table 6.3.4.2.53-1: Interpretation of m2m:acpCombiningAlgorithm

6.3.4.2.54	m2m:mashupMemberStoreType

Used for memberStoreType attribute of <semanticMashupInstance> resource.

Table 6.3.4.2.54-1: Interpretation of m2m:mashupMemberStoreType

6.3.4.2.55	m2m:mashupResultGenType

Used for resultGenType attribute of <semanticMashupInstance> resource.

Table 6.3.4.2.55-1: Interpretation of m2m:mashupResultGenType

6.3.4.2.56	m2m:locationUpdateEventCriteria

Used for locationUpdateEventCriteria attribute of <locationPolicy> resource.

Table 6.3.4.2.56-1: Interpretation of m2m:locationUpdateEventCriteria

6.3.4.2.57	m2m:AERegistrationStatus

Used for registrationStatus attribute in <AE> resource.

Table 6.3.4.2.57-1: Interpretation of m2m:AERegistrationStatus

6.3.4.2.58	m2m:multicastCapability

Used for the multicastCapability attribute of the <remoteCSE> resource and the multicastType element in the Multicast Group Information data object.

Table 6.3.4.2.58-1: Interpretation of m2m:multicastCapability

6.3.4.2.59	m2m:sessionState

Used for the sessionState attribute of the <multimediaSession> resource.

Table 6.3.4.2.59-1: Interpretation of m2m:sessionState

6.3.4.2.60	m2m:triggerStatus

Used for the triggerStatus attribute of the <triggerRequest> resource.

Table 6.3.4.2.60-1: Interpretation of m2m:triggerStatus

6.3.4.2.61	m2m:timeWindowType

Used for the timeWindowType attribute of the <crossResourceSubscription> resource.

Table 6.3.4.2.61-1: Interpretation of m2m:timeWindowType

6.3.4.2.62	m2m:transferSelectionGuidance

Used for the transferSelectionGuidance attribute of the <backgroundDataTransfer> resource. Specified by an originator to provide guidance, together with local policies, on how to choose a Background Data Transfer policy if multiple policies are provided to the IN-CSE by the SCEF.

Table 6.3.4.2.62-1: Interpretation of m2m:transferSelectionGuidance

6.3.4.2.63	m2m:transactionMode

This is used for the transactionMode attribute of the <transactionMgmt> resource to define whether the Hosting CSE or the creator of a <transactionMgmt> resource is responsible for controlling the execution of the transaction.

Table 6.3.4.2.63-1: Interpretation of m2m:transactionMode

6.3.4.2.64	m2m:transactionControl

This is used for the transactionControl attribute of the <transactionMgmt> and <transaction> resources to control the state of a transaction.

Table 6.3.4.2.64-1: Interpretation of m2m:transactionControl

6.3.4.2.65	m2m:transactionState

This is used for the transactionState attribute of the <transactionMgmt> and <transaction> resources to monitor the state of a transaction.

Table 6.3.4.2.65-1: Interpretation of m2m:transactionState

6.3.4.2.66	m2m:transactionLockType

This is used for the transactionLockType attribute of the <transactionMgmt> and <transaction> resources to configure the type of lock that is required on the targeted resource in order to perform the transaction.

Table 6.3.4.2.66-1: Interpretation of m2m:transactionLockType

6.3.4.2.67	m2m:transactionMgmtHandling

This is used for the transactionMgmtHandling attribute of the <transactionMgmt> resource to configure whether to persist or delete the <transactionMgmt> resource after its completion.

Table 6.3.4.2.67-1: Interpretation of m2m:transactionMgmtHandling


### 6.3.5	Complex data types


6.3.5.1	Introduction

The present clause defines structured information for specific use in oneM2M protocol. These types are defined to be xs:sequence complex types, unless specified otherwise. XML Schema data type definitions for these data types can be found in the XSD file called CDT-commonTypes-v3_32_0.xsd, or in their own schema definition files. In addition, each oneM2M resource has a corresponding complex data type. These are described in clause 6.5.

6.3.5.2	m2m:deliveryMetaData

Used for the deliveryMetaData attribute of the <delivery> resource.

Table 6.3.5.2-1: Type Definition of m2m:deliveryMetadata

6.3.5.3	m2m:aggregatedRequest

Used for the aggregatedRequest attribute of the <delivery> resource.

Table 6.3.5.3-1: Type Definition of m2m:aggregatedRequest

6.3.5.4	m2m:metaInformation

Used for the metaInformation attribute of the <request> resource, and in the m2m:aggregatedRequest data type.

Table 6.3.5.4-1: Type Definition of m2m:metaInformation

6.3.5.5	m2m:primitiveContent

Used for the Content parameter in request/response primitives and the content attribute of the <request> resource.

See clauses 7.2.1.1 and 7.2.1.2.

6.3.5.6	m2m:batchNotify

Used for the batchNotify attribute of the <subscription> resource and the notifyAggregation attribute of the <group> resource.

Table 6.3.5.6-1: Type Definition of m2m:batchNotify

6.3.5.7	m2m:eventNotificationCriteria

Used for the eventNotificationCriteria attribute of the <subscription> resource.

Table 6.3.5.7-1: Type Definition of m2m:eventNotificationCriteria

6.3.5.8	m2m:filterCriteria

Used indirectly in the <request> resource and for the Filter Criteria parameter in a request.

Table 6.3.5.8-1: Type Definition of m2m:filterCriteria

6.3.5.9	m2m:attribute

Used in m2m:filterCriteria.

Table 6.3.5.9-1: Type Definition of m2m:attribute

6.3.5.10	Void

6.3.5.11	m2m:scheduleEntries

Table 6.3.5.11-1: Type Definition of m2m:scheduleEntries

6.3.5.12	m2m:aggregatedNotification

Used in the Notification Data Object.

Table 6.3.5.12-1: Type Definition of m2m:aggregatedNotification

6.3.5.13	m2m:notification

Table 6.3.5.13-1: Type Definition of m2m:notification

6.3.5.14	m2m:actionStatus

Table 6.3.5.14-1: Type Definition of m2m:actionStatus

6.3.5.15	m2m:anyArgType

Table 6.3.5.15-1: Type Definition of m2m:anyArgType

6.3.5.16	m2m:resetArgsType

Table 6.3.5.16-1: Type Definition of m2m:resetArgsType

6.3.5.17	m2m:rebootArgsType

Table 6.3.5.17-1: Type Definition of m2m:rebootArgsType

6.3.5.18	m2m:uploadArgsType

Table 6.3.5.18-1: Type Definition of m2m:uploadArgsType

6.3.5.19	m2m:downloadArgsType

Table 6.3.5.19-1: Type Definition of m2m:downloadArgsType

6.3.5.20	m2m:softwareInstallArgsType

Table 6.3.5.20-1: Type Definition of m2m:softwareInstallArgsType

6.3.5.21	m2m:softwareUpdateArgsType

Table 6.3.5.21-1: Type Definition of m2m:softwareUpdateArgsType

6.3.5.22	m2m:softwareUninstallArgsType

Table 6.3.5.22-1: Type Definition of m2m:softwareUninstallArgsType

6.3.5.23	m2m:execReqArgsListType

Table 6.3.5.23-1: Type Definition of m2m:execReqArgsListType

This type is an xs:choice. It shall contain elements from no more than one row listed in Table 6.3.5.23-1.

6.3.5.24	m2m:mgmtLinkRef

Table 6.3.5.24-1: Type Definition of m2m:mgmtLinkRef

In Table 6.3.5.24-1, names of XML schema attributes are prefixed with a "@" character to differentiate these from Resource attribute names. The "@" character is not part of the actual attribute name.

6.3.5.25	m2m:resourceWrapper

This data type is used for the m2m:resource Global Element of the Content primitive parameter as defined in clause 7.5.2. It allows insertion of Global Elements prefixed with the m2m: namespace identifier, or of Global Elements defined in another namespace.

Table 6.3.5.25-1: Type Definition of m2m:resourceWrapper

6.3.5.26	m2m:setOfAcrs

Table 6.3.5.26-1: Type Definition of m2m:setOfAcrs

6.3.5.27	m2m:accessControlRule

Table 6.3.5.27-1: Type Definition of m2m:accessControlRule

The accessControlContexts/accessControlIpAddresses element may include either the ipv4Addresses element, ipv6Addresses element, or both elements.

Each individual IPv4 address of data type m2m:ipv4 in the list of IPv4 addresses is represented in dotted-decimal notation with optional Classless Inter-Domain Routing (CIDR) suffix in accordance with IETF RFC 4632 [29]. Each individual IPv6 address of data type m2m:ipv6 in the list of IPv6 addresses is represented in colon separated groups of hexadecimal digits with optional network prefix in accordance with IETF RFC 5952 [30]. Example IPv4 and IPv6 addresses which comply with data types m2m:ipv4 and m2m:ipv6, respectively, are given in Table 6.3.2-1. If the accessControlAuthenticationFlag element is not present, then the value is assumed to be false.

6.3.5.28	m2m:locationRegion

Table 6.3.5.28-1: Type Definition of m2m:locationRegion

This is an xs:choice. A locationRegion shall contain either:

A countryCode element, in which case circRegion shall not appear, or

A circRegion element, in which case countryCode shall not appear.

6.3.5.29	m2m:childResourceRef

Table 6.3.5.29-1: Type Definition of m2m:childResourceRef

In Table 6.3.5.29-1, names of XML schema attributes are prefixed with a "@" character to differentiate these from Resource attribute names. The "@" character is not part of the actual attribute name.

6.3.5.30	m2m:responseTypeInfo

Table 6.3.5.30-1: Type Definition of m2m:responseTypeInfo

6.3.5.31	m2m:rateLimit

Used in <subscription>.

Table 6.3.5.31-1: Type Definition of m2m:rateLimit

6.3.5.32	m2m:operationResult

Used for the operationResult attribute of the <request> resource.

NOTE:	This data type corresponds to the sequence of elements in the response primitive defined in clause 6.4.2.

Table 6.3.5.32-1: Type Definition of m2m:operationResult

6.3.5.33	m2m:aggregatedResponse

Used when aggregating responses by a group.

Table 6.3.5.33-1: Type Definition of m2m:aggregatedResponse

6.3.5.34	m2m:mgmtResource

Used This data type is used as base type of all <mgmtObj> specializations specified in Annex D. It includes the attributes commonly used by all <mgmtObj> resource type specializations.

It consists of the common attributes included in m2m:announceableResource as defined Table 6.3.6-2 and the additional common attributes shared by all <mgmtObj> specializations shown in Table 6.3.5.34-1.

Table 6.3.5.34-1: Type Definition of m2m:mgmtResource

NOTE:	objectAttribute is defined in the specializations of mgmtObj. See Annex D.

6.3.5.35	m2m:announcedMgmtResource

This data type is used as base type of the announced variants of announceable <mgmtObj> specializations specified in Annex D. It includes the attributes commonly used by all announced <mgmtObj> resource type specializations. Note that some specializations of the <mgmtObj> resource are announceable while others are not announceable.

It consists of the common attributes included in m2m:announcedResource as defined Table 6.3.6-2 and the additional common attributes shared by all announced <mgmtObj> specializations shown in Table 6.3.5.35-1.

Table 6.3.5.35-1: Type Definition of m2m:announcedMgmtResource

NOTE:	objectAttribute is defined in the specializations of mgmtObj. See Annex D.

6.3.5.36	m2m:contentRef

A complex type that represents the content reference with an associated reference name and URI of the referenced resource.

Table 6.3.5.36-1: Type Definition of m2m:contentRef

6.3.5.37	m2m:deletionContexts

Table 6.3.5.37-1: Type Definition of m2m:deletionContexts

6.3.5.38	m2m:flexContainerResource

This data type is used as base type of all <flexContainer> specializations listed in clause 9.6.1.2.2 of oneM2M TS-0001 [6]. It includes the attributes commonly used by all <flexContainer> resource type specializations.

It consists of the common attributes shown in Table 7.4.37.1-1 and the resource specific attributes shared by all <flexContainer> specializations shown in Table 7.4.37.1-2.

Table 6.3.5.38-1: Type Definition of m2m:flexContainerResource

6.3.5.39	m2m:announcedFlexContainerResource

This data type is used as base type of the announced variants of announceable <flexContainer> specializations listed in clause 9.6.1.2.2 of oneM2M TS-0001 [6]. It includes the attributes commonly used by all announced <flexContainer> resource type specializations. Note that some specializations of the <flexContainer> resource are announceable while others are not announceable.

It consists of the common attributes shown in Table 7.4.37.1-1 and the resource specific attributes shared by all announced <flexContainer> specializations shown in Table 7.4.37.1-2.

Table 6.3.5.39-1: Type Definition of m2m:announcedFlexContainerResource

6.3.5.40	m2m:missingData

Used for the eventNotificationCriteria attribute of the <subscription> resource. The condition only applies to subscribed-to resources of type <timeSeries>. If this condition is set in a <subscription> resource, it enables the AE to keep track of the number of missing data points (i.e. the "number" of the missingData) and the corresponding time-stamps over a predefined but renewable duration (i.e. the "duration" of the missingData). See clause 7.5.1.2.9.

Table 6.3.5.40-1: Type Definition of m2m:missingData

6.3.5.41	m2m:tokenPermission

Used in m2m:tokenPermissions.

Table 6.3.5.41-1: Type Definition of m2m:tokenPermission

6.3.5.42	m2m:tokenClaimSet

This data type defines how to represent the claim set of oneM2M JSON Web Tokens (JWT) required for generating secured tokens (i.e. signed or encrypted representations of JWTs) as defined in clause 7.3.2.6 of oneM2M TS-0003 [7]. Usage of this datatype is specified in oneM2M TS-0003 [7].

Table 6.3.5.42-1: Type Definition of m2m:tokenClaimSet

6.3.5.43	m2m:dynAuthLocalTokenIdAssignments

Used for the Assigned Token Identifiers parameter of a response primitive.

Table 6.3.5.43-1: Type Definition of m2m:dynAuthLocalTokenIdAssignments

6.3.5.44	m2m:dynAuthTokenSummary

Used for the Token Summary provided by a Dynamic Authorization Server to an Originator.

Table 6.3.5.44-1: Type Definition of m2m:dynAuthTokenSummary

6.3.5.45	m2m:dynAuthTokenReqInfo

Used for the Token Summary provided by a Dynamic Authorization Server to an Originator.

Table 6.3.5.45-1: Type Definition of m2m:dynAuthTokenReqInfo

6.3.5.46	m2m:dynAuthDasRequest

Used in m2m:securityInfo.

Table 6.3.5.46-1: Type Definition of m2m:dynAuthDasRequest

6.3.5.47	m2m:dynAuthDasResponse

Used in m2m:securityInfo.

Table 6.3.5.47-1: Type Definition of m2m:dynAuthDasResponse

6.3.5.48	m2m:securityInfo

Used for the Global Element m2m:securityInfo included into the Content primitive parameter.

Table 6.3.5.48-1: Type Definition of m2m:securityInfo

6.3.5.49	m2m:listOfChildResourceRef

Table 6.3.5.49-1: Type Definition of m2m:listOfChildResourceRef

6.3.5.50	m2m:originatorESPrimRandObject

Used for the originatorESPrimRandObject parameter in End-to-End Security of Primitives.

Table 6.3.5.50-1: Type Definition of m2m:originatorESPrimRandObject

6.3.5.51	m2m:receiverESPrimRandObject

Used in m2m:securityInfo.

Table 6.3.5.51-1: Type Definition of m2m:receiverESPrimRandObject

6.3.5.52	m2m:e2eSecInfo

Used for the e2eSecInfo attribute of the <CSEBase>, <AE> and <remoteCSE> resources.

Table 6.3.5.52-1: Type Definition of m2m:e2eSecInfo

6.3.5.53	m2m:tokenPermissions

Used for the permissions attribute of the <token> resource and for the permissions element in m2m:tokenClaimSet.

Table 6.3.5.53-1: Type Definition of m2m:tokenPermissions

6.3.5.54	m2m:backOffParameters

Used for the backOffParameters attribute of the <cmdhNwAccessRule> resource.

Table 6.3.5.54-1: Type Definition of m2m:backOffParameters

6.3.5.55	m2m:listOfDataLinks

Table 6.3.5.55-1: Type Definition of m2m:listOfDataLinks

6.3.5.56	m2m:dataLink

Table 6.3.5.56-1: Type Definition of m2m:dataLink

6.3.5.57	m2m:operationMonitor

Table 6.3.5.57-1: Type Definition of m2m:operationMonitor

6.3.5.58	m2m:dynAuthRelMapRequest

Used in m2m:securityInfo.

Table 6.3.5.58-1: Type Definition of m2m:dynAuthRelMapRequest

6.3.5.59	m2m:dynAuthRelMapResponse

Used in m2m:securityInfo.

Table 6.3.5.59-1: Type Definition of m2m:dynAuthRelMapResponse

6.3.5.60	m2m:ipAddress

Used for the originatorIP attribute of the <authorizationDecision> resource.

Table 6.3.5.60-1: Type Definition of m2m:ipAddress

6.3.5.61	m2m:setOfPermissions

Used for the policies attribute of the <authorizationPolicy> resource.

Table 6.3.5.61-1: Type Definition of m2m:setOfPermissions

6.3.5.62	m2m:representation

Used for the representation element in the notificationEvent element of a notification. Table 6.3.5.62-1 defines what shall be included in the representation element depending on the value of the notificationContentType of the <subscription> resource which triggered the notification.

Table 6.3.5.62-1: Elements used for representation element

The XML representation element shall include a root element which is associated with an XSD Global Element. The root element shall be prefixed with a namespace prefix identifier (e.g. m2m:) specified in the associated XSD which defines the respective Global Element. The representation element allows the inclusion of namespaces other than m2m.

6.3.5.63	m2m:sessionDescriptions

Used for the offeredSessionDescriptions and acceptedSessionDescriptions attributes in the <multimediaSession> resource.

Table 6.3.5.63-1: Type Definition of m2m:sessionDescriptions

6.3.5.64	m2m:activityPatternElements

Used for the activityPatternElements attribute of the <AE> and <remoteCSE> resources.

Table 6.3.5.64-1: Type Definition of m2m:activityPatternElements

6.3.5.65	m2m:activityPattern

Used for describing the anticipated availability of an AE or CSE for communications such as timing pattern, mobility status and expected data size.

Table 6.3.5.65-1: Type Definition of m2m:activityPattern

6.3.5.66	m2m:eventNotificationCriteriaSet

Used for eventNotificationCriteriaSet attribute in <crossResourceSubscription> resource.

Table 6.3.5.66-1: Type Definition of m2m:eventNotificationCriteriaSet

m2m:specializationType

Table 6.3.5.67-1: Type Definition of m2m: specializationType

This is an xs:choice. A specializationType shall contain either:

a containerDefinition element, in which case mgmtDefinition shall not appear, or

a mgmtDefinition element, in which case containerDefinition shall not appear.

m2m:mashupMembers

Used for the mashupMember attribute of the <semanticMashupInstance> resource.

Table 6.3.5.68-1: Type Definition of m2m:mashupMembers

6.3.5.69	m2m:timeSeriesNotificationType

This defines the notification data object to be included in the representation element in the notificationEvent element of a notification for notifications generated for timeSeries. Table 6.3.5.69-1 defines what shall be included in the timeSeriesNotification element:

Table 6.3.5.69-1: Elements of the timeSeriesNotificationType


### 6.3.6	Universal and Common attributes


oneM2M TS-0001 [6] defines a number of Universal Attributes (which appear in all resources) and Common Attributes (which appear in more than one resource and have the same meaning whenever they do appear). Their types and values are described in Table 6.3.6-1.

If a Resource is represented as an XML document then the resource attributes (if present) appear in the order listed in this table. They appear before any resource-specific attributes.

Table 6.3.6-1: Universal and Common Attributes

Table 6.3.6-2 describes some complex types that group together the universal and common attributes, to be used by Resource Type definitions. Note that stateTag and creator only appear in a limited number of resource types, and therefore are not included in these definitions, instead they are declared in the corresponding XSD files of the resources that support them.

Table 6.3.6-2: Complex Data Types declaring groups of resource common attributes

NOTE:	In Table 6.3.6-2, names of XML schema attributes are prefixed with a "@" character to differentiate these from Resource attribute names. The "@" character is not part of the actual attribute name.


## 6.4	Message parameter data types



### 6.4.1	Request primitive parameter data types


The data types of request primitive parameters are specified in this clause.

Detailed request primitive parameter descriptions and usage can be found in clause 8.1.2 of the oneM2M TS-0001 [6]. Further details on the representation of request primitives are specified in clauses 7.2.1.1 and 8 of the present document.

Table 6.4.1-1 shows the structure of the request primitive. This is defined as the m2m:requestPrimitive element in the XSD file CDT-requestPrimitive-v3_32_0.xsd.

Table 6.4.1-1: Data Types for Request primitive parameters


### 6.4.2	Response primitive parameter data types


The data types of response primitive parameters are specified in this clause.

Detailed response message parameter descriptions and usage can be found in clause 8.1.3 of oneM2M TS-0001 [6]. Further details on the representation of response primitives can be found in clauses 7.2.1.2 and 8 of the present document.

Table 6.4.2-1 shows the structure of the response primitive. This is defined as the m2m:responsePrimitive element in the XSD file CDT-responsePrimitive-v3_32_0.xsd.

Table 6.4.2-1: Data Types for Response primitive parameters


## 6.5	Resource data types



### 6.5.1	Description


Each oneM2M Resource Data Type is defined using XML Schema (XSD), and supplied as a separate XSD document. This XML Schema defines the attributes of the Resource in accordance with oneM2M TS-0001 [6]. It represents an entire resource. In other words if and only if a requestor retrieves an entire resource in XML format, the XML that is returned shall be valid with respect to the schema for that resource. Note that the payload of a Create or Update request primitive does not necessarily have to be valid according to the schema, as this payload is not required to contain values for all the resource attributes. For example, a resource might contain mandatory read-only attributes which do not appear in a Create or Update request.

Each Resource Type, along with its Announced variant (if there is one) is defined in a separate XSD file. The name of that file should be prefixed with "CDT-" and followed by the resource type name and version of the present document.

The individual Resource Types inherit from a set of base resource types. These definitions, which can be found in the file CDT-commonTypes-v3_32_0.xsd, contain definitions for the common and universal attributes, and establish an inheritance hierarchy shown in Figure 6.5.1-1.

Figure 6.5.1-1: Resource Types


### 6.5.2	resource


6.5.2.1	Description

This XSD type definition includes the six universal attributes that are present in all oneM2M resource type definitions. It forms the root of the resource inheritance hierarchy.

6.5.2.2	Reference

See Table 6.3.6-2.

6.5.2.3	Usage

This type is used indirectly by all resource types. It is used directly only by the <CSEBase> resource type.


### 6.5.3	regularResource


6.5.3.1	Description

This type definition includes the universal and common attributes used by the non-announceable oneM2M resources.

6.5.3.2	Reference

See Table 6.3.6-2.

6.5.3.3	Usage

This type is used by the following resource types:

<delivery>, <eventConfig>, <execInstance>, <m2mServiceSubscriptionProfile>, <mgmtCommand>, <request>, <serviceSubscribedNode>, <statsCollect>, <statsConfig>, <subscription>, <serviceSubscribedAppRule>, <notificationTargetMgmtPolicyRef>, <notificationTargetPolicy>, <policyDeletionRules>, <dynamicAuthorizationConsultation>, <role>, <token>, <authorizationDecision>, <authorizationPolicy> <authorizationInformation>, <AEContactList>, <AEContactListPerCSE>, <localMulticastGroup>, <triggerRequest>, <crossResourceSubscription>, <backgroundDataTransfer>, <transactionMgmt>, <transaction>.


### 6.5.4	announceableResource


6.5.4.1	Description

This type definition includes the universal and common attributes used by oneM2M resource types that are capable of being announced. In addition to the attributes of a regularResource, it includes (as optional) the common attributes that are used by the announcement mechanism.

6.5.4.2	Reference

See Table 6.3.6-2.

6.5.4.3	Usage

This type is used by the following resource types:

<AE>, <container>, <group>, <locationPolicy>, <node>, <remoteCSE>, <semanticDescriptor>, <timeSeries>, <ontologyRepository>, <ontology>, <semanticMashupJobProfile>, <semanticMashupInstance>, <semanticMashupResult>, <multimediaSession>, <schedule>.

It is also used by the specializations of <mgmtObj> and of <flexContainer>.


### 6.5.5	announcedResource


6.5.5.1	Description

This type definition includes the universal and common attributes used by a resource that is announcing an announceable resource. In addition to the attributes of a regularResource, it includes (as optional) the link common attribute.

6.5.5.2	Reference

See Table 6.3.6-2.

6.5.5.3	Usage

This type is used by the following resource types:

<AEAnnc>, <containerAnnc>,<CSEBaseAnnc>, <groupAnnc>, <locationPolicyAnnc>, <nodeAnnc>, <remoteCSEAnnc>, <semanticDescriptorAnnc>, <timeSeriesAnnc>, <ontologyRepositoryAnnc>, <ontologyAnnc>, <semanticMashupJobProfileAnnc>, <semanticMashupInstanceAnnc>, <semanticMashupResultAnne>, <multimediaSessionAnnc>,<scheduleAnnc>.

It is also used by the xxxAnnc variants of the <mgmtObj> specializations and the xxxAnnc variants of the <flexContainer> specializations.


### 6.5.6	announceableSubordinateResource


6.5.6.1	Description

This type definition includes the common attributes used by resource types that are subordinate children of other resource types. It excludes attributes like accessControlPolicyIDs, as this attribute is defined for such resources.

6.5.6.2	Reference

See Table 6.3.6-2.

6.5.6.3	Usage

This type is used by the following resource types:

<accessControlPolicy>, <contentInstance>, <timeSeriesInstance>.

It is also used by the xxxAnnc variants of the <mgmtObj> specializations.


### 6.5.7	announcedSubordinateResource


6.5.7.1	Description

This type definition includes the common attributes used by the Announced variants of the resource types that are subordinate children of other resource types.

6.5.7.2	Reference

See Table 6.3.6-2.

6.5.7.3	Usage

This type is used by the following resource types:

<accessControlPolicyAnnc>, <contentInstanceAnnc>, <timeSeriesInstanceAnnc>.


### 6.5.8	subordinateResource


6.5.8.1	Description

This type definition includes the universal and common attributes used by the non-announceable M2M resources except the accessControlPolicyIDs attribute.

6.5.8.2	Reference

See Table 6.3.6-2.

6.5.8.3	Usage

This type is used by the following resource types:

<pollingChannel>.


## 6.6	Response status codes



### 6.6.1	Introduction


The present clause specifies the assignment of oneM2M Response Status Code (RSC) values, which are returned in the Response Status Code parameter of Response primitive.

The RSC may be delivered as oneM2M defined structured data, or the mapped native status code for transport protocol binding (e.g. HTTP, CoAP, MQTT).


### 6.6.2	RSC framework overview


The RSCs are categorized as one of 6 classes:

Table 6.6.2-1: Definition of Response Status Code class


### 6.6.3	Definition of Response Status Codes


6.6.3.1	Overview

The tables in the following clauses specify the RSCs for oneM2M releases. Each RSC includes: a response status represented as numeric code. The supplemental information may be returned when it is needed.

6.6.3.2	Informational response class

Table 6.6.3.2-1 specifies the RSCs for acknowledgement responses for each release.

Table 6.6.3.2-1: Informational response class

6.6.3.3	Successful response class

Table 6.6.3.3-1 specifies the RSCs for successful responses.

Table 6.6.3.3-1: RSCs for successful response class

6.6.3.4	Redirection response class

In the present document, no values in this response class are defined.

Table 6.6.3.4-1: RSCs for redirection response class

6.6.3.5	Originator error response class

Table 6.6.3.5-1 specifies the RSCs for Originator error responses.

41xx codes are oneM2M specific.

Table 6.6.3.5-1: RSCs for Originator error response class

6.6.3.6	Receiver error response class

Table 6.6.3.6-1 specifies the RSCs for Receiver error responses.

51xx codes are oneM2M specific, which are used in generic procedures.

52xx codes are oneM2M specific, which are used in resource specific procedures.

Table 6.6.3.6-1: RSCs for Receiver error response class

6.6.3.7	Network system error response class

Table 6.6.3.7-1 specifies the RSCs for when the external system reported errors over Mcn reference point.

Table 6.6.3.7-1: RSCs for Network system error response class


## 6.7	oneM2M specific MIME media types


The present clause defines oneM2M specific MIME media types which may be used by protocol bindings.

The oneM2M specific MIME media types are defined under the vendor tree of the "application" media type which is prefixed with "application/vnd.onem2m-".

Table 6.7-1: oneM2M specific MIME media types


## 6.8	Virtual Resources


A virtual resource is used to trigger processing and/or retrieve results, but does not have a permanent representation in a CSE. Table 6.8-1 lists the Virtual Resources.

Table 6.8-1: Virtual Resources

Each resource instance listed in "Parent Resource" column of Table 6.8-1 has one virtual resource child of each type listed against it in the table. These child resource instances have fixed resourceNames, as shown in the second column.

A virtual resource shall be addressed using the hierarchical addressing method formed by taking the structured or unstructured resource identifier of the parent resource and appending a "/" followed by the resourceName of the virtual resource.


# 7	oneM2M procedures



## 7.1	Introduction


The following clauses (7.2 to 7.6) describe prerequisites such as primitive format and procedure outlines with three generic scenarios that are Originator, Receiver, and Resource Handling in accordance with CRUD+N operations. In addition, for specific resource types they provide common or resource-specific attributes, data type definitions for the resource-specific attributes, and child resources. They also explain the resource-specific procedures on CRUD+N operations to communicate with oneM2M compliant M2M Platform Systems by oneM2M protocols and APIs as follows:

Primitive formats and generic procedures

Common operations

Resource type-specific definitions and procedures

Notification definition and procedures


## 7.2	Primitive format and generic procedure



### 7.2.1	Primitive format


7.2.1.1	Request primitive format

Table 7.2.1.1-1 summarizes the primitive parameters of the Request primitive, indicating their presence depending on the C, R, U, D or N operations. "M" indicates mandatory, "O" indicates optional, "NP" indicates not present.

Refer to clause 8.1.2 of the oneM2M TS-0001 [6] for additional information on the request primitive parameters.

Table 7.2.1.1-1: Request Primitive Parameters

The Content parameter in a Request shall contain one of the following:

A partial Resource. This applies to Create and Update request primitives. In the case of Create request the Content parameter shall contain a single root element whose name is the name of the Resource and whose content consists of one or more attributes, child Resources or childResource references. In the case of an Update request primitive, the Content parameter shall contain the attribute and new values. Attributes to be deleted from the resource shall be indicated without a value. In both cases the resource type is as defined in clause 7.4, however since a partial resource is being transferred it is not required to be valid according to the XSD for that resource in terms of the presence of resource attributes. Any attribute that is present, however, shall comply to the data type defined in the XSD of that resource.

A Notification Data Object. This applies to Notification request primitives. The data type of the data object is named <m2m:notification> and is described in clause 7.5.1.

An Aggregated Notification. This applies to Notification request primitives. The data type of the data object is named <m2m:aggregatedNotification> and contains multiple <m2m:notification> objects. This is described in clause 7.5.1.

An AttributeList element, as described in clause 7.5.2. This is used in partial retrieve request primitives to indicate a list of attribute names whose values shall be retrieved in the response.

A ResponsePrimitive object as described in clause 7.5.1. This applies to Notification request primitives which are sent when accessing resources in asynchronous non-blocking mode.

7.2.1.2	Response primitive format

Table 7.2.1.2-1 summarizes the primitive parameters for Response primitive, indicating their presence depending on the C, R, U, D or N operations of the associated Request primitive and whether this operation was successful or caused an error. "M" indicates mandatory, "O" indicates optional, "NP" indicates not present.

Refer to clause 8.1.3 of oneM2M TS-0001 [6] for additional information on the request primitive parameters.

NOTE:	Response Code and Status Code parameters are merged into the Response Status Code parameter.

Table 7.2.1.2-1: Response Primitive Parameters

The Content parameter in a Response shall contain one of the following:

A complete or partial Resource. This applies to a response primitive sent in reply to create and retrieve request message. A partial resource also applies to a response primitive sent in reply to update request message. The Content parameter shall contain a single root element whose name is the name of the Resource and whose content consists of one or more attributes, child resources or childResource references. In this case the resource type is as defined in clause 7.4. However if a partial resource is being transferred, it is not required to be valid according to the XSD for that resource, in terms of the presence of resource attributes. Any attribute that is present, however, shall comply to the data type defined in the XSD of that resource.

The URI of a resource. This is included directly as the content of the Content parameter (like in case 6).

A partial resource and its hierarchical URI. These are included in a root element called m2m:resource defined in clause 7.5.2. The URI is included as an attribute of m2m:resource.

A list of URIs. This can be used for transferring the childResource URIs in a Discovery response. These are included in an element called m2m:URIList defined in clause 7.5.2.

A list of childResourceRef. This can be used for transferring the child resource references in a Discovery response. These are included in an element called m2m:resourceRefList defined in clause 7.5.2.

An Aggregated Response. This is sent as a result of a Group operation. This uses the element m2m:aggregatedResponse defined in clause 7.5.2.

A request primitive. A pending request is sent in a polling response. This uses the element m2m:requestPrimitive defined in clause 6.4.1.

Human-readable error message. This is included in an element called m2m:debugInfo defined in clause 7.5.2.


### 7.2.2	Description of generic procedures


7.2.2.1	Generic resource request procedure for originator

A generic resource Request procedure shall be comprised of the following actions. Additional actions specific to individual procedures are listed in the respective clauses by referencing these actions and providing additional steps. The Originator shall execute the following steps in order.

Figure 7.2.2.1-1: Generic procedure of Originator

Orig-1.0 "Compose Request primitive": Refer to clause 7.3.1.1 for details.

Orig-2.0 "Send a Request primitive to the Receiver CSE": The Request primitive shall include the mandatory parameters Operation, To, From and Request Identifier. Refer to clause 7.3.1.2 for details.

Orig-3.0 "Check Response Type": In this step, the Originator checks that the communication method is either blockingRequest, nonBlockingRequestSynch, nonBlockingRequestAsynch or flexBlocking by using the Response Type parameter (see detail in clause 8.1.2 in the oneM2M TS-0001 [6]). If the Response Type parameter does not exist, the communication method is "blockingRequest" as specified at clause 6.4.1.

If the Response Type is blockingRequest the Originator waits for the Response primitive and goes to step Orig-4.0. If the Response Type is nonBlockingRequestSync, it waits for an acknowledgement Response primitive and goes to step Orig-4.1. If the Response Type is nonBlockingRequestAsynch, it waits for an acknowledgement Response primitive and goes to step Orig-4.1. If the Response Type is flexBlocking, the Originator shall wait for a Response primitive as in Orig-4.0 and Orig-4.1 below, if the Response primitive is an acknowledgement it shall proceed according to Orig-4.1 (nonBlockingRequestSynch or nonBlockingRequestAsynch) otherwise it shall proceed according to Orig-4.0 (blockingRequest).

Orig-4.0 and Orig-4.1 "Wait for Response primitive": Refer to clause 7.3.1.3 for details.

Orig-5.0 "Send a Request primitive with op=R": The op=R means Retrieve operation. The Request primitive shall include the mandatory parameters Operation, To, From and Request Identifier. The Response Type of the "Request" primitive shall be blockingRequest. See clause 7.3.1.4 for details.

Orig-5.1 "Receive a Response primitive from the Hosting CSE": The Originator shall receive the mandatory parameters which are the Response Status Code and Request Identifier. The Request Identifier shall be identical to the value of that parameter from Orig-5.0. If present, the Content parameter gives information about the <request> resource. When the Response Status Code is successful and Content parameter exists, the Originator goes to Orig-5.2. Otherwise, it may go to Orig-5.0 and retry the operation.

Orig-5.2 "Completion of operation by requestStatus attribute": When the requestStatus is COMPLETED, the Originator goes to Orig-5.3. When the requestStatus is PENDING or FORWARDED or PARTIALLY_COMPLETED (indicating processing at the Receiver), it goes to Orig-5.0. When the requestStatus is FAILED, it goes to finish with error.

Orig-5.3 "Extract a result from Response primitive of Orig-5.1": The information in the operationResult attribute of the <request> resource in the Content parameter from Orig-5.1 is extracted from the Response primitive which included the Request Identifier, Response Status Code and optional Content parameters. The <request> resource shall include mandatory attributes as specified in clause 9.6.12 of oneM2M TS-0001 [6]. The Request Identifier in the operationResult attribute shall be identical to that in Orig-2.0.

Orig-6.0 "Process Response primitive": The Request Identifier shall be identical to that in Orig-2.0. The Originator processes the response.

Orig-7.0 "Receive a Request primitive with op=N": The op=N means Notify operation. The Originator receives a Request primitive with mandatory parameters Operation, To, From, Request Identifier and Content. The Operation parameter shall be Notify. The Content parameter is the notification information as specified in clause 7.5.1.1.

Orig-8.0 "Create a Response primitive": The Originator creates Response primitive with mandatory parameters Response Status Code and Request Identifier. The Request Identifier shall be identical to that in Orig-7.0.

Orig-9.0 "Send a Response primitive": The Response primitive which is created at Orig-8.0 shall be sent to the Receiver. Refer to clause 7.3.2.3 for details.

Orig-9.1 "Extract Response primitive of Orig-2.0 from Orig-7.0": The information in the operationResult attribute of the <request> resource from Orig-7.0 in Response primitive includes Request Identifier, Response Status Code and optional Content parameters. The <request> resource shall include mandatory attributes as specified in clause 9.6.12 of oneM2M TS-0001 [6]. The Request Identifier in the operationResult attribute shall be identical to that in Orig-2.0.

7.2.2.2	Generic procedure for handling a Request at a receiver

The Receiver shall execute the following steps in order. In case of error in any of the steps below, the Receiver shall execute "Create an error response" (refer to clause 7.3.3.13 for details) and then "Send Response primitive" (refer to clause 7.3.2.4 for details). The corresponding Response Status Code shall be included in the Response primitive.

Figure 7.2.2.2-1: Generic procedure of Receiver

Recv-1.0 "Check the validity of received request primitive": See clause 7.3.2.1 for details.

Recv-2.0 "Communication method?": The Receiver CSE checks whether a received request is blockingRequest, nonBlockingRequestSynch or nonBlockingRequestAsynch by using the Response Type parameter (see detail in clause 8.1.2 in oneM2M TS-0001 [6]). If the request is blockingRequest or the Response Type parameter is not included, it goes to step Recv-6.0 "Resource handling procedure". If the request is nonBlockingRequestSynch, it goes to step Recv-3.0 "Create <request> resource locally". If the request is nonBlockingRequestAsynch, it goes to step Recv-3.0 "Create <request> resource locally". If the request is flexBlocking, the Receiver CSE shall make the decision to respond using blocking or non-blocking based on its own local context (memory, processing capability, etc.) unless specified further in the resource-specific procedure.

Recv-3.0 "Create <request> resource locally": Refer to clause 7.3.2.2 for details.

Recv-4.0 "Create a successResponse": Refer to clause 7.3.3.12 for details.

Recv-5.0 "Send Response Primitive": Refer to clause 7.3.2.4 for details.

Recv-6.0 "Resource handling procedure": Refer to Figure 7.2.2.2-2 for details.

Recv-7.0 "Update <request> resource": Refer to clause 7.3.2.5 for details. This step is only valid when the request is non-blocking.

Recv-8.0 "Send Notification": Refer to clause 7.5.1.2.5 for details.

Recv-9.0 "Wait for a Response primitive": Refer to clause 7.3.1.3 for details.

Recv-10.0 "Send Response Primitive": Refer to clause 7.3.3.16 for details.

Figure 7.2.2.2-2: Resource handling procedure

Figure 7.2.2.2-2 describes the generic procedure to resource handling procedures.

Recv-6.0.1 "Requested operation is an AE registration?": If the requested operation is an AE registration, then it goes to Recv-6.0.2 "Check Service Subscription Profile". Otherwise, it goes to Recv-6.1.

Recv-6.0.2 "Check Service Subscription Profile": Refer to clause 7.3.2.7 for details.

Recv-6.1 "Hosting CSE of the targeted resource?": The step checks if the receiver is a transit CSE or the Hosting CSE of the received Request by examining the To parameter of the Request primitive. If the receiver hosts the resource that the address in the To parameter represents, the receiver is the Hosting CSE (goes to Recv-6.2"Check existence of the addressed resource", Yes branch). Otherwise, the receiver is the Transit CSE (goes to Recv-6.9 "CMDH processing supported?", No branch). Refer to clause 7.3.2.8 for details.

Recv-6.2 "Check existence of the addressed resource": Refer to clause 7.3.3.1 for details.

Recv-6.2.1 "Check for duplicate group requests": Refer to clause 7.3.3.2 for details.

Recv-6.3 "Check authorization of the Originator": Refer to clause 7.3.3.15 for details.

Recv-6.4 "Check validity of resource representation": Refer to clause 7.3.3.3 and clause 7.3.3.4 for details. Notify is not applicable for this step.

Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed": The step represents five common operations which are "Create the resource (clause 7.3.3.5)", "Retrieve the resource (clause 7.3.3.6)", "Update the resource (clause 7.3.3.7)", "Delete the resource (clause 7.3.3.8)" and "Notify processing (clause 7.3.3.9)".

Recv-6.6 "Announce/De-announce the resource": The step represents two common operations which are "Announce the resource" and "De-announce the resource". Refer to clause 7.3.3.10 and clause 7.3.3.11 for details. Notify is not applicable for this step.

Recv-6.6.1 "Communication method?": The Receiver CSE checks whether a received request is blockingRequest or not by using Response Type parameter (see detail in clause 8.1.2 in oneM2M TS-0001 [6]). If the request was blockingRequest or Response Type parameter was not included, it goes to step Recv-6.7 "Create a success response". Otherwise, it goes back to the generic procedure of the receiver (Figure 7.2.2.2-1).

Recv-6.7 "Create a success response": Refer to clause 7.3.3.12 for details.

Recv-6.9 "CMDH processing supported?": This step checks whether the Receiver supports the CMDH processing. If the receiver supports CMDH processing, it goes to Recv-6.10 "Queue request primitive and execute CMDH message forwarding procedure" otherwise, it goes to Recv-6.11 "Forwarding".

Recv-6.10 "Queue request primitive and execute CMDH message forwarding procedure": the Receiver CSE shall queue the received request primitive and execute the "CMDH message forwarding procedure". Refer to clause H.2.4 for details.

Recv-6.11 "Forwarding": carry out message forwarding as defined in clause 7.3.2.6.


## 7.3	Common operations



### 7.3.1	Originator actions


7.3.1.1	Compose request primitive

The originator shall compose a Request message that shall be mapped to a specific protocol.

The Request shall include mandatory parameters Operation, To, From and Request Identifier.

The Release Version Indicator parameter shall be included unless the primitive is being sent to a Release 1 entity. The Request may include the time related parameters Originating Timestamp, Request Expiration Timestamp, Result Expiration Timestamp and Operation Execution Time.

The Request may include the other parameters as specified in Table 7.2.1.1-1: Request Primitive Parameters.

When including a resource representation in the request primitive for create and update, the originator shall take into account the validation rules as specified in "Check validity for resource representation for create" and "Check validity for resource representation for update" respectively.

EXAMPLE:	Any attributes marked with NP shall not be present in the resource representation for the corresponding request primitive.

7.3.1.2	Send a request to the receiver CSE

The originator shall determine the receiver CSE.

The receiver of the Request shall be the registrar CSE of the originator in case the originator is not IN-CSE.

If the originator is the IN-CSE, the receiver of the Request shall be the CSE whose identifier is the prefix of the To parameter of the Request.

If this results in no matching CSE, then the request is rejected with a Response Status Code indicating "NOT_FOUND" error.

If this results in multiple CSEs, the request is rejected with a Response Status Code indicating "INTERNAL_SERVER_ERROR" error.

7.3.1.3	Wait for response primitive

The originator shall wait for the Response primitive from the receiver that corresponds to the Request primitive that was sent by the originator. Correlation between the Request and the corresponding Response is handled by the transport layer or by Request Identifier parameter of the primitive.

If no Response primitive is received within a certain time, specified by server policy and/or by the underlying transport technology, this shall be handled as if a Response primitive with a Response Status Code indicating "REQUEST_TIMEOUT" error was received.

The originator shall not wait for the Response primitive from the receiver after sending a Notification request to a non-oneM2M entity.

NOTE: For some protocol bindings (e.g. HTTP) the Originator may receive a transport-protocol specific response to a Notification that was sent to a non-oneM2M entity. The handling of such a response is out of scope of the present document.

7.3.1.4	Retrieve the <request> resource

When the Originator needs to retrieve information about an associated previously issued non-blocking request, the Originator shall request to Retrieve the attributes of the <request> resource. The Originator shall compose the Request primitive with the following parameters and send the Request to the Receiver CSE. See clauses 7.3.1.1 and 7.3.1.2.

NOTE:	The Originator may include optional parameters described in clause 8.1.2 of oneM2M TS-0001 [6].

Table 7.3.1.4-1: Request primitive parameter settings


### 7.3.2	Receiver CSE actions


7.3.2.1	Check the validity of received request primitive

The validity checking of the message carrying the received request primitive is specified by the protocol mapping Technical Specifications (CoAP binding [22], HTTP binding [23], MQTT binding [24], and Websocket binding [42]).

If the request contains a Request Expiration Timestamp, Result Expiration Timestamp, Operation Execution Time or a CMDH parameter listed in Annex H and the receiver does not support this parameter, the request shall be rejected with a Response Status Code indicating a "NOT_IMPLEMENTED" error.

If the Request Expiration Timestamp is given in the request and has expired, the Receiver CSE shall reject the request with a "REQUEST_TIMEOUT" Response Status Code parameter value.

If the From parameter is not present in the request, except in the case of an AE Create request, the Receiver CSE shall reject the request with a "BAD_REQUEST" Response Status Code parameter value.

If the From parameter in a request from a Registree AE has any format other than AE-ID-Stem, the Receiver CSE shall reject the request with a "BAD_REQUEST" Response Status Code parameter value.

If the received request is communicated within an established Security Association (oneM2M TS-0003 [7]), and

the Receiver knows that the Registree using the established Security Association is an AE; and

the Receiver knows the AE-ID(s) of the Registree using the established Security Association; and

the From parameter does not match the allowed AE-ID(s) of the Registree using the established Security Association;

then the request shall be rejected with an "ORIGINATOR_NOT_AUTHENTICATED" Response Status Code parameter value.

If the received request is communicated within an established Security Association, and:

the Receiver knows that the Registree using the established Security Association is a CSE; and

the Receiver knows the CSE -ID of the Registree using the established Security Association; and

if one of the following applies:

the From parameter is an CSE-ID that matches one of the Receiver's Registree CSE's CSE-ID other than the CSE-ID of the Registree using the established Security Association; or

the From parameter is an CSE-Relative C-Type AE-ID-Stem; or

the From parameter is an SP-Relative AE-ID or Absolute AE-ID with a C-Type AE-ID-Stem, and the CSE-ID portion of the From parameter matches one of the Receiver's Registree CSE's CSE-ID other than the CSE-ID of the Registree for the established Security Association;

then the request shall be rejected with an "ORIGINATOR_NOT_AUTHENTICATED" Response Status Code parameter value.

NOTE:	An SP-Relative-AE-ID or Absolute AE-ID with a C-Type AE-ID-Stem always includes a CSE-ID portion (see oneM2M TS-0001 [6]).

If the received request is communicated outside of an established Security Association; and:

if the From parameter includes an AE-ID; and

the request is not a CREATE <AE> Request; and

the From parameter does not match the AE-ID of an AE currently registered to the Receiver;

then the request shall be rejected with an "ORIGINATOR_NOT_AUTHENTICATED" Response Status Code parameter value.

If the received request is communicated outside of an established Security Association, and the From parameter includes a CSE-ID, then the request shall be rejected with a "SECURITY_ASSOCIATION_REQUIRED" Response Status Code parameter value.

If a received request needs to be forwarded to another CSE and if CMDH processing is supported, then in addition, the "CMDH message validation procedure" defined in clause H.2.3 shall be carried out. If the message is not valid, the request shall be rejected with a Response Status Code indicating a "BAD_REQUEST" error.

If Resource Type is not present or is invalid in a CREATE request, the request shall be rejected with a Response Status Code indicating a "BAD_REQUEST" error.

If the Filter Criteria parameter is included in a CREATE request, the request shall be rejected with a Response Status Code indicating a "BAD_REQUEST" error.

If the Result Content is invalid for a given operation (Refer TS-0001 Table 8.1.2-1: Summary of Result Content Values) then the Hosting CSE shall reject the request with a Response Status Code indicating a "BAD_REQUEST" error.

If the receiver does not support the content format (i.e. type of serialization for the response) requested by the originator, the request may be rejected with a Response Status Code indicating a "NOT_ACCEPTABLE" error.

If the receiver does not support the content format sent by the originator, the request may be rejected with a Response Status Code indicating an "UNSUPPORTED_MEDIA_TYPE" error.

If the Release Version Indicator is not present in the request the Receiver CSE shall add the Release Version Indicator with value set to 1.

If the Receiver CSE is the Hosting CSE and it does not support the release value present in the Release Version Indicator then the request shall be rejected with a Response Status Code indicating a "RELEASE_VERSION_NOT_SUPPORTED" error.

If the Receiver CSE is the Hosting CSE and the request contains any other primitive parameter that it does not support, or if it contains a primitive parameter with a value that relates to a feature that is not supported by that Hosting CSE, the request shall be rejected with a Response Status Code indicating a "NOT_IMPLEMENTED" error.

7.3.2.2	Create <request> resource locally

Creation of a <request> resource can only be done implicitly by a Receiver CSE. When the Receiver CSE receives a request in non-blocking mode (i.e. the Response Type parameter of the request is set to either "nonBlockingRequestSynch" or "nonBlockingRequestAsynch") targeting any other resource type or requesting a notification, and if the Receiver CSE supports the <request> resource type as indicated by the supportedResourceType attribute of the <CSEBase> resource, the Receiver CSE shall create an instance of <request> resource based on the following steps. If the Receiver CSE does not support the <request> resource type, the "nonBlockingRequestSynch" request shall be rejected with a Response Status Code indicating "NON_BLOCKING_SYNCH_REQUEST_NOT_SUPPORTED" error. In the case of a "nonBlockingRequestAsynch" request, a Receiver CSE that does not support the <request> resource type shall respond to an acceptable request with a response containing an Acknowledgement without a reference to a resource containing the context of the request.

The Receiver CSE of a non-blocking request is the Hosting CSE for the <request> resource that shall be associated with the non-blocking request.

Assign values to the common attributes of the <request> resource according to Table 7.3.2.2-1.

Table 7.3.2.2-1: Common attributes settings for <request> resource

Assign values to the resource-specific attributes of the <request> resource according to Table 7.3.2.2-2.

Table 7.3.2.2-2: Resource-specific attributes settings for <request> resource

7.3.2.3	Create a success response (acknowledgement)

The Receiver CSE shall create a Response primitive. The Receiver CSE shall include the following parameters in the Response primitive.

Table 7.3.2.3-1: Response primitive parameter settings

7.3.2.4	Send response primitive (acknowledgement)

A Response primitive shall be sent back to the originator.

7.3.2.5	Update <request> resource

Changes in the attributes of a <request> resource shall be done by the Hosting CSE implicitly due to changes of the status (requestStatus) of the associated non-blocking request or due to the reception of an operation result (operationResult) in response to the associated non-blocking request. The Receiver CSE shall update attributes of an instance of the <request> resource based on the following steps.

Update values of the common attributes of the <request> resource according to Table 7.3.2.5-1.

Table 7.3.2.5-1: Common attributes settings for <request> resource

Update values of the resource-specific attributes of <request> resource according to Table 7.3.2.5-2.

Table 7.3.2.5-2: Resource-specific attributes settings for <request> resource

7.3.2.6	Forwarding

When a receiver CSE is not the Hosting CSE, i.e. the CSE-ID of the receiver CSE is different from the CSE-ID in the To parameter, the receiver CSE shall attempt to forward the primitive. The Receiver CSE checks each of its <remoteCSE> resources to find whether the CSE-ID in the To parameter of the primitive matches either the CSE-ID attribute or one of the CSE-IDs in the descendantCSEs attribute of the <remoteCSE>.

If a match is found, the CSE shall retarget the request to the pointOfAccess of the matching <remoteCSE> resource.

If a match is not found, and the CSE received the request from an AE or a descendant CSE, and the CSE is not the IN-CSE, then it shall retarget the request to its Registrar CSE.

If a match is not found and the CSE is the IN-CSE, then the CSE shall not forward the request and it shall respond with an error using Response Status Code "NOT_FOUND".

If a match is not found and the CSE is not the IN-CSE and the CSE receives the request from its registrar CSE, then the CSE shall not forward the request and it shall respond with an error using Response Status Code "NOT_FOUND".

When the receiver CSE forwards the primitive and the From parameter value has CSE-relative-ID format, the receiver shall convert the ID format of the From parameter into SP-relative by pre-pending its own CSE-ID. If the receiver CSE is the IN-CSE and the To parameter targets another SP domain, the IN-CSE shall convert the ID format of the From parameter into Absolute format by pre-pending another SP-ID.

If any of the Request Expiration Timestamp, Result Expiration Timestamp or Operation Execution Time parameters are set in the request, the receiver CSE should forward the request before the earliest of these times. If the any of the timestamps are in the past, it shall reject the request with a "REQUEST_TIMEOUT" Response Status Code parameter value and not forward the request.

A receiver CSE shall remove the Release Version Indicator and Vendor Information from the request or response before retargeting a primitive to a Release 1 entity.

A receiver CSE shall indicate the content serialization to be used in a response in the retargeted primitive.

Acting as an originator the CSE shall perform the following procedures:

"Send a Request to the receiver CSE". Refer to clause 7.3.1.2 for details.

"Wait for Response primitive". Refer to clause 7.3.1.3 for details.

When the Response is received the receiver CSE shall:

Primitive specific procedure: Forward the Response to the original CSE.

7.3.2.7	Check Service Subscription Profile

In order to validate whether or not the AE registration request complies with the subscriber's service subscription profile, the Receiver shall have the subcriber’s profile information stored locally or retrieved from the IN-CSE. If the subscriber's service subscription profile is not available to the Receiver, then the Receiver CSE shall respond with a “SERVICE_SUBSCRIPTION_NOT_ESTABLISHED” error. The Receiver shall check if a <serviceSubscribedNode> child resource of the subscriber's <m2mService SubscriptionProfile> resource exists, with a CSE-ID attribute that matches the Receiver owned CSE-ID. If this condition is not met, then the Receiver CSE shall respond with a “SERVICE_SUBSCRIPTION_NOT_ESTABLISHED” error. If this condition is met, the Receiver shall further check whether the Registree AE complies with the linked (i.e. ruleLinks attribute) <serviceSubscribedAppRules> resource(s), see Clause 10.2.2 of oneM2M TS-0001 [6]. If no linked <serviceSubscribedAppRule> resource(s) is found or if rule link validation fails for the AE registration request, then the Receiver CSE shall respond with an “APP_RULE_VALIDATION_FAILED” error.

.

7.3.2.8	Check Hosting CSE of the targeted resource

The Receiver shall check the To parameter of the request, depending upon the addressing modes in the request. The following handling shall be done:

To parameter with Absolute Resource ID representation:

If the To parameter in the request starts with M2M-SP-ID (i.e. Absolute Resource ID representation) but M2M-SP-ID in the To parameter is different from M2M-SP-ID of the receiver, then receiver is a transit CSE.

If the To parameter in the request starts with M2M-SP-ID (i.e. Absolute Resource ID representation) of the receiver, but the CSE-ID in the To parameter is different from the CSE-ID of the receiver, then the receiver is a transit CSE.

If the To parameter in the request starts with M2M-SP-ID (i.e. Absolute Resource ID representation) of the receiver, and the CSE-ID in the To parameter is same as CSE-ID of the receiver, then the receiver is the Hosting CSE.

To parameter with SP-Relative Resource ID representation:

If the To parameter in the request starts with CSE-ID (i.e. SP-Relative Resource ID representation) of the receiver, and the CSE-ID in the To parameter is different from CSE-ID of the receiver, then the receiver is a transit CSE.

If the To parameter in the request starts with CSE-ID (i.e. SP-Relative Resource ID representation) of the receiver, and the CSE-ID in the To parameter is same as CSE-ID of the receiver, then the receiver is the Hosting CSE.

To parameter with CSE-Relative Resource ID representation:

If the To parameter in the request does not start with CSE-ID (i.e. CSE-Relative Resource ID representation), then the receiver is the Hosting CSE.

When the receiver is a transit CSE:

If the request is an AE/CSE registration request, then the request is rejected with a Response Status Code indicating "BAD_REQUEST" error.

If the transit CSE is not able to receive asynchronous messages from the next-hop CSE, it shall set the Response Type in the forwarded request to blockingRequest, nonBlockingRequestSynch or flexBlocking without notification targets.

Either CMDH Message Forwarding (Recv-6.9) or Forwarding (Recv-6.10) shall apply as depicted in Figure 7.2.2.2-2 Resource handling procedure except for AE/CSE registration request.

7.3.2.9	Blocking Subscription Notification Failure Handling

Whenever a oneM2M AE triggers the UPDATE operation on resources which have blocking subscription, the Receiver CSE sends a blocking notify request to the subscription’s notificationURI.

If a notification response is received from the notificationURI indicating TARGET_NOT_REACHABLE the Receiver CSE shall return an error response to the originator of the UPDATE request with Response StatusCode indicating error REMOTE_ENTITY_NOT_REACHABLE.

If the notification response is received from the notificationURI indicating OPERATION_NOT_ALLOWED the Receiver CSE shall return an error response with Response Status Code indicating error OPERATION_DENIED_BY_REMOTE_ENTITY to the originator.


### 7.3.3	Hosting CSE actions


7.3.3.1	Check existence of the addressed resource

If the Request Expiration Timestamp is given in the request and has expired, the Hosting CSE shall reject the request with a "REQUEST_TIMEOUT" Response Status Code parameter value. Otherwise, the Hosting CSE should handle the request before the time specified in Request Expiration Timestamp.

The Hosting CSE shall check if the resource addressed by the To parameter exists in the repository. If the resource does not exist, the Hosting CSE shall reject the request with a Response Status Code indicating "NOT_FOUND" error.

The Hosting CSE shall also check the existence of target resources based on conditions specified in the Filter Criteria parameter in the Retrieve/Update/Delete operation. If there are no matching target resources, the Hosting CSE shall reject the request with a Response Status Code indicating "NOT_FOUND" error.

If the Hosting CSE does not support the content format (i.e. type of serialization) requested by the originator, the request shall be rejected with a Response Status Code indicating "NOT_ACCEPTABLE" error.

If the Hosting CSE does not support the content format sent by the originator, the request shall be rejected with a Response Status Code indicating "UNSUPPORTED_MEDIA_TYPE" error.

7.3.3.2	Check for duplicate group requests

If the Hosting CSE receives a request containing a Group Request Identifier parameter it shall check that it has not already received a request that contains the same Group Request Identifier and that is addressed to the same target resource.

To do this, the Hosting CSE shall maintain a list of the group request identifiers from the requests that it has received. With each group request identifier it shall record the identifiers of the resource(s) that were targeted using it.  It shall compare the incoming request’s Group Request Identifier against this list and if it finds a match (of both group request identifier and target resource) it shall reject the request with the Response Status Code indicating "GROUP_REQUEST_IDENTIFIER_EXISTS" error in the Response primitive. Otherwise, the Hosting CSE shall add the Group Request Identifier, and the identifier of the targetted resource, to the list that it is storing locally. It shall then proceed with processing the request.

The Hosting CSE shall keep the group request identifier in its local store until the expiration time of the original request or for a period of time determined by local policy.

7.3.3.3	Check validity of resource representation for CREATE

If the Hosting CSE node type is MN/ASN and the CREATE request contains a resource whose type is only applicable to an IN-CSE e.g. <triggerRequest> or <m2mServiceSubscriptionProfile> then the Hosting CSE shall reject the request and return an error response with a Response Status Code indicating "OPERATION NOT ALLOWED". For a list of resource types that are only applicable to an IN-CSE see Table 6.3.4.2.1-1.

If the request is a valid CREATE request, but the Hosting CSE does not implement the requested resource type, then the Hosting CSE shall reject the request and return an error response with a Response Status Code indicating a "NOT_IMPLEMENTED" error.

If the CREATE request has a Resource Type that is not listed in the child resource tables, defined in clause 7.4 corresponding to the addressed resource, then the request shall be rejected with a Response Status Code indicating an "INVALID_CHILD_RESOURCE_TYPE" error.

If no resource representation is present in the CREATE request, then the request is rejected with a Response Status Code indicating a "BAD_REQUEST" error.

If the resource representation in Content parameter is not compatible with the Resource Type parameter in a CREATE request, the request shall be rejected with a Response Status Code indicating a "BAD_REQUEST" error.

If the expirationTime attribute is present in the resource representation, but its value indicates a time in the past, then the request shall be rejected with a Response Status Code indicating a "BAD_REQUEST" error.

There are three cases where the Hosting CSE shall configure or override an expirationTime value that differs from the value specified in the resource representation (if present):

The Originator does not specify an expirationTime.

The Originator requests an expiration time that is later than the expirationTime of the parent.

The Hosting CSE determines that the expiration time requested by the Originator does not meet its requirements (e.g. based on a local policy).

In each of these cases, the Hosting CSE shall configure an expirationTime into the resource that is less than or equal to the expirationTime of the parent resource. In addition, the Hosting CSE shall communicate the modified value back to the originator in the response if the Result Content parameter permits this.

If the creator attribute is present in the resource representation and supported by the type of resource to be created its value shall be NULL. If the originator provides a value for the creator attribute but resource type does not support the creator attribute, then the Hosting CSE shall reject the request with a Response Status Code indicating a "BAD_REQUEST" error. If the originator provides a value for the creator attribute within the request, the Hosting CSE shall reject the request with a Response Status Code indicating a "BAD_REQUEST" error.

The resource descriptions in clause 7.4 include tables that specify the attributes of each resource and the optionality of the attribute in a CREATE or UPDATE request, see clause 7.4.1.1. A request containing an attribute not listed in the table shall be rejected with a "BAD_REQUEST" error.

The handling below shall apply to each attribute in the resource for CREATE request primitives and the handling depends on the "presence in CREATE request" column of the resource table. If the request is rejected based on the rules below, then the other attributes do not have to be checked.

M attribute for create request

If the attribute is present in the resource representation in the CREATE request, the Hosting CSE shall check if the value is acceptable according to internal policies:

If the attribute value relates to a feature that is not supported by the Hosting CSE, that CSE shall reject the request with a Response Status Code indicating a "NOT_IMPLEMENTED" error.

If the provided value is not accepted for any other reason, the Hosting CSE shall reject the request with a Response Status Code indicating a "BAD_REQUEST" error.

If the attribute is not present in the resource representation in the CREATE request the Hosting CSE shall reject the request with a Response Status Code indicating a "BAD_REQUEST" error.

O attribute for create request

If the attribute is present in the resource representation in the CREATE request, the Hosting CSE shall check if the value is acceptable according to internal policies:

If the Hosting CSE does not support the attribute, it shall reject the request with a Response Status Code indicating a "NOT_IMPLEMENTED" error.

If the Hosting CSE supports the attribute but the value provided relates to a feature that is not supported by the Hosting CSE, it shall reject the request with a Response Status Code indicating a "NOT_IMPLEMENTED" error.

If the provided value is not accepted for any other reason,  the Hosting CSE shall reject the request with a Response Status Code indicating a "BAD_REQUEST" error.

NP attribute for create request

If the attribute is present in the resource representation in the CREATE request, the Hosting CSE shall reject the request with a Response Status Code indicating a "BAD_REQUEST" error.

7.3.3.4	Check validity of resource representation for UPDATE

The handling below shall apply to each attribute in the resource for UPDATE request primitives and the handling depends on the "presence in UPDATE request" column of the resource table. If the request is rejected based on the rules below, then the other attributes do not have to be checked.

If the expirationTime attribute is present in the resource representation, but its value indicates a time in the past, then the request shall be rejected with a Response Status Code indicating a "BAD_REQUEST" error.

If the expirationTime attribute is present in the UPDATE request, and its value is earlier than the value of the expirationTime attribute that it is updating, then the Hosting CSE shall check if the targeted resource has any child resource whose expirationTime attribute value is later than the expirationTime value in the UPDATE request. If yes, the request shall be rejected with a Response Status Code indicating a "BAD_REQUEST" error.

The resource descriptions in clause 7.4 include tables that specify the attributes of each resource and the optionality of the attribute in a CREATE or UPDATE request, see clause 7.4.1.1. A request containing an attribute not listed in the table shall be rejected with a "BAD_REQUEST" error.

O attribute for update request

If the attribute is present in the resource representation in the UPDATE request, the Hosting CSE shall check if the value is acceptable according to internal policies:

If the Hosting CSE does not support the attribute, it shall reject the request with a Response Status Code indicating a "NOT_IMPLEMENTED" error.

If the Hosting CSE supports the attribute but the value provided relates to a feature that is not supported by the Hosting CSE, it shall reject the request with a Response Status Code indicating a "NOT_IMPLEMENTED" error.

If the provided value is not accepted for any other reason, the Hosting CSE shall reject the request with a Response Status Code indicating a "BAD_REQUEST" error.

NP attribute for update request

If the attribute is present in the resource representation in the UPDATE request, the Hosting CSE shall reject the request with a Response Status Code indicating a "BAD_REQUEST" error.

7.3.3.5	Create the resource

If the Operation Execution Time is given in the request, the Hosting CSE should perform the following procedures at the time and shall not perform the procedures before the time.

A new resource shall be created with the lastModifiedTime attribute of the resource set to the same value as the creationTime attribute of the resource.

The following rules shall be applied:

The structured resource identifier of the created resource shall be the identifier of its parent resource with the resourceName appended. (e.g. myCSE/myContainer, for an application resource with resourceName "myContainer" created in the parent resource myCSE).

When configuring the resourceName attribute of the new resource, the Hosting CSE shall use the name provided in the resourceName attribute within the content of the request. The Hosting CSE shall first check for the presence of any resources having a resourceName attribute that matches the one specified in the request and that have the same parent as the new resource being created. If such a resource exists, then the Hosting CSE shall reject the request with a Response Status Code indicating "CONFLICT" error. If the resourceName is not provided in the request, the Hosting CSE shall generate and assign a name to the resourceName attribute of the new resource.

If the expirationTime attribute is present in the resource representation of the resource that is to be created and the expirationTime is set to a non-negative time, then an expiration timer shall be started by the Hosting CSE. At timer expiration the related resource is deleted as specified in "Delete the addressed resource".

Attributes of the parent resource shall be updated, if applicable. For example, the currentByteSize attribute of a <container> resource will be updated upon child <contentInstance> resource creation. An attribute update of a parent resource is resource type specific, as specified in clause 7.4.

If the creator attribute is present in the resource representation, and is supported by the type of resource to be created, and is NULL, then the Hosting CSE shall include the creator attribute in the resource to be created. The Hosting CSE shall assign the creator attribute with a value equal to the value carried in the From request parameter. If the creator attribute is not present in the resource representation of the request, the Hosting CSE shall not include the creator attribute in the resource to be created.

The Hosting CSE shall check if the created resource references an Application Entity Resource ID. If so the Hosting CSE shall send a Notify request primitive to the IN-CSE, requesting to add the entry to the <AEContactList> resource.

For setting the attributes in the resource representation the following rules shall apply in CREATE request primitives:

M attribute for create request

If the provided value is acceptable, the Hosting CSE shall use the provided value in the resource representation of the created resource.

O attribute for create request

If a value is provided and accepted, then the Hosting CSE shall use the provided value in the resource representation of the created resource.

If the attribute is not provided or accepted, but the multiplicity of the attribute is "1" in the resource, the Hosting CSE shall assign default value or assign value based on local policy, or the value of specified in clause 7.4.

If the attribute is not present in the resource representation in the CREATE request and the multiplicity of the attribute is "0..1" in the resource, the Hosting CSE shall create the resource without the attribute unless otherwise specified in resource type-specific procedures defined in clause 7.4.

NP attribute for create request

If the attribute is not present in the resource representation in the CREATE request, and the multiplicity of the attribute is "1" in the resource, then the Hosting CSE shall create the resource with the default value.

7.3.3.6	Retrieve the resource

If the Operation Execution Time is given in the request, the Hosting CSE should perform the following procedures at the time and shall not perform the procedures before the time.

When the resource is read to provide a response to Retrieve request primitives:

Full retrieve request: the request target is a resource given in the To parameter

The content of the Response to the Retrieve Request shall comply to the Result Content parameter in the Request. If a Result Content is not provided in the Request, the representation of the resource which includes all the attributes shall be returned.

Partial retrieve request: there are two cases:

Case 1)	the request target is a resource given in the To parameter and specific attribute names are provided in the Content parameter:

The values of the resource attribute(s) provided in the Content parameter shall be retrieved.

Case 2)	the request target is a resource given in the To parameter, the resource attribute is provided in the To parameter as a fragment identifier component of URI following '#' character [2]. The resource attribute shall be represented as a short name and shall belong to short name list in Table 8.2.3-1 to Table 8.2.3-5.

The resource attribute provided in the To parameter shall be retrieved.

7.3.3.7	Update the resource

If the Operation Execution Time parameter is given in the request, the Hosting CSE should perform the following procedures at that time and shall not perform the procedures before that time.

The Hosting CSE shall check to see if the target resource has a child <subscription> resource with notificationEventType attribute set to "Blocking_Update" according to the procedure specified in clause 7.5.1.2.19.

Attributes that are not included in the Content parameter of the addressed resource shall not be changed by the Hosting CSE. For attributes provided in the Content parameter, their content shall be updated while the following rules apply:

If the announceTo attribute or announcedAttribute attribute of the resource is requested to be updated, the Hosting CSE shall update the attribute as described in the "announce the resource or attribute" and "de-announce the resource or attribute" procedures as specified in the clause 7.3.3.10 and clause 7.3.3.11, respectively.

The Hosting CSE shall check if the update causes a change to a reference to an Application Entity Resource ID. If so the Hosting CSE shall send a Notify request primitive to the IN-CSE, requesting to update the entry to the <AEContactList> resource.

O attribute for update request

If an attribute value is provided and the value is accepted, the Hosting CSE shall use the provided value in the resource representation of the updated resource.

If the attribute is not provided, but the attribute exists in the target resource, the Hosting CSE shall leave the value of that attribute unchanged.

If this attribute is provided in the Content parameter and does not exist in the target resource, the Hosting CSE shall create such attribute with the provided value.

If this attribute is set to NULL in the Content parameter and exists in the target resource the following shall apply:

If the multiplicity of the attribute is shown as "1" or "1(L)" in oneM2M TS-0001 [6], the Hosting CSE shall reject the request with the Response Status Code indicating "BAD_REQUEST".

If the multiplicity of the attribute is shown as other than "1" or "1(L)" in oneM2M TS-0001 [6], the Hosting CSE shall delete the attribute.

If the expirationTime attribute is present and modified by the procedure and it is set to a non-negative time, then an expiration timer shall be re-started by the Hosting CSE. At timer expiration the related resource is deleted as specified in "Delete the addressed resource".

NP attribute for update request

If the update is successful, the Hosting CSE shall set the lastModifiedTime to the current time and the Hosting CSE shall increment the stateTag if present.

7.3.3.8	Delete the resource

If the Operation Execution Time is given in the request, the Hosting CSE should perform the following procedures at that time and shall not perform the procedures before that time.

The addressed resource with all its attributes shall be deleted. Any expiration timer shall be stopped. This same procedure shall be invoked (recursively) for each child resource of the deleted resource in case the child resource is only linked to the deleted resource.

The Hosting CSE shall check if the deleted child resource leads to changes in its parent resource's attribute(s) (e.g. currentNrOfInstances, currentByteSize etc.), then these attribute(s) shall be updated.

If the resource is announced, the CSE shall try to de-announce the resource correspondingly.

If the deleted resource had a reference to an Application Entity Resource ID, the Hosting CSE shall send a Notify request primitive to the IN-CSE, requesting to delete the entry from the <AEContactList> resource.

7.3.3.9	Notify processing

7.3.3.9.1	Notify processing when To parameter is an <AE> resource

If the Operation Execution Time is given in the request, the Hosting CSE should perform the following procedures at the time and shall not perform the procedures before the time.

When the Hosting CSE receives a Notify request primitive targeting (i.e. To parameter) its <AE> resource, the Hosting CSE re-targets the primitive to the AE if the <AE> resource does not have any <pollingChannel> resource as a child.

Get the pointOfAccess attribute value of the corresponding <AE> resource. If there is no available pointOfAccess address then the Hosting CSE shall send the Notify response primitive with a Response Status Code indicating "TARGET_NOT_REACHABLE" error.

Forward the Notify request primitive to the first address retrieved from the pointOfAccess value.

If the forwarding fails due to "Target not reachable", iterate 2) with the next address.

If the Hosting CSE cannot forward it in the end, then it sends a Notify response primitive with a Response Status Code indicating "TARGET_NOT_REACHABLE" error.

7.3.3.9.2	Notify processing when To parameter is the <CSEBase> resource

If the Operation Execution Time is given in the request, the Hosting CSE should perform the following procedures at the time and shall not perform the procedures before the time.

When the Hosting CSE receives a Notify request primitive targeting (i.e. To parameter) its <CSEBase> resource, the Hosting CSE shall process the Content of the Notify request primitive. See clause 7.5.1.

7.3.3.10	Announce the resource or attribute

If a CREATE Request that contains an announceTo attribute is received, or if an UPDATE Request is received that adds a URI or CSE-ID to the announceTo attribute that is not already stored in the announceTo attribute of the resource:

Compose the CREATE Request primitive as follows:

The link attribute is set to the URI of the original resource.

If the accessControlPolicyIDs attribute of the original resource is not present, the accessControlPolicyIDs attribute is set to the same value as the parent resource or is set using the local policy of the original resource.

Attributes marked with MA in oneM2M TS-0001 [6]. Such attributes shall be included if present in the original resource and set to same value as in the original resource.

Attributes marked with OA that are included in the announcedAttribute attribute. Such attributes shall be included if present in the original resource and set to same value as in the original resource.

The resourceType attribute is set to the announced variant of the original resource (see Table 6.3.4.2.1-1).

If an attribute that is to be announced has an identifier type that supports multiple formats (CSE-relative, SP-relative, absolute), the Hosting CSE shall send this attribute in each request in step 1a or 1b in a format that is permitted by the rules given in oneM2M TS-0001 [6] clause 7.2 for that request's target. If the attribute is a resource identifier the Hosting CSE shall not convert it from a structured to an unstructured format or vice versa.

Perform the following steps for each new item (announcement target) in the announceTo attribute list:

If the announcement target is a CSE-ID, check if the parent resource of the original resource has been announced to the announcement target CSE by checking the announceTo attribute of the parent resource:

-	If yes, announce the original resource by sending the CREATE Request with its To parameter set to the location of the announced parent resource.

-	If no, if the resource to be announced is either a <contentInstance>, a <timeSeriesInstance> or a <flexContainerInstance> the Hosting CSE shall send an unsuccessful response with the Response Status Code indicating an "OPERATION_NOT_ALLOWED" error in response to the received Request. Otherwise check if the Hosting CSE has created a <CSEBaseAnnc> resource as a child of the <CSEBase> of the announcement target CSE.

-	If yes, announce the original resource by sending the CREATE Request to the announcement target CSE with its To parameter set to the <CSEBaseAnnc> resource address.

-	If no, then the CSE hosting the original resource shall perform the following steps:

Create a <CSEBaseAnnc> that represents itself as a child of the <CSEBase> resource of the announcement target CSE. The Hosting CSE shall compose the CREATE <CSEBaseAnnc> request primitive as described for resource announcement above and shall provide a value for the expirationTime attribute of the <CSEBaseAnnc> to be created.

Once the <CSEBaseAnnc> resource has been created, send the CREATE Request prepared earlier with its To parameter set to the <CSEBaseAnnc> resource address.

If the announcement target is not a CSE-ID send the CREATE Request to the URI provided in the announceTo of the request.

Wait for the Response to the CREATE that was sent in step 1a or 1b.

Replace the CSE-ID or URI in the content of the announceTo attribute contained in the original request’s resource representation with the URI of the successfully-announced resource from the Response received in step 2.

Include the updated announceTo attribute in the Content parameter of the Response to the received request.

If an UPDATE Request is received that adds an attribute name into the announcedAttribute attribute and that attribute is specified as OA in oneM2M TS-0001 [6]) :

Compose the UPDATE Request primitive. The UPDATE Request shall provide the attribute name for the attribute to be announced and the initial value for this attribute in the Content parameter. The initial value shall be the same as the value from the original resource. If this attribute has an identifier type that supports multiple formats (CSE-relative, SP-relative, absolute), the Hosting CSE shall send this attribute in each request in step 2 in a format that is permitted by the rules given in oneM2M TS-0001 [6] clause 7.2 for that request's target. If the attribute is a resource identifier the Hosting CSE shall not convert it from a structured to an unstructured format or vice versa.

Send UPDATE Requests to all announced resources listed in the announceTo attribute.

Wait for the Response primitive(s).

Add the attribute name of the successfully announced attribute to the announcedAttribute attribute.

Include updated announcedAttribute attribute in the Content parameter in the Response to the received UPDATE Request.

If an UPDATE Request is received that updates attribute(s) specified as MA (see oneM2M TS-0001 [6]) or updates attribute(s) included in the announcedAttribute attribute:

Compose an UPDATE Request primitive including the updated attribute(s) with their associated updated value(s). If an attribute has an identifier type that supports multiple formats (CSE-relative, SP-relative, absolute), the Hosting CSE shall send this attribute in each request in step 2 in a format that is permitted by the rules given in oneM2M TS-0001 [6] clause 7.2 for that request's target. If the attribute is a resource identifier the Hosting CSE shall not convert it from a structured to an unstructured format or vice versa.

Send the UPDATE Request to all CSE(s) represented by the URI(s) in the announceTo attribute of the original resource.

Wait for the Response primitive(s).

7.3.3.11	De-announce the resource or attribute

If an UPDATE Request that deletes the URI from the announceTo attribute is received:

Compose a DELETE Request primitive.

Send a DELETE Request to the CSE(s) represented by URI(s) in the announceTo attribute of the resource, which is not included in the announceTo of the request. The To parameter in the DELETE Request shall be set to the URI for the announced resource that will be deleted.

Wait for the Response primitive(s).

Remove the URI of successfully de-announced resource from the announceTo attribute of the resource.

Include updated announceTo attribute in the Content parameter in the Response to the UPDATE Request of the original resource.

If a DELETE Request is received:

Compose a DELETE Request primitive.

Send DELETE Requests to all of the CSE(s) represented by the URI(s) in the announceTo attribute of the resource.

Wait for the Response primitive.

If an UPDATE Request is received that removes an attribute name from the announcedAttribute attribute and that attribute is specified as OA in oneM2M TS-0001 [6]):

Compose an UPDATE Request primitive. The To parameter in the UPDATE Request shall be set to the URI for the announced resource. The UPDATE Request shall set the attribute that will be de-announced (i.e. to be deleted) in the Content parameter to NULL. The attribute that will be de-announced shall be marked as OA.

Send UPDATE Requests to all announced resources listed in the announceTo attribute of the original resource.

Wait for the Response primitive(s).

Delete the attribute name of the successfully de-announced attribute from the announcedAttribute attribute.

Include updated announcedAttribute attribute in the Content parameter in the Response to the received UPDATE Request.

If an UPDATE request is received that deletes attribute(s) that are specified as MA (see oneM2M TS-0001 [6]) or deletes attribute(s) included in the announcedAttribute attribute:

Compose an UPDATE Request primitive by including the deleted attribute(s) with its value set to NULL.

Send the UPDATE Request to all CSE(s) represented by the URI(s) in the announceTo attribute of the original resource.

Wait for the Response primitive(s).

Delete the attribute name of the successfully de-announced attribute from the announcedAttribute attribute if it was present.

7.3.3.12	Create a success response

The Hosting CSE shall create a success response primitive with a Response Status Code indicating:

"CREATED" in case of Create operation;

"OK" in case of Retrieve operation;

"UPDATED" in case of Update operation;

"DELETED" in case of Delete operation; and

"OK" in case of Notify operation.

The Hosting CSE shall include Request Identifier parameter in the response primitive. The Release Version Indicator parameter shall be included unless the primitive is being sent to a Release 1 entity.

If the Result Content is not given in the Request, the default value for Delete is 0 (nothing), for Create/Retrieve/Update it is 1 (all attributes).

The Hosting CSE shall include the Content parameter in a Retrieve Response.

For Create/Update operation, if Result Content is modified-attributes then the Content parameter shall only be present if attributes which were not in the request Content  parameter were added, modified or deleted or if any attributes were set to values different from the values specified in the request Content parameter. The deleted attributes to be returned shall be set to NULL values in the response Content parameter.

The Hosting CSE shall not include the Content parameter in a Create/Update/Delete Response if Result Content is set to 0 (nothing).

The information of the Content parameter shall comply to the value of the Result Content request parameter of the corresponding Request.

More details can be found in clause 7.2.1.2 (Response primitive format).

The response content serialization shall use the type indicated in the received request. If a content serialization cannot be determined from the request then the serialization of the response shall use one of the serialization types specified in the contentSerialization attribute of the originator.

The Hosting CSE may include To, From, Originating Timestamp, Result Expiration Timestamp, Event Category parameters.

7.3.3.13	Create an error response

The receiver shall create an error response primitive with a Response Status Code indicating the detected error condition.

The response content serialization shall use the type indicated in the received request. If a content serialization cannot be determined from the request then the serialization of the response shall use one of the serialization types specified in the contentSerialization attribute of the originator.

NOTE:	Possible error codes and error handling is described in resource specific procedures.

7.3.3.14	Resource discovery procedure

If the Operation Execution Time is given in the request, the Hosting CSE should perform the following procedures at the time and shall not perform the procedures before the time.

Resource discovery is used to discover resources in a CSE. A Resource discovery request is done by sending a Retrieve request with filterUsage, one of the Filter Criteria parameters, configured as "Discovery" and the request may include other Filter Criteria parameters as well. A resource discovery request procedure shall be comprised of the following actions.

Originator:

The Originator shall follow the steps from Orig-1.0 to Orig-6.0 specified in clause 7.2.2.1 Generic Resource Request Procedure for Originator.

In addition to Orig-1.0, the following steps shall be performed.

The To parameter in the Retrieve Request indicates the root of where the discovery begins.

The Retrieve Request shall include a Filter Criteria request parameter that includes a filterUsage element configured with either "Discovery Criteria" or "IPE On-demand Discovery".

The Retrieve Request may include other elements of Filter Criteria.

Receiver:

The Receiver shall follow the steps from Recv-1.0 to Recv-7.0 specified in clause 7.2.2.2.

The Hosting CSE shall not perform steps from Recv-6.3 to Recv-6.6 but perform the following steps instead.

The Receiver shall find the resources that match all the configured Filter Criteria and to which the Originator has "Discover" privilege, among all the children/descendent resource of the addressed resource. As part of this search, the Receiver will not consider any child/descendent <AE> resource with registrationStatus attribute set to INACTIVE, and any child/descendent resources of this INACTIVE <AE> resource.

If the addressed resource is an <AE> resource representing the IPE by its labels attribute, the Hosting CSE shall find resources using the Filter Criteria. When the Hosting CSE finds no match, the Hosting CSE shall check the filterUsage element. If the filterUsage element is set to "IPE On-demand Discovery", then the Hosting CSE shall send the Notify request to the IPE to trigger the external discovery procedure (see clause 7.5.1.2.8 for more details). If the Hosting CSE receives a successful Notify response, the Hosting CSE shall find resources among the resources on the Hosting CSE listed in the Notify response using the Filter Criteria and check the Originator's "Discover" privilege. If the Hosting CSE receives an unsuccessful Notify response from the IPE, then the Hosting CSE shall use the same Response Status Code in the response to the Originator.

In Recv-6.7, the Receiver shall include addresses for all the found resources in the CSE-relative resource identifier format.

The Receiver shall perform Recv-6.8 and the procedure is terminated.

7.3.3.15	Check authorization of the originator

If the target resource contains the accessControlPolicyIDs attribute, the Hosting CSE shall use the linked <accessControlPolicy> resources as in the evaluation procedure below. See clause 9.6.1.3.2 in oneM2M TS-0001 [6] for how to handle the case where the target resource has no accessControlPolicyIDs attribute.

The evaluation procedure shall be performed as following:

The Hosting CSE retrieves the access control rules from privilege attribute of the <accessControlPolicy> which is linked as the accessControlPolicyIDs. If the target is <accessControlPolicy> resource, it retrieves the rules from selfPrivilege attribute instead.

The Hosting CSE checks the following conditions for the access control rules. If there is any rule satisfying all conditions then the evaluation is successful, otherwise access is denied. For more details, see clause 7.1.5 in oneM2M TS-0003 [7].

accessControlOriginators of the rule includes the Originator information. The accessControlOriginators parameter comprises a list of domain, CSE-IDs, AE-IDs, the resource-ID of a <group> resource that contains <AE> or <remoteCSE> as member or Role-ID. The accessControlOriginators parameter can be set to reserved keyword "all" to grant access to all originators. It is allowed to include the wildcard character, "*", into the URI string of domain, CSE-ID and AE-ID at any level. See clause 9.6.2.1 in oneM2M TS-0001 [6].

Table 7.3.3.15-1: Types of Parameters in accessControlOriginators

accessControlContexts of the rule includes the request context, if the rule includes the accessControlContexts.

If the accessControlOriginators includes a groupID, the Hosting CSE checks if the Originator is a member of that group resource.

accessControlOperations of the rule matches the operation type of the request.

If the accessControlAuthenticationFlag is true, then access control rule applies only if the Originator is considered to be authenticated by the Hosting CSE according to clause 7.1.2 in oneM2M TS-0003 [7].

If the evaluation of these access control rules results in access being permitted, the authorization check process ends. If the result is "DENY", the Hosting CSE proceeds with Dynamic Authorization (see clause 7.3 in oneM2M TS-0003 [7]) if it supports that.

If Dynamic Authorization returns "PERMIT", the authorization check process ends. If the result is "DENY" the Hosting CSE proceeds with Distributed Authorization (see clause 7.5 in oneM2M TS-0003 [7]) if it supports that. If this returns "PERMIT", the authorization check process ends.

If the Hosting CSE reaches the point where it has tried all the authorization processes that it supports and they have all returned "DENY" the Hosting CSE shall reject the request with an "ORIGINATOR_HAS_NO_PRIVILEGE" Response Status Code parameter value.

7.3.3.16	Send response primitive

A Response primitive shall be sent back to the Originator. If the primitive is successful response and the Result Expiration Timestamp is given in the request, then the Hosting CSE or Transit CSE should send the primitive before the Result Expiration Timestamp.

7.3.3.17	Using Filter Criteria for identification of target resources

7.3.3.17.0	Introduction

When the Filter Criteria primitive parameter is present in a request primitive, it shall be applied for identification of the applicable target resources of the respective operation. This may apply to Retrieve, Delete, Discovery and Semantic Resource Discovery operations as specified in clauses 7.3.3.6, 7.3.3.8, 7.3.3.14 and 7.3.3.18 respectively.

The Filter Criteria primitive parameter defines matching conditions on resource attributes and filter handling conditions. Matching conditions are evaluated against resources and, when true, determine the matched resources. The filter handling conditions provide additional input applied to the matched resource set to determine the filtering result (e.g. maximum number of resources to be included in the filtering result). The filtering result may be composed of one or more resources and shall be used as the target of the operation. Table 7.3.3.17.0-1 summarizes the various filter criteria and conditions. Each row in the table represents a different filter condition type.

If multiple matching conditions of the same type (i.e. same condition tag) are present in the Filter Criteria parameter, these shall be combined by applying logical OR operation.

If multiple matching conditions of different type (i.e. different condition tags) are present in the Filter Criteria parameter, then the combined condition shall be derived by applying the logical operation specified by the filterOperation condition. By default logical AND operation shall be used if the filterOperation condition is not present.

EXAMPLES:

labels="floor1", stateTagSmaller=3 will match if both conditions are true [default AND when filterOperation is not specified]

labels="floor1", stateTagSmaller=3, filterOperation=1 will match if both conditions are true

labels="floor1", stateTagSmaller=3, filterOperation=2 will match if either condition is true

labels="floor1 floor2", filterOperation=1 will match if either of the two labels match [filterOperation has no effect when there is only one condition tag]

"labels=floor1 floor2", stateTagSmaller=3, labels=floor2, filterOperation=2 will match if any of these conditions are true resource has [labels with value "floor1" OR "floor2"] OR stateTagSmaller than 3

Table 7.3.3.17.0-1: Summary on Filter conditions

7.3.3.17.1	Conditions on the creationTime attribute

The Filter Criteria elements createdBefore and createdAfter define a time interval which is tested against the creationTime attribute of the applicable resources in order to determine the matching resources.

This filter criterion shall be satisfied if any of the following three conditions is fulfilled:

only createdBefore given in Filter Criteria: 
creationTime < createdBefore

only createdAfter given in Filter Criteria:
createdAfter ≤ creationTime)

both createdBefore and createdAfter given in Filter Criteria: 
(createdAfter ≤ creationTime) AND (creationTime < createdBefore)

NOTE:	In case 3) the Filter Criteria will only generate a match if createdAfter < createdBefore.

7.3.3.17.2	Conditions on the lastModifiedTime attribute

The Filter Criteria elements lastModifiedBefore and lastModifiedAfter define a time interval which is tested against the lastModifiedTime attribute of the applicable resources in order to determine the matching resources.

This filter criterion shall be satisfied if any of the following three conditions is fulfilled:

only unmodifiedSince given in Filter Criteria: 
lastModifiedTime < unmodifiedSince

only modifiedSince given in Filter Criteria: 
modifiedSince ≤ lastModifiedTime

both unmodifiedSince and modifiedSince given in Filter Criteria: 
(modifiedSince ≤ lastModifiedTime) AND (lastModifiedTime < unmodifiedSince))

NOTE:	In case 3) the Filter Criteria will only generate a match if modifiedSince < unmodifiedSince.

7.3.3.17.3	Conditions on stateTag attribute

The Filter Criteria elements stateTagSmaller and stateTagBigger define a number range which is tested against the stateTag attribute of the applicable resources in order to determine the matching resources.

This filter criterion shall be satisfied if any of the following three conditions is fulfilled:

only stateTagSmaller given in Filter Criteria: 
stateTag < stateTagSmaller

only stateTagBigger given in Filter Criteria: 
stateTagBigger ≤ stateTag

both stateTagSmaller and stateTagBigger given in Filter Criteria:
(stateTagBigger ≤ stateTag) AND (stateTag < stateTagSmaller)

NOTE:	In case 3) the Filter Criteria will only generate a match if stateTagBigger < stateTagSmaller.

7.3.3.17.4	Conditions on expirationTime attribute

The Filter Criteria elements expireBefore and expireAfter define a time interval which is tested against the expirationTime attribute of the applicable resources in order to determine the matching resources.

This filter criterion shall be satisfied if any of the following three conditions is fulfilled:

only expireBefore given in Filter Criteria: 
expirationTime < expireBefore

only expireAfter given in Filter Criteria: 
expireAfter ≤ expirationTime

both expireBefore and expireAfter given in Filter Criteria:
(expireAfter ≤ expirationTime) AND (expirationTime < expireBefore)

NOTE:	In case 3) the Filter Criteria will only generate a match if expireAfter < expireBefore.

7.3.3.17.5	Conditions on labels attribute

Each of the Filter Criteria elements labels, childLabels and parentLabels defines a list of labels which is tested against the labels attribute of applicable resource instances in order to determine the matching resources.

This filter criterion shall be satisfied if any of the labels in Filter Criteria matches any of the labels in the respective resource attribute. The matched resources are:

the resources with the matched label attribute, when applying the Filter Criteria element labels;

the parent resources of the resources with the matched label attribute, when applying the Filter Criteria element childLabels;

the child resources of the resources with the matched label attribute, when applying the Filter Criteria element parentLabels.

7.3.3.17.6	Conditions on resourceType attribute

Each of the Filter Criteria elements resourceType, childResourceType and parentResourceType defines a list of resource types which is tested against the resourceType attribute of the applicable resource instances in order to determine the matching resources.

This filter criterion shall be satisfied if any of the numbers in the resourceType Filter Criteria element matches the resourceType attribute. The matched resources are:

the resources with the matched resourceType attribute, when applying the Filter Criteria element resourceType;

the parent resources of the resources with the matched resourceType attribute, when applying the Filter Criteria element childResourceType;

the child resources of the resources with the matched resourceType attribute, when applying the Filter Criteria element parentResourceType.

7.3.3.17.7	Conditions on contentSize attribute

The Filter Criteria elements sizeBelow and sizeAbove define a number range which is tested against the value of the contentSize attribute of applicable <contentInstance> resources in order to determine the matching resources.

This filter criterion shall be satisfied if any of the following three conditions is fulfilled:

only sizeBelow given in Filter Criteria: 
contentSize < sizeBelow

only sizeAbove given in Filter Criteria: 
sizeAbove ≤ contentSize

both sizeBelow and sizeAbove given in Filter Criteria:
(sizeAbove ≤ contentSize) AND (contentSize < sizeBelow)

NOTE:	In case 3) the Filter Criteria will only generate a match if sizeAbove < sizeBelow.

7.3.3.17.8	Conditions on typeOfContent of contentInfo attribute

The Filter Criteria element contentType defines a string (or multiple such strings) which is compared against the contentInfo attribute of applicable <contentInstance> resources in order to determine the matching resources.

One or multiple such contentType elements may be included in the Filter Criteria parameter.

This filter criterion shall be satisfied if any of the contentType elements in Filter Criteria matches the typeOfContent part of the contentInfo attribute in a <contentInstance> resource.

7.3.3.17.9	Conditions on attribute name and value pairs

Each of the Filter Criteria elements attribute, childAttribute and parentAttribute defines one or more attribute name/value pairs (see clause 6.3.5.8) that are compared against all applicable resource representations which include a resource attribute with a name matching the attribute name in the Filter Criteria, in order to determine the matching resources.

This filter criterion shall be satisfied if any of the attribute elements in the Filter Criteria parameter matches both attribute name and attribute value in any applicable resource representation.

The following attributes shall not be used for this condition as they may conflict with other Filter Criteria parameters: creationTime, lastModifiedTime, stateTag, expirationTime, labels, resourceType, contentSize and contentInfo.

The attribute value may include wildcard (*) in case of discovery requests. The wildcard (*) can match 0 or more characters. For example, a wildcard can be used within the value of a creator attribute condition (E.g.creator=CAE-ID* or creator=*ID123).

The matched resources are:

the resources with the matched attribute elements, when applying the Filter Criteria element resourceAttribute;

the parent resources of the resources with the matched attribute elements, when applying the Filter Criteria element childAttribute;

the child resources of the resources with the matched attribute elements, when applying the Filter Criteria element parentAttribute.

7.3.3.17.10	Constraint on number of retrieved resources by limit element

The limit element of the Filter Criteria parameter does not represent a matching condition. It imposes a limit on the number of resources that should be retrieved with the given Retrieve request primitive.

The number of resources retrieved with the request primitive (and to be included into the corresponding response primitive) shall not exceed the number indicated in the limit element of the Filter Criteria parameter.

7.3.3.17.11	Filter Usage request parameter

The filterUsage element of the Filter Criteria parameter does not represent a matching condition. It indicates how the Filter Criteria parameter shall be used. If this parameter is not provided, the Retrieve request primitive which includes this element triggers a generic retrieve operation. The data type of filterUsage is defined in clause 6.3.4.2.31.

7.3.3.17.12	Filter Operation request attribute

The filterOperation element of the Filter Criteria parameter does not represent a matching condition. It indicates the logical operation to be performed between the condition tags when multiple condition tags of different types are specified. If this parameter is not provided logical AND operation shall be used by default. The data type of filterOperation is defined in clause 6.3.4.2.34.

7.3.3.17.13	Conditions on content-based discovery

7.3.3.17.13.1	Introduction

The Filter Criteria elements contentFilterSyntax and contentFilterQuery are used for "content based discovery".

The contentFilterSyntax element specifies the syntax to be used by the contentFilterQuery element to express the content-based discovery conditions. A contentFilterQuery shall be included if the contentFilterSyntax parameter is present.

The contentFilterQuery element contains the query expression for content-based discovery.

7.3.3.17.13.2	JSON path syntax

When the contentFilterSyntax element has the value "JSON_PATH_SYNTAX", the contentFilterQuery element shall be expressed using "jsonpath query syntax" (see clause K.2 of oneM2M TS-0001 [6]).

7.3.3.17.14	Constraint on number of applicable levels in resource tree

The level element of the Filter Criteria parameter does not represent a filter condition. It imposes a maximum limit on the depth of child resources in the resource tree that the Hosting CSE shall perform a Retrieve request upon. The level of 1 shall indicate the direct child resources.

7.3.3.17.15	Constraint on number of resources to skip over in retrieve response

The offset element of the Filter Criteria parameter does not represent a filter condition. It specifies the number of direct child resources and their descendants that the Hosting CSE shall skip over and not include within the response to a Retrieve request primitive. An offset of 1 shall indicate the first direct child resource.

7.3.3.17.16	Conditions on labelsQuery attribute

The Filter Criteria element labelsQuery contains a list of expressions to be tested against the labels attribute of the applicable resource instances.

This filter criterion shall be satisfied if any of the expressions in Filter Criteria matches the labels in the respective resource attribute.

Expressions can be in the following formats:

key

Matches if labels attribute of the resource contains the key either in a key-only or key-value format.

For example: labels = color will match resources with labels defined as "color", "color:red" or "color:green".

NT key

NT stands for not. Matches if labels attribute of the resource does not contain the key either in a key-only or key-value format.

For example: labels = NT color will match resources with labels that do not include "color" as a key.

Key EQ value or key:value

EQ stands for equals. Matches if labels attribute of the resource contains the key-value pair.

For example: labels = color EQ red will match resources with labels that contains "color:red". Labels = color:red will match resources with labels defined as "color:red".

Key NE value

NE stands for Not Equals to. Matches if the labels attribute of the resource contains at least one key-value pair that matches the key but none of these key-value pairs matches the value.

For example: labels = color NE red will match resources with labels that contains one key of "color" but with value not "red".

Key IN (value1, value2…)

Matches if the labels attribute of the resource contains at least one key-value pair matching the key and one of the value listed.

For example: labels = color IN (red, green) will match resources with labels that contains "color:red" or "color:green"

Key NI (value1, value2…)

NI stands for Not In. Matches if the labels attribute of the resource contains at least one key-value pair matching the key but none of these key-value pairs have any of the values listed.

For example: labels = color NI (red, green) will match resources with labels that contains "color:yellow" or "color:blue". Any resource that has label "color:red" or "color:green" will not be matched.

7.3.3.17.17	Applying a relative path

The applyRelativePath element of the Filter Criteria parameter does not represent a matching condition, it is a condition which applies after all the matching conditions have been used (i.e. a matching result has been obtained) in order to determine the set of resources in the final filtering result. The filtering result is computed by appending the relative path to each of the URIs of the resources in the matching result. All resources that exist at the resulting path(s) shall form the filtering result. If the combined relative path does not represent a valid resource, the outcome is the same as if no match was found, i.e. there is no corresponding entry in the filtering result.

7.3.3.18	Semantic resource discovery

7.3.3.18.0	Introduction

Semantic resource discovery is used to find resources in a CSE based on the semantic descriptions contained in the descriptor attribute of <semanticDescriptor> resources. Since an overall semantic description (forming a graph [i.5]) may be distributed across a set of <semanticDescriptor> resources, the semantic descriptions have to be retrieved (before or as needed) during the execution of the discovery request.

Semantic resource discovery is initiated by sending a Retrieve request with the discovery criteria in the semanticsFilter filter condition(s) with two alternatives:

Targeting a <semanticFanOutPoint> virtual resource, see clause 7.4.35.

Targeting a resource other than <semanticFanOutPoint>. In this alternative the semantic resource discovery request procedure shall be comprised of the following actions:

Originator:

The Originator shall follow the steps from Orig-1.0 to Orig-6.0 specified in clause 7.2.2.1 Generic Resource Request Procedure for Originator.

In addition to Orig-1.0, the following steps shall be performed.

The To parameter in the Retrieve Request shall indicate the root of where the semantic discovery begins.

The filterCriteria of the Retrieve Request shall include the filterUsage parameter configured as "discovery" and the semanticsFilter filter condition.

Receiver:

The Receiver shall follow the steps from Recv-1.0 to Recv-7.0 specified in clause 7.2.2.2 Generic Resource Request Procedure for Receiver.

After Recv-1.0 "Check the validity of received request primitive": check that the syntax of the semanticsFilter corresponds to a valid SPARQL query request [33]. If the semanticsFilter content does not correspond to a valid SPARQL query request, the Receiver shall generate a Response Status Code indicating an "INVALID_SPARQL_QUERY" error.

The Hosting CSE shall follow the steps from Recv-1.0 to Recv-6.2 specified in clause 7.2.2.2.The Hosting CSE shall not perform steps from Recv-6.3 to Recv-6.6 and perform the following steps instead:

The Hosting CSE shall find the <semanticDescriptor> resource(s) to which the Originator has "Discover" access right, under the addressed resource.

a)	If the relatedSemantics attribute does not exist, the "Annotation-based method" (using resourceDescriptorLink) detailed in clause 7.3.3.18.1 shall be used.

b)	If the relatedSemantics attribute exists the "Resource link-based method" (using the relatedSemantics attribute) detailed in clause 7.3.3.18.2 shall be used.

The Hosting CSE shall perform Recv-6.7 "Create a success response" where the Response shall include the resources matched based on the SPARQL engine result.

7.3.3.18.1	Annotation-based method

In the annotation-based method, related <semanticDescriptor> resources are identified within the RDF semantic description itself using a special annotation property called m2m:resourceDescriptorLink. This property points to another <semanticDescriptor> resource which may contain relevant information for matching the semantic filter. Whenever, during the execution of the SPARQL request (on the semantic description in the descriptor attribute of the <semanticDescriptor>) such an annotation property is found, the execution is halted, the content of the descriptor attribute of the referred to <semanticDescriptor> is retrieved, and the execution is continued on the combined content of the already present and the just retrieved semantic information.

7.3.3.18.2	Resource link-based method

In this option, the relatedSemantics attribute contains the list of <semanticDescriptor> resources which shall be retrieved for the purpose of creating the overall graph against which the SPARQL request is executed.

The Hosting CSE retrieves the <semanticDescriptor> child resource of the request target and the addresses provided in the relatedSemantics attribute. For each address from the relatedSemantics list the Hosting CSE:

checks that the Originator has "Discover" access rights, and the existence of the addressed resource;

retrieves the description in the descriptor attribute under the addressed resource.

The Hosting CSE shall aggregate all the retrieved descriptors and deliver the content for SPARQL request processing, along with the semanticsFilter content.

NOTE:	In the resource link-based method, no actions need to be performed during the execution of the SPARQL request if the notation property onem2m:resourceDescriptorLink is encountered.

Afterwards, the Hosting CSE performs Recv-6.7 "Create a success response" where the Response shall include the resources matched based on the SPARQL engine result.

7.3.3.19	Semantic query

7.3.3.19.0	Introduction

Semantic queries enable the retrieval of both explicitly and implicitly derived information based on syntactic, semantic and structural information contained in data (such as RDF data). The result of a semantic query is the semantic information/knowledge for answering/matching the query. The SPARQL query result shall use the XMLor JSON formats defined by the W3C [57], [58]. The XML result format shall be used for XML serialized response primitives. The JSON result format shall be used for JSON or CBOR serialized response primitives. Note that, in the following descriptions, the general term semantic resource is used to refer to <semanticDescriptor> resources and any other future resources containing semantic information.

A given semantic query needs to be executed on a set of RDF triples (called the "RDF data basis"), which may be distributed in the resource tree and stored in different semantic resources. The Receiver shall perform semantic graph scoping, which is the process of establishing the "query scope" for this semantic query in order to build its RDF data basis. The following two approaches may be used to decide the semantic query scope of a semantic query:

Approach-1: The scope of the semantic query is provided implicitly.

Approach-2: The scope of the semantic query is provided explicitly

7.3.3.19.1	Approach-1: Semantic query with implicit scope

In Approach-1, a semantic query request message targets any resource (i.e. as specified by the To parameter) and the semantic query shall be executed relative to this target resource, similarly to other request messages. The scope of the semantic query is formed through the aggregation of the semantic contents of the target resource's descendants. All the contents of semantic resource descendants of the target resource shall form the RDF data basis for this semantic query to be executed on. In this alternative, the semantic query procedure shall be comprised of the following actions:

Originator:

The Originator shall follow the steps from Orig-1.0 to Orig-6.0 specified in clause 7.2.2.1 Generic Resource Request Procedure for Originator.

In addition to Orig-1.0, the following steps shall be performed.

The To parameter in the Retrieve Request shall define the scope of this semantic query as mentioned earlier.

The Retrieve Request shall include the following parameters:

the Semantic Query Indicator, which is set to true;

filterCriteria of the Retrieve Request shall include the semanticsFilter condition tag; and

the parameter Result Content shall be set to "semantic content" to indicate that the response message shall contain the result of a semantic query.

Receiver:

The Receiver shall follow the steps from Recv-1.0 to Recv-7.0 specified in clause 7.2.2.2 Generic Resource Request Procedure for Receiver.

After Recv-1.0 "Check the validity of received request primitive": check that the syntax of the semanticsFilter corresponds to a valid SPARQL query request [33]. If the semanticsFilter content does not correspond to a valid SPARQL query request, the Receiver shall generate a Response Status Code indicating an "INVALID_SPARQL_QUERY" error.

The Hosting CSE shall follow the steps from Recv-1.0 to Recv-6.2 specified in clause 7.2.2.2. The Hosting CSE shall not perform steps from Recv-6.3 to Recv-6.6 and perform the following steps instead:

The Hosting CSE shall find the semantic resources to which the Originator has "RETRIEVE" access right, under the addressed resource as specified by the To parameter.

Aggregate the semantic resources and deliver the content for SPARQL processing, along with the semanticsFilter content.

Wait for a SPARQL processing response.

Perform Recv-6.7 "Create a success response" where the Response shall include the SPARQL processing result, which is the semantic query result to be returned.

Perform Recv-6.8 and the procedure is terminated.

7.3.3.19.2	Approach-2: Semantic query with explicit scope

In Approach-2, the relevant semantic resources are the members of a <group> resource. The scope of the semantic query is formed through the aggregation of the semantic contents of all the group members. In this approach, the request targets the <semanticFanOutPoint> (as specified by the To parameter), i.e. the child resources of the <group> resource. As a result, this <group> resource explicitly specifies the RDF data basis of the semantic query. The details of Approach-2 are introduced in clause 7.4.35.


### 7.3.4	Management common operations


7.3.4.1	Identify the managed entity and the technology specific protocol

Where a managed entity is being addressed via a <mgmtObj> resource, the Hosting CSE shall identify the managed entity via the <node> resource that is the parent resource of the <mgmtObj> resource. In case of a <mgmtCmd> resource the entity to be managed is indicated by its execTarget attribute. This addresses either a <node> resource or a group of resources of type <node>. Hence, in all cases the managed entity is ultimately identified through a <node> resource, from which the identifier of the device can be retrieved.

The Hosting CSE shall determine the technology specific protocol to be used for communicating with the managed entity based on the objectIDs attribute of the addressed <mgmtObj> resource.

If the managed entity cannot be identified, the Hosting CSE shall reject the request with the Response Status Code indicating "EXTERNAL_OBJECT_NOT_REACHABLE" in the Response primitive.

7.3.4.2	Locate the technology specific data model objects to be managed on the managed entity

The Hosting CSE shall locate the technology specific data model object to be managed on the managed entity by the objectPaths attribute of the <mgmtObj> resource addressed by the URI provided in the To primitive parameter. In the case that the To addresses an [objectAttribute], the Hosting CSE shall locate the technology specific data model object on the managed entity through the objectPaths attribute of the <mgmtObj> resource of the addressed [objectAttribute], combined with their relative position in the technology specific data model object tree. If the technology specific data model object cannot be located, the Hosting CSE shall reject the request with the Response Status Code indicating "EXTERNAL_OBJECT_NOT_FOUND" in the Response primitive.

In the case that the management server is external to the Hosting CSE, the Hosting CSE shall identify the management server that is capable of performing the operation on the technology specific data model object. If the management server cannot be identified, the Hosting CSE shall reject the request with the Response Status Code indicating "EXTERNAL_OBJECT_NOT_REACHABLE" in the Response primitive.

7.3.4.3	Establish a management session with the managed entity or management server

In the case that the management server is embedded with the CSE, if there is no existing management session between the Hosting CSE and the managed entity, the Hosting CSE shall also trigger the managed entity to establish a management session with the Hosting CSE by sending triggering message to the managed entity using the determined technology specific protocol in case such triggering mechanism is supported by the technology specific protocol. If the triggering mechanism is not supported by the technology specific protocol, the Hosting CSE shall reject the request with the Response Status Code indicating "MGMT_SESSION_CANNOT_BE_ESTABLISHED". If the management session cannot be established with the managed entity, the Hosting CSE shall reject the request with the Response Status Code indicating "MGMT_SESSION_CANNOT_BE_ESTABLISHED". If the management session cannot be established within a limited time span as per local policy, the Hosting CSE shall reject the request with the Response Status Code indicating "MGMT_SESSION_ESTABLISHMENT_TIMEOUT" in the Response primitive.

In the case that the management server is external to the Hosting CSE, if there is no existing management session between the Hosting CSE and the management server that manages the technology specific data model objects, the Hosting CSE shall establish a session with the managed entity with the necessary access control privileges to perform the technology specific request on the technology specific protocol. If the management session cannot be established with the management server, the Hosting CSE shall reject the request with Response Status Code indicating "MGMT_SESSION_CANNOT_BE_ESTABLISHED". If the management session cannot be established within a limited time span as per local policy, the Hosting CSE shall reject the request with Response Status Code indicating "MGMT_SESSION_ESTABLISHMENT_TIMEOUT" in the Response primitive.

7.3.4.4	Send the management request(s) to the managed entity corresponding to the received Request primitive

The Hosting CSE shall send the management request(s) to the managed entity or management server in the established management session in order to perform the management operation as requested by the received Request primitive. The management request shall address the technology-specific data model object on the managed entity as determined in clause 7.3.4 or in the primitive-specific clauses. The management request being used is specific to the technology specific protocol according to a pre-defined mapping relationship with the Request primitive. The internal data structure of the technology specific data model object addressed by the technology specific request shall be determined based on the mapping relationship of the <mgmtObj> or <mgmtCmd> resources and the technology specific data model objects or based on the generic mapping rule as specified in oneM2M TS-0001 [6], clauses 9.6.15, 9.6.16 and 9.6.17. The Hosting CSE shall extract the management results received from the managed entity or management server in order to prepare a Response primitive to be sent to the originator later. Unless explicitly stated, if the management request cannot be performed successfully, the Hosting CSE shall reject the Request primitive with the management server in the Response primitive according to the mapping relationship with the technology specific protocol.


## 7.4	Resource type-specific procedures and definitions



### 7.4.0	Introduction


This clause specifies the structure of each individual resource type and the resource type specific details of procedures (i.e. differences from the generic procedures specified in clauses 7.2 and 7.3) to be performed by the originator and receiver of a request message.

The applicability of each of the following resource type-specific procedures to an interface reference point (i.e. Mca, Mcc and Mcc') is defined in clause 10.2 (Resource Type-Specific Procedures) of oneM2M TS-0001 [6].


### 7.4.1	Resource type specification conventions


7.4.1.1	Resource type definition conventions

This clause provides general information on conventions applied to resource type specifications and how to interpret the provided information. Each resource type is defined in a tabular format as shown in the tables below. A reference to the XSD file associated with the given resource type is provided in the format shown in Table 7.4.1.1-1. Further information on usage and limitations of the XSD is given in clause 6.1.

Table 7.4.1.1-1: Data type definition of <resourceType>

Information about universal/common resource attributes of a resource type is provided in the format shown in Table 7.4.1.1-2. The column "Request optionality" specifies the presence of each resource attribute in the Content parameter of the request primitive. This is defined as Mandatory (M), Optional (O), or NP (Not Present). The table applies only to Create and Update operations. A Retrieve request operation may include a Content parameter containing a list of attribute names to be retrieved. A Delete request shall not include a Content parameter.

Universal/common resource attributes do not have any default value. However, value restrictions and notes given in Table 6.3.6-1 apply.

Table 7.4.1.1-2: Universal/Common Attributes of <resourceType> resource

Information about resource specific attributes of the resource type is provided in the format shown in Table 7.4.1.1-3. Request optionality shall be interpreted the same way as described for universal/common attributes above.

Table 7.4.1.1-3: Resource Specific Attributes of <resourceType> resource

Request primitives shall comply with the request optionality of universal/common and resource specific attributes in Create and Update request primitives as defined for each individual resource type in the following clauses. The values of each resource attribute shall comply with its assigned datatype and any indicated constraints. See clause 6.1 for limitations on using the XSD files associated with the resource type for validation of compliance.

Table 7.4.1.1-4 provides the information of child resources of the resource type.

Table 7.4.1.1-4: Child resources of <resourceType> resource

7.4.1.2	Resource type-specific procedure conventions

This clause describes resource type specific procedures referring to generic procedures defined in clause 7.2.2. Each operation specific procedure describes procedures for the Originator and the Receiver. If the resource and operation specific procedure is the same as the generic procedure, the Originator and Receiver procedure refer to them. Otherwise, the deviation/addition is clearly described with related procedure numbers (e.g. Recv 6.1) in clause 7.2.2.

If a deviation/addition procedure includes sub-procedures in one more level(s), proper numbering is used to show the levels (e.g. "1)", "a)"). If sub-procedures do not care about the order, bullets are used instead of numbers.


### 7.4.2	Resource type <accessControlPolicy>


7.4.2.1	Introduction

The <accessControlPolicy> resource is comprised of privileges and selfPrivileges attributes which represent a set of access control rules defining which entities (defined as accessControlOriginators) have the privilege to perform certain operations (defined as accessControlOperations) within specified contexts (defined as accessControlContexts) and are used by the CSEs in making access decision to specific resources.

The detailed description can be found in clause 9.6.2 in oneM2M TS-0001 [6].

Table 7.4.2.1-1: Data type definition of <accessControlPolicy> resource

Table 7.4.2.1-2: Universal/Common Attributes of <accessControlPolicy> resource

Table 7.4.2.1-3: Resource Specific Attributes of <accessControlPolicy> resource

Table 7.4.2.1-4 includes information about the child resources of the resource type.

Table 7.4.2.1-4: Child Resources of <accessControlPolicy> resource

7.4.2.2	accessControlPolicy resource specific procedures for CRUD operations

7.4.2.2.0	Introduction

This clause describes accessControlPolicy resource-specific behaviour for CRUD operations.

7.4.2.2.1	Create

Originator:

No changes from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the <accessControlPolicy> received does not have at least one accessControlRule specified in the selfPrivileges attribute then "Create an unsuccessful Response primitive" with the Response Status Code indicating "BAD_REQUEST" error.

7.4.2.2.2	Retrieve

Originator:

No changes from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.2.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the <accessControlPolicy> received removes all accessControlRules specified in the selfPrivileges attribute then "Create an unsuccessful Response primitive" with the Response Status Code indicating "BAD_REQUEST" error.

7.4.2.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.3	Resource Type <CSEBase>


7.4.3.1	Introduction

A <CSEBase> resource shall represent a CSE. This <CSEBase> resource shall be the root for all the resources that are residing on the CSE. The detailed description can be found in clause 9.6.3 in oneM2M TS-0001 [6].

Table 7.4.3.1-1: Data type definition of <CSEBase> resource

Table 7.4.3.1-2: Universal/Common Attributes of <CSEBase> resource

The value of the parentID attribute for the <CSEBase> resource shall be an empty string since the <CSEBase> resource does not have a parent. The common attributes accessControlPolicyIDs and dynamicAuthorizationConsultationIDs are treated as resource-specific attributes.

Table 7.4.3.1-3: Resource Specific Attributes of <CSEBase> resource

Table 7.4.3.1-4: Child resources of <CSEBase> resource

7.4.3.2	<CSEBase> resource specific procedures for CRUD+N operations

7.4.3.2.1	Create

Originator:

The <CSEBase> resource can not be created via API.

Receiver:

Not applicable.

7.4.3.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.3.2.3	Update

Originator:

The <CSEBase> resource shall not be updated via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order.

"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

"Send the Response primitive".

7.4.3.2.4	Delete

Originator:

The <CSEBase> resource shall not be deleted via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order.

a)	"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

b)	"Send the Response primitive".

7.4.3.2.5	Notify

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.4	Resource Type <remoteCSE>


7.4.4.1	Introduction

A <remoteCSE> resource shall represent a remote CSE that is registered to the Registrar CSE. <remoteCSE> resources shall be located directly under the <CSEBase> of the Registrar CSE.

In addition each registered CSE shall have a <remoteCSE> resource representing its Registrar CSE. This is located directly under the registered CSE's <CSEBase>.

The detailed description can be found in clause 9.6.4 in oneM2M TS-0001 [6].

Table 7.4.4.1-1: Data type definition of <remoteCSE> resource

Table 7.4.4.1-2: Universal/Common Attributes of <remoteCSE> resource

Table 7.4.4.1-3: Resource Specific Attributes of <remoteCSE> resource

Table 7.4.4.1-4: Child resources of <remoteCSE> resource

7.4.4.2	<remoteCSE> resource specific procedures for CRUD operations

7.4.4.2.0	Introduction

The entire CSE registration procedure including <remoteCSE> resource creation procedure below is defined in clause 10.1.1.2.1 in oneM2M TS-0001 [6] ("CSE registration procedure").

7.4.4.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1 with the following exception:

An AE shall not originate a Create <remoteCSE> resource request.

The Originator, upon receipt of successful CREATE response message, shall create a <remoteCSE> resource locally. It shall populate this resource with all the mandatory attributes for a <remoteCSE>.

The Originator may issue a RETRIEVE request to the registrar <CSEBase> to fetch additional information about the registrar CSE and add this information to its local <remoteCSE> resource. The Originator may choose which optional attributes to include in its <remoteCSE> resource.

Receiver:

Same as the generic procedures in clause 7.2.2.2 except replacement of Recv-6.3 step with following:

The Hosting CSE shall check if the credential provided by the Originator is valid.

If this check fails, then the Hosting CSE shall return a response primitive with a Response Status Code indicating a "SECURITY_ASSOCIATION_REQUIRED" error.

The Hosting CSE shall check the From parameter. If it contains an AE-ID the Hosting CSE shall reject the request with a Response Status Code indicating an “OPERATION_NOT_ALLOWED" error.

And addition of the following to step Recv-6.4:

If the Hosting CSE is an ASN-CSE, then it shall reject the request with Response Status Code indicating an “OPERATION_NOT_ALLOWED" error.

The Hosting CSE shall check for the presence of any resources having a CSE-ID that matches the one specified in the From parameter in the request and that have the same parent as the new resource being created.

If such a resource exists, then the Hosting CSE shall reject the request with a Response Status Code indicating an "ORIGINATOR_HAS_ALREADY_REGISTERED" error.

And addition of the following to step Recv-6.5:

The Receiver CSE shall set the CSE-ID attribute to the value carried in the From request parameter.

If the Receiver CSE has registered to another CSE, the Receiver CSE shall send an update request to its Registrar CSE to add the CSE-IDs of the Originator CSE and the Originator CSE's descendants into the descendantCSEs attribute of the Receiver CSE's <remoteCSE> hosted by the Registrar CSE.

7.4.4.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.4.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1 with the following exception:

An AE shall not originate a Update <remoteCSE> resource request.

Receiver:

Same as the generic procedures in clause 7.2.2.2 except addition of the following to step Recv-6.5:

If the descendantCSEs attribute is updated, and the Receiver CSE has registered to another CSE, the Receiver CSE shall send an update request to its Registrar CSE to make the corresponding updates to the descendantCSEs attribute of the Receiver CSE's <remoteCSE> hosted by the Registrar CSE.

7.4.4.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1 with the following exceptions:

An AE shall not originate a Delete <remoteCSE> resource request.

The Originator, upon receipt of successful DELETE response message, shall delete the corresponding <remoteCSE> resource locally.

Receiver:

Same as the generic procedures in clause 7.2.2.2 except addition of the following to step Recv-6.5:

If the Receiver CSE has registered to another CSE, the Receiver CSE shall send an update request to its Registrar CSE to delete the CSE-IDs of the Originator CSE and the Originator CSE's descendants from the descendantCSEs attribute of the Receiver CSE's <remoteCSE> hosted by the Registrar CSE.


### 7.4.5	Resource Type <AE>


7.4.5.1	Introduction

The <AE> resource represents information about an Application Entity known to a given Common Services Entity.

The detailed description can be found in clause 9.6.5 in oneM2M TS-0001 [6].

Table 7.4.5.1-1: Data type definition of <AE> resource

Table 7.4.5.1-2: Universal/Common Attributes of <AE> resource

Table 7.4.5.1-3: Resource Specific Attributes of <AE> resource

Table 7.4.5.1-4: Child resources of <AE> resource

7.4.5.2	<AE> resource specific procedures for CRUD+N operations

7.4.5.2.0	Introduction

This clause describes AE resource specific behaviour for CRUD+N operations.

The entire AE registration procedure including <AE> resource creation procedure below is defined in clause 10.1.1.2.2 of oneM2M TS-0001 [6] ("Application Entity registration procedure").

7.4.5.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1 with the with the following exception:

A CSE shall not originate a Create <AE> resource request.

Receiver:

Recv-6.0.1 "Requested operation is an AE registration?" will return Yes so Recv-6.0.2 step “ Check Service Subscription Profile” (refer to clause 7.3.2.7) shall be executed.

The generic procedures in clause 7.2.2.2 shall be executed except for Recv-6.3 which shall be skipped.

The following operations shall be added to step Recv-6.4:

The Hosting CSE shall check for the presence of any resources having an AE-ID that matches the one specified in the request and that have the same parent as the new resource being created.

If such a resource exists, then the Hosting CSE shall reject the request with a Response Status Code indicating an "ORIGINATOR_HAS_ALREADY_REGISTERED" error.

If the App-ID attribute is set to a value starting with anything other than ‘r’, 'R' or 'N' the Hosting CSE shall reject the request with a Response Status Code indicating a "BAD _REQUEST" error.

The following additional primitive specific operations shall be performed in Recv-6.5:

If the request is for an <AE> resource and if it is received at a MN-CSE or ASN-CSE with "/S" in the From parameter, but no specific AE-ID-Stem was provided with the CREATE request of the Registree AE, then this is an initial registration and the receiver shall execute the following steps in order:

a)	Compose a Create <AEAnnc> Request primitive with the following attribute values:

The link attribute of the <AEAnnc> resource to be created shall be set to the SP-Relative-Resource-ID format of a - not yet existent - <AE> resource hosted on the Registrar CSE constructed with a Unstructured-CSE-relative-Resource-ID that is equal to the AE-ID-Stem value used for the Registree AE.

The App-ID attribute of the <AEAnnc> resource to be created shall be set to the App-ID attribute value of the Registree AE.

The concatenation of the string 'Credential-ID:' and the actual Credential-ID of the Security Association used by the Registree AE - if any - shall be placed into the labels attribute of the <AEAnnc> resource. If no Security Association was used by the Registree AE, then no value shall be used for Credential-ID , i.e. the labels attribute shall include the string ‘Credential-ID:’.

b)	The From parameter of the CREATE request for the <AEAnnc> resource shall be set to the SP-relative-CSE-ID or Absolute-CSE-ID followed by '/S'.

c)	Send Create request to the IN-CSE that is associated with the Registree AE.

d)	Wait for Response primitive.

Upon receipt of a successful response from the IN-CSE, the Registrar/Host CSE shall use the Unstructured-CSE-relative-Resource-ID that was used for the <AEAnnc> resource on the IN-CSE also as the assigned Unstructured-CSE-relative-Resource-ID for the <AE> resource to be created on the Registrar/Host CSE.

If the request is for an <AE> resource and if it is received at a MN-CSE or ASN-CSE with an AE-ID-Stem starting with "S", and this is an initial registration or a re-registration to the same Registrar CSE, then the receiver shall execute the following steps in order:

a)	Determine if <AEAnnc> resource already exists in the IN-CSE for the Registree AE. If so, compose an Update <AEAnnc> Request primitive to update the <AEAnnc> resource. If no <AEAnnc> resource already exists in the IN-CSE for the Registree AE, the receiver shall compose a Create <AEAnnc> Request primitive. In both cases, the request primitive shall have the following attribute values:

The link attribute of the <AEAnnc> resource shall be set or updated to the SP-Relative-Resource-ID format of a - not yet existent - <AE> resource hosted on the Registrar CSE constructed with a Unstructured-CSE-relative-Resource-ID that is equal to the AE-ID-Stem value used for the Registree AE.

The labels attribute of the <AEAnnc> resource shall be set or updated to the concatenation of the string 'Credential-ID:' and the Credential-ID of the Security Association used by the Registree AE, replacing the existing entry starting with 'Credential-ID:' if present. If no Security Association was used by the Registree AE, then no value shall be used for Credential-ID, i.e. the labels attribute shall include the string ‘Credential-ID:’.

b)	The From parameter of the CREATE or UPDATE request for the <AEAnnc> resource shall be set to the SP-relative-CSE-ID or Absolute-CSE-ID followed by '/' and the AE-ID-Stem value.

c)	The To parameter shall contain the SP-relative-Resource-ID format of the Resource ID for the <AEAnnc> resource which shall be constructed from the CSE-ID of the IN-CSE and the AE-ID-Stem that the Registree AE provided.

d)	Send Create or Update request to the IN-CSE that is associated with the Registree AE.

e)	Wait for Response primitive.

Upon receipt of a successful response from the IN-CSE, the Registrar/Host CSE shall use the Unstructured-CSE-relative-Resource-ID equal to the AE-ID-Stem provided by the Registree AE for the <AE> resource to be created on the Registrar/Host CSE.

If the request is for an <AE> resource and if it is received at a MN-CSE or ASN-CSE with an AE-ID-Stem starting with "S", and this is a re-registration to a new Registrar CSE, then the receiver shall execute the following steps in order:

a)	Determine if <AEAnnc> resource already exists in the IN-CSE for the Registree AE. If so, compose an Update <AEAnnc> Request primitive to update the <AEAnnc> resource. If no <AEAnnc> resource already exists in the IN-CSE for the Registree AE, the receiver shall compose a Create <AEAnnc> Request primitive. In both cases, the request primitive shall have the following attribute values:

The link attribute of the <AEAnnc> resource shall be set or updated to the SP-Relative-Resource-ID format of a - not yet existent - <AE> resource hosted on the Registrar CSE constructed with an Unstructured-CSE-relative-Resource-ID that is equal to the AE-ID-Stem value used for the Registree AE.

The labels attribute of the <AEAnnc> resource shall be set or updated to the concatenation of the string 'Credential-ID:' and the Credential-ID of the Security Association used by the Registree AE, replacing the existing entry starting with 'Credential-ID:' if present. If no Security Association was used by the Registree AE, then no value shall be used for Credential-ID, i.e. the labels attribute shall include the string ‘Credential-ID:’.

b)	The From parameter of the CREATE or UPDATE request for the <AEAnnc> resource shall be set to the SP-relative-CSE-ID or Absolute-CSE-ID followed by '/' and the AE-ID-Stem value.

c)	The To parameter shall contain the SP-relative-Resource-ID format of the Resource ID for the <AEAnnc> resource which shall be constructed from the CSE-ID of the IN-CSE and the AE-ID-Stem that the Registree AE provided.

d)	Send Create or Update request to the IN-CSE that is associated with the Registree AE.

e)	Wait for Response primitive.

Upon receipt of a successful response from the IN-CSE, the Registrar/Host CSE shall use the Unstructured-CSE-relative-Resource-ID equal to the AE-ID-Stem provided by the Registree AE for the <AE> resource to be created on the Registrar/Host CSE.

7.4.5.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.5.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.5.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following addition:

Primitive Specific operation on Recv-6.6 "Announce/De-announce the resource":

If the request is for an <AE> resource and if it is received at a MN-CSE or ASN-CSE with AE-ID-Stem starting with "S" the receiver shall execute the following steps in order:

a)	Compose the Update <AEAnnc> Request primitive with the link attribute set to "INACTIVE".

b)	Send Update request to the announced to IN-CSE.

c)	Wait for Response primitive.

7.4.5.2.5	Notify

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.6	Resource Type <container>


7.4.6.1	Introduction

This resource represents a container for data instances. It is used to share information among other entities and potentially to track the data. A <container> resource has no associated content, only attributes and child resources.

The detailed description can be found in clause 9.6.6 in oneM2M TS-0001 [6].

Table 7.4.6.1-1: Data type definition of <container> resource

Table 7.4.6.1-2: Universal/Common Attributes of <container> resource

Table 7.4.6.1-3: Resource Specific Attributes of <container> resource

Table 7.4.6.1-4: Child resources of <container> resource

7.4.6.2	<container> resource specific procedures for CRUD operations

7.4.6.2.0	Introduction

This clause describes container resource specific behaviour for CRUD operations.

7.4.6.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

The primitive-specific operation Recv-6.4 is performed with following exceptions for optional attributes while executing procedures defined in clause 7.3.3.3.

The Hosting CSE may assign default values based on local policy for optional attributes maxNrOfInstances, maxByteSize and maxInstanceAge.

If the maxNrOfInstances, maxByteSize or maxInstanceAge attributes are present in the resource representation, but their value indicates an invalid value, then the request shall be rejected with a Response Status Code indicating "BAD_REQUEST" error.

There are two cases where the Hosting CSE may configure or override a maxNrOfInstances, maxByteSize or maxInstanceAge value specified in the resource representation (if present).

If the Originator does not specify a value the Hosting CSE may configure a maxNrOfInstances, maxByteSize or maxInstanceAge into the resource according to local policy. If the Hosting CSE has configured a value it shall return this value back to the originator in the response if the Result Content parameter permits this.

If the Hosting CSE determines that the maxNrOfInstances, maxByteSize or maxInstanceAge requested by the Originator does not meet its requirements (e.g. based on a local policy) the Hosting CSE shall configure a maxNrOfInstances, maxByteSize or maxInstanceAge into the resource according to local policy. The Hosting CSE shall return the modified value back to the originator in the response if the Result Content parameter permits this.

No other changes from the generic procedures in clause 7.2.2.2.

7.4.6.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.6.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.6.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.7	Resource Type <contentInstance>


7.4.7.1	Introduction

The <contentInstance> resource represents a data instance in the container.

The detailed description can be found in clause 9.6.7 in oneM2M TS-0001 [6].

Table 7.4.7.1-1: Data type definition of <contentInstance> resource

Table 7.4.7.1-2: Universal/Common Attributes of <contentInstance> resource

Table 7.4.7.1-3: Resource Specific Attributes of <contentInstance> resource

Table 7.4.7.1-4: Child resources of <contentInstance> resource

The contentInfo attribute shall provide meta information about the stored data in content and is optional. See the definition of m2m:contentInfo in Table 6.3.3-1: oneM2M Simple Data Types for details

7.4.7.2	<contentInstance> resource specific procedures for CRUD operations

7.4.7.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation on Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed" with the following additional operations.

The Hosting CSE shall check whether the size in bytes of the content attribute of the <contentInstance> resource is greater than maxByteSize of the targeted parent <container> resource.

a)	If true, the Hosting CSE shall return the response primitive with a Response Status Code indicating "NOT_ACCEPTABLE" error. Skip steps 2 and 3 below.

b)	If false, the Hosting CSE shall set the contentSize attribute of the <contentInstance> resource to the size in bytes of the content attribute.

The Hosting CSE shall check the currentNrOfInstances and currentByteSize of the targeted parent <container> resource.

a)	If maxNrOfInstances of the targeted parent <container> resource is specified then if the currentNrOfInstances when modified to reflect the addition of the new <contentInstance> exceeds maxNrOfInstances, the Hosting CSE shall remove the oldest <contentInstance> resource from the targeted <container> resource.

b)	If maxByteSize of the targeted parent <container> resource is specified then if the currentByteSize when modified to reflect the addition of the new <contentInstance> exceeds maxByteSize the Hosting CSE shall remove the oldest <contentInstance> resources from the targeted <container> resource until maxByteSize conditions are met.

c)	The Hosting CSE shall update the currentNrOfInstances of the targeted parent <container> resource with the count of <contentInstance> resources in the targeted parent <container> resource. The Hosting CSE shall update the currentByteSize of the targeted parent <container> resource with the sum of the contentSize attributes of the <contentInstance> resources in the targeted parent <container> resource.

d)	When removing the oldest <contentInstance> resources, the Hosting CSE shall not generate notifications even if there exists a <subscription> to the targeted <container> resource and this <subscription> is configured to generate a notification on "Delete_of_Direct_Child_Resource".

e)	If the maxInstanceAge attribute is present in the targeted parent <container> resource, then the Hosting CSE shall set the expirationTime attribute in <contentInstance> resource such that the time difference between expirationTime and the creationTime of the <contentInstance> resource shall not exceed the maxInstanceAge of the targeted parent <container> resource.

The Hosting CSE shall increment the stateTag attribute of the targeted parent <container> resource and copy the value into the stateTag attribute of the <contentInstance> resource.

If the hosting CSE has the capability to duplicate the actual data in semantic triples, it may decide whether to represent the content as semantic triples, depending on local policies/configurations. If the hosting CSE decides to do so, it shall execute the following actions: a) represent the actual data contained in the content attribute to semantic triples (e.g. RDF triples); b) create a <semanticDescriptor> child resource for the <contentInstance> resource with its descriptor attribute set to these semantic triples generated in a).

If the hosting CSE does not have the capability to duplicate the actual data in semantic triples complying with an ontology that it supports, this step will be skipped.

No other changes from the generic procedures in clause 7.2.2.2.

7.4.7.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Same as the generic procedures in clause 7.2.2.2 except following conditions:

If the value of disableRetrieval attribute of the parent <container> resource is true, then the Hosting CSE shall return a response primitive with a Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

7.4.7.2.3	Update

Originator:

The <contentInstance> resource shall not be Updated via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order:

"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

"Send the Response primitive".

7.4.7.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 except for the addition of the following steps:

If the value of the disableRetrieval attribute of the immediate parent <container> resource is true, the Hosting CSE shall return an unsuccessful Response primitive with the Response Status Code indicating an "OPERATION_NOT_ALLOWED" error.

The currentNrOfInstances and currentByteSize attributes of the immediate parent <container> resource shall be updated.


### 7.4.8	Resource Type <subscription>


7.4.8.1	Introduction

The <subscription> resource contains subscription information for its subscribed-to resource. The subscription resource is a child of the subscribed to resource.

The detailed description can be found in clause 9.6.8 in oneM2M TS-0001 [6].

Table 7.4.8.1-1: Data type definition of <subscription> resource

Table 7.4.8.1-2: Universal/Common Attributes of <subscription> resource

Table 7.4.8.1-3: Resource Specific Attributes of <subscription> resource

Table 7.4.8.1-4: Child resources of <subscription> resource

7.4.8.2	<subscription> resource specific procedures for CRUD operations

7.4.8.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

If the Originator specifies a missingData condition with a duration value greater than the periodicInterval attribute of the <timeSeries> resource no notification on missing data points will be generated.

Receiver:

The following are additional Hosting CSE procedures to the generic resource handling procedures (Figure 7.2.2.2-1 in clause 7.2.2.2). The additional procedures shall be inserted from Recv-6.2 to Recv-6.5 as below.

Recv-6.3 The following step is in addition to the procedures defined in clause 7.3.3.15:

Check if the Originator has privileges for retrieving the subscribed-to resource. If the Originator does not have the privilege, the Hosting CSE shall return the response primitive with a Response Status Code indicating an "ORIGINATOR_HAS_NO_PRIVILEGE" error.

Recv-6.4 The following steps are in addition to the procedures defined in clause 7.3.3.3:

Check if the subscribed-to resource, addressed in To parameter in the Request, is subscribable. Subscribable resource types are defined in TS-0001 [6]; they have <subscription> resource types as their child resources. If it is not subscribable, the Hosting CSE shall return the Notify response primitive with a Response Status Code indicating a "TARGET_NOT_SUBSCRIBABLE" error instead of the Response Status Code "INVALID_CHILD_RESOURCE_TYPE".

Check if the notificationEventType is set to "Blocking_Update":

If the subscribed-to resource already has a subscription with this notificationEventType the Hosting CSE shall return the response primitive with a Response Status Code indicating a "BLOCKING_SUBSCRIPTION_ALREADY_EXISTS" error if more than one notification of this type could be sent.

If more than one Notification Target is specified in notificationURI, the Hosting CSE shall return the response primitive with a Response Status Code indicating a "BAD_REQUEST" error.

If any resource-specific attributes of the <subscription> resource other than eventNotificationCriteria or notificationURI are specified the Hosting CSE shall return the primitive with a Response Status Code indicating a "BAD_REQUEST" error.

If any condition tag of the eventNotificationCriteria attribute other than attribute condition tag is specified, the Hosting CSE shall return the response primitive with a Response Status Code indicating a "BAD_REQUEST" error.

If the Notification Target is not a oneM2M-compliant resource-ID, the Hosting CSE shall return the response primitive with a Response Status Code indicating a "BAD_REQUEST" error.

Check if the notificationEventType is set to “Report on missing data points”. If the missingData attribute is not provided as well, the request shall be rejected with a Response Status Code indicating a "BAD_REQUEST" error.

Check if the missingData element of eventNotificationCriteria is provided.

If the subscribed-to resource (i.e. the resource given by the To parameter in the Request) is not a <timeSeries>, the request shall be rejected with a Response Status Code  indicating a "BAD_REQUEST" error.

If any of the notificationURI entries are not the Originator and are formatted as oneM2M-compliant resource-IDs, the Hosting CSE may send a Subscription Verification request primitive to each of them as described in clause 7.5.1.2.3.

a)	If the Hosting CSE cannot send one or more Subscription Verification request primitives, the Hosting CSE shall return the Create <subscription> response primitive with a Response Status Code indicating a "SUBSCRIPTION_VERIFICATION_INITIATION_FAILED" error.

b)	If the Hosting CSE sent all the Subscription Verification request primitives, the Hosting CSE shall check if each Notify response primitive contains a Response Status Code indicating "OK". If not, the Hosting CSE shall return the Create <subscription> response primitive containing a Response Status Code indicating a "SUBSCRIPTION_VERIFICATION_INITIATION_FAILED" error.

If the Originator provides a value of childResourceType which is not a valid child of the subscribed-to resource, the request shall be rejected with a Response Status Code indicating a “BAD_REQUEST” error.

If the Originator provides missingData, check that subscribed-to resource is of type <timeSeries>. If not, the request shall be rejected with a Response Status Code indicating a "BAD_REQUEST" error.

If both the notificationEventType and operationMonitor are present in the Request, the request shall be rejected with a Response Status Code  indicating a "BAD_REQUEST" error.

If the notificationContentType is invalid for a given operation (refer to oneM2M TS-0001 [6] Table 9.6.8-4: Default and allowed values of notificationContentType) the request shall be rejected with a Response Status Code indicating a "BAD_REQUEST" error.

Recv-6.5: The following steps are in addition to the procedures defined in clause 7.3.3.5:

If the Originator does not provide notificationContentType, the Hosting CSE shall set it according to the default shown in oneM2M TS-0001 [6] Table 9.6.8-4: Default and allowed values of notificationContentType.

If the notificationURI is not the Originator, the Hosting CSE shall set the Originator’s ID as the <subscription> resource's creator attribute.

If the batchNotify attribute is present in the Request but batchNotify/duration is not provided by the Originator, the Hosting CSE shall set the value of batchNotify/duration to the default duration as given by the M2M Service Provider.

7.4.8.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.8.2.3	Update

Originator:

The following change from the generic procedures in clause 7.2.2.1.

Orig-1.0: The originator shall not specify notificationEventType set to "Blocking_Update".

If the Originator specifies a missingData condition with a duration value greater than the periodicInterval attribute of the <timeSeries> resource no notification on missing data points will be generated.

Receiver:

The following are additional Hosting CSE procedures to the generic resource handling procedures in clause 7.2.2.2.

Recv-6.4: The following steps are in addition to the procedures defined in clause 7.3.3.4:

Check if the notificationEventType in the request is set to "Blocking_Update". If so, the request shall be rejected with a Response Status Code indicating a "BAD_REQUEST" error.

Check if the notificationEventType is set to “Report on missing data points”. If the missingData attribute is not set in the target resource or provided in the request, the request shall be rejected with a Response Status Code indicating a "BAD_REQUEST" error.

Check if the missingData element of eventNotificationCriteria is provided.

If the subscribed-to resource (i.e. the resource given by the To parameter in the Request) is not a <timeSeries>, the request shall be rejected with a Response Status Code  indicating a "BAD_REQUEST" error.

If the Originator provides a value of childResourceType which is not a valid child of the subscribed-to resource, the request shall be rejected with a Response Status Code indicating a “BAD_REQUEST” error.

If the Originator provides missingData, check that the subscribed-to resource is of type <timeSeries>. If not, the request shall be rejected with a Response Status Code indicating a "BAD_REQUEST" error.

If the UPDATE operation would result in both operationMonitor and notificationEventType being present in the resource, the request shall be rejected with a Response Status Code indicating a “BAD_REQUEST” error.

If the notificationContentType is invalid for a given operation (refer to oneM2M TS-0001 [6] Table 9.6.8-4: Default and allowed values of notificationContentType) the request shall be rejected with a Response Status Code indicating a “BAD_REQUEST” error.

Recv-6.5. The following steps are in addition to the procedures defined in clause 7.3.3.7:

If a <crossResourceSubscription> resource identifier is removed from associatedCrossResourceSub, the Hosting CSE shall send a Notify request for Subscription Deletion, using the procedures in clause 7.5.1.2.4, to the <crossResourceSubscription> Hosting CSE.

Check if the pendingNotification attribute is being removed by the request or is being changed from "sendAllPending" to "sendLatest". If the pendingNotification attribute is being removed, then all cached pending Notify request primitives for the subscription resource shall be removed. If the pendingNotification attribute is being changed from "sendAllPending" to "sendLatest", then all cached pending Notify request primitives except the latest notification for the subscription resource shall be removed.

7.4.8.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

The following changes to the receiver procedures described in clause 7.2.2.2.

Recv-6.5.

The Hosting CSE shall send a Notify request for Subscription Deletion using the procedures in clause 7.5.1.2.4 to all <crossResourceSubscription> hosting CSEs indicated in associatedCrossResourceSub.

The Hosting CSE shall remove all cached pending Notify request primitives for the subscription.


### 7.4.9	Resource Type <schedule>


7.4.9.1	Introduction

The <schedule> resource shall represent scheduling information in the context of its parent resource. If a <schedule> resource is not present as a child resource then there are no time-constraints on the context of its parent resource.

The detailed <schedule> resource description can be found in clause 9.6.9 of the TS-0001 [6].

Table 7.4.9.1-1: Data type definition of <schedule> resource

Table 7.4.9.1-2: Universal/Common Attributes of <schedule> resource

Table 7.4.9.1-3: Resource Specific Attributes of <schedule> resource

The scheduleElement attribute represents the list of scheduled execution times.

Each entry of the scheduleElement attribute shall consist of a line with 7 field values (see Table 7.4.9.1-4).

The time to be matched with the schedule pattern shall be interpreted in UTC timezone.

Table 7.4.9.1-4: Definition of m2m:scheduleEntry string format

Each field value can be either an asterisk ('*': matching all valid values), an element, or a list of elements separated by commas(',').

An element shall be either a number, a range (two numbers separated by a hyphen '-') or a range followed by a step value. A step value (a slash '/' followed by an interval number) specifies that values are repeated over and over with the interval between them. For example, note "0-23/2" in the Hour field is equivalent to "0,2,4,6,8,10,12,14,16,18,20,22". A step value can also be used after an asterisk (e.g. "*/2").

EXAMPLE 1:

EXAMPLE: * 0-5 2,6,10 * * * *

If the parent resource is a <node>, the Hosting CSE will forward requests to an AE or CSE hosted on the corresponding node during the time windows 2:00-2:05, 6:00-6:05, and 10:00-10:05 every day.

End of EXAMPLE 1:

EXAMPLE 2:

EXAMPLE: * * 8-20 * * * *

If the parent resource is a <subscription>, the Hosting CSE will not send notifications for the subscribed-to event between the hours of 20:00 and 8:00 every day.

End of EXAMPLE 2:

EXAMPLE 3:

EXAMPLE: * * 0-23/2 * * * *

If the parent resource is a  <node>, the Hosting CSE will forward requests to an AE or CSE hosted on the corresponding node for an hour every other hour of every day.

End of EXAMPLE 3:

EXAMPLE 4:

EXAMPLE: * * * * * */2 *

If the parent resource is a <node>, the Hosting CSE will forward requests to an AE or CSE hosted on the corresponding node on Sundays, Tuesdays, Thursdays and Saturdays (*/2 in the day of the week field is equivalent to 0,2,4,6).

End of EXAMPLE 4:

Table 7.4.9.1-6: Child resources of <schedule > resource

7.4.9.2	<schedule> resource specific procedures for CRUD operations

7.4.9.2.0	Introduction

This clause describes <schedule> resource specific behaviour for CRUD operations.

7.4.9.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

The following are changes to the receiver procedures described in clause 7.2.2.2:

Recv-6.5: The following step is in addition to the generic Create procedures defined in clause 7.3.3.5:

The request shall be rejected with the "CONTENTS_UNACCEPTABLE" Response Status Code if the target resource is not a <node> resource and if the networkCoordinated attribute is present in the request.

7.4.9.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.9.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

The following are changes to the receiver procedures described in clause 7.2.2.2.

Recv-6.5: The following step is in addition to the generic Update procedures defined in clause 7.3.3.7:

The request shall be rejected with the "CONTENTS_UNACCEPTABLE" Response Status Code if the target resource is not a <node> resource and if the networkCoordinated attribute is present in the request.

7.4.9.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.10	Resource Type <locationPolicy>


7.4.10.1	Introduction

The <locationPolicy> resource represents the method for obtaining and managing geographical location information of an M2M Node. The detailed description can be found in the clause 9.6.10 in oneM2M TS-0001 [6].

Table 7.4.10.1-1: Data type definition of <locationPolicy> resource

Table 7.4.10.1-2: Universal/Common Attributes of <locationPolicy> resource

Table 7.4.10.1-3: Resource Specific Attributes of <locationPolicy> resource

Table 7.4.10.1-4: Child resources of <locationPolicy> resource

7.4.10.2	<locationPolicy> resource specific procedures for CRUD Operations

7.4.10.2.0	Introduction

This clause describes <locationPolicy> resource specific primitive behaviour for CRUD operations.

7.4.10.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

The following <locationPolicy> resource type specific procedures shall be performed after Recv-6.5 and before Recv-6.6 generic procedures.

The Hosting CSE shall create a <container> resource in which the actual location information will be stored. Then the Hosting CSE shall create a <locationPolicy> resource and shall fill in cross-references for both resources. Both of these resources shall be hosted locally on the Hosting CSE. The locationContainerID attribute of the <locationPolicy> resource shall contain the resourceID of the created <container> resource and the locationID attribute of the <container> resource shall contain the resourceID of the <locationPolicy> resource. The name of the created <container> resource shall be determined by the locationContainerName attribute if it is applicable.

Check the locationSource and locationUpdatePeriod attributes:

If the locationSource attribute is set by 'Network Based' and locationUpdatePeriod attribute is set by any duration value (higher than 0 second), or if the locationSource attribute is set by 'Network Based' and locationUpdatePeriod attribute is zero or not defined and locationUpdateEventCriteria is LocationChange, then continue with the step 3.

If the locationSource attribute is set by 'Device Based' and locationUpdatePeriod attribute is set by any duration value (higher than 0 second), then continue with the step 4.

If the locationSource attribute is set by 'Sharing Based' and locationUpdatePeriod attribute is set by any duration value (higher than 0 second), then continue with the step 5.

If the locationUpdatePeriod has more than one values, the first value in the list shall be used as the current location update period in step 3,4 and 5. In this case, based on the local context information of the Hosting CSE such as velocity, available memory, the Hosting CSE may choose one of the value out of the list to be the active location update period. If the device is moving at the high speed, it is expected that the location of the device would be update more frequently. The Hosting CSE would acquire the current velocity of the device and compare the value with some predefined value, depend on the result of the comparison, the Hosting CSE would choose a smaller value from the list if the current velocity is higher than the predefined value. Otherwise, the Hosting CSE would choose a larger value.

The Hosting CSE shall retrieve the locationTargetID and locationServer attributes from the stored <location Policy> resource.

If the locationServer is absent in the Originator's request, the Hosting CSE shall either derive the locationServer value from the locationTargetID or be pre-provisioned with the identity of a Location Server.

In case either the locationTargetID or locationServer attribute cannot be obtained, the Hosting CSE shall reject the request with the Response Status Code indicating "BAD_REQUEST" error. Then, the Hosting CSE shall transform the location-acquisition request into Location Server request, using the attributes stored in <locationPolicy> resource. The Hosting CSE shall also provide default values for other required parameters (e.g. quality of position) in the Location Server request according to local policies.

If the request which requests the location information of the target device towards the Location Server crosses over the Mcn reference point, the Hosting CSE shall add the authID in to requester parameter of the Location Server request [28].

The Hosting CSE shall send this Location Server request to the location server which could use one of the two API interfaces: one is OMA Mobile Location Protocol [i.4] and OMA RESTful NetAPI for Terminal Location [28]. The other one is 3GPP Monitoring Event API for terminal location [51]. If retrieveLastKnownLocation is true, the Hosting CSE shall use the 3GPP Monitoring Event API only. If the requester parameter is present in the request, the Location Server shall verify whether the requester is authorized to request the location information. If the requester is not authorized, PolicyException (POL0002) will be returned. If the requester is permitted, then the location server performs positioning procedure based upon the Location Server request. Then continue with step 6.

Based on the period information, locationUpdatePeriod attribute, this step can be periodically repeated or the location server can only notify the Hosting CSE of location information that performs periodically.

NOTE 1:	The location server performs the privacy control and only responds successfully if the positioning procedure is permitted.

NOTE 2:	Detailed information on how the Location Server request message is converted into OMA RESTful NetAPI for Terminal Location message is described in clause G.2.

NOTE 3:	Detailed information on how the Location Server request message is converted into 3GPP Monitoring Event API for terminal location message is described in clause G.3.

The Hosting CSE shall perform positioning procedure using location determination modules and technologies (e.g. GPS). Then continue with step 6.

Based on the period information, locationUpdatePeriod attribute, this step can be periodically repeated.

NOTE 4:	The Hosting CSE can utilize the internal interface (e.g. System Call) to communicate with the modules and technologies. The detailed procedure is out of scope.

The Hosting CSE shall collect information of topology of M2M Area Network using <node> resource and find the closest Node from the Originator that has registered with the Hosting CSE and has location information. The closest Node is determined by the minimum hop based on the collected topology information.

If the Hosting CSE can find the closest Node from the Originator, the location information of the closest Node shall be stored as the location information of the Originator into a <contentInstance> resource under the created <container> resource.

If the Hosting CSE cannot find the closest Node from the Originator, the location information of the Hosting CSE shall be stored as the location information of the Originator into a <contentInstance> resource under the created <container> resource.

The Hosting CSE shall receive the corresponding response and transform it into a Response primitive.

If the positioning procedure failed and retrieveLastKnownLocation is false, the Hosting CSE shall store a statusCode based on the error code in the locationStatus attribute in the created <locationPolicy> resource. If the positioning procedure failed and retrieveLastKnownLocation is true, the Hosting CSE shall repeat step 3), once only, but requesting the last known location from the Location Server using 3GPP Monitoring Event API [51].

If the positioning procedure is successfully complete which means that the Hosting CSE acquires the location information, The Hosting CSE shall store the acquired location information into a <contentInstance> resource under the created <container> resource.

NOTE 5:	The format of location information in the content of <contentInstance> is decided by the Location Server.

7.4.10.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.10.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.10.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

The procedure of the Receiver written in the clause 7.2.2.2 shall be the same as initial steps. A following step is the <locationPolicy> resource type specific procedure for DELETE operation.

Once the <locationPolicy> resource is deleted, the Receiver shall delete the associated resources (e.g. <container>, <contentInstance> resources). If the locationSource attribute and the locationUpdatePeriod attribute of the <locationPolicy> resource have been set with appropriate values, the Receiver shall tear down the session. The specific mechanism used to tear down the session depends on the support of the Underlying Network and other factors.


### 7.4.11	Resource Type <delivery>


7.4.11.1	Introduction

In order to be able to initiate and manage the execution of data delivery in a resource-based manner, the resource type delivery is defined. This resource type shall be used for forwarding requests from one CSE to another CSE when the Delivery Aggregation parameter in the request is set to true. The detailed description can be found in clause 9.6.11 in oneM2M TS-0001 [6].

Table 7.4.11.1-1: Data type definition of <delivery> resource

Table 7.4.11.1-2: Universal/Common Attributes of <delivery> resource

Table 7.4.11.1-3: Resource Specific Attributes of <delivery> resource

Table 7.4.11.1-4: Child resources of <delivery> resource

7.4.11.2	<delivery> resource specific procedures for CRUD operations

7.4.11.2.0	Introduction

This clause describes <delivery> resource specific behaviour for CRUD operations.

7.4.11.2.1	Create

Originator:

An AE shall not originate a Create <delivery> resource request.

Primitive specific operation on Orig-1.0 "Compose Request primitive":

The Originator shall use a blocking request (i.e. Response Type=blockingRequest).

The Originator shall provide the content of the <delivery> resource.

No change for the remaining steps from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received over Mca reference point, the Receiver CSE shall execute the following steps in order:

a)	"Create an unsuccessful Response primitive" with a Response Status Code indicating 'OPERATION_NOT_ALLOWED' error.

b)	"Send the Response primitive".

Otherwise:

a)	No change from the generic procedures in clause 7.2.2.2.

NOTE:	Determination of the reference point is at the discretion of the Receiver CSE implementation.

7.4.11.2.2	Retrieve

Originator:

Primitive specific operation on Orig-1.0 "Compose Request primitive":

The Originator shall use a blocking request (i.e. Response Type=blockingRequest).

No change for the remaining steps from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.11.2.3	Update

Originator:

An AE shall not originate a Create <delivery> resource request.

Primitive specific operation on Orig-1.0 "Compose Request primitive":

The Originator shall use a blocking request (i.e. Response Type=blockingRequest).

The Originator shall provide the content of the <delivery> resource.

No change for the remaining steps from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received over Mca reference point, the Receiver CSE shall execute the following steps in order:

a)	"Create an unsuccessful Response primitive" with a Response Status Code indicating 'OPERATION_NOT_ALLOWED' error.

b)	"Send the Response primitive".

Otherwise:

a)	No change from the generic procedures in clause 7.2.2.2.

NOTE:	Determination of the reference point is at the discretion of the Receiver CSE implementation.

7.4.11.2.4	Delete

Originator:

An AE shall not originate a Create <delivery> resource request.

Primitive specific operation on Org-1.0 "Compose Request primitive":

The Originator shall use a blocking request (i.e. Response Type=blockingRequest).

No change for the remaining steps from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received over Mca reference point, the Receiver CSE shall execute the following steps in order:

a)	"Create an unsuccessful Response primitive" with a Response Status Code indicating 'OPERATION_NOT_ALLOWED' error.

b)	"Send the Response primitive".

Otherwise:

a)	No change from the generic procedures in clause 7.2.2.2.

NOTE:	Determination of the reference point is at the discretion of the Receiver CSE implementation.


### 7.4.12	Resource Type <request>


7.4.12.1	Introduction

The <request> resource is used to represent information relating to a non-blocking request. If an AE or CSE issues a request (including a notification request) targeting any resource other than a <request>, using a non-blocking mode (e.g. if the Response Type parameter of the request is set to "nonBlockingRequestSynch" or "nonBlockingRequestAsynch") and if the Registrar CSE of the Originator supports the <request> resource type, as indicated by the supportedResourceType attribute of the <CSEBase> resource representing the Registrar CSE of the Originator, the Registrar CSE of the Originator shall create an instance of <request> to capture and expose the context of the associated non-blocking request. More details can be found in clause 7.3.2 of the present document and in clause 9.6.12 in oneM2M TS-0001 [6].

Table 7.4.12.1-1: Data type definition of <request> resource

Table 7.4.12.1-2: Universal/Common Attributes of <request> resource

Table 7.4.12.1-3: Resource Specific Attributes of <request> resource

Table 7.4.12.1-4: Reference of child resources

7.4.12.2	<request> resource specific procedures for CRUD operations

7.4.12.2.0	Introduction

This clause describes request resource specific procedure on Resource Hosting CSE for CRUD operations.

7.4.12.2.1	Create

Originator:

The <request> resource shall not be created via API. It is only created implicitly by a Receiver CSE. See clause 7.3.2.2 Create <request> resource locally.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

"Create an unsuccessful Response primitive" with a Response Status Code indicating 'OPERATION_NOT_ALLOWED' error.

"Send the Response primitive".

7.4.12.2.2	Retrieve

Originator:

The procedure of the Originator is the same as the clause 7.2.2.1, except that the Originator shall not use the "nonBlockingRequestSynch" or "nonBlockingRequestAsynch" communication methods.

Receiver:

The generic operation Recv-2.0 "Communication method?" is performed with the following additions:

If the Response Type parameter is "nonBlockingRequestSynch" or "nonBlockingRequestAsynch" return an unsuccessful Response primitive with a Response Status Code indicating a "BAD_REQUEST" error.

If the Response Type parameter is "flexBlocking" treat the request as if the Response Type were "blockingRequest".

7.4.12.2.3	Update

Originator:

The procedure of the Originator is the same as the clause 7.2.2.1, except that the Originator shall not use the "nonBlockingRequestSynch" or "nonBlockingRequestAsynch" communication methods.

Receiver:

The generic operation Recv-2.0 "Communication method?" is performed with the following additions:

If the Response Type parameter is "nonBlockingRequestSynch" or "nonBlockingRequestAsynch" return an unsuccessful Response primitive with a Response Status Code indicating a "BAD_REQUEST" error.

If the Response Type parameter is "flexBlocking" treat the request as if the Response Type were "blockingRequest".

7.4.12.2.4	Delete

Originator:

The procedure of the Originator is the same as the clause 7.2.2.1, except that the Originator shall not use the "nonBlockingRequestSynch" or "nonBlockingRequestAsynch" communication methods.

An Originator is not required to delete a <request> resource explicitly, as the CSE hosting the <request> resource will do it implicitly, but an Originator can use Delete to attempt to cancel a request.

Receiver:

The generic operation Recv-2.0 "Communication method?" is performed with the following additions:

If the Response Type parameter is "nonBlockingRequestSynch" or "nonBlockingRequestAsynch" return an unsuccessful Response primitive with a Response Status Code indicating a "BAD_REQUEST" error.

If the Response Type parameter is "flexBlocking" treat the request as if the Response Type were "blockingRequest".

The generic operation Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation” is performed with the following additional operations:

If the <request> resource's requestStatus is PENDING, the associated operation shall be cancelled if possible. If it is not possible to cancel the operation return an unsuccessful Response primitive with a Response Status Code indicating an "UNABLE_TO_RECALL_REQUEST" error and do not delete the <request> resource.

If the <request> resource's requestStatus is FORWARDED or PARTIALLY_COMPLETED, return an unsuccessful Response primitive with a Response Status Code indicating an "UNABLE_TO_RECALL_REQUEST" error and do not delete the <request> resource.


### 7.4.13	Resource Type <group>


7.4.13.1	Introduction

The <group> resource represents a group of resources of the same or mixed types. The <group> resource can be used to do bulk manipulations on the resources represented by the memberIDs attribute. The <group> resource contains an attribute that represents the members of the group and a virtual resource (the <fanOutPoint>) that allows operations to be applied to the resources represented by those members. The detailed description can be found in clause 9.6.13 in oneM2M TS-0001 [6].

Table 7.4.13.1-1: Data type definition of <group> resource

Table 7.4.13.1-2: Universal/Common Attributes of <group> resource

Table 7.4.13.1-3: Resource Specific Attributes of <group> resource

Table 7.4.13.1-4: Child resources of <group> resource

7.4.13.2	<group> resource specific procedures for CRUD operations

7.4.13.2.0	Introduction

This clause describes <group> resource specific procedure on Resource Hosting CSE for CRUD operations.

7.4.13.2.1	Create

Originator:

If an Originator is creating a <group> containing members which are themselves of type <group>, the Originator shall add the suffix '/fopt' to a member ID if the Originator wants to fan-out group requests to each member of that sub-<group>, else the Originator shall not suffix the '/fopt' to that member ID.

For a group of resources of the same resourceType the originator shall set the memberType attribute to the type of resource desired. If the originator wants to create a group of the same specialized type of <flexContainer> resource then memberType shall be set to “flexContainer” and specializationType shall be set to the containerDefinition for the specialized type. If the originator wants to create a group of the same specialization of <mgmtObj>, memberType shall be set to "mgmtObj" and specializationType shall be set to the mgmtDefinition for the specialized type. If the originator wants to create a group with a variety of specialized resources the specializationType attribute shall be empty.

Receiver:

Primitive-specific operations after Recv-6.4 "Check validity of resource representation for the given resource type" and before Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed". See clause 7.2.2.2.

Validate the provided attributes. The receiver shall also check that the number of URIs present in the memberIDs attribute of the group resource representation does not exceed the maximum as specified by the maxNrOfMembers attribute. If the maximum is exceeded, the request shall be rejected with a Response Status Code indicating a "MAX_NUMBER_OF_MEMBER_EXCEEDED" error. If there are duplicate members in the memberIDs attribute then the duplicate members are removed before creation of the <group> resource.
If the memberType attribute of the <group> resource is not "MIXED", the Hosting CSE shall also verify that all the member IDs, including sub-groups, in the attribute memberIDs of the <group> resource representation provided in the request shall conform to the memberType of the group resource. To validate a resource type of a member, the Hosting CSE shall check the resourceType attribute of the resource which is indicated by the member ID. If the specializationType attribute is set in the request, the Hosting CSE shall verify that all the member IDs, including sub-groups, in the memberIDs attribute of the <group> resource representation provided in the request conform to that specializationType. To check the resourceType and specializationType attributes, the Hosting CSE may retrieve the member resources. When a member is a virtual resource other than a <fanOutPoint>, the Hosting CSE shall check the resourceType attribute of the parent resource. If the resource type of the parent allows this child virtual resource type, the Hosting CSE checks whether the virtual resource type matches with the memberType attribute of the group. If they match, then the Hosting CSE considers that the virtual member resource is validated. If the resourceType cannot be retrieved due to lack of privilege, the request shall be rejected with a Response Status Code indicating the "RECEIVER_HAS_NO_PRIVILEGE" error.

In the case that the <group> resource contains a fanOutPoint sub-group member resource (i.e. a memberID of a sub-group member is suffixed with /fopt), the receiver shall retrieve the memberType of each sub-group member resource to validate the memberType. If a memberType cannot be retrieved due to lack of privilege, the request shall be rejected with a Response Status Code indicating a "RECEIVER_HAS_NO_PRIVILEGE" error. If the sub-group member resources are temporarily unreachable, the receiver shall set the memberTypeValidated attribute of the <group> resource to false and return the result to the originator in the response of the request. As soon as any unreachable sub-group resource becomes reachable, the receiver shall perform the memberType validation procedure. Upon unsuccessful validation, the receiver shall delete the <group> resource if the consistencyStrategy of the <group> resource is ABANDON_GROUP, or remove the inconsistent members from the <group> resource if the consistencyStrategy attribute is ABANDON_MEMBER, or set the memberType attribute of the <group> resource to "MIXED" if the consistencyStrategy attribute is SET_MIXED.

The memberTypeValidated attribute shall be set to true if all the members have been validated successfully. If a member validation for the memberType of the <group> resource is unsuccessful, then the Hosting CSE shall perform the following:

a)	If the consistencyStrategy of the <group> resource is ABANDON_GROUP then the request shall be rejected with a Response Status Code indicating the "GROUP_MEMBER_TYPE_INCONSISTENT" error.

b)	If the consistencyStrategy of the <group> resource is ABANDON_MEMBER then remove the inconsistent members and create the <group> resource and the memberTypeValidated attribute shall be set to true.

c)	If the consistencyStrategy of the <group> resource is SET_MIXED then set the memberType attribute of the <group> resource to "MIXED" and create the <group> resource and the memberTypeValidated attribute shall be set to true.

After Recv-6.7 "Create a success response", the receiver shall perform multicast group creation procedure if the group-hosting CSE supports multicast. See clause 7.5.3.1.

7.4.13.2.2	Retrieve

No primitive specific operations.

7.4.13.2.3	Update

Originator:

If the Originator intends to update the memberIDs attribute, to add members which are themselves of type <group>, the Originator shall add the suffix the '/fopt' to a member ID if the Originator wants to fan-out group requests to each member of that sub-<group>, else the Originator shall not suffix the '/fopt' to that member ID.

Receiver:

Primitive specific operations after Recv-6.4 "Check validity of resource representation for the given resource type" and before Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed". See clause 7.2.2.2.

If there are duplicate members in the memberIDs attribute of the request then the duplicate members are removed before updating the <group> resource. If the memberType attribute of the <group> resource is not "MIXED", the Hosting CSE shall verify that all the member IDs, including sub-groups, in the attribute memberIDs of the <group> resource representation provided in the request shall conform to the memberType of the <group> resource. Virtual member resource validation shall be done as specified in the group creation procedure (clause 7.4.13.2.1). If the specializationType attribute was set in the <group> resource, the Hosting CSE shall verify that all of the member IDs, including sub-groups, in the memberIDs attribute of the <group> resource representation provided in the request conform to that specializationType.

In the case that the <group> resource contains a fanOutPoint sub-group member resource (i.e. a memberID of a sub-group member is suffixed with /fopt), the Receiver shall retrieve the memberType of each sub-group member resource to validate the memberType. If a memberType cannot be retrieved due to lack of privilege, the request shall be rejected with a Response Status Code indicating a "RECEIVER_HAS_NO_PRIVILEGE" error. If the sub-group member resources are temporarily unreachable, the receiver shall set the memberTypeValidated attribute of the <group> resource to false and return the result to the originator in the response of the request. As soon as any unreachable sub-group resource becomes reachable, the receiver shall perform the memberType validation procedure. The Originator may get to know the validation result by subscribing to the created resource if the memberTypeValidated attribute is false. Upon unsuccessful validation, the receiver shall delete the <group> resource if the consistencyStrategy of the <group> resource is ABANDON_GROUP, or remove the inconsistent members from the <group> resource if the consistencyStrategy attribute is ABANDON_MEMBER, or set the memberType attribute of the <group> resource to "MIXED" if the consistencyStrategy attribute is SET_MIXED.

The memberTypeValidated attribute shall be set to true if all the members have been validated successfully. If a member validation for the memberType of the <group> resource is unsuccessful, then the Hosting CSE shall perform the following:

If the consistencyStrategy of the <group> resource is ABANDON_GROUP then the request shall be rejected with a Response Status Code indicating "GROUP_MEMBER_TYPE_INCONSISTENT" error.

If the consistencyStrategy of the <group> resource is ABANDON_MEMBER then remove the inconsistent members and update the <group> resource and the memberTypeValidated attribute shall be set to true.

If the consistencyStrategy of the <group> resource is SET_MIXED then set the memberType attribute of the <group> resource to "MIXED" and update the <group> resource and the memberTypeValidated attribute shall be set to true.

Primitive-specific operation: The Hosting CSE shall check whether the number of members in the request's memberIDs attribute exceeds the limitation of maxNrOfMembers. The Hosting CSE shall also check whether the value provided in the maxNrOfMembers attribute is smaller than the currentNrOfMembers attribute value. If any of these conditions is true, the Hosting CSE shall reject the request with Response Status Code indicating a "MAX_NUMBER_OF_MEMBER_EXCEEDED" error.

After Recv-10.0 "Send Response Primitive", the receiver shall perform multicast group UPDATE procedure if the group-hosting CSE supports multicast. See clause 7.5.3.2.

7.4.13.2.4	Delete

After Recv-10.0 "Send Response Primitive", the receiver shall perform multicast group DELETE procedure if the group-hosting CSE supports multicast. See clause 7.5.3.3.


### 7.4.14	Resource Type <fanOutPoint>


7.4.14.1	Introduction

The <fanOutPoint> resource is a virtual resource because it does not have a representation. It is the child resource of a <group> resource. Whenever a request is sent to the <fanOutPoint> resource, the request is fanned out to each of the members of the <group> resource indicated by the memberIDs attribute of the <group> resource. The responses (to the request) from each member are then aggregated and returned to the Originator. The detailed description can be found in clause 9.6.14 of oneM2M TS-0001 [6].

There are no common attributes, resource specific attributes or xsd file to <fanOutPoint> resource because it is a virtual resource.

A <fanOutPoint> is addressed in the following way:

Using a hierarchical URI formed by taking the structured or unstructured resource identifier of the parent <group> and appending the string /fopt to that URI.

This hierarchical URI can be extended by appending further path elements beyond the place where /fopt/ occurs. A request sent to such a URI is not fanned out to the group members, but instead it is fanned out to the resources located by taking the hierarchical URI of each group member in turn and then appending the additional path elements to that URI.

For example, if /IN-CSE-0001/myGroup were a group with members:

/IN-CSE-0001/m1 and

/IN-CSE-0001/m2

then a request sent to /IN-CSE-0001/myGroup/fopt/x/y would be fanned out to:

/IN-CSE-0001/m1/x/y and

/IN-CSE-0001/m2/x/y

The additional path elements can reference virtual resources, for example if m1 and m2 were both <container> resources then a request sent to /IN-CSE-0001/myGroup/fopt/la would be fanned out to the most recent <contentInstance> child resource of both m1 and m2.

If the memberIDs m1 and m2 are themselves the fanOutPoints of <group> resources (i.e. suffixed with /fopt), a request sent to /IN-CSE-0001/myGroup/fopt will be fanned out to all the members of m1 and all members of m2.

7.4.14.2	<fanOutPoint> operations

7.4.14.2.1	Validate the type of resource to be created

If this is a CREATE request and the memberType attribute of the addressed parent group resource is not "MIXED", the group-hosting CSE may check whether the type of resource to be created is a valid and compatible child resource type of the group members. If they are not consistent, the request shall be rejected with a Response Status Code indicating "INVALID_CHILD_RESOURCE_TYPE" error.

7.4.14.2.2	Sub-group creation for members residing on the same CSE

The group-hosting CSE shall obtain URIs of addressed resources from the attribute memberIDs of the parent <group> resource. The group-hosting CSE may determine that multiple member resources belong to the same remote member hosting CSE, and may act as an Originator to request to create a sub-group containing the specific multiple member resources in that member hosting CSE. This sub-group is created in the member hosting CSE as described in clause 7.4.13.2.1. The To parameter of this group Create request shall be <memberHosting cseBase>/<groupHosting remoteCse>/ or <memberHosting cseBase>/. The group-hosting CSE shall also provide From parameter (i.e. group-hosting CSE) and sub-group resource representation that contains a memberIDs attribute with all the members residing on the addressed member Hosting CSE. The sub-group representation may include the attribute accessControlPolicyIDs, so that both the group-hosting CSE and all permissions of the original group apply to this sub-group. The ID of the sub-group may be proposed by the group-hosting CSE and accepted by the member-hosting CSE or it may be given by the member-hosting CSE.

The memberIDs attribute of the parent <group> does not get updated in the case where the group-hosting CSE decides to create a sub-group.

If there is already a sub-group resource defined in the remote member hosting CSE, then the group-hosting CSE may utilize the existing sub-group resource. If the group-hosting CSE decides to re-use an existing sub-group, it shall check that the members of this sub-group are still members of the parent <group>.

If the group-hosting CSE creates a sub-group it should delete the sub-group when it determines that it is no longer needed.

7.4.14.2.3	Assign URI for aggregation of notification

If the request is to create a <subscription> resource, the group-hosting CSE shall validate the request to check whether it contains a notificationForwardingURI attribute or not. If it does not, the group-hosting CSE shall forward it to the group members. If it does, the group-hosting CSE shall assign a new URI to the notificationURI attribute of the <subscription> in the requests before forwarding it to the group members. This new URI shall address the group-hosting CSE so that it can receive and aggregate Notifications from those subscriptions.

7.4.14.2.4	Fan out Request to each member

If the parent group has no members, the group-hosting CSE shall reject the request with the Response Status Code indicating "NO_MEMBERS".

If the request to be fanned out does not contain a Group Request Identifier already and if any of the target addresses, as found in step a) below, involves a further <fanOutPoint>the group-hosting CSE shall generate a unique group request identifier and store this group request identifier locally. The group-hosting CSE may choose to generate and store a unique group request identifier whenever the request to be fanned out does not already contain one, regardless of whether any targets involve further <fanOutPoint>s.

If the request to be fanned out already contains a Group Request Identifier parameter, the group-hosting CSE shall validate it, as described in clause 7.3.3.2, and if the validation is successful it shall include this parameter value in all the requests that it fans out in step b) below.

If the request contains a Group Request Target Members parameter, and if any of the member IDs in this parameter is not present in the memberIDs list of the parent group or any of its sub-group's memberIDs lists then the request shall be rejected with BAD_REQUEST Response Status Code. Otherwise the group-hosting CSE shall fan out the request to members contained in the Group Request Target Members parameter only.

The group-hosting CSE shall then perform the following steps for each member:

a)	The group-hosting CSE shall execute "Compose Request primitives". The primitive parameters From and To shall be mapped to the primitive parameters of the corresponding Request to be sent out to each member of the group. The primitive parameter From shall be used directly. The primitive parameter To (i.e. <URI of group resource>/fopt) shall be replaced by resource identifiers present in the memberIDs attribute of the group resource. Any additional relative address that was appended to .../fopt in the original Request shall be appended to each To URI. If the group-hosting CSE received a Group Request Identifier in the incoming request, or if it generated a new one as described above, it shall include this unique Group Request Identifier primitive parameter in every Request.

b)	"Send the Request to the receiver CSE".

c)	"Wait for Response primitives".

The procedures between group-hosting CSE and member-hosting CSEs shall comply with the corresponding procedures as described in clause 7. The detailed procedures are according to the type of Resource provided in the Request primitive.

7.4.14.2.5	Aggregation of member responses

After receiving the member responses from the member hosting CSEs, the group-hosting CSE shall respond to the Originator with an aggregated response. To indicate which response is generated by which member resource, the Hosting CSE shall set that member's resource ID into the From response parameter in each member response.

If Response Type, Result Expiration Timestamp or Result Persistence were set in the request, these affect the behaviour of the group-hosting CSE as follows:

If Response Type is set to blockingRequest, the group-hosting CSE shall respond only once with the aggregated response. It shall do this before the time indicated by the Result Expiration Timestamp is reached. The group-hosting CSE shall discard any member responses received after this time.

If Response Type is set to nonBlockingRequestSynch, the group-hosting CSE shall create a <request> resource locally and respond the Originator with the address of this <request> resource. Until the Result Expiration Timestamp time is reached, the group-hosting CSE shall aggregate the member responses and include this aggregated response in the operationResult of the <request> resource.

If Response Type is set to nonBlockingRequestAsynch, the group-hosting CSE shall notify the Originator or the notification targets with aggregated responses received before the Result Expiration Timestamp is reached. The group-hosting CSE may notify the Originator more than once during the period until the Result Expiration Timestamp is reached. Each notification shall contain different member responses.

If Response Type is set to flexBlocking, the group-hosting CSE shall keep aggregating the member responses until the group-hosting CSE determines that it is time to send a response – this depends on the properties of the group-hosting CSE related to the <group> resource (the number of aggregated responses or the time period of the aggregation). By that time, if the aggregated response contains all the member responses, the group-hosting CSE shall respond with the aggregated response. However if only some of the member responses have been received, the group-hosting CSE shall create a <request> resource from the received request, and respond to the Originator with the reference to the created <request> resource as well as the currently aggregated responses. Until the time specified in Result Expiration Timestamp is reached, the group-hosting CSE shall keep aggregating the remaining member responses and updating the aggregated response in the operationResult of the <request> resource. If notificationTarget is provided in the request, the group-hosting CSE shall notify the Originator with the aggregated response. Each notification shall contain different member responses.

If the group-hosting CSE supports <request> resource, in the nonBlockingRequestAsynch, nonBlockingRequestSynch and flexBlocking case, it shall set the requestStatus of the <request> resource to PARTIALLY_COMPLETED if some of the member responses are received. If the group-hosting CSE has aggregated all the member responses, it shall set the requestStatus to COMPLETED.

In any of the cases above, member responses received after the Result Expiration Timestamp shall be discarded. After the time specified in Result Persistence, the aggregated response shall not be retrievable.

If the group-hosting CSE gets no response before the Result Expiration Timestamp expiry, then the Hosting CSE shall return an error with the Response Status Code parameter set as "GROUP_MEMBERS_NOT_RESPONDED". Otherwise, the group-hosting CSE shall return the successful Response Status Code parameter value "OK" regardless of the requested operation. Note that the "OK" successful Response Status Code parameter is set regardless of the Response Status Code parameter value in each response primitive from the group member(s).

When aggregating notifications the group-hosting CSE, upon receiving the first notification, shall use the group's notifyAggregation attribute and wait until notifyAggregation/number notifications have been received or until the notifyAggregation/duration has elapsed, whichever comes first, and send a Notify primitive containing the aggregatedNotification data object defined in Table 7.5.1.1-2. If the notifyAggregation attribute is not specified in the <group> resource then the group-hosting CSE shall use the currentNrOfMembers attribute of the <group> and a duration specified by the M2M Service Provider instead of the number and duration from the notifyAggregation attribute.

If any of the parameters mentioned above are missing from the request, the group-hosting CSE shall determine the time to respond using its local Policy.

7.4.14.2.6	Multicast fan out procedure

If the group-hosting CSE holds a Multicast Group Information data object (see clause 7.5.3) that refers to the parent <group> resource it shall perform the following steps. Refer to clause 10.2.7.13.2 of oneM2M TS-0001 [6] for further details.

Figure 7.4.14.2.6-1: Generic procedure of Group-Hosting CSE

GrphostCSE-1.0 "Compose a Request primitive": The group-hosting CSE shall prepare the primitive parameters according to the Multicast Group Information: To shall be multicastGroupFanoutTarget, Request Expiration Timestamp shall be Request Expiration Timestamp in the request from the Originator. If the Request Expiration Timestamp was not set in the request, Request Expiration Timestamp shall be set as the responseTimeWindow according to the local policy. The Response Type shall not be included in the request primitive.

GrphostCSE-2.0 "Send a Request primitive to the Member Hosting CSE by multicast": The group-hosting CSE shall check the multicastType in the Multicast Group Information: if the multicastType is MBMS, follow the 3GPP MBMS fanout procedure, refer to clause 7.4.14.2.7; if the multicastType is IP, send the Request to the multicastAddress in the Multicast Group Information.

GrphostCSE-2.1 "Fanout Request to each member": The group-hosting CSE shall perform Fanout Request to each member, refer to clause 7.4.14.2.4.

GrphostCSE-3.0 "Wait for Response primitive": If the group-hosting CSE receives responses from the multicast group member hosting CSEs before the Request Expiration Timestamp expiry, the group-hosting CSE shall get their Request Identifier and From parameters and match them against the multicast fan out request: if the Request Identifier is the same as the parameter in the request, and the From is the same as the member-hosting CSE ID of the multicast group, the group-hosting CSE shall accept the response of multicast fan out.

The member-hosting CSE shall perform the following primitive specific operations:

Figure 7.4.14.2.6-2: Generic procedure of Member Hosting CSE

MemhostCSE-1.0 "Check the validity of received request primitive": The Member Hosting CSE shall check the To primitive parameter in the request from the multicastAddress which it joined, and compare the To with the multicastGroupFanoutTarget attribute of all the <localMulticastGroup> resources to get the memberList. If there is no match result, the Member Hosting CSE shall return an error response with Response Status Code indicating "NOT_FOUND"; if there is a match result, the Member Hosting CSE shall replace the primitive parameter To by resource identifiers present in the memberList attribute of the local multicast group resource.

MemhostCSE-2.0: Resource handling procedures: Refer to Figure 7.2.2.2-2 for details.

MemhostCSE-3.0 "Send Response Primitive": The Member Hosting shall aggregate the operation results if there are multiple member IDs hosted on the same Member Hosting CSE, set the To primitive parameter as the value of responseTarget of the resource <localMulticastGroup> if the responseTarget exists. Set the From primitive parameter as the value of CSE-ID of the member Hosting CSE, and wait a randomized time that is less than the value of the responseTimeWindow of the resource <localMulticastGroup> if responseTimeWindow exists.

7.4.14.2.7	3GPPTM MBMS fan out procedure

The procedure is specified in the clause 7.7.3.2 in oneM2M TS-0026 [43].

The group-hosting CSE shall check the TMGIExpiration in the Multicast Group Information: if the TMGIExpiration expires, the group-hosting CSE shall execute the following steps in order:

a)	Send 3GPP Allocate TMGI Request [51] to the groupServiceServerAddress over Mcn reference point.

b)	Receive the corresponding response from 3GPP network: if the procedure completes successfully the group-hosting CSE shall get the TMGI and TMGIExpiration from the response, then go to 2). If the procedure fails, the group-hosting CSE shall perform a Fanout Request to each member in the Multicast Group Information, refer to clause 7.4.14.2.4.

If the TMGIExpiration does not expire, the group-hosting CSE shall execute the following steps in order:

a)	Check the existing <schedule> child resources for all the Member Hosting CSE <Node> resources. If there is no time intersection of the existing <schedule>s, then return an error response with Response Status Code indicating "EXTERNAL_OBJECT_NOT_REACHABLE" to the originator after which the procedure is terminated. If there is the time intersection, the group-hosting CSE shall check if the Operation Execution Time or Request Expiration Timestamp is in the scope of the intersection when Operation Execution Time or Request Expiration Timestamp is included in the request, If Operation Execution Time is not in the scope of the intersection, the group-hosting CSE shall return an error with Response Status Code indicating "EXTERNAL_OBJECT_NOT_REACHABLE_BEFORE_RQET_TIMEOUT" after which the procedure is terminated. If Request Expiration Timestamp is not in the scope of the intersection, the group-hosting CSE shall return an error with Response Status Code indicating "EXTERNAL_OBJECT_NOT_REACHABLE_BEFORE_OET_TIMEOUT" after which the procedure is terminated. Otherwise, go to b).

b)	Send 3GPP Group Message Delivery via MBMS [51] to the groupServiceServerAddress in the Multicast Group Information over the Mcn reference point.

c)	Receive the corresponding response from 3GPP network: if the procedure fails or the parameter in the result indicates the delivery to some members failed, the group-hosting CSE shall perform the Fan out Request to each failed member, refer to clause 7.4.14.2.4.

7.4.14.3	<fanOutPoint> resource specific procedures for CRUD operations

7.4.14.3.1	Introduction

This clause describes <fanOutPoint> resource specific behaviour for CRUD operations.

7.4.14.3.2	Create

A <fanOutPoint> is a virtual resource and cannot be created via API. However, a Create operation can be sent to an existing <fanOutPoint>. A Create operation sent to a <fanOutPoint> does not create a child resource of that <fanOutPoint>. Instead, that Create operation is fanned out to the members (if any) of the parent <group>. It is equivalent to sending a Create to each member and therefore results in new resources being created as children of these existing members.

If the Create is sent to a hierarchical URI containing a fanOutPoint and an additional path relative to that fanOutPoint then the new resources are not created as immediate children of the members, rather they are created as children of descendants of those members (as determined by the relative path).

Originator:

Primitive specific operation after Orig-1.0 "Compose Request primitive" and before Orig-2.0 "Send the Request to the receiver CSE": In the case the Originator wants to subscribe to all the member resources of the group and the originator wants the group-hosting CSE to aggregate all the notifications come from its member-hosting CSEs, the Originator shall include the notificationForwardingURI attribute in the <subscription> resource.

If one or more of the individual responses has a Response Status Code other than CREATED then the Originator may issue a new CREATE request to the group-hosting CSE with the Group Request Target Members parameter containing the list of members for which the first CREATE failed.

Receiver:

Primitive specific operation after Recv-6.2 "Check existence of the addressed resource" and before Recv-6.3 "Check authorization of the Originator".

Primitive specific operation additional to Recv-6.3 "Check authorization of the Originator": The group-hosting CSE shall check the authorization of the Originator based on the membersAccessControlPolicyIDs of the parent <group> resource. In the case the membersAccessControlPolicyIDs is not provided, the accessControlPolicyIDs of the parent <group> resource shall be used.

Primitive specific operation to replace Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed" and Recv-6.6 "Announce/De-announce the resource" in the generic procedure:

Validate the type of resource to be created, refer to clause 7.4.14.2.1.

If the members are not in the Multicast Group Information locally, then perform sub-group creation for members residing on the same CSE, refer to clause 7.4.14.2.2.

Assign URI for aggregation of notification, refer to clause 7.4.14.2.3.

If there is Multicast Group Information held locally, the receiver shall perform the Multicast fan out procedure, refer to clause 7.4.14.2.6. For the members which are not in the multicast group, the receiver shall perform the fan out Request to each member, refer to clause 7.4.14.2.4.

Aggregation of member responses, refer to clause 7.4.14.2.5.

7.4.14.3.3	Retrieve

Originator:

No primitive specific operations.

If one or more of the individual responses has a Response Status Code other than OK then the Originator may issue a new RETRIEVE request to the group-hosting CSE with the Group Request Target Members parameter containing the list of members for which the first RETRIEVE failed.

Receiver:

Primitive specific operation after Recv-6.2 "Check existence of the addressed resource" and before Recv-6.3 "Check authorization of the Originator".

Primitive specific operation additional to Recv-6.3 "Check authorization of the Originator": The group-hosting CSE shall check the authorization of the Originator based on the membersAccessControlPolicyIDs of the parent group resource. In the case the membersAccessControlPolicyIDs is not provided, the accessControlPolicyIDs of the parent <group> resource shall be used.

Primitive specific operation to replace Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed" and Recv-6.6 "Announce/De-announce the resource" in the generic procedure:

If the members are not in the Multicast Group Information held locally, then perform sub-group creation for members residing on the same CSE, refer to 7.4.14.2.2.

If there is Multicast Group Information held locally, the receiver shall perform the Multicast fan out procedure, refer to clause 7.4.14.2.6. For the members which are not in the multicast group, the receiver shall perform the fan out Request to each member, refer to clause 7.4.14.2.4.

Aggregation of member responses, refer to clause 7.4.14.2.5.

7.4.14.3.4	Update

Originator:

No primitive specific operations.

If one or more of the individual responses has a Response Status Code other than UPDATED then the Originator may issue a new UPDATE request to the group-hosting CSE with the Group Request Target Members parameter containing the list of members for which the first UPDATE failed.

Receiver:

Primitive specific operation after Recv-6.2 "Check existence of the addressed resource" and before Recv-6.3 "Check authorization of the Originator".

Primitive specific operation additional to Recv-6.3 "Check authorization of the Originator": The group-hosting CSE shall check the authorization of the Originator based on the membersAccessControlPolicyIDs of the parent group resource. In the case the membersAccessControlPolicyIDs is not provided, the accessControlPolicyIDs of the parent <group> resource shall be used.

Primitive specific operation to replace Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed" and Recv-6.6 "Announce/De-announce the resource" in the generic procedure:

If the members are not in the Multicast Group Information held locally, then perform sub-group creation for members residing on the same CSE, refer to clause 7.4.14.2.2.

If there is Multicast Group Information held locally, the receiver shall perform the Multicast fan out procedure, refer to clause 7.4.14.2.6. For the members which are not in the multicast group, the receiver shall perform the fan out Request to each member. See clause 7.4.14.2.4.

Aggregation of member responses, refer to clause 7.4.14.2.5.

7.4.14.3.5	Delete

The primitive deletes the member resources belonging to an existing <group> resource, along with their child resources.

Originator:

No primitive specific operations.

If one or more of the individual responses has a Response Status Code other than DELETED then the Originator may issue a new DELETE request to the group-hosting CSE with the Group Request Target Members parameter containing the list of members for which the first DELETE failed.

Receiver:

Primitive specific operation after Recv-6.2 "Check existence of the addressed resource" and Recv-6.3 "Check authorization of the Originator": The To parameter consists of the URI of the group resource plus a suffix consisting of /fopt or /fopt/ plus any additional appended relative address.

Primitive specific operation additional to Recv-6.3 "Check authorization of the Originator": The group-hosting CSE shall check the authorization of the Originator based on the membersAccessControlPolicyIDs of the parent group resource. In the case the membersAccessControlPolicyIDs is not provided, the accessControlPolicyIDs of the parent <group> resource shall be used.

Primitive specific operation to replace Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed" and Recv-6.6 "Announce/De-announce the resource" in the generic procedure:

If the members are not in the Multicast Group Information held locally, then perform sub-group creation for members residing on the same CSE, refer to clause 7.4.14.2.2.

If there is Multicast Group Information held locally, the receiver shall perform the Multicast fan out procedure, refer to clause 7.4.14.2.6. For the members which are not in the multicast group, the receiver shall perform the fan out Request to each member. See clause 7.4.14.2.4.

Aggregation of member responses, refer to clause 7.4.14.2.5.

If one or more members respond with a DELETED Response Status Code, the <group> hosting CSE shall remove the references to them from the membersIDs attribute of the targeted <group>, unless the reference in question is a virtual resource reference.


### 7.4.15	Resource Type <mgmtObj>


7.4.15.1	Introduction

The <mgmtObj> resource contains management data which represents individual M2M management functions. It represents a general structure to map to technology specific data models. There are multiple specializations of <mgmtObj>; these are defined in the Annex D. Each of these specializations has its own schema file. There is no separate schema file just for <mgmtObj>, however the XML schema types for the specializations all conform to the pattern described in this clause.

Table 7.4.15.1-1: Universal/Common Attributes of <mgmtObj> resource

Table 7.4.15.1-2: Resource Specific Attributes of <mgmtObj> resource

Table 7.4.15.1-3: Child resources of <mgmtObj> resource

7.4.15.2	<mgmtObj> resource specific procedures for CRUD operations

7.4.15.2.1	Introduction

This clause describes <mgmtObj> resource specific procedure on resource Hosting CSE for CRUD operations.

The procedures are defined for management when technology specific protocols are used. When service layer management is performed, generic procedures defined in clause 7.2.2 shall comply for resource creation, update, retrieval and deletion. Procedures additional to resource manipulations to perform the management are further defined in Annex D.

7.4.15.2.2	Create

Originator:

Primitive specific operation before Orig-1.0 "Compose Request primitive":

If the originator is the managed entity, it shall generate the <mgmtObj> resource representation based on the technology-specific data model object of the managed entity to be exposed. The objectIDs and objectPaths attributes may be set in the Request.

Receiver:

The following steps shall be performed after Recv-6.4 "Check validity of resource representation for the given resource type" and before Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed":

"Identify the managed entity and the technology-specific protocol". See clause 7.3.4.1.

The receiver shall generate the technology-specific data model object to be added to the managed entity based on the <mgmtObj> resource representation provided in the Request primitive. The receiver may determine the target location on the managed entity where the generated technology specific data model object shall be added based on the objectIDs and objectPaths provided in the request primitive and the technology-specific data model being used. The receiver may also choose to let the managed entity decide the target location where the generated technology specific data model object shall be added using technology specific mechanism.

"Establish a management session with the managed entity". See clause 7.3.4.3.

"Send the management request(s) to the managed entity corresponding to the received Request primitive". See clause 7.3.4.4.
If the receiver receives an error response from the managed entity because the technology-specific data model object to be added already exists on the managed entity, the receiver shall check (e.g. by using the OMA-DM Get command) if the existing technology-specific data model object is the same as the one to be added, then it shall consider the requested primitive as successfully performed instead of sending an error response primitive; otherwise, it shall reject the request with the Response Status Code indicating an "ALREADY_EXISTS" error in the Response primitive. The receiver shall also record the location where the technology-specific data model object is added to the managed entity in the successful case. The objectIDs and objectPaths attributes may be set in the Request.

The receiver may repeat step 3 in order to add to the managed entity the technology-specific data model objects that are mapped from the mandatory sub-resources (including any descendants) that are required to be created automatically with the default attribute values.

7.4.15.2.3	Retrieve

Receiver:

Primitive specific operation after Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed" and before Recv-6.6 "Announce/De-announce the resource":

"Identify the managed entity and the technology-specific protocol". See clause 7.3.4.1.

"Locate the technology-specific data model objects to be managed on the managed entity". See clause 7.3.4.2.

"Establish a management session with the managed entity". See clause 7.3.4.3.

"Send the management request(s) to the managed entity corresponding to the received Request primitive". See clause 7.3.4.4. The receiver may also update the <mgmtObj> resource representation with the retrieved technology-specific data model object if required according to the local policy.

7.4.15.2.4	Update

The Update primitive is used for the update of the resource as well as the execution of a management procedure. The execution is performed using an Update primitive by addressing specific attribute to start the management procedure (see Annex D). If the Update primitive addresses both normal as well as executable attributes then it shall perform the execution after the update of normal attributes.

Receiver:

Primitive specific operation after Recv-6.4 "Check validity of resource representation" and before Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed":

"Identify the managed entity and the technology-specific protocol". See clause 7.3.4.1.

"Locate the technology-specific data model objects to be managed on the managed entity". See clause 7.3.4.2.

"Establish a management session with the managed entity". See clause 7.3.4.3.

"Send the management request(s) to the managed entity corresponding to the received Request primitive". The receiver may also update the <mgmtObj> resource representation with the retrieved technology-specific data model object information if required according to the local policy. See clause 7.3.4.4.

7.4.15.2.5	Delete

Receiver:

Primitive specific operation after Recv-6.4 "Check validity of resource representation" and before Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed":

"Identify the managed entity and the technology-specific protocol". See clause 7.3.4.1.

"Locate the technology-specific data model objects to be managed on the managed entity". See clause 7.3.4.2.

"Establish a management session with the managed entity". See clause 7.3.4.3.

"Send the management request(s) to the managed entity corresponding to the received Request primitive". See clause 7.3.4.4.


### 7.4.16	Resource Type <mgmtCmd>


7.4.16.1	Introduction

The <mgmtCmd> resource represents a method to execute management procedures or to model commands and remote procedure calls (RPC) required by existing management protocols and enables AEs to request management procedures to be executed on a remote entity. The detailed description can be found in clause 9.6.16 in oneM2M TS-0001 Architecture TS [6].

Table 7.4.16.1-1: Data type definition of <mgmtCmd> resource

Table 7.4.16.1-2: Universal/Common Attributes of <mgmtCmd> resource

Table 7.4.16.1-3: Resource Specific Attributes of <mgmtCmd> resource

Table 7.4.16.1-4: Child resources of <mgmtCmd> resource

The <mgmtCmd> shall be executed for the following modes:

If execMode is IMMEDIATEONCE, <mgmtCmd> shall be executed immediately and only once. In this mode, execFrequency, execDelay, and execNumber shall not be used.

If execMode is IMMEDIATEREPEAT, <mgmtCmd> shall be executed immediately and repeated multiple times as determined by execNumber and the time interval between each execution is specified by execFrequency. In this mode, execDelay shall not be used.

If execMode is RANDOMONCE, <mgmtCmd> shall be executed only once at a delayed time which is specified by execDelay. In this mode, execFrequency and execNumber shall not be used.

If execMode is RANDOMREPEAT, <mgmtCmd> shall be executed multiple times as specified by execNumber but the first execution shall be executed at a delayed time. execDelay specifies the delayed time. The time interval between each execution is specified by execFrequency.

7.4.16.2	<mgmtCmd> resource specific procedures for CRUD operations

7.4.16.2.0	Introduction

This clause describes <mgmtCmd> resource specific procedures for CRUD operations.

7.4.16.2.1	Create

This procedure shall use the Create common operations detailed in clause 7.3 without primitive-specific actions. The Originator shall use the steps described in clause 7.2.2.1. The Receiver shall use the steps described in clause 7.2.2.2.

The Originator shall provide the <mgmtCmd> resource representation to the Receiver (e.g. IN-CSE). The Receiver may generate one of the following status codes and send it to the Originator.

If the Originator provides an invalid cmdType value in the Create primitive, the Receiver shall generate a Response Status Code indicating "INVALID_CMDTYPE" error.

If the name/value entry in execReqArgs does not match the value of cmdType in the Create primitive, the Receiver shall generate a Response Status Code indicating "INVALID_ARGUMENTS" error.

If the name/value entries in execReqArgs do not contain mandatory arguments as required by cmdType, the Receiver shall generate a Response Status Code indicating "INSUFFICIENT_ARGUMENTS" error.

7.4.16.2.2	Retrieve

This procedure shall use the Retrieve common operations detailed in clause 7.3 without primitive specific actions. The Originator shall use the steps described in clause 7.2.2.1. The Receiver shall use the steps described in clause 7.2.2.2.

7.4.16.2.3	Update

7.4.16.2.3.1	Update (Normal)

If the Update primitive does not address the execEnable attribute of the <mgmtCmd> it results in update of all or part of the information of an existing <mgmtCmd> resource with the new attribute values. The procedure uses the common Update operations detailed in clause 7.3, without primitive specific actions.

The Originator shall use the steps described in clause 7.2.2.1. The Receiver shall use the steps described in clause 7.2.2.2.

If the Originator attempts to update attributes execTarget, execMode, but the <mgmtCmd> has a child resource <execInstance> already created, the Receiver shall generate a Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

If the Update primitive does address the execEnable attribute of the <mgmtCmd> it effectively triggers an Execute <mgmtCmd> procedure, see clause 7.4.16.2.3.2.

7.4.16.2.3.2	Update (Execute)

The execute operation is triggered by an Update primitive if the primitive addresses the execEnable attribute of the <mgmtCmd>. The procedure uses the Update common operations detailed in clause 7.2.2.2 with the following primitive specific operations after Recv-6.5:

The Receiver shall identify the managed entity and the management protocol. The execTarget attribute of <mgmtCmd> indicates the managed entity.

The Receiver shall automatically create an <execInstance> based on the <mgmtCmd> resource. If the execTarget attribute addresses a <group> resource, the Receiver shall create multiple <execInstance> sub-resources based on the value of currentNrOfMembers attribute.

The Receiver shall copy the following attributes from <mgmtCmd> to each <execInstance> created: execMode, execFrequency, execDelay, execNumber, and execReqArgs. The execStatus of <execInstance> is set to INITIATED. The Receiver shall set the execTarget attribute of each <execInstance> sub-resource to the URI of each target <node> resource.

The Receiver shall determine if the <mgmtCmd> shall be executed immediately or postponed according to the combination of execMode, execFrequency, execDelay, and execNumber. If the <mgmtCmd> shall be executed immediately (e.g. execMode is IMMEDIATEONCE), the following steps shall be performed; otherwise the following steps shall be postponed and skipped until the delay is expired (e.g. as indicated by execDelay).

The Receiver shall establish a management session with the identified managed entity.

The Receiver shall perform management command conversion and execution and set the execStatus attribute of <execInstance> to PENDING. If the Receiver cannot perform the command conversion successfully (e.g. execReqArgs does not have sufficient name/value pairs), the Receiver shall generate a Response Status Code indicating "MGMT_CONVERSION_ERROR" error.

After receiving completion response from the managed entity, the Receiver shall set execStatus attribute of corresponding <execInstance> to FINISHED.

If the Update primitive does not address the execEnable attribute of the <mgmtCmd>, it is treated as a normal Update, see clause 7.4.16.2.3.1.

7.4.16.2.4	Delete

This procedure is based on the Delete common operations detailed in clause 7.3.

The Receiver shall determine:

If there are related management operations pending on the managed entity by checking if the execStatus attributes of all the <execInstance> child resources of the <mgmtCmd> to see if any of them are PENDING.

If the related management operations are cancellable by checking the cmdType attribute of <mgmtCmd>.

If there are no management commands pending on the remote entity the Receiver shall delete the addressed <mgmtCmd> resource and send a success response to the Originator.

If there are cancellable management commands still pending on any remote entity, the Receiver shall perform the following steps:

The Receiver shall identify the managed entity and the management protocol. The execTarget attribute of each <execInstance> sub-resource which has execStatus of PENDING indicates the managed entity.

The Receiver shall establish a management session with each managed entity.

The Receiver shall perform management command conversion and execution resulting in cancellation of the commands which are pending on the managed entity.

For each successful cancellation RPC the execStatus attribute of the corresponding <execInstance> is set to CANCELLED. For each unsuccessful cancellation RPCs the execStatus attribute of the corresponding <execInstance> is determined from the reported fault codes for the unsuccessful RPCs.

Upon completion of all the cancellation operations, if any fault codes are returned by the managed entity, an error response to the Delete primitive with a Response Status Code indicating "CANCELLATION_FAILED" is returned, and the <mgmtCmd> resource is not deleted. If all cancellation operations are successful on the managed entity, a success response to the Delete primitive is returned and the <mgmtCmd> resource is deleted.

If there are non-cancellable management commands still pending on the remote entity, the Receiver shall send an error response to the Delete request to the Originator with a Response Status Code indicating "MGMT_COMMAND_NOT_CANCELLABLE" error. The execStatus attribute of the specific <execInstance> sub-resource is changed to STATUS_NON_CANCELLABLE.


### 7.4.17	Resource Type <execInstance>


7.4.17.1	Introduction

The <execInstance> resource shall contain the following child resource and attributes.

Table 7.4.17.1-1: Data type definition of <execInstance> resource

Table 7.4.17.1-2: Universal/Common Attributes of <execInstance> resource

Table 7.4.17.1-3: Resource Specific Attributes of <execInstance> resource

Table 7.4.17.1-4: Child Resources of <execInstance> resource

7.4.17.2	<execInstance> resource specific procedures for CRUD operations

7.4.17.2.0	Create

The <execInstance> resource shall not be created via API.

7.4.17.2.1	Update (Cancel)

The <execInstance> Cancel operation is triggered by an Update primitive, if the primitive addresses the execDisable attribute. The procedure is based on Update common operations detailed in clause 7.3.

The Receiver shall determine:

If there are related management operations pending on the managed entity by checking if the execStatus attribute of the addressed <execInstance> sub-resource is PENDING.

If the related management operations are cancellable, by checking the cmdType attribute of the parent <mgmtCmd> resource.

If there are no management commands still pending on the remote entity, an error response to the Update primitive with a Response Status Code indicating "ALREADY_COMPLETE" is returned to the Originator.

If there are cancellable management commands still pending on the remote entity, the Receiver shall perform the following steps:

The Receiver shall identify the managed entity and the management protocol. The execTarget attribute of the addressed <execInstance> indicates the managed entity.

The Receiver shall establish a management session with the managed entity.

The Receiver shall perform management command conversion and execution resulting in cancellation of the commands which are pending on the managed entity.

If the cancellation is successfully executed on the managed entity, the Receiver shall return a success response to the Originator and shall set the execStatus attribute of <execInstance> to CANCELLED.

If the cancellation is unsuccessful on the managed entity, the Receiver shall return an error response to the Originator with a Response Status Code indicating "MGMT_CANCELLATION_FAILED". The execStatus attribute is determined from the fault codes reported by the managed entity.

If there are non-cancellable management commands still pending on the remote entity, the Receiver shall return an error response to the Originator with a Response Status Code indicating "MGMT_COMMAND_NOT_CANCELLABLE" and the execStatus attribute is changed to STATUS_NON_CANCELLABLE.

7.4.17.2.2	Retrieve

This procedure shall use the Retrieve common operations detailed in clause 7.3, without primitive specific actions. The Originator shall use the steps described in clause 7.2.2.1. The Receiver shall use the steps described in clause 7.2.2.2.

7.4.17.2.3	Delete

This procedure is based on the Delete common operations detailed in clause 7.3.

The Receiver shall determine:

If there are related management operations pending on the managed entity by checking if the execStatus attribute of the addressed <execInstance> sub-resource is PENDING.

If the related management operations are cancellable, by checking the cmdType attribute of the parent <mgmtCmd> resource.

If there are no management commands still pending on the remote entity, the Receiver shall delete the addressed resource and send a success response to the Originator.

If there are cancellable management commands still pending on the remote entity, the Receiver shall perform the following steps:

The Receiver shall identify the managed entity and the management protocol. The execTarget attribute of the addressed <execInstance> indicates the managed entity.

The Receiver shall establish a management session with the managed entity.

The Receiver shall perform management command conversion and execution resulting in cancellation of the commands which are pending on the managed entity.

If the cancellation is successfully executed on the managed entity, the Receiver shall return a success response to the Delete request to the Originator and shall delete the <execInstance> resource.

If the cancellation is unsuccessful on the managed entity, the Receiver shall return an error response to the Delete request to the Originator with a Response Status Code indicating "MGMT_CANCELLATION_FAILED". The execStatus attribute is determined from the fault codes reported by the managed entity.

If there are non-cancellable management commands still pending on the remote entity, the Receiver shall return an error response to the Delete request to the Originator with a Response Status Code indicating "MGMT_COMMAND_NOT_CANCELLABLE". The execStatus attribute is set to STATUS_NOT_CANCELLABLE.


### 7.4.18	Resource Type <node>


7.4.18.1	Introduction

The <node> resource represents specific information that provides properties of an oneM2M Node that can be utilized by other oneM2M operations. The <node> resource has <mgmtObj> as its child resources.

Table 7.4.18.1-1: Data type definition of <node> resource

Table 7.4.18.1-2: Universal/Common Attributes of <node> resource

Table 7.4.18.1-3: Resource Specific Attributes of <node> resource

Table 7.4.18.1-4: Child resources of <node> resource

7.4.18.2	<node> resource specific procedures for CRUD operations

7.4.18.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.18.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.18.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.18.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.19	Resource Type <m2mServiceSubscriptionProfile>


7.4.19.1	Introduction

The <m2mServiceSubscriptionProfile> resource represents an M2M Service Subscription Profile. It is used to represent all data pertaining to the M2M Service Subscription Profile, i.e. the technical part of the contract between an M2M Application Service Provider and an M2M Service Provider.

The detailed description can be found in clause 9.6.19 in oneM2M TS-0001 [6].

Table 7.4.19.1-1: Data type definition of <m2mServiceSubscriptionProfile> resource

Table 7.4.19.1-2: Universal/Common Attributes of <m2mServiceSubscriptionProfile>

Table 7.4.19.1-3: Child resources of <m2mServiceSubscriptionProfile>

7.4.19.2	<m2mServiceSubscriptionProfile> resource specific procedures for CRUD operations

7.4.19.2.0	Introduction

This clause describes <m2mServiceSubscriptionProfile> resource specific behaviour for CRUD operations.

7.4.19.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.19.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.19.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.19.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.20	Resource Type <serviceSubscribedNode>


7.4.20.1	Introduction

The <serviceSubscribedNode> resource represents M2M Node information that is needed as part of the M2M Service Subscription resource. It shall contain information about the M2M Node as well as application identifiers of the Applications running on that Node.

The detailed description can be found in clause 9.6.20 in oneM2M TS-0001 [6].

Table 7.4.20.1-1: Data type definition of <serviceSubscribedNode> resource

Table 7.4.20.1-2: Universal/Common Attributes of <serviceSubscribedNode> resource

Table 7.4.20.1-3: Resource Specific Attributes of <serviceSubscribedNode> resource

Table 7.4.20.1-4: Child resources of <serviceSubscribedNode> resource

7.4.20.2	<serviceSubscribedNode> resource specific procedures for CRUD operations

7.4.20.2.0	Introduction

This clause describes <serviceSubscribedNode> resource specific behaviour for CRUD operations.

7.4.20.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Addition to the generic procedure in clause 7.2.2.2.

Recv-6.4 The following steps are in addition to the procedures defined in clause 7.3.3.3:

If the ruleLinks attribute is present in the resource representation, but the CSE-ID attribute is not present in the resource representation, then the request shall be rejected with a Response Status Code indicating "BAD_REQUEST" error.

7.4.20.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedure in clause 7.2.2.2.

7.4.20.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Addition to the generic procedures in clause 7.2.2.2.

Recv-6.4: The following step is in addition to the procedures defined in clause 7.3.3.4

If the ruleLinks attribute is present in the resource representation, but the CSE-ID attribute is not present in the original resource, then the request shall be rejected with a Response Status Code indicating "BAD_REQUEST" error.

7.4.20.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.21	Resource Type <pollingChannel>


7.4.21.1	Introduction

The <pollingChannel> resource is used to perform service layer long polling when an AE/CSE cannot receive a request from other entities, however it can get a request as a response to a long polling request. Actual long polling can be performed on the <pollingChannelURI> resource which is the child resource of the <pollingChannel> resource.

The detailed description can be found in clause 9.6.21 in oneM2M TS-0001 [6].

Table 7.4.21.1-1: Data type definition of <pollingChannel> resource

Table 7.4.21.1-2: Universal/Common Attributes of <pollingChannel> resource

Table 7.4.21.1-3: Child resources of <pollingChannel> resource

7.4.21.2	<pollingChannel> resource specific procedures for CRUD operations

7.4.21.2.0	Introduction

This clause describes <pollingChannel> resource specific behaviour for CRUD operations.

7.4.21.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Same as the generic procedures in clause 7.2.2.2 except one addition:

After Recv-6.3 procedure, the Hosting CSE shall check if the Originator ID is the same as the AE-ID or CSE-ID of the target <AE> resource or <remoteCSE> resource, respectively. If the check fails, then the Hosting CSE shall return a response primitive with a Response Status Code indicating "ORIGINATOR_HAS_NO_PRIVILEGE" error.

7.4.21.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Same as the generic procedures in clause 7.2.2.2 except one addition:

After Recv-6.3 procedure, the Hosting CSE shall check if the Originator ID is the same as the AE-ID or CSE-ID of the target <AE> resource or <remoteCSE> resource, respectively. If the check fails, then the Hosting CSE shall return a response primitive with a Response Status Code indicating "ORIGINATOR_HAS_NO_PRIVILEGE" error.

7.4.21.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Same as the generic procedures in clause 7.2.2.2 except one addition:

After Recv-6.3 procedure, the Hosting CSE shall check if the Originator ID is the same as the AE-ID or CSE-ID of the target <AE> resource or <remoteCSE> resource, respectively. If the check fails, then the Hosting CSE shall return a response primitive with a Response Status Code indicating "ORIGINATOR_HAS_NO_PRIVILEGE" error.

7.4.21.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Same as the generic procedures in clause 7.2.2.2 except one addition:

After Recv-6.3 procedure, the Hosting CSE shall check if the Originator ID is the same as the AE-ID or CSE-ID of the target <AE> resource or <remoteCSE> resource, respectively. If the check fails, then the Hosting CSE shall return a response primitive with a Response Status Code indicating "ORIGINATOR_HAS_NO_PRIVILEGE" error.


### 7.4.22	Resource Type <pollingChannelURI>


7.4.22.1	Introduction

The <pollingChannelURI> resource is the virtual child resource which is automatically generated during the parent <pollingChannel> resource creation. The detailed description can be found in clause 9.6.22 in oneM2M TS-0001 [6].

There is no data type definition for <pollingChannelURI> resource because it is a virtual resource type.

7.4.22.2	<pollingChannelURI> resource specific procedures for CRUD operations

7.4.22.2.0	Introduction

This clause describes <pollingChannelURI> resource specific behaviour for the Retrieve operation as a service layer long polling request.

7.4.22.2.1	Create

Originator:

The <pollingChannelURI> resource shall not be created via API.

Receiver:

Not applicable.

7.4.22.2.2	Retrieve

Originator:

Shall execute Originator actions in clause 7.2.2.1 as a service layer long polling request. It is the Originator's responsibility to initiate this procedure after it gets long polling response either successful or unsuccessful. The Originator shall send this Retrieve request as blocking request (clause 8.2.1 in oneM2M TS-0001 [6]).

Receiver:

Shall execute the following steps in order and these are modifications to the generic procedure from Recv-6.3 to Recv-6.5 in clause 7.2.2.2:

Recv-6.3 Check if the request Originator is the creator of the parent <pollingChannel> resource. If it is not the creator, the Hosting CSE shall send a response primitive with a Response Status Code indicating "ORIGINATOR_HAS_NO_PRIVILEGE" error.

Recv-6.4 No change from the generic procedure.

Recv-6.5 If there is a pending request(s) to be sent to the Originator:

Create a Response primitive by setting the Content parameter with one of the pending request(s).

Else:

Wait for a request for the Originator until the Request Expiration Timestamp of the Originator's request. If a request is available before the Request Expiration Timestamp timeout, create a Response primitive setting the Content parameter to the received pending request. Otherwise, create a response primitive with a Response Status Code indicating "REQUEST_TIMEOUT" error.

7.4.22.2.3	Update

Originator:

The <pollingChannelURI> resource shall not be updated via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the validity of received request primitive":

If the request is received, the Receiver CSE shall execute the following steps in order:

"Create an unsuccessful Response primitive" with the Response Status Code indicating an "OPERATION_NOT_ALLOWED" error.

"Send the Response primitive".

7.4.22.2.4	Delete

Originator:

The <pollingChannelURI> resource shall not be deleted via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the validity of received request primitive":

If the request is received, the Receiver CSE shall execute the following steps in order:

"Create an unsuccessful Response primitive" with the Response Status Code indicating an "OPERATION_NOT_ALLOWED" error.

"Send the Response primitive".

7.4.22.2.5	Notify

When an Originator receives one or more request messages as a result of a long polling request to a <pollingChannelURI>  (clause 7.4.22.2.2) it shall send response(s) to those requests as Notify requests to the same <pollingChannelURI>, one Notify request for each primitive received in the long polling response. This is described in TS-0001 [6] clause 10.2.5.19 19 and depicted in TS-0001 [6], Figure 10.2.5.12-1 (Request/response delivery via polling channel). In this procedure, the Originator is the Target AE/CSE and the Receiver is the <pollingChannelURI> Hosting CSE, respectively.

Originator:

This procedure follows the procedure specified in clause 7.2.2.1 with the following <pollingChannelURI> resource-specific updates.

Additional primitive specific operation on Orig-1.0:

The Originator shall generate and populate a Notify request as described in clause 7.5.1.2.7.

Receiver:

The following are additional Hosting CSE procedures to the generic resource handling procedures from Recv-6.3 to Recv-6.5 in clause 7.2.2.2:

Recv-6.3 Check if the request Originator is the creator of the parent <pollingChannel> resource. If it is not the creator, the Hosting CSE shall send response primitive with a Response Status Code indicating "ORIGINATOR_HAS_NO_PRIVILEGE" error.

Recv-6.4 No change from the generic procedure.

Recv-6.5 Forward the response (step 006 in Figure 10.2.5.12-1 of TS-0001 [6]), which was contained in the Content parameter of the Notify request, to the entity that sent the associated request to the Hosting CSE (Originator in the figure 10.2.5.12-1). The associated request is the request that the Hosting CSE received and forwarded to the Registree AE or CSE over the polling channel (step 002 and step 004 in the figure). The association shall be done by matching the Request Identifier parameter of the request delivered in <pollingChannelURI> Retrieve response (step 004 in the figure) and the Request Identifier parameter of the response delivered in the Content parameter in a <pollingChannelURI> Notify request (step 005 in the figure).


### 7.4.23	Resource Type <statsConfig>


7.4.23.1	Introduction

The <statsConfig> resource is used to store configuration data for collecting statistics for AEs. The <eventConfig> child resource is a mechanism for defining events that trigger statistics collection activity. Additional description of the <statsConfig> resource is contained in clauses 9.6.23 and 10.2.11 of oneM2M TS-0001 [6].

Table 7.4.23.1-1: Data type definition of <statsConfig>

Table 7.4.23.1-2: Universal/Common Attributes of <statsConfig> resource

Table 7.4.23.1-3: Child resources of <statsConfig> resource

7.4.23.2	<statsConfig> resource-specific procedures for CRUD operations

7.4.23.2.1	Create

Originator:

No change from the generic procedure in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.23.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.23.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.23.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.24	Resource Type <eventConfig>


7.4.24.1	Introduction

The <eventConfig> resource defines events that trigger statistics collection activity on an IN-CSE. Additional description of the <eventConfig> resource is contained in clauses 9.6.24 and 10.2.11 of oneM2M TS-0001 [6].

Table 7.4.24.1-1: Data type definition of <eventConfig>

Table 7.4.24.1-2: Universal/Common Attributes of <eventConfig> resource

Table 7.4.24.1-3: Resource Specific Attributes of <eventConfig> resource

Table 7.4.24.1-4: Child Resources of <eventConfig> resource

7.4.24.2	<eventConfig> resource-specific procedures for CRUD operations

7.4.24.2.1	Create

Originator:

This procedure follows the Generic Resource Request Procedure for Originator specified in clause 7.2.2.1, with the following <eventConfig> resource-specific updates.

Resource-specific operation before Orig-1.0 "Compose Request primitive":

If event-based statistics collection will be used, the Originator shall generate the representation of the <eventConfig> child resource instance to produce the desired trigger condition for the intended event. For example, one representation of <eventConfig> could have eventType set to DATA OPERATION and operationType set to Retrieve. In another example, a representation could have eventType set to TIMER-BASED, eventStart set to midnight tomorrow and eventEnd set to midnight of the day after tomorrow. See Table 7.4.24.1-3 for value restrictions and default settings pertaining to the attributes of <eventConfig>.

Receiver:

Primitive specific operation on Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed" with the following additional operations.

If the eventType attribute is STORAGEBASED and the dataSize attribute is not specified in the Create request then the Hosting CSE shall reject the request with a BAD_REQUEST Response Status Code.

If the Create request specifies both the eventResourceTypes attribute and the eventResourceIDs attribute then the Hosting CSE shall reject the request with a BAD_REQUEST Response Status Code.

If the value of the eventEnd attribute is less than the eventStart attribute then the Hosting CSE shall reject the request with a BAD_REQUEST Response Status Code.

No other change from the generic procedure in clause 7.2.2.2.

7.4.24.2.2	Retrieve

Originator:

No change from the generic procedure in clause 7.2.2.1.

Receiver:

No change from the generic procedure in clause 7.2.2.2.

7.4.24.2.3	Update

Originator:

No change from the generic procedure in clause 7.2.2.1.

Receiver:

Addition to the generic procedure in clause 7.2.2.2.

Recv-6.4: The following step is in addition to the procedures defined in clause 7.3.3.4

If the Update request would lead to both the eventResourceTypes attribute and the eventResourceIDs attributes being present in the resource, then the Hosting CSE shall reject the request with a BAD_REQUEST Response Status Code.

7.4.24.2.4	Delete

Originator:

No change from the generic procedure in clause 7.2.2.1.

Receiver:

No change from the generic procedure in clause 7.2.2.2.


### 7.4.25	Resource Type <statsCollect>


7.4.25.1	Introduction

The <statsCollect> resource controls the collection of statistics information on an IN-CSE. Information in an associated <eventConfig> resource shall be used by the IN-CSE or IN-AE to define specific event-related triggers. Additional description of the <statsCollect> resource is contained in clauses 9.6.25 and 10.2.11 of oneM2M TS-0001 [6].

Table 7.4.25.1-1: Data type definition of <statsCollect>

Table 7.4.25.1-2: Universal/Common Attributes of <statsCollect> resource

Table 7.4.25.1-3: Resource Specific Attributes of <statsCollect> resource

Table 7.4.25.1-4: Child Resources of <statsCollect> resource

7.4.25.2	<statsCollect> resource-specific procedures for CRUD operations

7.4.25.2.1	Create

Originator:

This procedure follows the Generic Resource Request Procedure for Originator specified in clause 7.2.2.1, with the following <statsCollect> resource-specific updates.

Resource-specific operation before Orig-1.0:

The Originator shall generate and populate a representation of the <statsCollect> resource to produce the desired collection scenario, with the exception of statsCollectID (which is populated by the IN-CSE). If statModel is set to EVENT-BASED then the Originator shall provide a value for eventID that corresponds to an eventID value stored in an <eventConfig> resource (which defines the event triggers to be used).
See Table 7.4.25.1-3 for value restrictions and default settings pertaining to the attributes of <statsCollect>.

Receiver:

This procedure follows the Generic Request Procedure for Receiver specified in clause 7.2.2.2, with the following <statsCollect> resource-specific updates.

Resource-specific operations before Recv-6.6 and after Recv-6.5:

The receiver IN-CSE shall generate and store a unique (within the Service Provider domain) value for statsCollectID.

If status is set to ACTIVE, the IN-CSE shall begin monitoring the conditions defined by the <statsCollect> resource and generating Service Statistics Collection Records as the conditions are met.

7.4.25.2.2	Retrieve

Originator:

This procedure follows the Generic Resource Request Procedure for Originator specified in clause 7.2.2.1.

Receiver:

This procedure follows the Generic Request Procedure for Receiver specified in clause 7.2.2.2.

7.4.25.2.3	Update

Originator:

This procedure follows the Generic Resource Request Procedure for Originator specified in clause 7.2.2.1.

Receiver:

This procedure follows the Generic Request Procedure for Receiver specified in clause 7.2.2.2, with the following <statsCollect> resource-specific updates.

Resource-specific operation before Recv-6.6 and after Recv-6.5:

If status is set to ACTIVE, the IN-CSE shall begin monitoring the conditions defined by the <statsCollect> resource and generating Service Statistics Collection Records as the conditions are met.

If status is set to INACTIVE, the IN-CSE shall stop monitoring the conditions defined by the <statsCollect> resource.

7.4.25.2.4	Delete

Originator:

This procedure follows the Generic Resource Request Procedure for Originator specified in clause 7.2.2.1.

Receiver:

This procedure follows the Generic Request Procedure for Receiver specified in clause 7.2.2.2.


### 7.4.26	Announced resource types


7.4.26.1	Introduction

Instances of certain resource types can be announced by the Hosting CSE to one or more remote CSEs to inform the remote CSEs of the existence of the original resource instance. Table 7.4.26.1-1 lists the resource types which are announceable together with its resource type identifier and the name of the XSD file that specifies its data type.

Resource-specific attributes of a resource type may be declared announceable (mandatory or optional) or not announceable. Clause 9.6 in oneM2M TS-0001 [6] defines which attributes of each resource type are announceable.

The universal/common attributes of an announced resource type are listed in Table 7.4.26.1-2, together with their request optionality in Create and Update requests (see clause 7.4.1). The announced resource includes a common attribute link which represents a link to the original resource hosted by the original resource-Hosting CSE.

The child resources applicable to each announced resource type are listed in Table 9.6.26.1-1 of oneM2M TS-0001 [6].

Table 7.4.26.1-1: Data type definition of announced Resource types

Table 7.4.26.1-2: Universal/Common Attributes of announcedResource

Each announced resource type has the resource specific attributes that is the subset of the original resource.

Table 7.4.26.1-3: Resource Specific Attributes of announcedResource

The procedures defined in the following clause 7.4.26.2 apply to all announced resources regardless of the resource type.

7.4.26.2	Resource specific procedures for CRUD operations

7.4.26.2.1	Introduction

This clause describes announced resource specific procedure for CRUD operations.

The original resource Hosting CSE shall create/update/delete the announced resource as specified at the clause 7.3.3.10 and clause 7.2.2.2.

7.4.26.2.2	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.26.2.3	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

In case of the Result Content information is set to the "original-resource", the Recv-6.5 shall be changed as follows:

Recv-6.5 "Read the original resource whose address is provided by the link attribute of the announced resource".

7.4.26.2.4	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2, except that Recv-6.3 is replaced as follows:

Recv-6.3 "Check if the value of the From parameter in Request message is identical to the CSE-ID included in the link attribute in the announced resource".

7.4.26.2.5	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2, except that Recv-6.3 is replaced as follows:

Recv-6.3 "Check if the value of the From parameter in Request message is identical to the CSE-ID included in the link attribute in the announced resource".


### 7.4.27	Resource Type <latest>


7.4.27.1	Introduction

The <latest> resource is a virtual resource because it does not have a representation. It is a child resource of the <container> and <timeSeries> resources. Whenever a request addresses the <latest> resource, the Hosting CSE shall apply the request to the latest <contentInstance> resource or the latest <timeSeriesInstance> resource among all existing <contentInstance> and <timeSeriesInstance> resources of the <container> resource or <timeSeries> resource.

7.4.27.2	<latest> Resource Specific Procedures for CRUD Operations

7.4.27.2.0	Introduction

This clause describes <latest> resource specific behaviour for operations. Only Retrieve and Delete operations shall be allowed for the <latest> resource.

7.4.27.2.1	Create

Originator:

The <latest> resource shall not be created via API.

Receiver:

Not applicable.

7.4.27.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

If the parent is a <container> resource and its locationID attribute is configured and the value of locationUpdatePeriod is marked '0' or not defined and locationSource attribute is 'Network Based', the following <latest> resource type specific procedures shall be performed after Recv-6.3 and before Recv-6.6 generic procedures.

The Hosting CSE shall transform the location-acquisition request into a Location Server request, using the attributes stored in <locationPolicy> resource. The Hosting CSE shall also provide default values for other required parameters (e.g. quality of position) in the Location Server request according to local policies.

The Hosting CSE shall send this Location Server request to the location server which could use either one of the two API interfaces: one is, OMA Mobile Location Protocol [i.4] and OMA RESTful NetAPI for Terminal Location [28]. The other one is 3GPP Monitoring Event API for terminal location [51]. The location server performs positioning procedure based upon the Location Server request.

The Hosting CSE shall receive the corresponding response and transform it into a Response primitive.

If the positioning procedure is failed and retrieveLastKnownLocation is false, the Hosting CSE returns the response with a Response Status Code based on the error code and shall store a statusCode based on the error code in the locationStatus attribute in the <locationPolicy> resource. If the positioning procedure failed and retrieveLastKnownLocation is true and if the Hosting CSE supports the 3GPP API, the Hosting CSE shall repeat step 1), once only, but requesting the last known location from the Location Server using 3GPP Monitoring Event API [51].

If the positioning procedure is successfully completed which means that the Hosting CSE acquires the location information, the Hosting CSE shall perform the procedures of creating a <contentInstance> as described in clause 7.4.7.2.1 according to the acquired location information and perform the normal Recv-6.5 procedure.

NOTE 1:	For information on how the Location Server request message is converted to the OMA RESTful NetAPI for Terminal Location message, see clause G.2.

NOTE 2:	For information on how the Location Server request message is converted to the 3GPP Monitoring Event API for terminal location message, see clause G.3.

Otherwise (i.e. if the parent is not a <container> resource or if the conditions for steps 1 and 2 above do not apply) follow the generic procedures in clause 7.2.2.2 with the following modifications:

Recv-6.2 Check the existence of the latest <contentInstance> resource or the latest <timeSeriesInstance> resource among all existing <contentInstance> or <timeSeriesInstance> resources in the parent <container> or <timeSeries> resource. If the resource exists, the subsequent procedures of the Receiver (i.e. after Recv-6.2) shall be performed for the resource. If the resource does not exist, the Hosting CSE shall reject the request with a Response Status Code indicating "NOT_FOUND" error.

Recv-6.3 Addition to the normal procedure of Recv-6.3 "Check authorization of the Originator": If the parent is a <container> resource and the value of its disableRetrieval attribute is true then the Hosting CSE shall reject the request with a Response Status Code indicating an "OPERATION_NOT_ALLOWED" error.

7.4.27.2.3	Update

Originator:

The <latest> resource shall not be updated via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the validity of received request primitive":

If the request is received, the Receiver CSE shall execute the following steps in order:

"Create an unsuccessful Response primitive" with the Response Status Code indicating an "OPERATION_NOT_ALLOWED" error.

"Send the Response primitive".

7.4.27.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 except the following modification:

Recv-6.2 Check the existence of the latest <contentInstance> resource or the latest <timeSeriesInstance> resource among all existing <contentInstance> or <timeSeriesInstance> resources in the parent <container> or <timeSeries> resource. If the resource exists, the subsequent procedures of the Receiver (i.e. after Recv-6.2) shall be performed for the resource. If the resource does not exist, the Hosting CSE shall reject the request with a Response Status Code indicating "NOT_FOUND" error.

Recv-6.3 Addition to the normal procedure of Recv-6.3 "Check authorization of the Originator": If the parent is a <container> resource and the value of its disableRetrieval attribute is true then the Hosting CSE shall reject the request with a Response Status Code indicating "OPERATION_NOT_ALLOWED" error.


### 7.4.28	Resource Type <oldest>


7.4.28.1	Introduction

The <oldest> resource is a virtual resource because it does not have a representation. It is a child resource of the <container> and <timeSeries> resources. Whenever a request addresses the <oldest> resource, the Hosting CSE shall apply the request to the oldest <contentInstance> resource or the oldest <timeSeriesInstance> resource among all existing <contentInstance> resources of the <container> resource or <timeSeries> resource.

7.4.28.2	<oldest> Resource Specific Procedures for CRUD Operations

7.4.28.2.0	Introduction

Only Retrieve and Delete operations shall be allowed for the <oldest> resource.

7.4.28.2.1	Create

Originator:

The <oldest> resource shall not be created via API.

Receiver:

Not applicable.

7.4.28.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 except the following modification:

Recv-6.2 Check the existence of the oldest <contentInstance> resource or the oldest <timeSeriesInstance> resource among all existing <contentInstance> or <timeSeriesInstance> resources in the parent <container> or <timeSeries> resource. If the resource exists, the subsequent procedures of the Receiver (i.e. after Recv-6.2) shall be performed for the resource. If the resource does not exist, the Hosting CSE shall reject the request with a Response Status Code indicating "NOT_FOUND" error.

Recv-6.3 Addition to the normal procedure of Recv-6.3 "Check authorization of the Originator": If the parent is a <container> resource and the value of its disableRetrieval attribute is true then the Hosting CSE shall reject the request with a Response Status Code indicating an "OPERATION_NOT_ALLOWED" error.

7.4.28.2.3	Update

Originator:

The <oldest> resource shall not be updated via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the validity of received request primitive":

If the request is received, the Receiver CSE shall execute the following steps in order:

"Create an unsuccessful Response primitive" with the Response Status Code indicating an "OPERATION_NOT_ALLOWED" error.

"Send the Response primitive".

7.4.28.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 except the following modification:

Recv-6.2 Check the existence of the oldest <contentInstance> resource or the oldest <timeSeriesInstance> resource among all existing <contentInstance> or <timeSeriesInstance> resources in the parent <container> or <timeSeries> resource. If the resource exists, the subsequent procedures of the Receiver (i.e. after Recv-6.2) shall be performed for the resource. If the resource does not exist, the Hosting CSE shall reject the request with a Response Status Code indicating "NOT_FOUND" error.

Recv-6.3 Addition to the normal procedure of Recv-6.3 "Check authorization of the Originator": If the parent is a <container> resource and the value of its disableRetrieval attribute is true then the Hosting CSE shall reject the request with a Response Status Code indicating an "OPERATION_NOT_ALLOWED" error.


### 7.4.29	Resource Type <serviceSubscribedAppRule>


7.4.29.1	Introduction

The <serviceSubscribedAppRule> resource represents a rule that defines allowed App-ID and AE-ID combinations that are acceptable for registering an AE on a Registrar CSE. The detailed description can be found in the clause 9.6.29 in oneM2M TS-0001 [6].

Table 7.4.29.1-1: Data type definition of <serviceSubscribedAppRule> resource

Table 7.4.29.1-2: Universal/Common Attributes of <serviceSubscribedAppRule> resource

Table 7.4.29.1-3: Resource Specific Attributes of <serviceSubscribedAppRule> resource

Table 7.4.29.1-4: Child resources of <serviceSubscribedAppRule> resource

7.4.29.2	<serviceSubscribedAppRule> resource specific procedures for CRUD operations

7.4.29.2.0	Introduction

This clause describes <serviceSubscribedAppRule> resource specific primitive behaviour for CRUD operations.

7.4.29.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Addition to the generic procedures in clause 7.2.2.2.

If allowedApp-IDs contains an identifier pattern starting with anything other than ‘*’, 'R' or 'N'  the request shall be rejected with a "BAD_REQUEST" Response Status Code.

7.4.29.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.29.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Addition to the generic procedures in clause 7.2.2.2.

If allowedApp-IDs contains an identifier pattern starting with anything other than ‘*’, 'R' or 'N' the request shall be rejected with a "BAD_REQUEST" Response Status Code.

7.4.29.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.30	Resource Type <notificationTargetMgmtPolicyRef>


7.4.30.1	Introduction

This is a child resource of a <subscription> resource. This resource represents reference(s) to the policy to be followed by the Hosting CSE to manage Notification Targets of a resource subscription.

The detailed description can be found in clause 9.6.31 in oneM2M TS-0001 Functional Architecture [6].

Table 7.4.30.1-1: Data type definition of <notificationTargetMgmtPolicyRef> resource

Table 7.4.30.1-2: Universal/Common Attributes of <notificationTargetMgmtPolicyRef> resource

Table 7.4.30.1-3: Resource Specific Attributes of <notificationTargetMgmtPolicyRef> resource

Table 7.4.30.1-4: Child resources of <notificationTargetMgmtPolicyRef> resource

7.4.30.2	<notificationTargetMgmtPolicyRef> resource specific procedures for CRUD operations

7.4.30.2.0	Introduction

This clause describes <notificationTargetMgmtPolicyRef> resource specific primitive behaviour for CRUD operations.

7.4.30.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2, but with one additional check to in Recv-6.4 "Check validity of resource representation":

The Hosting CSE shall check if any Notification Target in the notificationTargetURI in the request primitive already exists in other <notificationTargetMgmtPolicyRef> resources which are the children of the targeted <subscription> resource. If so, the Hosting CSE shall send a response with Response Status Code indicating a "CONFLICT" error.

7.4.30.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.30.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.30.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.31	Resource Type <notificationTargetPolicy>


7.4.31.1	Introduction

This is a child resource of the <CSEBase> resource. This resource represents a policy to be followed by the Hosting CSE to manage the Notification Targets of a resource subscription. Each policy has Notification Target deletion rules.

The detailed description can be found in clause 9.6.32 in oneM2M TS-0001 Functional Architecture [6].

Table 7.4.31.1-1: Data type definition of <notificationTargetPolicy> resource

Table 7.4.31.1-2: Universal/Common Attributes of <notificationTargetPolicy> resource

Table 7.4.31.1-3: Resource Specific Attributes of <notificationTargetPolicy> resource

Table 7.4.31.1-4: Child resources of <notificationTargetPolicy> resource

7.4.31.2	<notificationTargetPolicy> resource specific procedures for CRUD operations

7.4.31.2.0	Introduction

This clause describes <notificationTargetPolicy> resource specific primitive behaviour for CRUD operations.

7.4.31.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.31.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.31.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.31.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.32	Resource Type <policyDeletionRules>


7.4.32.1	Introduction

This is a child resource of a <notificationTargetPolicy> resource. This resource represents rules to be applied by the Hosting CSE during Notification Target policy execution. Multiple rules are combined with AND or OR logical operation.

The detailed description can be found in clause 9.6.33 in oneM2M TS-0001 Functional Architecture [6].

Table 7.4.32.1-1: Data type definition of <policyDeletionRules> resource

Table 7.4.32.1-2: Universal/Common Attributes of <policyDeletionRules> resource

Table 7.4.32.1-3: Resource Specific Attributes of <policyDeletionRules> resource

Table 7.4.32.1-4: Child resources of <policyDeletionRules> resource

7.4.32.2	<policyDeletionRules> resource specific procedures for CRUD operations

7.4.32.2.0	Introduction

This clause describes <policyDeletionRules> resource specific primitive behaviour for CRUD operations.

7.4.32.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2, but with one additional check in Recv-6.2 "Check existence of the addressed resource":

The Hosting CSE shall check if there are more than two existing <policyDeletionRules> resources as the children of the targeted <notificationTargetPolicy> resource. If so, the Hosting CSE shall send a response with Response Status Code indicating a "CONFLICT" error.

7.4.32.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.32.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.32.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.33	Resource Type <notificationTargetSelfReference>


7.4.33.1	Introduction

This is a child resource of a <subscription> resource. It is a virtual resource type so it has no resource representation nor XSD. Only the Delete operation is applicable to this resource.

7.4.33.2	<notificationTargetSelfReference> resource specific procedures for CRUD operations

7.4.33.2.0	Introduction

This clause describes <notificationTargetSelfReference> resource-specific primitive behaviour for CRUD operations.

7.4.33.2.1	Create

The <notificationTargetSelfReference> resource is not created via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order:

"Create an unsuccessful Response primitive" with the Response Status Code indicating an "OPERATION_NOT_ALLOWED" error.

"Send the Response primitive".

7.4.33.2.2	Retrieve

The <notificationTargetSelfReference> resource cannot be retrieved via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order:

a)	"Create an unsuccessful Response primitive" with the Response Status Code indicating an "OPERATION_NOT_ALLOWED" error.

b)	"Send the Response primitive".

7.4.33.2.3	Update

The <notificationTargetSelfReference> resource cannot be updated via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order:

a)	"Create an unsuccessful Response primitive" with the Response Status Code indicating an "OPERATION_NOT_ALLOWED" error.

b)	"Send the Response primitive".

7.4.33.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 except the Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed". The Hosting CSE shall perform the Delete operation procedure for this resource type as follows:

Check if the Originator is listed as one of the Notification Targets in the notificationTargetURI attribute of a <notificationTargetMgmtPolicyRef> resource which is the sibling resource of the targeted <notificationTargetSelfReference> resource. 
If there is a resource, then the Hosting CSE shall fetch the <notificationTargetPolicy> resource linked from notificationPolicyID attribute. 
If there is no such resource, then the Hosting CSE shall fetch the default <notificationTargetPolicy> resource among children of the <CSEBase> resource as follows:

The Hosting CSE shall find a <notificationTargetPolicy> resource which has the policyLabel attribute set as "Default" and the creator attribute set as the Originator ID.

If there is no such resource in step a), then the Hosting CSE shall find the <notificationTargetPolicy> resource which has the policyLabel attribute set as "Default".
Note that there is always the default <notificationTargetPolicy> resource created by the M2M Service Provider.

When there is one <policyDeletionRules> resource as a child of the fetched <notificationTargetPolicy> resource, the Hosting CSE evaluates the <policyDeletionRules> resource and perform action as specified in the action attribute.
When there are two <policyDeletionRules> resources as a children of the fetched <notificationTargetPolicy> resource, the Hosting CSE evaluates the two <policyDeletionRules> resources and perform logical operation(i.e. AND or OR) as specified in the rulesRelationship attribute for the two evaluation results. If the logical operation result is true, then the Hosting CSE shall perform the action as specified in the action attribute.
The action is performed as follows:

If the action is the "accept request", the Hosting CSE shall remove the Originator in the notificationURI attribute in the <subscription> resource.

If the action is the "reject request", the Hosting CSE shall send the response with Response Status Code indicating an "ORIGINATOR_HAS_NO_PRIVILEGE" error.

If the action is the "seek authorization from subscription originator before responding", the Hosting CSE shall send the Notify request with the information of the indication for Notification Target deletion, the Originator ID and the subscription reference from the Originator's request to the <subscription> resource creator (i.e. the creator attribute of the <subscription> resource). If the Hosting CSE gets the response from the creator with Notification Target removal allowance indication, then the Hosting CSE shall remove the Originator in the notificationURI attribute in the <subscription> resource.

If the action is the "inform the subscription originator without taking any action", the Hosting CSE shall send the Notify request with the information of the indication for Notification Target deletion, the Originator ID and the subscription reference from the Originator's request to the <subscription> resource creator (i.e. the creator attribute of the <subscription> resource) and send the response to the Originator with a Response Status Code indicating an "ORIGINATOR_HAS_NO_PRIVILEGE" error.


### 7.4.34	Resource Type <semanticDescriptor>


7.4.34.1	Introduction

The <semanticDescriptor> resource is used to store a semantic description pertaining to a resource and potentially sub-resources. Such a description shall be according to subject-predicate-object triples as defined in the RDF graph-based data model [34].

The detailed description can be found in clause 9.6.34 in oneM2M TS-0001 Functional Architecture [6].

Table 7.4.34.1-1: Data type definition of <semanticDescriptor> resource

Table 7.4.34.1-2: Universal/Common Attributes of <semanticDescriptor> resource

Table 7.4.34.1-3: Resource Specific Attributes of <semanticDescriptor> resource

Table 7.4.34.1-4: Child resources of <semanticDescriptor> resource

7.4.34.2	<semanticDescriptor> resource specific procedures for CRUD operations

7.4.34.2.0	Introduction

This clause describes <semanticDescriptor> resource specific primitive behaviour for CRUD operations.

7.4.34.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following exception:

Primitive specific operation on Recv-6.4 "Check validity of resource representation for the given resource type":

a)	The Hosting CSE shall check that the descriptor attribute conforms to the syntax defined by the descriptorRepresentation attribute.

b)	If the descriptor attribute does not conform, the Hosting CSE shall reject the request with a Response Status Code indicating a "BAD_REQUEST" error .

c)	The Hosting CSE shall reject the request with a Response Status Code indicating a "BAD_REQUEST" error if the descriptorRepresentation attribute is set to "IRI".

Primitive specific operation on Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed":

a)	The Hosting CSE shall set the validationEnable attribute of the <semanticDescriptor> resource based on the value provided in the request and its local policy. Note that the local policy may override the suggested value provided in the request from the originator to enforce or disable the following semantic validation procedures. There are different cases depending on how the local policy is configured (which is out of the scope of the present document) and whether/how the validationEnable attribute is provided in the request:

validationEnable attribute is not present if it was not provided in the request or if the local policy does not allow for the validationEnable attribute;

validationEnable attribute is set to true or false according to the local policy no matter how the value is provided in the request;

validationEnable attribute is set to true or false according to the value provided in the request.

b)	If the validationEnable attribute is set as true, the hosting CSE shall perform the semantic validation process in the following steps according to clause 7.10.2 in oneM2M TS-0034 [50]. Otherwise, skip the following steps.

c)	Check if the addressed <semanticDescriptor> resource is linked to other <semanticDescriptor> resources on a remote CSE by the relatedSemantics attribute or by triples with annotation property m2m:resourceDescriptorLink in descriptor attribute. This process shall consider the recursive links.

If yes, the Hosting CSE shall generate an Update request primitive with itself as the Originator and with the Content parameter set to the addressed <semanticDescriptor> resource representation, and send it to the <semanticValidation> virtual resource URI on the CSE which hosts the referenced ontology (following the ontologyRef attribute) of the addressed <semanticDescriptor> resource (see details in clause 7.4.48.2.3). After receiving the response primitive, i.e. the validation result, go to step k. If no response primitive was received due to time-out or other exceptional cases, the hosting CSE shall generate a Response Status Code indicating a "TARGET_NOT_REACHABLE" error.

If no, perform the following steps.

d)	Access the semantic triples from the descriptor attribute of the received <semanticDescriptor> resource.

e)	Access the ontology referenced in the ontologyRef attribute of the received <semanticDescriptor> resource.

If the ontology referenced by the ontologyRef attribute is an external ontology, not locally hosted by the Hosting CSE, the Hosting CSE shall retrieve it using the corresponding protocol and identifier information specified in the ontologyRef attribute.

If the referenced ontology cannot be retrieved within a reasonable time (as defined by a local policy), the Hosting CSE shall generate a Response Status Code indicating an "ONTOLOGY_NOT_AVAILABLE" error.

f)	Retrieve any local linked <semanticDescriptor> resources of the received <semanticDescriptor> resource following the URI(s) in the relatedSemantics attribute (if it exists) and the URI(s) in the triples with annotation property m2m:resourceDescriptorLink (if there are any).

Repeat this step recursively to Retrieve any further local linked <semanticDescriptor> resources.

If the local linked <semanticDescriptor> resources cannot be retrieved within a reasonable time (which is subject to a local policy), the Hosting CSE shall generate a Response Status Code indicating a "LINKED_SEMANTICS_NOT_AVAILABLE" error.

g)	Retrieve the semantic triples from the descriptor attribute of the local linked <semanticDescriptor> resource.

h)	Retrieve the referenced ontologies of the local linked <semanticDescriptor> resources following the URI(s) in ontologyRef attribute of the linked <semanticDescriptor> resources; If the referenced ontologies cannot be retrieved within a reasonable time (as defined by a local policy), the Hosting CSE shall generate a Response Status Code indicating an "ONTOLOGY_NOT_AVAILABLE" error.

i)	Combine all the semantic triples of the addressed and local linked <semanticDescriptor> resources as the set of semantic triples to be validated, and combine all the referenced ontologies as the set of ontologies to validate the semantic triples against.

j)	Check all the aspects of semantic validation according to clause 7.10.3 in oneM2M TS-0034 [50] based upon the semantic triples and referenced ontology. If any problem occurs, the Hosting CSE shall generate a Response Status Code indicating an "INVALID_SEMANTICS" error.

k)	After the semantic validation process, the Hosting CSE shall set the semanticValidated attribute of the addressed <semanticDescriptor> resource according to the validation result (i.e. set to true if the no error occurs until now, otherwise false).

l)	Based on its local policy, the Hosting CSE may also update the value of the semanticValidated attributes of the local linked <semanticDescriptor> resources according to the validation result.

7.4.34.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following exception:

The semanticOpExec attribute is never returned in the response.

7.4.34.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1 with the following exception:

The descriptor attribute can be updated using SPARQL as follows:

Primitive specific operation on Orig-1.0 "Compose Request primitive": The originator creates a request to update the semanticOpExec attribute. The value of this attribute is set to a SPARQL request that includes INSERT, DELETE, or DELETE/INSERT with conditional SPARQL statements as defined in the SPARQL query language [33].

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following exceptions:

Primitive specific operation on Recv-6.4 "Check validity of resource representation for the given resource type":

a)	If both semanticOpExec and descriptor attributes exist, the Receiver shall generate a Response Status Code indicating a "BAD_REQUEST" error.

b)	If semanticOpExec attribute exists in the Request check that the syntax of its content corresponds to a valid SPARQL query request [33]. If the content does not correspond to a valid SPARQL query request, the Receiver shall generate a Response Status Code indicating an "INVALID_SPARQL_QUERY" error.

c)	If the descriptor attribute exists in the Request, check that the syntax of its content conforms to the syntax defined by the descriptorRepresentation attribute. If the content does not conform, the Receiver shall reject the request with a Response Status Code indicating a "BAD_REQUEST" error.

d)	The Hosting CSE shall reject the request with a Response Status Code indicating a "BAD_REQUEST" error if the descriptorRepresentation attribute is set to "IRI".

Primitive specific operation on Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed" in addition:

a)	If semanticOpExec attribute exists in the Request, the Hosting CSE shall update the semantic triples in the descriptor attribute according to SPARQL update request in the semanticOpExec attribute. If the SPARQL update request cannot be executed, the Hosting CSE shall "create an unsuccessful Response primitive" with the Response Status Code indicating "SPARQL_UPDATE_ERROR", otherwise proceed to step Recv-6.6.

b)	The hosting CSE shall set the validationEnable attribute of the addressed <semanticDescriptor> resource based on the value provided in the request and its local policy. Note that the local policy may override the suggested value provided in the request from the originator to enforce or disable the following semantic validation procedures. There are different cases depending on how the local policy is configured (which is out of the scope of the present document) and whether/how the validationEnable attribute is provided in the request:

no change to the existing validationEnable attribute if it is not provided in the request;

validationEnable attribute is not present if the local policy does not allow for the validationEnable attribute;

validationEnable attribute is set to true or false according to the local policy no matter how the value is provided in the request;

validationEnable attribute is set to true or false according to the value provided in the request.

c)	The hosting CSE shall perform steps 2b-2l as specified in clause 7.4.34.2.1.

d)	If validationEnable attribute is changed from true to false, then the hosting CSE shall set the semanticValidated attribute of the addressed <semanticDescriptor> resource as false.

7.4.34.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.35	Resource Type <semanticFanOutPoint>


7.4.35.1	Introduction

The <semanticFanOutPoint> resource is a virtual resource because it does not have a representation; there are no common attributes, resource specific attributes or xsd. It is the child resource of a <group> resource. In the following descriptions, the general term semantic resource is used to refer to <semanticDescriptor> resources and any other future resources containing semantic information.

A <semanticFanOutPoint> can be addressed in one of two ways:

Using the URI retrieved from its parent <group> resource; or

Using a hierarchical URI formed by taking the hierarchical URI of the parent <group> and appending the string /sfop to that URI

Only Retrieve requests to the <semanticFanOutPoint> resource are valid, other operations are are rejected by the syntax check step at the Receiver. When a Retrieve request is received by the <semanticFanOutPoint> it triggers a semantic query operation if the Semantic Query Indicator parameter in the request primitive is set to true. Otherwise, it triggers a semantic resource discovery operation.

Semantic resource discovery is used to find resources in a CSE based on the semantic descriptions contained in the descriptor attribute of semantic resources. Since an overall semantic description (forming a graph [i.5]) may be distributed across a set of semantic resources, the semantic descriptions have to be retrieved (before or as needed) during the execution of the discovery request.

When using <semanticFanOutPoint>, the graph is distributed across the descriptors of the members of the parent <group> resource. The group-hosting CSE indicates support for and availability of semantic functionality by setting the semanticSupportIndicator attribute of the <group> resource to true.

Similarly, semantic queries enable the retrieval of both explicitly and implicitly derived information based on syntactic, semantic and structural information contained in data (such as RDF data). The query result is produced by executing the semantic query statement over a set of distributed semantic resources, which are the members of the parent <group> resource and they constitute the RDF data basis (forming a graph) for the query statement to be executed on.

Targeting the <semanticFanOutPoint> virtual resource results in creating and distributing retrieve operations to all the member resources. The results of the retrieve requests are used to form an aggregated semantic description containing the overall graph, on which the graph pattern matching is performed for supporting semantic query or semantic resource discovery operations.

7.4.35.2	<semanticFanOutPoint> resource specific procedures for CRUD operations

7.4.35.2.0	Introduction

This clause describes <semanticFanOutPoint> resource specific primitive behaviour for CRUD operations.

7.4.35.2.1	Create

Originator:

The <semanticFanOutPoint> resource shall not be created via API.

Receiver:

Not applicable.

7.4.35.2.2	Retrieve

Originator:

No primitive specific operations.

Receiver:

The Receiver shall follow the steps from Recv-1.0 to Recv-6.2 specified in clause 7.2.2.2 Generic Resource Request Procedure for Receiver, with the following primitive specific operations:

After Recv-1.0 "Check the validity of received request primitive":

Check that the syntax of the semanticsFilter corresponds to a valid SPARQL query request [33]. If the semanticsFilter does not correspond to a valid SPARQL query request, the Receiver shall generate a Response Status Code indicating an "INVALID_SPARQL_QUERY" error.

If the Semantic Query Indicator parameter included in the request message is set to true, the request shall be processed as a semantic query. Otherwise, the request shall be processed as a semantic resource discovery.

After Recv-6.2 "Check existence of the addressed resource":

Check that the semanticSupportIndicator of the parent <group> resource is set to true.

Check the authorization of the Originator using the membersAccessControlPolicyIDs of the parent group resource. In the case the membersAccessControlPolicyIDs is not provided, the accessControlPolicyIDs of the parent group resource shall be used.

Fan-out <semanticDescriptor> Retrieve Requests to each CSE hosting sub-groups or members as follows:

For each group member, the Hosting CSE shall perform the following steps:

The primitive parameters From and To shall be mapped to corresponding Retrieve Requests to be sent out to each member of the group. The primitive parameter From shall be used directly. The prefix of primitive parameter To i.e. <URI of group resource>/sfop shall be replaced by hierarchical URIs derived from the attribute memberIDs of the <group> resource.

The group-hosting CSE shall execute "Compose Request primitives" with the semanticsFilter filter condition set to false.

"Send the Request to the receiver CSE".

"Wait for Response primitive".

Once the Responses to the Retrieve Requests have been received, proceed to the following steps:

Aggregate the descriptors from the Retrieve Responses and deliver the content for SPARQL processing, along with the semanticsFilter content.

Wait for a SPARQL processing response.

Perform Recv-6.7 "Create a success response" where the Response shall include the SPARQL processing result. In case of semantic query, the Response shall include the semantic query result. In case of semantic resource discovery, the Response shall include a list of identified resource URIs.

Perform Recv-6.8 and the procedure is terminated.

7.4.35.2.3	Update

Originator:

The <semanticFanOutPoint> resource shall not support Update operations via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order:

"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

"Send the Response primitive".

7.4.35.2.4	Delete

Originator:

The <semanticFanOutPoint> resource shall not support Delete operations via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order:

"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

"Send the Response primitive".


### 7.4.36	Resource Type <dynamicAuthorizationConsultation>


7.4.36.1	Introduction

A <dynamicAuthorizationConsultation> resource shall be used by a CSE to perform consultation-based dynamic access control to resources as specified in the present document and in oneM2M TS-0003 [7].

The detailed description can be found in clause 9.6.43 in oneM2M TS-0001 Functional Architecture [6].

Table 7.4.36.1-1: Data type definition of <dynamicAuthorizationConsultation> resource

Table 7.4.36.1-2: Universal/Common Attributes of <dynamicAuthorizationConsultation > resource

Table 7.4.36.1-3: Resource Specific Attributes of <dynamicAuthorizationConsultation> resource

Table 7.4.36.1-4: Child resources of <dynamicAuthorizationConsultation> resource

7.4.36.2	<dynamicAuthorizationConsultation> resource specific procedures for CRUD operations

7.4.36.2.0	Introduction

This clause describes <dynamicAuthorizationConsultation> resource specific primitive behaviour for CRUD operations.

7.4.36.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.36.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.36.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.36.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.37	Resource Type <flexContainer>


7.4.37.1	Introduction

This resource represents a customizable container for data instances. It is a template for the definition of flexible specializations of data containers.

The detailed description can be found in clause 9.6.35 in oneM2M TS-0001 [6].

There are multiple specializations of <flexContainer> specified by oneM2M. Each of these specializations has its own schema file. There is no separate schema file just for <flexContainer>, however the XML schema types for the specializations all conform to the pattern described in this clause. The XSD of <flexContainer> specializations may use a targetNamespace other than the one identified by the m2m: prefix. Specializations of <flexContainer> which employ the namespace prefix m2m: are defined in Annex J. Specialization of <flexContainer> which employ the namespace prefix hd: for Home Domain use cases are specified in oneM2M TS-0023 [40].

The following resource types are allowed to include <flexContainer> specializations as children: <CSEBase>, <AE>, <remoteCSE> and <container>.

Table 7.4.37.1-1: Universal/Common Attributes of <flexContainer> resource

Table 7.4.37.1-2: Resource Specific Attributes of <flexContainer> resource

Table 7.4.37.1-3: Child Resources of <flexContainer> resource

7.4.37.2	<flexContainer> resource specific procedures for CRUD operations

7.4.37.2.0	Introduction

This clause describes <flexContainer> resource specific behaviour for CRUD operations.

7.4.37.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation on Recv-1.0 with the following additional operations.

The hosting CSE shall validate the received resource representation against the schema value present in the received resource containerDefinition attribute. If the schema is not available then the Hosting CSE shall return a response primitive with a Response Status Code indicating "SPECIALIZATION_SCHEMA_NOT_FOUND" error. If the received resource is not valid then the Hosting CSE shall return a response primitive with a Response Status Code indicating "BAD_REQUEST" error.

Primitive specific operation on Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed" with the following additional operations:

The Hosting CSE shall set the contentSize attribute to the sum of the size in bytes of all of the custom attributes.

No other changes from the generic procedures in clause 7.2.2.2.

7.4.37.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.37.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation on Recv-1.0 with the following additional operations.

The hosting CSE shall validate the received resource representation against the schema value present in the resource containerDefinition attribute. If the received resource is not valid then the Hosting CSE shall return a response primitive with a Response Status Code indicating "BAD_REQUEST" error.

Primitive specific operation on Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed" with the following additional operations:

The Hosting CSE shall update the contentSize attribute to the sum of the size in bytes of all of the custom attributes.

No other changes from the generic procedures in clause 7.2.2.2.

7.4.37.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.38	Resource Type <timeSeries>


7.4.38.1	Introduction

The resource represents a container for Time Series Data instances. It is used to share information with other entities and potentially to track, detect and report the missing data in Time Series. A <timeSeries> resource has no associated content, only attributes and child resources.

The detailed description can be found in clause 9.6.36 in oneM2M TS-0001 [6].

Table 7.4.38.1-1: Data type definition of <timeSeries> resource

Table 7.4.38.1-2: Universal/Common Attributes of <timeSeries> resource

Table 7.4.38.1-3: Resource Specific Attributes of <timeSeries> resource

Table 7.4.38.1-4: Child Resources of <timeSeries> resource

7.4.38.2	<timeSeries> resource specific procedures for CRUD operations

7.4.38.2.0	Introduction

This clause describes <timeSeries> resource specific behaviour for CRUD operations.

7.4.38.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operations on Recv-6.4 "Check validity of resource representation for the given resource type" in addition to the procedures defined in clause 7.3.3.4.

If the Originator provides a value for periodicInterval the Hosting CSE shall check that the periodicIntervalDelta has a value less than or equal to periodicInterval/2. If not, the Hosting CSE shall return a response primitive with a Response Status Code indicating “BAD_REQUEST”. If the Originator provides a value for periodicInterval and does not set the periodicIntervalDelta, the Hosting CSE shall set the periodicIntervalDelta according to local policy.

If missingDataDetect is set to true the Hosting CSE shall check that missingDataDetectTimer is set and that its value is greater than periodicIntervalDelta. If not, the Hosting CSE shall return a response primitive with a Response Status Code indicating “BAD_REQUEST”.

Primitive specific operation after Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed ". See clause 7.2.2.2.

In the case that the periodicInterval attribute is set and missingDataDetect is true, the Hosting CSE shall monitor the Time Series Data based on its periodicInterval. The monitoring shall start upon creation of the first <timeSeriesInstance>. The Hosting CSE shall consider an expected <timeSeriesInstance> to be missing when the amount of time equal to missingDataDetectTimer has passed after its expected dataGenerationTime as defined in TS-0001 [6] clause 10.2.4.29.

When the Hosting CSE detects a missing data point, the dataGenerationTime of the missing data point is inserted into the missingDataList attribute and the missingDataCurrentNr shall be increased by one. When the missingDataCurrentNr exceeds the missingDataMaxNr, the oldest dataGenerationTime shall be removed from missingDataList to enable the insertion of the new missing data point information and missingDataCurrentNr shall be set to the value of missingDataMaxNr.

7.4.38.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.38.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operations on Recv-6.4 "Check validity of resource representation for the given resource type" in addition to the procedures defined in clause 7.3.3.4.

Check if missingDataDetect is present in the received request. In the case that missingDataDetect is present:

The Hosting CSE shall return the response primitive with a Response Status Code indicating “BAD_REQUEST” if any of the following attributes are present in the UPDATE request: missingDataDetectTimer, missingDataMaxNr, periodicIntervalDelta, periodicInterval.

If missingDataDetect is true the Hosting CSE shall clear the values in missingDataList and missingDataCurrentNr and begin or restart the time series data monitoring process.

If missingDataDetect is false the Hosting CSE shall stop the time series data monitoring process and keep the current state of missingDataList and missingDataCurrentNr.

If the current value of missingDataDetect is true the Hosting CSE shall return the response primitive with a Response Status Code indicating “BAD_REQUEST” if any of the following attributes are present in the UPDATE request: missingDataDetectTimer, missingDataMaxNr, periodicIntervalDelta, periodicInterval.

If the Originator provides a value for periodicInterval the Hosting CSE shall check that the periodicIntervalDelta has a value less than or equal to periodicInterval/2. If not, the Hosting CSE shall return a response primitive with a Response Status Code indicating “BAD_REQUEST”. If the Originator provides a value for periodicInterval and does not set the periodicIntervalDelta, the Hosting CSE shall set the periodicIntervalDelta according to local policy.

If missingDataDetect is set to true The Hosting CSE shall check that the value of missingDataDetectTimer attribute is greater than periodicIntervalDelta and if not the Hosting CSE shall return a response primitive with a Response Status Code indicating “BAD_REQUEST”.

7.4.38.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

The following are changes to the receiver procedures described in clause 7.2.2.2.

Recv-6.5. The Hosting CSE shall terminate timers related to the missing data detection process, if applicable.


### 7.4.39	Resource Type <timeSeriesInstance>


7.4.39.1	Introduction

The <timeSeriesInstance> resource represents a data instance in the <timeSeries> resource.

The detailed description can be found in clause 9.6.37 in oneM2M TS-0001 [6].

Table 7.4.39.1-1: Data type definition of <timeSeriesInstance> resource

Table 7.4.39.1-2: Universal/Common Attributes of <timeSeriesInstance> resource

Table 7.4.39.1-3: Resource Specific Attributes of <timeSeriesInstance> resource

Table 7.4.39.1-4: Child resources of <timeSeriesInstance> resource

7.4.39.2	<timeSeriesInstance> resource specific procedures for CRUD operations

7.4.39.2.0	Introduction

This clause describes <timeSeriesInstance> resource specific behaviour for CRUD operations.

7.4.39.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1 with the following exception:

The Originator shall maintain an internal counter to generate sequenceNr which is increased by one. When the sequenceNr reaches to the maxNrOfInstances of the direct parent <timeSeries> resource, it shall be set to one.

Receiver:

Primitive specific operation on Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed":

Steps for Create procedure of <timeSeriesInstance> resource shall be same as that steps of <contentInstance> resource described in clause 7.4.7.2.1, except <container> resource in that procedure would correspond to <timeSeries> resource and <contentInstance> resource would correspond to <timeSeriesInstance> resource.

In addition, the Hosting CSE shall first check for the presence of any other <timeSeriesInstance> resources having a dataGenerationTime attribute that equals the one specified in the request and that has the same parent as the new resource being created. If such a resource exists, then the Hosting CSE shall reject the request with a Response Status Code indicating a "CONFLICT" error.

No other changes from the generic procedures in clause 7.2.2.2.

7.4.39.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.39.2.3	Update

Originator:

The <timeSeriesInstance> resource shall not be Updated via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order:

"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

"Send the Response primitive".

7.4.39.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation on Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed":

currentNrOfInstances and currentByteSize of direct parent <timeSeries> resource shall be updated.


### 7.4.40	Resource Type <role>


7.4.40.1	Introduction

The <role> resource represents a role that is assigned to an AE or CSE.

The detailed description can be found in clause 9.6.38 in oneM2M TS-0001 [6].

Table 7.4.40.1-1: Data type definition of <role> resource

Table 7.4.40.1-2: Universal/Common Attributes of <role> resource

Table 7.4.40.1-3: Resource Specific Attributes of <role> resource

Table 7.4.40.1-4: Child Resources of <role> resource

7.4.40.2	<role> resource specific procedures for CRUD operations

7.4.40.2.0	Introduction

This clause describes <role> resource specific behaviour for CRUD operations.

7.4.40.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.40.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.40.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.40.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.41	Resource Type <token>


7.4.41.1	Introduction

The <token> resource represents a token that is issued to an AE or CSE.

The detailed description can be found in clause 9.6.39 in oneM2M TS-0001 [6].

Table 7.4.41.1-1: Data type definition of <token> resource

Table 7.4.41.1-2: Universal/Common Attributes of <token> resource

Table 7.4.41.1-3: Resource Specific Attributes of <token> resource

Table 7.4.41.1-4: Child Resources of <token> resource

7.4.41.2	<token> resource specific procedures for CRUD operations

7.4.41.2.0	Introduction

This clause describes <token> resource specific behaviour for CRUD operations.

7.4.41.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.41.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.41.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.41.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.42	Void



### 7.4.43	Resource Type <authorizationDecision>


7.4.43.1	Introduction

The <authorizationDecision> resource represents an access control decision. The detailed description can be found in clause 9.6.41 in oneM2M TS-0001 [6].

Table 7.4.43.1-1: Data type definition of <authorizationDecision> resource

Table 7.4.43.1-2: Universal/Common Attributes of <authorizationDecision> resource

Table 7.4.43.1-3: Resource Specific Attributes of <authorizationDecision> resource

Table 7.4.43.1-4: Child Resources of <authorizationDecision> resource

7.4.43.2	<authorizationDecision> resource specific procedures for CRUD operations

7.4.43.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.43.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.43.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following exception:

The Hosting CSE shall check whether a PDP procedure is bound to the <authorizationDecision> resource. If it is, the Hosting CSE shall trigger the PDP procedure, otherwise no other changes from the generic procedures in clause 7.2.2.2.

The triggered PDP procedure shall perform as follows:

Check if the access control decision request satisfies the following conditions. If it does, continue with the remaining steps, otherwise stop this procedure and return an error Response Status Code of "BAD_REQUEST":

a)	Only to, from, operation, resourceType, filterUsage, roleIDs, tokenIDs, tokens, requestTime, originatorLocation, and/or originatorIP resource attributes may be in the update request.

b)	All the mandatory resource attributes (i.e. to, from and operation attributes) used for constructing an access control decision request are in the update request.

c)	The formats of the updated values are all correct.

Delete any existing resource specific attributes before performing the resource update operation, and then perform the resource update operation.

Construct an access control decision request with the updated resource attributes.

Obtain applicable access control policies and information according to the access control decision request. If it is not successful, the status attribute shall be set as follows:

a)	If the procedure cannot obtain applicable access control policies or required access control information without error, update the status attribute with "NOT_APPLICABLE" and go to step 6.

b)	If the procedure cannot obtain applicable access control policies or required access control information with error, update the status attribute with "INDETERMINATE" and go to step 6.

NOTE:	How to obtain the applicable access control policies or required access control information is out of scope of the present document.

Evaluate the access control decision request against access control policies as specified in oneM2M TS-0003 [7] and update the decision and status attributes with the evaluation result as follows:

a)	If some access control information required by the evaluation procedure is not provided by the request, update the status attribute with "MISSING_ATTRIBUTE" and go to step 6.

b)	If there are some errors in access control policies and/or tokens, update the status attribute with "SYNTAX_ERROR" and go to step 6.

c)	If an error occurs during the evaluation process, update the status attribute with "PROCESSING_ERROR" and go to step 6.

d)	If the access control policy evaluation is successful, update the decision attribute with the evaluation result (i.e. "PERMIT" or "DENY") and the status attribute with "OK" and go to step 6.

Generate an UPDATE response using the decision and status attributes and returning it back to the requester.

Delete all the resource specific attributes after the response has been sent in order to avoid an information leak.

7.4.43.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.44	Resource Type <authorizationPolicy>


7.4.44.1	Introduction

The <authorizationPolicy> resource represents a set of access control policies. The detailed description can be found in clause 9.6.42 in oneM2M TS-0001 [6].

Table 7.4.44.1-1: Data type definition of <authorizationPolicy> resource

Table 7.4.44.1-2: Universal/Common Attributes of <authorizationPolicy> resource

Table 7.4.44.1-3: Resource Specific Attributes of <authorizationPolicy> resource

Table 7.4.44.1-4: Child Resources of <authorizationPolicy> resource

7.4.44.2	<authorizationPolicy> resource specific procedures for CRUD operations

7.4.44.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.44.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.44.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following exception:

The Hosting CSE shall check whether a PRP procedure is bound to the <authorizationPolicy> resource. If it is, the Hosting CSE shall trigger the PRP procedure, otherwise no other changes from the generic procedures in clause 7.2.2.2.

The triggered PRP procedure shall perform as follows:

Check if the access control policy request satisfies the following conditions. If it does, continue with the remaining steps, otherwise stop this procedure and return an error Response Status Code of "BAD_REQUEST":

a)	Only the to resource attribute is in the update request.

b)	The format of the updated value is correct.

Delete any existing resource specific attributes before performing the resource update operation, and then perform the resource update operation.

Construct an access control policy request with the updated resource attributes.

Obtain applicable access control policies and policy combining algorithm according to the access control policy request and set the policies, combiningAlgorithm and status attributes as follows:

a)	If the procedure cannot obtain applicable access control policies without error, update the status attribute with "NOT_APPLICABLE" and go to step 5.

b)	If an error occurs during the access control policy retrieval process, update the status attribute with "PROCESSING_ERROR" and go to step 5.

c)	If the access control policy retrieval is successful, update the policies attribute with the retrieved access control policies, combiningAlgorithm attribute with the retrieved policy combining algorithm and status attribute with "OK" and go to step 5.

NOTE:	How to obtain the applicable access control policies and policy combining algorithm is out of scope of the present document.

Generate an UPDATE response using the policies, combiningAlgorithm and status attributes and return it to the requester.

Delete all the resource specific attributes after the response has been sent in order to avoid an information leak.

7.4.44.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.45	Resource Type <authorizationInformation>


7.4.45.1	Introduction

The <authorizationInformation> resource represents access control information. The detailed description can be found in clause 9.6.43 in oneM2M TS-0001 [6].

Table 7.4.45.1-1: Data type definition of <authorizationInformation> resource

Table 7.4.45.1-2: Universal/Common Attributes of <authorizationInformation> resource

Table 7.4.45.1-3: Resource Specific Attributes of <authorizationInformation> resource

Table 7.4.45.1-4: Child Resources of <authorizationInformation> resource

7.4.45.2	<authorizationInformation> resource specific procedures for CRUD operations

7.4.45.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.45.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.45.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following exception:

The Hosting CSE shall check whether a PIP procedure is bound to the <authorizationInformation> resource. If it is, the Hosting CSE shall trigger the PIP procedure, otherwise no other changes from the generic procedures in clause 7.2.2.2.

The triggered PIP procedure shall perform as follows:

Check if the access control information request satisfies the following conditions. If it does, continue with the remaining steps, otherwise stop this procedure and return an error Response Status Code of "BAD_REQUEST":

a)	Only from, roleIDs and/or tokenIDs resource attributes may be in the update request.

b)	All the mandatory resource attributes (i.e. from attribute) used for constructing an access control information request are in the update request.

c)	The format of the updated value is correct.

Delete any existing resource specific attributes and child resources before performing the resource update operation, and then perform the resource update operation.

Construct an access control information request with the updated resource attributes.

Obtain requested access control information according to the access control information request and create <role> and/or <token> child resources and update the status attribute as follows:

a)	If the procedure cannot obtain required access control information without error, update the status attribute with "NOT_APPLICABLE" and go to step 5.

b)	If an error occurs during the access control information retrieval process, update the status attribute with "PROCESSING_ERROR" and go to step 5.

c)	If the access control information retrieval is successful, create corresponding <role> and/or <token> child resources and update the status attribute with "OK" and go to step 5.

NOTE:	How to obtain the requested access control information is out of scope of the present document.

Generate an UPDATE response using the <role> and/or <token> resources and status attribute and return it to the requester.

Delete all the resource specific child resources and attributes after the response has been sent in order to avoid an information leak.

7.4.45.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.46	Resource Type <ontologyRepository>


7.4.46.1	Introduction

The <ontologyRepository> resource is a repository of ontologies used for reference and management of the associated <ontology> resources. It also provides semantic validation functionality as detailed in clause 6.7 in oneM2M TS-0034 Semantics Support [50].

The detailed description can be found in clause 9.6.50 in oneM2M TS-0001 Functional Architecture [6].

Table 7.4.46.1-1: Data type definition of <ontologyRepository> resource

Table 7.4.46.1-2: Universal/Common Attributes of <ontologyRepository> resource

There is no resource specific attributes of <ontologyRepository> resource.

Table 7.4.46.1-3: Child Resources of <ontologyRepository> resource

7.4.46.2	<ontologyRepository> resource specific procedures for CRUD operations

7.4.46.2.0	Introduction

This clause describes <ontologyRepository> resource specific primitive behaviour for CRUD operations.

7.4.46.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following exception:

Primitive specific operation on Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed":

a)	The Hosting CSE shall also create the <semanticValidation> virtual child resource if the <ontologyRepository> resource is created successfully.

7.4.46.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.46.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.46.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following exception:

Primitive specific operation on Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed":

a)	The Hosting CSE shall also delete the <semanticValidation> virtual child resource if the <ontologyRepository> resource is deleted successfully.


### 7.4.47	Resource Type <ontology>


7.4.47.1	Introduction

The <ontology> resource is used to store the representation of a specific ontology. This representation may contain ontology descriptions in a variety of formats.

The detailed description can be found in clause 9.6.51 in oneM2M TS-0001 Functional Architecture [6].

Table 7.4.47.1-1: Data type definition of <ontology> resource

Table 7.4.47.1-2: Universal/Common Attributes of <ontology> resource

Table 7.4.47.1-3: Resource Specific Attributes of <ontology> resource

Table 7.4.47.1-4: Child Resources of <ontology> resource

7.4.47.2	<ontology> resource specific procedures for CRUD operations

7.4.47.2.0	Introduction

This clause describes <ontology> resource specific primitive behaviour for CRUD operations.

7.4.47.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following exception:

Primitive specific operation on Recv-6.4 "Check validity of resource representation for the given resource type":

a)	The Hosting CSE shall check that the ontologyContent attribute conforms to the syntax defined by the ontologyFormat attribute.

b)	If the ontologyContent attribute does not conform, the Hosting CSE shall reject the request with a Response Status Code indicating a "BAD_REQUEST" error.

7.4.47.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.47.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1 with the following exception:

Primitive specific operation on Orig-1.0 "Compose Request primitive": The originator creates a request to update the semanticOpExec attribute. The value of this attribute is set to a SPARQL request that includes INSERT, DELETE, or DELETE/INSERT with conditional SPARQL statements as defined in the SPARQL query language [33].

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following exceptions:

Primitive specific operation on Recv-6.4 "Check validity of resource representation for the given resource type":

a)	If both semanticOpExec and ontologyContent attributes exist, the Receiver shall generate a Response Status Code indicating a "BAD_REQUEST" error.

b)	If the semanticOpExec attribute exists in the Request check that the syntax of its content corresponds to a valid SPARQL query request [33]. If the content does not correspond to a valid SPARQL query request, the Receiver shall reject the Request with a Response Status Code indicating an "INVALID_SPARQL_QUERY" error.

c)	If the ontologyContent attribute exists in the Request, check that the syntax of its content conforms to the syntax specified by the ontologyFormat attribute. If the content does not conform, the Receiver shall reject the Request with a Response Status Code indicating a "BAD_REQUEST" error.

Primitive specific operation on Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed" in addition:

a)	If the semanticOpExec attribute exists in the Request, the Hosting CSE shall update the semantic triples in the ontologyContent attribute according to the SPARQL update request in the semanticOpExec attribute. If the SPARQL update request cannot be executed, the Hosting CSE shall "create an unsuccessful Response primitive" with the Response Status Code indicating "SPARQL_UPDATE_ERROR", otherwise proceed to step Recv-6.6.

7.4.47.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.48	Resource Type <semanticValidation>


7.4.48.1	Introduction

The <semanticValidation> virtual resource is used as the interface for semantic validation of an input <semanticDescriptor> resource.

The detailed description can be found in clause 9.6.52 in oneM2M TS-0001 Functional Architecture [6].

There are no common attributes, resource specific attributes or xsd file to <semanticValidation> resource because it is a virtual resource.

7.4.48.2	<semanticValidation> resource specific procedures for CRUD operations

7.4.48.2.0	Introduction

This clause describes <semanticValidation> resource specific primitive behaviour for CRUD operations.

7.4.48.2.1	Create

Originator:

The <semanticValidation> resource shall not be created via API.

Receiver:

Not applicable.

7.4.48.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

"Send the Response primitive".

7.4.48.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1 with the following exception:

Primitive specific operation on Orig-1.0 "Compose Request primitive": The resource representation in the Content parameter of the request message shall be set as the <semanticDescriptor> resource to be validated.

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following exceptions:

Primitive specific operation on Recv-6.4 "Check validity of resource representation for the given resource type":

a)	Check if the Content parameter contains a valid resource representation conforming to the <semanticDescriptor> resource type. The Receiver shall perform the validity check as specified in clause 7.3.3.4.

b)	Check if the received <semanticDescriptor> resource contains the ontologyRef attribute with a valid URI value. If not, the Receiver shall generate a Response Status Code indicating a "CONTENTS_UNACCEPTABLE" error.

Skip Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed" and Recv-6.6 "Announce/De-announce the resource". Instead, the Hosting CSE shall perform the following procedures according to oneM2M TS-0034 [50] to perform semantic validation:

a)	Access the semantic triples from the descriptor attribute of the received <semanticDescriptor> resource.

b)	Access the ontology referenced in the ontologyRef attribute of the received <semanticDescriptor> resource.

If the ontology referenced by the ontologyRef attribute is an external ontology, not locally hosted by the Hosting CSE, the Hosting CSE shall retrieve it using the corresponding protocol and identifier information specified in the ontologyRef attribute.

If the referenced ontology cannot be retrieved within a reasonable time (as defined by a local policy), the Hosting CSE shall generate a Response Status Code indicating an "ONTOLOGY_NOT_AVAILABLE" error.

c)	Retrieve any linked <semanticDescriptor> resources of the received <semanticDescriptor> resource according to the procedures defined in clause 7.4.34.2.2 with the following details:

If the relatedSemantics attribute exists in the received <semanticDescriptor> resource, retrieve the linked <semanticDescriptor> resources following the URI(s) in the relatedSemantics attribute.

If the descriptor attribute of the received <semanticDescriptor> resource contains triples with annotation property m2m:resourceDescriptorLink, retrieve the linked <semanticDescriptor> resources following the URI(s) in those triples.

Repeat this step recursively to retrieve any further linked <semanticDescriptor> resources of the linked <semanticDescriptor> resources.

If the linked <semanticDescriptor> resources cannot be retrieved within a reasonable time (as defined by a local policy), the Hosting CSE shall generate a Response Status Code indicating a "LINKED_SEMANTICS_NOT_AVAILABLE" error.

d)	Retrieve the semantic triples from the descriptor attribute of the linked <semanticDescriptor> resource.

e)	Retrieve the referenced ontologies of any linked <semanticDescriptor> resources following the URI(s) in ontologyRef attribute of the linked <semanticDescriptor> resources using the procedure defined in step 2e of clause 7.4.34.2.1. If the referenced ontologies cannot be retrieved within a reasonable time (as defined by a local policy), the Hosting CSE shall generate a Response Status Code indicating an "ONTOLOGY_NOT_AVAILABLE" error.

f)	Combine all the semantic triples of the received and linked <semanticDescriptor> resources as the set of semantic triples to be validated, and combine all the referenced ontologies as the set of ontologies to validate the semantic triples against.

g)	Check all the aspects of semantic validation according to clause 7.10.3 in oneM2M TS-0034 [50] based upon the combined semantic triples and referenced ontologies. If any problem occurs, the Hosting CSE shall generate a Response Status Code indicating a "INVALID_SEMANTICS" error and update the received <semanticDescriptor> resource with the semanticValidated attribute set to 'false'.

Primitive specific operation on Recv-6.7 "Create a success response":

a)	The Hosting CSE shall update the received <semanticDescriptor> resource with the semanticValidated attribute set to 'true'.

As an optimization, the Hosting CSE may buffer the retrieved referenced ontologies and linked <semanticDescriptor> resources for the semantic process in future.

7.4.48.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

"Send the Response primitive".


### 7.4.49	Resource Type <semanticMashupJobProfile>


7.4.49.1	Introduction

The <semanticMashupJobProfile> resource is used to store a Semantic Mashup Job Profile (SMJP).

The detailed description can be found in clause 6.3 in oneM2M TS-0034: Semantics Support [50] and clause 9.6.53 in oneM2M TS-0001: Functional Architecture [6].

Table 7.4.49.1-1: Data type definition of <semanticMashupJobProfile> resource

Table 7.4.49.1-2: Universal/Common Attributes of <semanticMashupJobProfile> resource

Table 7.4.49.1-3: Resource Specific Attributes of <semanticMashupJobProfile> resource

Table 7.4.49.1-4: Child Resources of <semanticMashupJobProfile> resource

7.4.49.2	<semanticMashupJobProfile> resource specific procedures for CRUD operations

7.4.49.2.0	Introduction

This clause describes <semanticMashupJobProfile> resource specific primitive behaviour for CRUD operations.

7.4.49.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following exception:

Primitive specific operation on Recv-6.4 "Check validity of resource representation for the given resource type":

a)	The Hosting CSE shall check that the inputDescriptor, outputDescriptor and functionDescriptor attributes conform to the RDF/XML syntax as defined in RDF 1.1 XML Syntax [34]. If any of those attributes does not conform, the Hosting CSE shall generate a Response Status Code indicating a "BAD_REQUEST" error.

b)	The hosting CSE shall also check that the memberFilter attribute conforms to a valid SPARQL query request [33]. If not, the Receiver shall reject the Request with a Response Status Code indicating an "INVALID_SPARQL_QUERY" error.

7.4.49.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.49.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following exceptions:

Primitive specific operation on Recv-6.4 "Check validity of resource representation for the given resource type":

a)	If any of these attributes (inputDescriptor, outputDescriptor and functionDescriptor) is being updated, The Hosting CSE shall check that the new values of those attributes being updated conform to the RDF/XML syntax as defined in RDF 1.1 XML Syntax [34]. If any of the new values of those attributes does not conform, the Hosting CSE shall generate a Response Status Code indicating a "BAD_REQUEST" error.

b)	If the memberFilter attribute is being updated, the hosting CSE shall check that the new value of the memberFilter attribute conforms to a valid SPARQL query request [33]. If not, the Receiver shall reject the Request with a Response Status Code indicating an "INVALID_SPARQL_QUERY" error.

7.4.49.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following exceptions:

Primitive specific operation on Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed":

a)	The Hosting CSE shall set a NULL value into the smjpID attribute of each <semanticMashupInstance> resource that is referenced by this resource's smiID.


### 7.4.50	Resource Type <semanticMashupInstance>


7.4.50.1	Introduction

The <semanticMashupInstance> resource is used to represent a Semantic Mashup Instance (SMI) that is instantiated based on a specific SMJP. The detailed description can be found in clause 6.4 in oneM2M TS-0034: Semantics Support [50] and clause 9.6.54 in oneM2M TS-0001: Functional Architecture [6].

Table 7.4.50.1-1: Data type definition of <semanticMashupInstance> resource

Table 7.4.50.1-2: Universal/Common Attributes of <semanticMashupInstance> resource

Table 7.4.50.1-3: Resource Specific Attributes of <semanticMashupInstance> resource

Table 7.4.50.1-4: Child Resources of <semanticMashupInstance> resource

7.4.50.2	<semanticMashupInstance> resource specific procedures for CRUD operations

7.4.50.2.0	Introduction

This clause describes <semanticMashupInstance> resource specific primitive behaviour for CRUD operations.

7.4.50.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following exceptions:

Primitive specific operation on Recv-6.4 "Check validity of resource representation for the given resource type":

a)	The Hosting CSE shall check that the value of the smjpID attribute is not NULL and a valid SMJP can be retrieved by using the SMJP ID indicated in the smjpID attribute.

b)	The Hosting CSE shall check that the value of smjpInputParameter attribute conforms to the RDF/XML syntax as defined in RDF 1.1 XML Syntax [34] and that it meets the requirement described in the "inputDescriptor" attribute of the retrieved <semanticMashupJobProfile>.

c)	If any of the above checks fail, the Hosting CSE shall generate a Response Status Code indicating a "BAD_REQUEST" error.

d)	The Hosting CSE shall use the SPARQL query specified in the memberFilter attribute of the retrieved <semanticMashupJobProfile> to discover mashup member resources for the <semanticMashupInstance> to be created. The hosting CSE shall conduct semantic resource discovery on one or more CSEs by using the SPARQL query statement as the semantics filter to identify qualified mashup members.

e)	If not all of the required mashup members can be identified, the Hosting CSE shall generate a Response Status Code indicating a "MASHUP_MEMBER_NOT_FOUND" error.

f)	If all the mashup members are identified, the mashupMember attribute shall be updated. If the memberStoreType attribute has the value of "URI_ONLY", then the URIs of those member resources identified (during step d) will be stored in the mashupMember attribute. If the memberStoreType attribute has the value of "URI_AND_VALUE", then the URIs as well as the values of those member resources identified (during step d) will be stored in the mashupMember attribute.

Primitive specific operation on Recv-6.5 “Create/Update/Retrieve/Delete/Notify operation is performed”:

a)	If the resultGenType is set to WHEN_SMI_IS_CREATED the procedure for calculation of the semantic mashup result is performed and a new <semanticMashupResult> child resource is created.

b)	If the resultGenType is set to PERIODICALLY, a timer is started with the given period, at which time the procedure for calculation of the semantic mashup result is performed and a new <semanticMashupResult> child resource is created.

7.4.50.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.50.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2 with the following exceptions:

Primitive specific operation on Recv-6.4 "Check validity of resource representation for the given resource type":

a)	If the updated attribute in the Request message is smjpInputParameter, the Hosting CSE shall re-calculate the semantic mashup result. A <semanticMashupInstance> resource may have multiple <semanticMashupResult> child resources, which means that every time the Hosting CSE re-calculates the semantic mashup result, a new <semanticMashupResult> child resource shall be created to store the latest result.

b)	If the updated attribute in the Request message is memberStoreType, the Receiver shall change the way mashup member resources are represented by the mashupMember attribute.

c)	If the updated attribute in the Request message is resultGenType, the Receiver shall change the condition under which subsequent semantic mashup results are generated.

d)	If the updated attribute in the Request message is mashupMember and resultGenType is "WHEN_A_MASHUP_MEMBER_IS_UPDATED", the Hosting CSE shall first update the attributes and then re-calculate the semantic mashup result.

7.4.50.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.51	Resource Type <mashup>


7.4.51.1	Introduction

<mashup> is a virtual resource and is the child resource of a <semanticMashupInstance> resource. When a RETRIEVE operation is sent to the <mashup> resource, it triggers a calculation and generation of the mashup result based on its parent resource <semanticMashupInstance>. The detailed description can be found in clause 6.5 in oneM2M TS-0034: Semantics Support [50] and clause 9.6.55 in oneM2M TS-0001: Functional Architecture [6].

7.4.51.2	<mashup> resource specific procedures for CRUD operations

7.4.51.2.0	Introduction

Only Retrieve operation shall be allowed on a <mashup> virtual resource. A Create, an Update, or a Delete operation on a <mashup> virtual resource shall not be supported.

7.4.51.2.1	Create

Originator:

The <mashup> resource shall not be created via API.

Receiver:

Not applicable.

7.4.51.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

The Receiver shall follow the steps from Recv-1.0 to Recv-6.3 specified in clause 7.2.2.2 Generic Resource Request Procedure for Receiver, with the following primitive specific operations:

After Recv-6.3 "Check authorization of the Originator":

Check the mashupMember attribute of the parent <semanticMashupInstance> resource.

Collect latest data from each of the mashup members. If data cannot be collected from all of the mashup members, the Hosting CSE shall generate a Response Status Code indicating a "MASHUP_MEMBER_NOT_FOUND" error.

Retrieve the mashup function from the functionDescriptor attribute of the <semanticMashupJobProfile> resource that is specified by the smjpID attribute of the parent <semanticMashupInstance> resource.

Apply the mashup function with the data collected from the mashup members and produce a mashup result.

Create a <semanticMashupResult> child resource under the parent <semanticMashupInstance> resource, and use it to store the newly-generated mashup result.

Perform Recv-6.7 "Create a success response".

Perform Recv-6.8 and the procedure is terminated.

Note that, in case of the resultGenType attribute of the parent <semanticMashupInstance> resource is set to PERIODICALLY, steps 1) through 5) will be executed periodically by the Hosting CSE in order to generate the mashup result.

7.4.51.2.3	Update

Originator:

The <mashup> resource shall not support Update operations via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order:

"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

"Send the Response primitive".

7.4.51.2.4	Delete

Originator:

The <mashup> resource shall not support Delete operations via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

"Send the Response primitive".


### 7.4.52	Resource Type <semanticMashupResult>


7.4.52.1	Introduction

<semanticMashupResult> resource stores the mashup result. It is a child resource of a <semanticMashupInstance> resource. A <semanticMashupResult> child resource shall be generated by a Hosting CSE when it executes a semantic mashup operation on the parent <semanticMashupInstance> resource. The further detailed description can be found in clause 6.6 in oneM2M TS-0034: Semantics Support [50] and clause 9.6.56 in oneM2M TS-0001: Functional Architecture [6].

Table 7.4.52.1-1: Data type definition of <semanticMashupResult> resource

Table 7.4.52.1-2: Universal/Common Attributes of <semanticMashupResult> resource

Table 7.4.52.1-3: Resource Specific Attributes of <semanticMashupResult> resource

Table 7.4.52.1-4: Child Resources of <semanticMashupResult> resource

7.4.52.2	<semanticMashupResult> resource specific procedures for CRUD operations

7.4.52.2.0	Introduction

This clause describes <semanticMashupResult> resource specific primitive behaviour for CRUD operations.

A <semanticMashupResult> resource shall be created by a Hosting CSE itself (the CSE that hosts the parent <semanticMashupInstance> resource and that executes the semantic mashup operation producing the mashup result) to store a newly-generated mashup result. Entities other than the Hosting CSE shall only be allowed to perform Retrieve and Delete operations on a <semanticMashupResult> resource.

7.4.52.2.1	Create

Originator:

The <semanticMashupResult> resource shall not support Create operations via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order.

"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

"Send the Response primitive".

7.4.52.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.52.2.3	Update

Originator:

The <semanticMashupResult> resource shall not support Update operations via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order.

"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

"Send the Response primitive".

7.4.52.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.53	Resource Type <AEContactList>


7.4.53.1	Introduction

The <AEContactList> contains <AEContactListPerCSE> child resources, one for each CSE for which AE resource identifier information is being maintained. The <AEContactList> resource shall only be created as a child of <CSEBase> in the IN-CSE.

The detailed description can be found in clause 9.6.45 in oneM2M TS-0001 [6].

Table 7.4.53.1-1: Data type definition of <AEContactList> resource

Table 7.4.53.1-2: Universal/Common Attributes of <AEContactList> resource

Table 7.4.53.1-3: Resource Specific Attributes of <AEContactList> resource

Table 7.4.53.1-4: Child Resources of <AEContactList> resource

7.4.53.2	<AEContactList> resource specific procedures for CRUD operations

7.4.53.2.0	Introduction

This clause describes <AEContactList> resource specific primitive behaviour for CRUD operations.

7.4.53.2.1	Create

Originator:

The <AEContactList> resource shall not be created via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order:

a)	"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

b)	"Send the Response primitive".

7.4.53.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.53.2.3	Update

Originator:

The <AEContactList> resource shall not be updated via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order:

a)	"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

b)	"Send the Response primitive".

7.4.53.2.4	Delete

Originator:

The <AEContactList> resource shall not be deleted via API.

Receiver:

If the request is received, the Receiver CSE shall execute the following steps in order:

a)	"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

b)	"Send the Response primitive".


### 7.4.54	Resource Type <AEContactListPerCSE>


7.4.54.1	Introduction

The <AEContactListPerCSE> resource contains AE resource identifier information which is being maintained. The <AEContactListPerCSE> is a child of a <AEContactList> resource in the IN-CSE and has no child resources.

The detailed description can be found in clause 9.6.46 in oneM2M TS-0001 [6].

Table 7.4.54.1-1: Data type definition of <AEContactListPerCSE> resource

Table 7.4.54.1-2: Universal/Common Attributes of <AEContactListPerCSE> resource

Table 7.4.54.1-3: Resource Specific Attributes of <AEContactListPerCSE> resource

7.4.54.2	<AEContactListPerCSE> resource specific procedures for CRUD operations

7.4.54.2.0	Introduction

This clause describes <AEContactListPerCSE> resource specific primitive behaviour for CRUD operations.

7.4.54.2.1	Create

Originator:

The <AEContactListPerCSE> resource shall not be created via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order:

a)	"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

b)	"Send the Response primitive".

7.4.54.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.54.2.3	Update

Originator:

The <AEContactListPerCSE> resource shall not be updated via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order:

a)	"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

b)	"Send the Response primitive".

7.4.54.2.4	Delete

Originator:

The <AEContactListPerCSE> resource shall not be deleted via API.

Receiver:

Primitive specific operation on Recv-1.0 "Check the syntax of received message":

If the request is received, the Receiver CSE shall execute the following steps in order:

a)	"Create an unsuccessful Response primitive" with the Response Status Code indicating "OPERATION_NOT_ALLOWED" error.

b)	"Send the Response primitive".


### 7.4.55	Resource Type <localMulticastGroup>


7.4.55.1	Introduction

The <localMulticastGroup> resource is used by a member-hosting CSE to indicate that this CSE is a member of a multicast group. The <localMulticastGroup> is created as a child resource of the <CSEBase> resource. There may be multiple <localMulticastGroup> resources under the same <CSEBase>.

The detailed description can be found in clause 9.6.44 in oneM2M TS-0001: Functional Architecture [6].

Table 7.4.55.1-1: Data type definition of <localMulticastGroup> resource

Table 7.4.55.1-2: Universal/Common Attributes of <localMulticastGroup> resource

Table 7.4.55.1-3: Resource Specific Attributes of <localMulticastGroup> resource

7.4.55.2	<localMulticastGroup> resource specific procedures for CRUD operations

7.4.55.2.0	Introduction

This clause describes <localMulticastGroup> resource specific primitive behaviour for CRUD operations.

A <localMulticastGroup> resource shall be created by a group-hosting CSE.

7.4.55.2.1	Create

Originator:

Primitive specific operation on Orig-1.0 "Compose Request primitive":

The group-hosting CSE shall set the accessControlPolicyIDs attribute as an <accessControlPolicy> resource with the group-hosting CSE as the only entity that has CRUD privileges to the <localMulticastGroup>.

Primitive specific operation on Orig-6.0 "Process Response primitive":

If at least two members responded successfully, a Multicast Group Information data object shall be created and maintained by the group-hosting CSE. Details of Multicast Group Information are specified in clause 10.2.7.13 of oneM2M TS-0001 [6].

No change for the remaining steps from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation after Recv-1.0 "Check the syntax of received message" and before Recv-2.0 "Communication method?":

Comply with the multicast management protocol such as MLD or IGMP to join the multicast group corresponding to the multicastAddress in the request. If this procedure fails, the Receiver returns an error response with Response Status Code indicating "JOIN_MULTICAST_GROUP_FAILED".

No change for the remaining steps from the generic procedures in clause 7.2.2.1.

7.4.55.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.55.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.55.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Same as the generic procedures in clause 7.2.2.2 except addition of the following to step Recv-6.5:

The receiver shall comply with the multicast management protocol such as MLD or IGMP to leave the multicast group. If this procedure fails, the Receiver returns an error response with Response Status Code indicating "LEAVE_MULTICAST_GROUP_FAILED".


### 7.4.56	Resource Type <multimediaSession>


7.4.56.1	Introduction

The <multimediaSession> resource represents a multimedia session between two AEs. The resource contains the session information which is used by the AEs to manage (e.g. establish, tear-down) the session using non-oneM2M protocols.

Table 7.4.56.1-1: Data type definition of <multimediaSession> resource

Table 7.4.56.1-2: Universal/Common Attributes of <multimediaSession> resource

Table 7.4.56.1-3: Resource Specific Attributes of <multimediaSession> resource

Table 7.4.56.1-4: Child Resources of <multimediaSession> resource

7.4.56.2	<multimediaSession> resource specific procedures for CRUD operations

7.4.56.2.0	Introduction

This clause describes <multimediaSession> resource specific primitive behaviour for CRUD operations.

7.4.56.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation on Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed" with the following additional operations.

The hosting CSE shall check if the targeted <AE> resource has the sessionCapabilities attribute present, and if not the Hosting CSE shall return the response primitive with a Response Status Code indicating "TARGET_HAS_NO_SESSION_CAPABILITY" error.

No other changes from the generic procedures in clause 7.2.2.2.

7.4.56.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.56.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation on Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed" with the following additional operations.

The Hosting CSE shall check if the UPDATE is modifying the sessionState, offeredSessionDescriptions or acceptedSessionDescriptions attributes.

a)	If yes, the Hosting CSE shall check if the sessionState attribute is set to ONLINE. If ONLINE, and the UPDATE is not modifying sessionState to OFFLINE but the UPDATE is modifying offeredSessionDescriptions or acceptedSessionDescriptions then the Hosting CSE shall reject the request and return the response primitive with a Response Status Code indicating "SESSION_IS_ONLINE" error. Otherwise the Hosting CSE shall perform the UPDATE.

No other changes from the generic procedures in clause 7.2.2.2.

7.4.56.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.57	Resource Type <triggerRequest>


7.4.57.1	Introduction

The <triggerRequest> resource is used to initiate a device trigger request. This resource type shall only be instantiated on an IN-CSE.

The successful creation of a <triggerRequest> resource results in the IN-CSE initiating a trigger request to a targeted device (e.g. 3GPP UE). The trigger will be routed to an application on the targeted device. The device is identified by M2M-Ext-ID and the application on the device is identified by Trigger-Recipient-ID. A pending trigger request can be replaced with a new trigger request by updating the <triggerRequest> resource. A pending trigger request can be recalled by deleting the <triggerRequest> resource.

Table 7.4.57.1-1: Data type definition of <triggerRequest> resource

Table 7.4.57.1-2: Universal/Common Attributes of <triggerRequest> resource

Table 7.4.57.1-3: Resource Specific Attributes of <triggerRequest> resource

Table 7.4.57.1-4: Child Resources of <triggerRequest> resource

7.4.57.2	<triggerRequest> resource specific procedures for CRUD operations

7.4.57.2.0	Introduction

This clause describes <triggerRequest> resource specific primitive behaviour for CRUD operations.

7.4.57.2.1	Create

Originator:

The Originator shall use the steps Orig-1.0, Orig-2.0, and Orig-3.0 as described in clause 7.2.2.1.

Receiver:

The Receiver shall use the steps Recv-1.0 to Recv-10.0 as described in clause 7.2.2.2.

While processing the <triggerRequest> Create primitive, the Receiver shall detect the following types of errors and send a corresponding status code to the Originator.

If the Originator specifies a Trigger-Recipient-ID value in the Create primitive for a Registree AE or CSE, and the triggerEnable attribute of the Registree's <AE> or <remoteCSE> resource has a value of false, the Receiver shall generate a Response Status Code indicating "TRIGGERING_DISABLED_FOR_RECIPIENT".

While processing the <triggerRequest> Create primitive the Receiver shall determine which NSE to forward the trigger request to based on locally provisioned information or based on a DNS lookup of the M2M-Ext-ID attribute of the <triggerRequest>. If an NSE cannot be determined, the Receiver shall set the triggerStatus attribute to ERROR_NSE_NOT_FOUND. Otherwise, the Receiver shall continue to process the trigger request and set the triggerStatus attribute to PROCESSING.

To continue processing the request, the Receiver shall submit a trigger request to the NSE via the Mcn triggering procedure as defined in clause 9. The message shall contain information needed by the NSE to generate a trigger request for the corresponding underlying network. For a 3GPP trigger request, the required information within the trigger request message is captured in clause 7.5.1 of oneM2M TS-0026 [43].

Upon receipt of trigger response(s) from the NSE, the Receiver shall set the triggerStatus attribute of the <triggerRequest> resource:

If the Receiver receives a confirmation from the NSE that the trigger was accepted, the Receiver shall set the triggerStatus attribute to TRIGGER_TRIGGERED.

If the Receiver receives an indication that the trigger request was successfully delivered, the Receiver shall set the triggerStatus attribute to TRIGGER_DELIVERED.

If the Receiver receives an indication that the trigger request was not accepted or the delivery was not successful, the Receiver shall set the triggerStatus attribute to TRIGGER_FAILED.

If the Receiver receives an indication that the trigger request expired before completion the Receiver shall set the triggerStatus attribute to TRIGGER_EXPIRED.

If the Receiver receives an indication that the trigger request is terminated before completion the Receiver shall set the triggerStatus attribute to TRIGGER_TERMINATED.

If the Receiver receives an indication that the delivery of trigger request is not confirmed the Receiver shall set the triggerStatus attribute to TRIGGER_UNCONFIRMED.

7.4.57.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.57.2.3	Update

The following procedure replaces an outstanding trigger request that is still being processed by an underlying network with an updated trigger request.

Originator:

The Originator shall use the steps Orig-1.0, Orig-2.0, and Orig-3.0 as described in clause 7.2.2.1.

Receiver:

The Receiver shall use the steps Recv-1.0 to Recv-10.0 as described in clause 7.2.2.2.

The Originator shall provide the <triggerRequest> resource representation to the Receiver IN-CSE. While processing the <triggerRequest> Update primitive, the Receiver shall detect the following types of errors and send a corresponding status code to the Originator.

If the value of triggerStatus of the existing <triggerRequest> is PROCESSING, the Receiver shall continue to process the Update request. Otherwise, the Receiver shall generate a Response Status Code indicating "UNABLE_TO_REPLACE_REQUEST".

If the Originator specifies a Trigger-Recipient-ID value in the Update primitive for a Registree AE or CSE, and the triggerEnable attribute of the Registree's <AE> or <remoteCSE> resource has a value of false, the Receiver shall generate a Response Status Code indicating "TRIGGERING_DISABLED_FOR_RECIPIENT".

While processing the <triggerRequest> Update primitive, the Receiver shall forward the trigger replace request to the same NSE that the trigger request was forwarded to when the <triggerRequest> was created. If the NSE cannot be reached, the Receiver shall set the triggerStatus attribute to ERROR_NSE_NOT_FOUND.

To continue processing the request, the Receiver shall submit the trigger request to the NSE via the Mcn triggering procedure defined in clause 9. The message shall contain information needed by the NSE to replace the trigger request for the corresponding underlying network. For a 3GPP trigger replace request, the required information within the trigger request message is captured in clause 7.5.2 of oneM2M TS-0026 [43].

Upon receipt of a successful trigger replace response from the NSE, the Receiver shall set the triggerStatus attribute of the <triggerRequest> resource to TRIGGER_REPLACED and generate a Response Status Code indicating "UPDATED". Otherwise, the Receiver shall generate a Response Status Code indicating "UNABLE_TO_REPLACE_REQUEST".

7.4.57.2.4	Delete

Originator:

The Originator shall issue a request to the Receiver IN-CSE to delete the <triggerRequest> resource. The Originator shall use the steps Orig-1.0, Orig-2.0, and Orig-3.0 as described in clause 7.2.2.1.

Receiver:

The Receiver shall use the steps Recv-1.0 to Recv-10.0 as described in clause 7.2.2.2.

While processing the <triggerRequest> Delete primitive, the Receiver shall detect the following types of errors and send a corresponding status code to the Originator:

If the value of triggerStatus of the existing <triggerRequest> is PROCESSING, the Receiver shall continue to process the Delete request. Otherwise, the Receiver shall generate a Response Status Code indicating "UNABLE_TO_RECALL_REQUEST".

While processing the <triggerRequest> Delete primitive, the Receiver shall send a request to the same NSE that the trigger request was sent to when the <triggerRequest> was created. If the NSE cannot be reached, the Receiver shall set the triggerStatus attribute to ERROR_NSE_NOT_FOUND.

To continue processing the request, the Receiver shall submit the trigger recall request to the NSE via the Mcn triggering procedure defined in clause 9. The message shall contain information needed by the NSE to recall the trigger request for the corresponding underlying network. For a 3GPP trigger recall request, the required information within the trigger recall request message is captured in clause 7.5.2 of oneM2M TS-0026 [43].

Upon receipt of a successful trigger recall response from the NSE, the Receiver shall delete the <triggerRequest> resource and generate a Response Status Code indicating "DELETED". Otherwise, the Receiver shall not delete the <triggerRequest> resource and instead generate a Response Status Code indicating "UNABLE_TO_RECALL_REQUEST".


### 7.4.58	Resource Type <crossResourceSubscription>


7.4.58.1	Introduction

The <crossResourceSubscription> resource is used to support cross-resource subscription and cross-resource notification. A cross-resource subscription is made on multiple target resources. A cross-resource notification shall be generated if and only if expected events on all target resources occur within a designated time window. When notifications from all target resources occur within a specified time window the Hosting CSE shall issue a cross-resource notification.

The detailed description can be found in clause 9.6.58 in oneM2M TS-0001 [6].

Table 7.4.58.1-1: Data type definition of <crossResourceSubscription> resource

Table 7.4.58.1-2: Universal/Common Attributes of <crossResourceSubscription> resource

Table 7.4.58.1-3: Resource Specific Attributes of <crossResourceSubscription> resource

Table 7.4.58.1-4: Child Resources of <crossResourceSubscription> resource

7.4.58.2	<crossResourceSubscription> resource specific procedures for CRUD operations

7.4.58.2.0	Introduction

This clause describes <crossResourceSubscription> resource specific primitive behaviour for CRUD operations.

7.4.58.2.1	Create

Originator:

The following are changes to the Originator procedures described in clause 7.2.2.1:

Orig-1.0 When composing a request primitive, the Originator shall include regularResourcesAsTarget and/or subscriptionResourcesAsTarget attributes in the resource representation of the <crossResourceSubscription> in the content of the primitive. If regularResourcesAsTarget attribute is included, eventNotificationCriteriaSet attribute shall be included. If eventNotificationCriteriaSet contains only one eventNotificationCriteria, this eventNotificationCriteria shall be applied to all regular resources included in regularResourcesAsTarget attribute; otherwise, eventNotificationCriteriaSet shall contain the same number of eventNotificationCriteria elements as the number of regular target resources contained in regularResourcesAsTarget and each eventNotificationCriteria element shall be sequentially applied to corresponding target resource as listed in the regularResourcesAsTarget.

Receiver:

The following are changes to the receiver procedures described in clause 7.2.2.2:

Recv-6.5: The following steps are in addition to the generic Create procedures defined in clause 7.3.3.5:

The request shall be rejected with a "BAD_REQUEST" Response Status Code if at least one of regularResourcesAsTarget or subscriptionResourcesAsTarget attributes is not present in the request.

If subscriptionResourcesAsTarget is included, the Hosting CSE shall retrieve and update each <subscription> resource indicated in subscriptionResourcesAsTarget by issuing an UPDATE request to the <subscription> resource host as follows:

In the UPDATE request, the receiver shall use the From parameter from the current CREATE request.

The associatedCrossResourceSub attribute shall be updated by adding the resource identifier of the <crossResourceSubscription> resource being created.

The notificationURI attribute shall be updated by adding the resource identifier of the <crossResourceSubscription> resource being created. The Hosting CSE shall properly reply to a potential subscription verification request.

If any <subscription> for a target resource cannot be successfully updated or if the <crossResourceSubscription> CREATE Request timeout is exceeded, the receiver shall send an unsuccessful response with a "CROSS_RESOURCE_OPERATION_FAILURE" Response Status Code to the Originator; the Hosting CSE shall also remove itself from any already successfully associated <subscription> resources using the procedures in clause 7.4.8.2.4 and also delete any already-created <subscription> resources at other target resources

c)	If regularResourcesAsTarget is included, the Hosting CSE shall send a CREATE <subscription> request message to each target resource indicated by regularResourcesAsTarget.

i)	The request shall be rejected with a “BAD_REQUEST” Response Status Code if the eventNoficationCriteriaSet attribute is not present in the request. If present, the eventNotificationCriteriaSet attribute shall contain either one eventNotificationCriteria or the same number as the number of regular target resources contained in regularResourcesAsTarget attribute. Otherwise, the request shall be rejected with “BAD_REQUEST”.

ii)     In the new CREATE <subscription> request, the receiver shall use the From of the current CREATE request. For this new <subscription>:

1)	The eventNotificationCriteria attribute shall use the corresponding entry from the eventNotificationCriteriaSet attribute of the <crossResourceSubscription> that is being created. If the eventNotificationCriteriaSet attribute contains only one entry, the eventNotificationCriteria attribute shall use that entry.

2)	The notificationURI attribute shall be set to the resource identifier of the <crossResourceSubscription> that is being created. The Hosting CSE shall properly reply to a potential subscription verification request.

3)	The associatedCrossResourceSub attribute shall be set to the resource identifier of the <crossResourceSubscription> that is being created.

4)	The notificationEventCat attribute shall be set to the value of the notificationEventCat attribute of the <crossResourceSubscription> if present. Otherwise, it shall not be set.

5)	The expirationTime attribute shall be set to value of the expirationTime attribute of the <crossResourceSubscription> resource. This is the value that was included in the <crossResourceSubscription> CREATE request or, if a value was not included in that request, it is the value provided by the Hosting CSE for the <crossResourceSubscription> resource.

iii)	If any <subscription> for a target resource cannot be successfully created or if the <crossResourceSubscription> CREATE Request timeout is exceeded, the receiver shall send an unsuccessful response with a "CROSS_RESOURCE_OPERATION_FAILURE" Response Status Code to the Originator; the receiver shall also delete already-created <subscription> resources at other target resources that were created based on the presence of regularResourcesAsTarget.

iv)     Upon successful creation of each <subscription> resource, the resource identifier of the recently created <subscription> shall be added to the regularResourcesAsTargetSubscriptions attribute at the position of the corresponding entry in regularResourcesAsTarget.

d)	Once the <crossResourceSubscription> resource is created, the Hosting CSE shall start the time window if the timeWindowType=PERIODICWINDOW; if timeWindowType=SLIDINGWINDOW, the Hosting CSE shall start the time window after the first notification is received from a Target Resource Hosting CSE.

7.4.58.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.58.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

The following are changes to the receiver procedures described in clause 7.2.2.2.

Recv-6.5: The following steps are in addition to the generic Update procedures defined in clause 7.3.3.7:

If the timeWindowSize attribute is updated and/or the timeWindowType attribute is updated, the receiver shall restart the time window as described in clause 7.4.58.2.1.

7.4.58.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

The following are changes to the receiver procedures described in clause 7.2.2.2:

Recv-6.5: The following steps are in addition to the generic Delete procedures defined in clause 7.3.3.8:

The Hosting CSE shall stop the time window timer if running.

If this procedure was caused by a subscription deletion notification (see clause 7.5.1.2.4), then the following steps shall not be performed on the <subscription> indicated in the subscription deletion notification.

The Hosting CSE shall delete the previously-created <subscription> child resource of each target resource indicated in the regularResourcesAsTarget attribute. Target subscriptions are indicated in regularResourcesAsTargetSubscriptions attribute of the <crossResourceSubscription>. If this procedure is triggered by a DELETE operation, then the Receiver shall use the From of the current request for these requests. Otherwise, the Receiver shall use the creator of this <crossResourceSubscription> as its From parameter.

The Hosting CSE shall retrieve and update each <subscription> resource indicated in the subscriptionResourcesAsTarget attribute using the procedure in clause 7.4.8.2.3 to remove the resource identifier of this <crossResourceSubscription> from the <subscription> resource's associatedCrossResourceSub and notificationURI attributes. If this procedure is triggered by a DELETE operation, then the Receiver shall use the From of the current request for these requests. Otherwise, the Receiver shall use the creator of this <crossResourceSubscription> as its From parameter.

Any failures in steps c) or d) shall be ignored

The Hosting CSE shall send a Notify request for Cross Resource Subscription Deletion using the procedures in clause 7.5.1.2.20.


### 7.4.59	Resource Type <backgroundDataTransfer>


7.4.59.1	Introduction

The <backgroundDataTransfer> resource is used to request that the IN-CSE negotiates a background data transfer for a set of field nodes, with the Underlying Network. The resource attributes provide the characteristics of the background data transfer, optional guidance for transfer policy selection and the field nodes involved with the data transfer. Additional description of the <backgroundDataTransfer> resource is contained in clauses 9.6.60 and 10.2.20 of oneM2M TS-0001 [6]. The corresponding procedures over the Mcn reference point are described in oneM2M TS-0026 [43].

Table 7.4.59.1-1: Data type definition of <backgroundDataTransfer> resource

Table 7.4.59.1-2: Universal/Common Attributes of <backgroundDataTransfer> resource

Table 7.4.59.1-3: Resource Specific Attributes of <backgroundDataTransfer> resource

Table 7.4.59.1-4: Child Resources of <backgroundDataTransfer> resource

7.4.59.2	<backgroundDataTransfer> resource specific procedures for CRUD operations

7.4.59.2.0	Introduction

This clause describes <backgroundDataTransfer> resource specific primitive behaviour for CRUD operations.

7.4.59.2.1	Create

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.59.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.59.2.3	Update

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.59.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### 7.4.60	Resource Type <transactionMgmt>


7.4.60.1	Introduction

This resource is used to initiate and manage the atomic and consistent processing of a transaction consisting of multiple oneM2M request primitives. The detailed description can be found in clause 9.6.47 of oneM2M TS-0001 [6].

Table 7.4.60.1-1: Data type definition of <transactionMgmt> resource

Table 7.4.60.1-2: Universal/Common Attributes of <transactionMgmt> resource

Table 7.4.60.1-3: Resource Specific Attributes of <transactionMgmt> resource

Table 7.4.60.1-4: Child Resources of <transactionMgmt> resource

7.4.60.2	<transactionMgmt> resource specific procedures for CRUD operations

7.4.60.2.0	Introduction

This clause describes <transactionMgmt> resource specific primitive behaviour for CRUD operations.

7.4.60.2.1	Create

Originator:

The following are changes to the Originator procedures described in clause 7.2.2.1.

Orig-1.0 When composing a request primitive, the Originator shall include the requestPrimitives attribute in the resource representation of the <transactionMgmt> in the content of the primitive. Each request primitive in the requestPrimitives attribute shall be created using the procedures described in clause 7.2.2.1.

Receiver:

Same as the generic operations detailed in clause 7.2.2.2 with the following additions.

1)	Recv-6.4:

a)	The receiver shall set the transactionControl value to INITIAL.

b)	If any of the From parameters contained in the requestPrimitives attribute of the received <transactionMgmt> resource is not equal to the Originator of the received request primitive, the receiver shall generate a Response Status Code indicating "BAD_REQUEST".

NOTE:	Process the <transactionMgmt> resource as described in clause 10.2.18.1 of oneM2M TS-0001 [6] after Recv-6.7.

7.4.60.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.60.2.3	Update

Originator:

The following are changes to the Originator procedures described in clause 7.2.2.1:

1)	Orig-1.0 When composing a request primitive, if the originator changes the transactionControl value the originator shall use allowed values as specified in Table 10.2.18.1-1 of oneM2M TS-0001 [6].

Receiver:

Same as the generic operations detailed in clause 7.2.2.2 with the following additions:

1)	Recv-6.3:

If there is a transactionControl value in the update primitive and if the Originator does not match the creator of the <transactionMgmt> resource the receiver shall generate a Response Status Code indicating "ORIGINATOR_HAS_NO_PRIVILEGE".

2)	Recv-6.4:

If there is a transactionControl value in the update primitive:

i)	If transactionMode has the value "CSE_CONTROLLED" then the Receiver shall generate a Response Status Code indicating "BAD_REQUEST".

ii)	If the transactionState value indicates that the previous transition [as shown by the transactionControl value in the <transactionMgmt> resource] is not complete the Receiver shall generate a Response Status Code indicating "TRANSACTION_PROCESSING_IS_INCOMPLETE".

iii)	If the transactionControl value in the request primitive does not transition to values specified in Table 10.2.18.1-1 of oneM2M TS-0001 [6] the Receiver shall generate a Response Status Code indicating "ILLEGAL_TRANSACTION_STATE_TRANSITION_ATTEMPTED".

NOTE:	Process the <transactionMgmt> resource as described in clause 10.2.18.1 of oneM2M TS-0001 [6] after Recv-6.7.

7.4.60.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Same as the generic operations detailed in clause 7.2.2.2 with the following additions.

Recv-6.5:

The receiver shall check that the transactionState is either COMMITTED or ABORTED before deleting the <transactionMgmt> resource. To commit or abort the transaction the Receiver shall follow the procedure defined in clause 10.2.18.1 of oneM2M TS-0001 [6].

If the transactionState is neither COMMITTED nor ABORTED, the Receiver shall generate a Response Status Code indicating "TRANSACTION_PROCESSING_IS_INCOMPLETE".


### 7.4.61	Resource Type <transaction>


7.4.61.1	Introduction

This resource is used to initiate and manage the atomic and consistent processing of a single oneM2M request primitive of a oneM2M transaction.

The detailed description can be found in clause 9.6.48 in oneM2M TS-0001 [6].

A <transaction> create request may be originated by a CSE that hosts a <transactionMgmt> resource. Alternatively, a <transaction> resource may be used independent of a <transactionMgmt> resource when an AE creates individual <transaction> resources itself.

Table 7.4.61.1-1: Data type definition of <transaction> resource

Table 7.4.61.1-2: Universal/Common Attributes of <transaction> resource

Table 7.4.61.1-3: Resource Specific Attributes of <transaction> resource

Table 7.4.61.1-4: Child Resources of <transaction> resource

7.4.61.2	<transaction> resource specific procedures for CRUD operations

7.4.61.2.0	Introduction

This clause describes <transaction> resource specific primitive behaviour for CRUD operations.

7.4.61.2.1	Create

Originator:

No change from the generic procedures described in clause 7.2.2.1.

Receiver:

Same as the generic operations detailed in clause 7.2.2.2 with the following additions.

Recv-6.4: The following steps are in addition to the generic Create procedures defined in clause 7.3.3.5:

The receiver shall set the transactionControl value to LOCK.

If the From parameter contained in the m2m:requestPrimitive attribute of the received <transaction> resource is not equal to the Originator of the received request primitive, the receiver shall generate a Response Status Code indicating "BAD_REQUEST".

Recv-6.5: The following steps are in addition to the generic Create procedures defined in clause 7.3.3.5:

Process the <transaction> resource as described in clause 10.2.18.1 of oneM2M TS-0001 [6].

7.4.61.2.2	Retrieve

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

7.4.61.2.3	Update

Originator:

The following are changes to the Originator procedures described in clause 7.2.2.1.

Orig-1.0 When composing a request primitive, if the originator changes the transactionControl value the originator shall use allowed values as specified in Table 10.2.18.1-1 of oneM2M TS-0001 [6].

Receiver:

Same as the generic operations detailed in clause 7.2.2.2 with the following additions.

Recv-6.3:

If there is a transactionControl value in the update primitive and if the Originator does not match the creator of the <transaction> resource the receiver shall generate a Response Status Code indicating "ORIGINATOR_HAS_NO_PRIVILEGE".

Recv-6.4:

If the transactionControl value is in the update primitive:

If the transactionControl value does not transition to values specified in Table 10.2.18.1-1 of oneM2M TS-0001 [6] the Receiver shall generate a Response Status Code indicating "ILLEGAL_TRANSACTION_STATE_TRANSITION_ATTEMPTED".

If transactionState is not equal to the value of transactionControl being replaced by this Update operation the Receiver shall generate a Response Status Code indicating "TRANSACTION_PROCESSING_IS_INCOMPLETE".

Recv-6.5: The following steps are in addition to the generic Update procedures defined in clause 7.3.3.7:

Process the <transaction> resource as described in clause 10.2.18.1 of oneM2M TS-0001 [6].

7.4.61.2.4	Delete

Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Same as the generic operations detailed in clause 7.2.2.2 with the following additions.

1)	Recv-6.5:

The Receiver shall check that the transactionState is either COMMITTED or ABORTED before deleting the <transaction> resource. To commit or abort the transaction the Receiver shall follow the procedure defined in clause 10.2.18.1 of oneM2M TS-0001 [6].

If the transactionState is neither COMMITTED nor ABORTED, the Receiver shall generate a Response Status Code indicating "TRANSACTION_PROCESSING_IS_INCOMPLETE".


## 7.5	Primitive-specific procedures and definitions



### 7.5.1	Notification data object and procedures


7.5.1.1	Notification data object

Notification procedures represent a special case of the generic procedures defined in clause 7.2.2, where the Operation parameter of the request primitive is set to value "N" (Notify). In this case, the request primitive is referred to as Notify request primitive, and the associated response primitive is denoted as Notify response primitive.

A Notify request primitive shall convey a special notification data object in its Content parameter. This notification data object has no resource type representation in the oneM2M TS-0001 [6], since it does not represent a resource accessible by any M2M entities. The data type of the notification data object is defined in the tables below. The first column of Table 7.5.1.1-2 defines the permitted names the root element the notification data object can take with the data type listed in the third column.

Table 7.5.1.1-1: Data Type Definition of notification data object

Table 7.5.1.1-2: Data Types for notification data objects

When an Originator sends a Notify primitive to an AE Receiver, it shall use one of the serializations specified in that <AE>'s contentSerialization attribute. When an Originator sends a Notify primitive to a CSE, as the receiver or a transit CSE, it shall use one of the serializations specified in that <remoteCSE>'s contentSerialization attribute. If there is no contentSerialization value specified the Originator may use any serialization format.

7.5.1.2	Notification procedures

7.5.1.2.1	Introduction

Notification procedures shall be employed for the following use cases:

to notify Receiver(s) of modifications of a resource for an associated <subscription> resource;

to request Receiver(s) to perform resource subscription verification;

to notify deletion of the <subscription> resource;

to notify Receiver(s) for Asynchronous Non-blocking Request;

to notify Receiver(s) of modifications of a resource when the subscription relationship is established through the <group> resource;

to send the response corresponding to a request delivered via service layer long polling (clause 7.4.22.2.2 Retrieve <pollingChannelURI>);

to notify Receiver(s)(i.e. IPE) for on-demand discovery request;

to notify Receiver(s) of the missing Time Series Data points for an associated <subscription> resource;

to notify Receiver(s) of a security related request (e.g. dynamic authorization and end-to-end security);

to notify Receivers that an AE has changed registration point;

to notify an IN-CSE that the Originator has a new/updated/deleted reference to an Application Entity Resource identifier;

to notify Receiver(s) of a cross-resource notification generated by a <crossResourceSubscription> Hosting CSE;

to notify a Receiver that a triggered update on the subscribed-to resource has been blocked and retargeted to the Receiver.

The following clauses specify the notification procedures for each of the above use cases.

7.5.1.2.2	Notification for <subscription> resources

When the notification message is forwarded or aggregated by transit CSEs, the Originator or a transit CSE shall check whether there are notification policies to enforce between subscription resource Hosting CSE and the notification target. In that case, the transit CSE as well as the Originator shall process Notify request primitive(s) by using the corresponding policy and send processed Notify request primitive(s) to the next CSE with notification policies related to the enforcement so that the transit CSE is able to enforce the policy defined by the subscriber. The notification policies related to the enforcement at this time is verified by using the subscription reference in the Notify request primitive. In the notification policies, the latestNotify attribute is only enforced in the transit CSE as well as the Originator.

If Event Category parameter is set to "latest" in the notification request primitive, the transit CSE as well as Originator shall cache the most recent Notify request. That is, if a new Notify request is received by the CSE with a subscription reference that has already been buffered for a pending Notify request, the newer Notify request will replace the buffered older Notify request.

Originator:

When an event is generated, the Originator shall execute the following steps in order:

Step 1.0	Check the eventNotificationCriteria attribute of the <subscription> resource associated with the modified resource:

If the eventNotificationCriteria attribute is set, then the Originator shall check whether the corresponding event matches with the event criteria. If multiple matching conditions of different types (i.e. different condition tags) are present in the eventNotificationCriteria attribute, then the combined condition shall be derived by applying the logical operation specified by the filterOperation condition. By default the logical AND operation shall be used if the filterOperation condition is not present.

If notificationEventType is not set within the eventNotificationCriteria attribute and the operationMonitor is also not present, the Originator shall use the default setting of "Update_of_Resource" to compare against the event.

If the notificationEventType has the value "Create_of_Direct_Child_Resource" or "Delete of Direct Child Resource" and the childResourceType condition is also present, then the matching event shall only be detected if one of the child resource types present in the list has been created or deleted, respectively. If the childResourceType condition is not present then a matching event is generated whenever any child resource is created or deleted.

If the notificationEventType has either an explicit or default value of "Update_of_Resource" and the attribute condition is also present then the matching event shall only be detected if one of the attributes in the list has been updated. If the attribute condition is not present then a matching event is generated whenever any attribute has been updated.

If the event matches, go to the step 2.0. Otherwise, the Originator shall discard the corresponding event.

If the eventNotificationCriteria attribute is not configured, the Originator shall use the default setting of "Update_of_Resource" for the notificationEventType and then continue with the step 2.0.

Step 2.0	The Originator shall check the notification policy as described in the below steps, but the notification policy may be checked in different order. After checking the notification policy in step 2.0 (i.e. from step 2.1 to step 2.6), then continue with step 3.0.

Step 2.1	The Originator shall determine the type of the notification per the notificationContentType attribute. The possible values of for notificationContentType attribute are "Modified Attributes", "All Attributes", "ResourceID", "Trigger Payload" or “TimeSeries notification”. This attribute may be used jointly with the notificationEventType attribute in the eventNotificationCriteria to determine if it is the attributes/resourceID of the subscribed-to resource or the attributes/resourceID of the child resource of the subscribed-to resource that shall be returned in the notification:

If the value of notificationContentType is set to "Modified Attributes", the Notify request primitive shall include the partial resource containing modified attribute(s) only (Refer to clause 7.2.1.2 for response content description).

If the value of notificationContentType is set to "All Attributes", the Notify request primitive shall include the complete resource with all attributes (Refer to clause 7.2.1.2 for response content description).

If the value of notificationContentType is set to "ResourceID", the Notify request primitive shall include the URI of the resource (Refer to clause 7.2.1.2 for response content description).

If the value of notificationContentType is set to "Trigger Payload", the Notify request primitive shall include the trigger payload (Refer to clause 9.2.1 for trigger payload description).

If the value of notificationContentType is set to "TimeSeries notification", the Notify request primitive shall include a timeSeriesNotification (Refer to clause 6.3.5.69 for timeSeriesNotification description).

Step 2.2	Check the notificationEventCat attribute:

If the notificationEventCat attribute is set, the Notify request primitive shall employ the Event Category parameter as given in the notificationEventCat attribute. Then continue with the step 2.3.

If the notificationEventCat attribute is not configured, then continue with step 2.3.

Step 2.3	Check the latestNotify attribute:

If the latestNotify attribute is set, the Originator shall assign Event Category parameter of value "latest" of the notifications generated pertaining to the subscription created.

Step 2.4	Check the batching notifications policy and the rateLimit attribute:

See details in oneM2M TS-0001 [6], clause 10.2.10.7.

NOTE:	The use of some attributes such as preSubscriptionNotify is not supported in the present document.

Step 2.5	Check the notificationURI attribute:

The Originator shall fetch the notificationURI attribute and set the value to the To parameter of the Notify request. When the notificationURI attribute contains more than one target, the Originator shall generate each Notify request per target.

If the notificationURI attribute includes the notification serialization indication, in form of key-value pair, e.g. "ct=json", after the delimiter "?", the Originator shall serialize the notification for the notification target in that serialization type. The delimiter with the serialization indication shall be removed when the target is set to the To parameter of the Notify request. Then continue with step 3.0.

Step 3.0	The Originator shall check the notification and reachability schedules, but the notification schedules may be checked in different order:

If the <subscription> resource associated with the modified resource includes a <notificationSchedule> child resource, the Originator shall check the time periods given in the scheduleElement attribute of the <notificationSchedule> child resource.

Also, the Originator shall check the reachability schedule associated with the Receiver by exploring its <schedule> resource. If reachability schedules are not present in a Node then that Entity is considered to be always reachable.

If notificationSchedule and reachability schedule indicate that message transmission is allowed, then proceed with step 5.0. Otherwise, proceed with step 4.0.

In particular, if the notificationEventCat attribute is set to 'immediate' and the <notificationSchedule> resource does not allow transmission, then go to step 5.0 and send the corresponding Notify request primitive by temporarily ignoring the Originator's notification schedule.

Step 4.0	Check the pendingNotification attribute:

If the pendingNotification attribute is set, then the Originator shall cache pending Notify request primitives according to the pendingNotification attribute. The possible values are 'sendLatest' and 'sendAllPending'. If the value of pendingNotification is set to 'sendLatest', the most recent Notify request primitive shall be cached by the Originator and it shall set the Event Category parameter to "latest". If pendingNotification is set to 'sendAllPending', all Notify request primitives shall be cached by the Originator. If the pendingNotification attribute is not configured, the Originator shall discard the corresponding Notify request primitive. Any cached Notify request primitives are sent to the Receiver once message transmission becomes possible (see the step 6.0).

Step 5.0	Check the expirationCounter attribute:

If the expirationCounter attribute is set, then it shall be decreased by one when the Originator successfully sends the Notify request primitive. If the counter equals to zero('0'), the corresponding <subscription> resource shall be deleted. Then end the 'Compose Notify Request Primitive' procedure.

If the expirationCounter attribute is not configured, then end the 'Compose Notify Request Primitive' procedure.

When message transmission becomes possible, the Originator shall execute the following steps in order:

Step 6.0	If the pendingNotification attribute is set, the Originator shall send any cached Notify request primitives and then continue with the step 7.0

Step 7.0	Check the expirationCounter attribute:

If the expirationCounter attribute is set, then its value shall be decreased by one when the Originator successfully sends the Notify request primitive. If the counter meets zero, the corresponding <subscription> resource shall be deleted. Then end the 'Compose Notify Request Primitive' procedure.

If the expirationCounter attribute is not configured, then end the 'Compose Notify Request Primitive' procedure.

Receiver:

When the Hosting CSE receives a Notify request primitive, the Hosting CSE shall check validity of the primitive parameters. In case the Receiver is a transit CSE which forwards or aggregates Notify request primitives before sending to the subscriber or other transit CSEs, upon receiving the Notify request primitive with the Event Category parameter set to "latest", the Receiver shall identify the latest Notify request primitive with the same subscription reference while storing Notify request primitives locally. When the Receiver as a transit CSE needs to send pending Notify request primitives, it shall send the latest Notify request primitive. When the Receiver as a transit CSE needs to send Notify request primitives, it shall use one of the serializations specified in the subscriber or other transit CSE contentSerialization attribute. If there is no contentSerialization value specified the transit CSE may use any serialization format.

7.5.1.2.3	Subscription Verification during Subscription Creation

Originator:

When the Originator is triggered to perform subscription verification (clause 7.4.8.2.1) during <subscription> creation procedure, it performs the following steps in order:

Set the verificationRequest element of the notification data object as true in the Notify request primitive.

Set the creator element of the notification data object as the Originator ID of the <subscription> creation in the primitive.

Set the To parameter as the notificationURI in the primitive. If the notificationURI contains more than one value, then set the other value to the duplicated primitives from step 2).

Send the Notify request primitive(s).

Receiver:

When the Hosting CSE receives a Notify request primitive which includes verificationRequest element of the notification data object set as true, the Hosting CSE shall check if the creator and the Originator have NOTIFY privilege to the notificationURI.

If it fails, the Hosting CSE shall return a Response Status Code indicating "SUBSCRIPTION_CREATOR_HAS_NO_PRIVILEGE" or "SUBSCRIPTION_HOST_HAS_NO_PRIVILEGE" error, respectively, with the Notify response primitive. Otherwise, it shall return successful response primitive.

7.5.1.2.4	Notification of Subscription Deletion

Originator:

When a <subscription> resource is deleted the Originator shall send Notify request primitives to the <subscription> resource's subscriberURI and associatedCrossResourceSub if they are configured:

a)	The subscriptionDeletion element of the notification data object set as true.

b)	The subscriptionReference element of the notification data object set as the resource identifier of the <subscription> resource.

c)	The To parameter shall be set to the entity indicated in subscriberURI or associatedCrossResourceSub.

When a <subscription> is not itself deleted but a target is removed from its associatedCrossResourceSub attribute, the Originator shall send a Notify request primitive to that target as follows:

a)	The subscriptionDeletion element of the notification data object set as true.

b)	The subscriptionReference element of the notification data object set as the resource identifier of the <subscription> resource.

c)	The To parameter shall be set to the target removed from associatedCrossResourceSub.

Receiver:

When a Hosting CSE receives a subscription deletion notification targeted to an existing <crossResourceSubscription> resource then the <crossResourceSubscription> resource is deleted using the procedure defined in clause 7.4.58.2.4 except when the crossResourceSubscription resource delete procedure is already in process (so as to avoid an endless loop).

7.5.1.2.5	Notification for Asynchronous Non-blocking Request

Originator:

When the requested operation for a nonBlockingRequestAsynch request is completed, the Originator (=Hosting CSE of the resource) shall send a Notify request primitive to inform the final result of requested operation against the oneM2M resource. When the notificationURI was present and empty in the Response Type parameter in the previously received nonBlockingRequestAsynch request, no notification with the result of the requested operation shall be sent at all by the Originator. Otherwise, the Originator shall send a Notify request primitive as follows: (If the notificationURI was present and contains multiple entries, then the Originator shall send a Notify request primitive for each entry in the notificationURI list.)

a)	The From parameter shall be set to the ID of the Originator (i.e. Hosting CSE which hosts the resource targeted by the previously received nonBlockingRequestAsynch request).

b)	If the notificationURI was not present in the Response Type parameter in the previously received nonBlockingRequestAsynch request, then the To parameter shall be set to the Originator of the previously received nonBlockingRequestAsynch request.
If the notificationURI was present and not empty in the Response Type parameter in the previously received nonBlockingRequestAsynch request, then the To parameter shall be set to the next notificationURI list entry.

c)	The Response Type: If the Originator chooses to send the Notification in nonBlockingRequestAsynch mode, the Originator shall include a notificationURI in the Response Type and set it to empty.

d)	The Content parameter shall be set to the response to the previously received nonBlockingRequestAsynch request as m2m:responsePrimitive.

Receiver:

No change from the generic procedure in clause 7.2.2.2.

7.5.1.2.6	Notification for subscription via group

Whenever the subscription relationship is established through a <group> resource and either:

modification of a subscribed-to resource triggers a notification procedure as defined in clause 7.5.1.2.2, or

the subscribed-to sub-<group> triggers a aggregated notification procedure as defined in clause 7.5.1.2.6, the following procedures shall be performed.

The member-hosting CSE shall perform the steps defined in clause 7.5.1.2.2.

The group-hosting CSE shall perform the following steps in order:

Validate if the notification or the aggregated notification has been sent from one of its own member resources when it gets a notification at the notificationURI. The group-hosting CSE shall return a response primitive with the Response Status Code indicating "ORIGINATOR_HAS_NO_PRIVILEGE" error if the validation fails.

Upon successful validation, the group-hosting CSE shall collect notification requests targeted at the same subscriber according to the notificationForwardingURI element of each notification data object. The group-hosting CSE shall aggregate the notification requests into an aggregatedNotification element of the notification data object. If the group-hosting CSE receives an aggregated notification from a group member then it shall extract the notifications contained in that aggregated notification and insert them into the aggregatedNotification element (aggregatedNotification(s) are not nested). If the duration is not specified, then the Hosting CSE shall batch notifications using the default duration value as given by the M2M Service Provider. When the group-hosting CSE gets first notification, it starts new aggregation by the number of notifications and/or the duration in notifyAggregation attribute.

When the number or duration time is reached, send the aggregated notification to the notificationURI according to the notificationForwardingURI element in the notification data object. Then the group-hosting CSE waits for next notification to start aggregation. In case the group-hosting CSE is member of another group-hosting CSE through which the subscription is created, the notification request shall be sent according to the mapping of the notificationURI of the two group-hosting CSEs. When aggregating the notification requests, the group-hosting CSE may utilize the Request Expiration Timestamp parameter of the notification request primitive to determine the time by which the aggregated notifications need to be sent.

"Wait for Response primitive" procedure.

Upon receiving the response, the group-hosting CSE shall send the response separately to each individual member hosting CSEs to respond their corresponding notify request.

The group-hosting CSE shall perform notification aggregation while the <group> resource has not expired and has a notificationForwardingURI attribute value.

The Subscriber shall perform the following steps in order:

Extract each notification from the aggregated notification.

Treat the notification as if it is sent from the original subscribed-to resource.

"Create a success response" procedure.

"Send the Response primitive" procedure.

7.5.1.2.7	Notification for service layer long polling

When an AE or CSE receives a long polling response (clause 7.4.22.2.2 Retrieve <pollingChannelURI>) containing a request primitive, then the AE or CSE shall generate an appropriate response for the request in the long polling response. The AE or CSE, as the Originator, shall send the response in a Notify request to the <pollingChannelURI> Hosting CSE.

The Originator shall compose a Notify Request primitive according to clause 7.3.1.1 with following additional parameter settings:

The To parameter shall be set to the address of the <pollingChannelURI> that belongs to the Originator.

The Content parameter shall be set to the response to the previously received request as a m2m:responsePrimitive.

The Operation parameter shall be set to NOTIFY.

7.5.1.2.8	Notification for on-demand discovery request

In this procedure, the Originator is the Hosting CSE which performs resource discovery and the Receiver is the IPE.

Originator:

The Hosting CSE shall include the Originator ID of the original discovery request and the Filter Criteria in the Notify request. The To parameter of this request shall be set to the pointOfAccess of the <AE> resource of the IPE.

Receiver:

When the IPE receives the Notify request, it shall check the Originator ID and determines whether it performs external discovery. If the IPE does not accept the discovery, it shall send the unsuccessful response with the Response Status Code indicating "DISCOVERY_DENIED_BY_IPE". If the IPE accepts the discovery, it performs external discovery. If the discovery result contains one or more match, the IPE shall create resource(s) for the result and send the Notify response including the list of created resource(s) in the Content parameter. The IPE may configure "Discover" privilege for the original discovery request Originator for the newly created resource(s).

7.5.1.2.9	Notification for missing Time Series Data

When an AE wants to be informed of the number of missing data points in a given renewable time duration, the AE shall request the creation of a <subscription> resource and set the missingData in the eventNotificationCriteria conditions to specify the reporting policy. The notificationEventType element in the eventNotificationCriteria shall have a value of “Report on missing data points”. This enables the AE to keep track of the number of missing data points and their corresponding time-stamps over a predefined but renewable duration (the "window duration" of the missingData).

Originator(Hosting CSE):

No change from the procedures in clause 7.5.1.2.2 except the following addition in Step 1.0:

When the first missing data point is detected (i.e. a detection of the first discontinuous time-stamp), following the creation of the subscription, the Hosting CSE shall start a timer associated with that subscription and start counting the number of the missing data points. The timer is set according to the duration in the subscription’s missingData condition. The reporting policy is governed by the rules below:

If the total number of missing data points becomes equal to the number specified in the missingData condition before the timer expires, a NOTIFY request shall be sent with a timeSeriesNotification element in the notificationEvent/representation element of the notification. The missing data points counter shall continue counting while the timer continues to run (since it did not expire). A similar NOTIFY request shall be sent for each subsequent missing data point detected until the timer expires (see next bullet for behaviour when the timer expires).

If the timer expires the missing data points counter is reset back to 0. The timer is restarted upon subsequent detection of missing data.

The reset of the timer and the missing data points counter upon timer expiry shall continue until such time as the subscription is cancelled or terminated.

If no missing data points have been detected at all during the lifetime of a subscription, then no timer shall be started at all. But once a timer is started, triggered by the first missing data point, then the rules in the previous bullets shall apply.

No change for the remaining steps from the procedures in clause 7.5.1.2.2.

7.5.1.2.10	Notification for Dynamic Authorization

Dynamic Authorization uses a two-way exchange of information between a Hosting CSE (i.e. Originator) and a Dynamic Authorization System (DAS) Server (i.e. Receiver). This two-way handshake is performed using a Notification request and response.

Originator:

When the Originator (i.e. Hosting CSE) is triggered to perform dynamic authorization for an incoming request that it receives, then it performs the following steps in order:

Configure the To parameter with the address of the corresponding DAS Server associated with the resource targeted by the received request. The Hosting CSE shall use the DAS Server address information configured within the dynamicAuthorizationPoA attribute of the <dynamicAuthorizationConsultation> resource associated with the targeted resource. The Hosting CSE shall determine the corresponding <dynamicAuthorizationConsultation> resource using the dynamicAuthorizationConsultationIDs attribute of the targeted resource. If the attribute is not supported by the targeted resource, or it is not set, or it has a value that does not correspond to a valid <dynamicAuthorizationConsultation> resource(s), or it refers to a <dynamicAuthorizationConsultation> resource(s) that is not reachable, then based on system policies, the dynamicAuthorizationConsultationIDs associated with the parent may apply to the child resource if present, or a system default <dynamicAuthorizationConsultation> may apply if present. If a dynamicAuthorizationConsultationID attribute and corresponding <dynamicAuthorizationConsultation> resource cannot be found or if the dynamicAuthorizationEnabled of a <dynamicAuthorizationConsultation> has a value of false and Distributed Authorization is not supported (see oneM2M TS-0001 Functional Architecture [6] clause 10.2.3), the Hosting CSE shall reject the request by returning an "ORIGINATOR_HAS_NO_PRIVILEGE" Response Status Code to the Originator of the received request and no additional steps shall be performed.

Configure the From parameter with the ID of the Hosting CSE which hosts the resource targeted by the received request.

Configure the mandatory sub-elements of the securityInfo element of the notification data:

a)	The securityInfoType element shall be configured as "1" (Dynamic Authorization Request) in the Notify request primitive.

b)	The originator element shall be configured with the ID of the Originator of the received request.

c)	The targetedResourceType element shall be configured with the type of resource targeted by the received request.

d)	The operation element shall be configured with the type of operation targeted by the received request.

Optionally configure one or more optional sub-elements of the securityInfo element of the notification data:

a)	The originatorIP element may be configured with the IP address of the Originator of the received request.

b)	The originatorLocation may be configured with the location of the Originator of the received request.

c)	The originatorRole may be configured with the role of the Originator of the received request.

d)	The requestTimestamp may be configured with the time at which the request was received.

e)	The targetedResourceID may be configured with the identifier of the targeted resource of the received request.

f)	The proposedPrivilegesLifetime may be configured with a time duration for which the Hosting CSE is requesting privileges be granted to the Originator of the received request.

g)	The rolesFromACPs may be configured with a list of roles specified in the ACPs associated with the resource targeted by the received request.

h)	The tokenIDs may be configured with a list of token identifiers specified by the Originator of the received request.

i)	The authorSignIndicator may be configured with the value specified by the received request.

The Hosting CSE shall send the notification request for dynamic authorization to the targeted DAS Server.

Receiver:

When the DAS Server receives a notification request for dynamic authorization, it processes the request and returns a notification response for dynamic authorization to the originating Hosting CSE.

NOTE 1:	The details of how the DAS Server processes the notification request for dynamic authorization are not visible to the oneM2M system, and are not addressed in the present document.

Originator:

When the Hosting CSE receives a notification response for dynamic authorization, it performs the following steps in order:

The Hosting CSE shall verify that the securityInfoType element of the securityInfo element of the notification is configured as "2" (Dynamic Authorization Response). If it is not, the Hosting CSE shall not grant privileges to the Originator of the request for which the Hosting CSE was attempting dynamic authorization. If Distributed Authorization is not supported (see oneM2M TS-0001 Functional Architecture [6] clause 10.2.3) the Hosting CSE shall reject the request by returning an "ORIGINATOR_HAS_NO_PRIVILEGE" Response Status Code to the Originator of the received request and no additional steps shall be performed.

The Hosting CSE shall check whether the response contains a dynamicACPInfo element. If present, the Hosting CSE shall create a <accessControlPolicy> child resource under the targeted resource and configure its privileges using the dynamicACPInfo. In this case, the Hosting CSE shall configure the privileges attribute with the grantedPrivileges and the expirationTime attribute with the privilegesLifetime. The Hosting CSE shall also configure the selfPrivileges attribute to allow itself to perform Update/Retrieve/Delete operations on the newly created <accessControlPolicy> resource.

The Hosting CSE shall check whether the response contains a tokens element. If present the Hosting CSE shall perform verification and caching of the token as specified in clause 7.3.2 in oneM2M TS-0003 [7] and the Hosting CSE shall check whether an AuthorSignReqInfo is contained in the response. If it is present, the Hosting CSE shall add the AuthorSignReqInfo into the response to the Originator of the incoming request.

NOTE 2:	The Hosting CSE uses the information in the DAS response for authorization, see clause 7.3.3.15.

7.5.1.2.11	Notification for receiverESPrimRandObject Generation

Originator:

When the Originator is triggered to perform receiverESPrimRandObject generation as part of establishing sessionESPrimKey with a Receiver, it performs the following steps in order:

Configure the To parameter with the address of the Receiver's <CSEBase> or <AE> resource.

Configure the From parameter with the ID of the Originator.

The securityInfoType element of the securityInfo element of the notification data shall be configured as "3" (receiverESPrimRandObject Request) in the Notify request primitive.

The Originator shall send the notification request for dynamic authorization to the targeted Receiver.

Receiver:

When a Receiver receives a notification request, it processes the securityInfoType element of the securityInfo element and determines that the notification is for receiverESPrimRandObject generation. The Receiver generates a receiverESPrimRandObject as specified in oneM2M TS-0003 [7]. Then the Receiver sends a notification response to the Originator, with the securityInfo element containing the following elements:

The securityInfoType element shall be configured as "4" (receiverESPrimRandObject Response) in the Notify response primitive.

The esprimRandObject shall contain the receiverESPrimRandObject.

When the Originator receives a notification response for dynamic authorization, it performs the following steps in order:

The Originator shall verify that the securityInfoType element of the securityInfo element of the notification is as configured as "4" (receiverESPrimRandObject Response).

The Originator shall check whether the securityInfo element contains an esprimRandObject element. If it does, the Originator shall use the receiverESPrimRandObject in esprimRandObject element in the generation of sessionESPrimKey.

7.5.1.2.12	Notification for End-to-End Security Certificate-based Key Establishment (ESCertKE)

The End-to-End Security Certificate-based Key Establishment (ESCertKE) uses a four-way exchange of messages to establish a symmetric key for end-to-end security between the Originator and Receiver. This four-way exchange consists of two sequential two-way (request and response) exchanges using Notification for transport.

Originator:

When the Originator is to perform ESCertKE with the Receiver, then the Originator performs following steps in order:

The Originator shall form the ESCertKE Message 1 as specified in oneM2M TS-0003 [7].

The Originator performs the general procedure for an Originator as described in clause 7.2.2.1 with the following additional details:

a)	In step Orig-1.0, described in clause 7.3.1.1, a Notify Request primitive shall be formed with the Notification data comprising a securityInfo element with securityInfoType element set to "6" (ESCertKE Message) and escertkeMessage element set to the value of the ESCertKE message 1.

Receiver:

When a Receiver receives the Request, then the Receiver performs the general procedure for a Receiver with the following additional steps performed as part of Recv-6.5 for Notify Retargeting described in clause 7.3.3.9:

The Receiver extracts the securityInfo element from the notification data.

The Receiver examines the securityInfoType element of the securityInfo element and determines from its value "6" (ESCertKE Message) that the notification is for ESCertKE.

The Receiver extracts the ESCertKE message 1 contained in escertkeMessage element of the securityInfo element.

The Receiver processes ESCertKE message 1 as specified in clause 8.7 of oneM2M TS-0003 [7], resulting in ESCertKEY message 2.

The Receiver forms the Response content comprising a securityInfo element with securityInfoType element set to "6" (ESCertKE Message) and escertkeMessage element set to the value of the ESCertKE message 2.

Originator:

The Originator performs the following steps at Orig-6.0 "Process Response Primitive":

The Originator extracts the securityInfo element from the Response Content parameter.

The Originator examines the securityInfoType element of the securityInfo element and verifies that from its value is "6" (ESCertKE Message).

The Originator extracts the ESCertKE message 2 contained in escertkeMessage element of the securityInfo element.

The Originator processes ESCertKE message 2 as specified in clause 8.7 of oneM2M TS-0003 [7], resulting in ESCertKEY message 3.

The Originator and Receiver now repeat steps 2) to 10), with ESCertKE message 3 replacing ESCertKE message 1, and ESCertKE message 4 replacing ESCertKE message 2. Following the repeat of Steps 2) to 10), the following step is performed to conclude the procedure:

The Originator processes ESCertKE message 2 as specified in clause 8.7 of oneM2M TS-0003 [7].

7.5.1.2.13	Using Notify for transport of ESPrim Objects

The Notify operation is used for transport of ESPrim Objects protecting an exchange of inner primitives, as part of clause 7.6.2 "Procedure for applying End-to-End Security of Primitives (ESPrim)".

NOTE:	The inner request primitive can request any operation (Create, Retrieve, Update, Delete, Notify) allowed by the resource addressed by the inner request primitive. The composing or processing of the inner request primitive and the corresponding inner response primitive follows the general procedures in clause 7.2.2, and is not addressed further in the present clause.

Originator:

When the originator is to secure an exchange of inner primitives, then the Receiver shall apply the following steps in order:

Encrypt the inner request primitive to form an ESPrim Object as described in step E of clause 7.6.2.

Form the Notify request from the ESPrim Object as described in step F of clause 7.6.2.

Deliver the Notify request to the Receiver as described in step G and H of clause 7.6.2.

Receiver:

When a Receiver receives a Notify request transporting an ESPrim Object, then the Receiver shall apply the following steps in order:

Process the Notify request to extract the ESPrim Object as described in step I of clause 7.6.2.

Decrypt the ESPrim Object to form the inner request primitive as described in step J of clause 7.6.2.

The inner request primitive is processed, resulting in an inner response primitive.

Encrypt the inner response primitive to form an ESPrim Object as described in step L of clause 7.6.2.

Form a successful Notify response as described in step M of clause 7.6.2.

Deliver the Notify response to the Originator as described in step N of clause 7.6.2.

Originator:

When the Originator receives a Notify response transporting an ESPrim Object, it shall perform the following steps in order:

Process the Notify request to extract the ESPrim Object as described in step O of clause 7.6.2.

Decrypt the ESPrim Object to form the inner request primitive as described in step P of clause 7.6.2.

The inner response primitive is processed.

Error cases are addressed in clause 7.6.2.

7.5.1.2.14	Notification for Authorization Relationship Mapping Record creation

Originator-AE:

The AE sends the AuthorSigns to the Hosting CSE using a Notification Request. It performs the following steps:

Configure the To parameter with the ID of the Hosting CSE.

Configure the From parameter with the ID of the Originator-AE.

Configure the mandatory sub-elements of the securityInfo element of the notification data:

a)	The securityInfoType element shall be configured as "7" (Dynamic Authorization Relationship Mapping Request) in the Notify request primitive.

Optionally configure one or more optional sub-elements of the securityInfo element of the notification data:

a)	The authorSigns element shall be configured with the value of the authorSigns generated by the Originator-AE.

b)	The tokenIDs element shall be configured with the a list of token identifiers.

c)	The tokens element may be configured with a list of tokens.

NOTE 1:	At least one of the Token representation elements (tokenIDs and tokens) shall be present in the request.

Receiver/Originator-the Hosting CSE:

When the Hosting CSE receives a request including authorSigns from AE, it will forward the authorSigns to the DAS Server AE using a Notification Request:

Configure the To parameter:

No change from the procedures in clause 7.5.1.2.10.

Configure the From parameter:

No change from the procedures in clause 7.5.1.2.10.

Configure the mandatory sub-elements of the securityInfo element of the notification data:

a)	The securityInfoType element shall be configured as "7" (Dynamic Authorization Relationship Mapping Request) in the Notify request primitive.

b)	The originator element shall be configured with the ID of the Originator-AE of the received request.

Optionally configure one or more optional sub-elements of the securityInfo element of the notification data:

a)	The authorSigns element shall be configured with the value of the authorSigns specified by the Originator-AE of the received request.

b)	The tokenIDs element shall be configured with the a list of token identifiers specified by the Originator-AE of the received request.

c)	The tokens element may be configured with a list of tokens.

NOTE 2:	At least one of the Token representation elements (tokenIDs and tokens) shall be present in the request.

Receiver:

When the DAS server receives a notification to create an Authorization Relationship Mapping Record, it processes the request and returns a notification response to the originating Hosting CSE.

NOTE 3:	The details of how the DAS Server processes the notification request for dynamic authorization are not visible to the oneM2M system, and are not addressed in the present document.

7.5.1.2.15	Notification for Authorization Relationship Mapping Record Request

Originator:

When the Hosting CSE receives an incoming request from an AE including Tokens or TokenIDs which are valid but the holder attribute stored locally for the Token(s) is not equal to the AE-ID which sent the incoming request, the Hosting CSE shall send a Notification request to DAS server AE to get the value of AuthorSigns for this Token:

Configure the To parameter:

No change from the procedures in clause 7.5.1.2.10.

Configure the From parameter:

No change from the procedures in clause 7.5.1.2.10.

Configure the mandatory sub-elements of the securityInfo element of the notification data:

a)	The securityInfoType element shall be configured as "7" (Dynamic Authorization Relationship Mapping Request) in the Notify request primitive.

Optionally configure one or more optional sub-elements of the securityInfo element of the notification data:

a)	The tokenIDs element shall be configured with the a list of token identifiers specified by the Originator-AE of the received request.

b)	The tokens shall be configured with a list of tokens specified by the Originator of the received request.

c)	The authorSignReqInfo element shall be configured with the value true to request the Signature for the token which is contained in the Authorization Relationship Mapping Record.

NOTE 1:	At least one of the Token representation elements (tokenIDs and tokens) shall be present in the request.

Receiver:

When the DAS server receives the Notification request for requesting the signature, it processes the request and returns a notification response including the Signature to the originating Hosting CSE.

NOTE 2:	The details of how the DAS Server processes the notification request for dynamic authorization are not visible to the oneM2M system, and are not addressed in the present document.

Originator:

When the Hosting CSE receives a notification response for Authorization Relationship Mapping, it performs the following steps in order:

The Hosting CSE shall verify that the securityInfoType element of the securityInfo element of the notification is configured as "8" (Dynamic Authorization Relationship Mapping Response).

The Hosting CSE shall check if the Signature element is in the response. If the Signature element is present, the Hosting CSE shall further confirm whether the AE has the possession of the token sent in the incoming request.

7.5.1.2.16	Notification of a Change in AE Registration Point

Originator:

Case a) When an AE that wants its registration points tracked, attempts to re-register to a new Registrar CSE using an AE-ID-Stem starting with a 'C', that was previously assigned by a prior Registrar CSE, the new Registrar CSE, acting as the Originator, shall send a Notify request primitive to inform the IN-CSE that the AE has changed registration point.

Case b) When the IN-CSE determines that an AE has changed its registration point, the IN-CSE, acting as the Originator, shall send a Notify request primitive to the CSEs, so that these may update the references to the <AE> resources for the AE that has changed its registration point. If the IN-CSE maintains an <AEContactList> resource, the IN-CSE shall determine which CSEs are effected, and shall send a Notify request primitive only to these. If the IN-CSE does not maintain an <AEContactList> resource, the IN-CSE shall send a Notify request primitive to all CSEs.

In both cases, the Originator shall:

Set the AERegistrationPointChange element of the notification data object as true in the Notify request primitive.

Set the trackingID1 element of the notification data object as SP-relative-Resource-ID at the prior registration point.

Set the trackingID2 element of the notification data object as SP-relative-Resource-ID at the new registration point.

Send the Notify request primitive(s).

Receiver:

For both cases, upon receiving the Notify request primitive with an AERegistrationPointChange element of the notification data object set as true, the Hosting CSE shall use this to indicate a change in registration point. The Receiver shall:

Update references to the SP-Relative-Resource-ID (e.g. in Announce links, Notification targets, group Member IDs, <accessControlPolicy> resource OriginatorID lists) tied to the prior registration point (trackingID1), so that these refer to the new registration point (trackingID2).

Update the status of this registration to "INACTIVE". if the Receiver hosts the registration of the prior AE registration point.

7.5.1.2.17	Notification of a Reference to Application Entity Resource identifier

Originator:

When a Hosting CSE (acting as Originator) determines that a child resource has a modified (new, updated, or deleted) reference an Application Entity Resource ID, the Hosting CSE shall send a Notify request primitive to the IN-CSE, requesting to add, update, or delete the entry to the <AEContactList> resource. The Originator shall:

Set the AEReferenceIDChange element of the notification data object as true in the Notify request primitive.

For a new AE reference (from a CREATE operation):

a)	Set trackingID1 element of the notification data object to NULL.

b)	Set trackingID2 element of the notification data object to the SP-relative-Resource-ID used in the new AE reference.

For an updated AE reference (from an UPDATE operation):

a)	Set trackingID1 element of the notification data object to the SP-relative-Resource-ID used in the AE reference before the UPDATE.

b)	Set trackingID2 element of the notification data object to the SP-relative-Resource-ID used in the AE reference after the UPDATE.

For a deleted AE reference (from an DELETE operation or resource expiration):

a)	Set trackingID1 element of the notification data object to the SP-relative-Resource-ID used in the AE reference.

b)	Set trackingID2 element of the notification data object to NULL.

Send the Notify request primitive(s).

Receiver:

Upon receiving the Notify request primitive with an AEReferenceIDChange element of the notification data object set as true, the IN-CSE (acting as Receiver) shall update its <AEContactList> resource. IN-CSE will add, update, or remove entries from the AE-IDList attribute of the <AEContactListPerCSE> resource corresponding to the impacted CSE.

7.5.1.2.18	Cross-Resource Notification

When the <crossResourceSubscription> Hosting CSE receives a notification from the Host of a <subscription> indicated in regularResourcesAsTarget or subscriptionResourcesAsTarget the <crossResourceSubscription> Hosting CSE shall perform the following steps:

The Hosting CSE shall send a notification response to the <subscription> resource Hosting CSE.

Aggregate notifications using the time window mechanism indicated by timeWindowType attribute of the <crossResourceSubscription> resource to determine if a cross-resource notification shall be issued:

The Hosting CSE shall store the received notification until the current time window expires. When the current time window expires, the Hosting CSE shall discard stored notifications:

If timeWindowType is PERIODICWINDOW then a new time window shall be started when the current time window expires.

If timeWindowType is SLIDINGWINDOW then a new time window shall be started when the next notification is received.

When notifications from all target <subscription> resources occur within the required time window the Hosting CSE shall compose a cross-resource notification in a notification data object with type m2m:notification:

Set the subscriptionReference element to the URI of the <crossResourceSubscription> resource.

If the expirationCounter attribute is set, then it shall be decreased by one when the Originator successfully sends the Notify request primitive. If the counter equals to zero ('0'), the corresponding <crossResourceSubscription> resource shall be deleted as described in 7.4.58.2.4.

Send the notification to the notificationURI using the procedure defined in clause 7.5.1.2.2.

"Wait for Response primitive" procedure.

The Subscriber or Notification Targets which receive cross-resource notifications from the Hosting CSE shall perform the following steps in order:

"Create a success response" procedure defined in clause 7.3.3.12.

"Send the Response primitive" procedure.

7.5.1.2.19	Notification for Subscription Blocking Triggered update

Whenever the Hosting CSE receives an update request primitive for a target resource which has subscription with notificationEventType set to "Blocking_Update", it shall perform the steps listed below before Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation” is performed.

If the attribute condition tag of the eventNotificationCriteria attribute of the <subscription> resource is set, check that the attribute condition tag matches the modified attributes in the received UPDATE request.

Prevent or block all other UPDATE request primitives to this target resource

Create a Notification request primitive and configure the request parameters as follows.

a)	Set the representation attribute of the notification to the representation of the target resource contained in the received UPDATE request primitive.

Send the Notification request primitive to the target specified in notificationURI.

Wait for a Notification response.

Process the Notification response primitive

a)	If the notification Response Status Code is not successful, return a response to the original blocked UPDATE request primitive with a Response Status Code according to clause 7.3.2.9 .

b)	If the notification Response Status Code is successful, perform Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation” for the received UPDATE request.

Allow all other UPDATE request primitives for this target resource.

7.5.1.2.20	Notification of Cross Resource Subscription Deletion

Originator:

When a <crossResourceSubscription> resource is deleted the Originator shall send Notify request primitives to the <crossResourceSubscription> resource's subscriberURI if it is configured:

a)	The subscriptionDeletion element of the notification data object set as true.

b)	The subscriptionReference element of the notification data object set as the resource identifier of the <crossResourceSubscription> resource.

c)	The To parameter shall be set to the entity indicated in subscriberURI.


### 7.5.2	Elements contained in the Content primitive parameter


Clauses 7.2.1.1 and 7.2.1.2 enumerate the forms that the Content primitive parameter takes in various Request and Response cases. Note that the Content primitive parameter is denoted as primitiveContent in both CDT-requestPrimitive-v3_32_0.xsd and CDT-responsePrimitive-v3_32_0.xsd.

This clause details the Objects (elements) used in some of these cases. in the tables below.

The following elements are defined for use in the Content parameter of a request:

Table 7.5.2-1: Elements used for request content

The following elements are defined for use in the Content parameter of a response sent in reply to a request message with Operation and Result Content (rcn) parameters as given in the column "Applicable Operations" (the settings of the Result Content parameters are defined in clause 6.3.4.2.7; NP means the rcn parameter is not present).

Table 7.5.2-2: Elements used for response content

The XML schema definition of the Content primitive parameter (i.e. datatype m2m:primitiveContent) allows to include XML wildcard elements. An XML representation of the Content primitive parameter shall include a root element which is associated with an XSD Global Element. The root element shall be prefixed with a namespace prefix identifier (e.g. m2m:) specified in the associated XSD which defines the respective Global Element. The Content primitive parameter allows to include namespaces other than m2m.


### 7.5.3	Multicast group procedures


7.5.3.1	Multicast group CREATE procedure

7.5.3.1.1	Common procedure

The group-hosting CSE shall perform the following operations:

The group-hosting CSE shall check the multicastCapability attribute of each remote Member Hosting CSE's <remoteCSE> resource:

a)	If at least two remote member-hosting CSEs support multicast capability MBMS, then the group-hosting CSE shall create 3GPP MBMS multicast group for the members that support MBMS multicast capability, refer to clause 7.5.3.1.2.

b)	If at least two remote member-hosting CSEs support multicast capability IP, then the group-hosting CSE shall create an IP multicast group for the members that support IP multicast capability, refer to clause 7.5.3.1.3.

Table 7.5.3.1.1-1: Elements of Multicast Group Information Data Object

7.5.3.1.2	3GPPTM  MBMS group creation procedure

The group-hosting CSE shall perform the operations which are specified in clause 10.2.7.13.1 of oneM2M TS-0001 [6] and in clause 7.7.3.1 of oneM2M TS-0026 [43]:

Get the externalGroupID of the <remoteCSE> resource for each member whose externalGroupID exists, send a 3GPP Allocate TMGI Request [51] to the group Service Server Address as local configuration over Mcn reference point.

When the group-hosting CSE receives the corresponding response from 3GPP network:

a)	If the response indicates failure, then the group-hosting CSE shall stop the multicast group create procedure.

b)	If the response indicates success, then the group-hosting CSE shall get the TMGI and TMGIExpiration from the response.

Create a Multicast Group Information data object locally for each distinct externalGroupID: set its groupID to the value of the created <group>, assign the multicastType to MBMS, allocate a multicastAddress, set the externalGroupID to the same value as the externalGroupID of the <remoteCSE> resources, set the memberList to the members that belong to this multicast group, set the groupServiceServerAddress to the value provisioned by the 3GPP service provider, set the TMGI and TMGIExpiration to the values in the response from 3GPP network, set responseTimeWindow according to local policy. Assign a{fanout-segment} string, and set the multicastGroupFanoutTarget to /{groupHostingCSE-ID}/ {fanout-segment}.

NOTE:	For a guide to an allocation scheme of IPv4 and IPv6 multicast address spaces, reference may be made to standard documents such as IETF RFC 5771 [i.10] and IETF RFC 4291 [i.11].

Send a Create <localMulticastGroup> primitive to each Member Hosting CSE in the multicast group:

a)	Prepare the attributes of the <localMulticastGroup> resource according to the Multicast Group Information and send <localMulticastGroup> create request to each Member Hosting CSE in the multicast group. See clause 7.2.2.1.

When the group-hosting CSE receives the corresponding response from each Member Hosting CSE:

a)	If at least two member-hosting CSEs respond successfully, the group-hosting CSE shall remove the member ID(s) from the memberList for any Member Hosting CSEs whose response indicates failure.

b)	If no member-hosting CSEs respond successfully, the group-hosting CSE shall delete the local Multicast Group Information data object.

c)	If only one member-hosting CSEs responds successfully, the group-hosting CSE shall delete the local Multicast Group Information data object and send a <localMulticastGroup> delete request to that member-hosting CSE. See clause 7.2.2.1.

7.5.3.1.3	IP multicast group creation procedure

The group-hosting CSE shall perform the operations which are specified in clause 10.2.7.13.1 of oneM2M TS-0001 [6]:

Create a Multicast Group Information data object locally: set its groupID to the value of the created <group>, assign the multicastType to IP, allocate a multicastAddress, set the memberList to the members that belong to this multicast group, set responseTimeWindow according to local policy. Assign a{fanout-segment} string, and set the multicastGroupFanoutTarget to /{groupHostingCSE-ID}/ {fanout-segment}.

NOTE:	For a guide to an allocation scheme of IPv4 and IPv6 multicast address spaces, reference may be made to standard documents such as IETF RFC 5771 [i.10] and IETF RFC 4291 [i.11].

Send a CREATE <localMulticastGroup> primitive to each Member Hosting CSE in the multicast group:

a)	Prepare the attributes of the <localMulticastGroup> resource according to the Multicast Group Information and send <localMulticastGroup> create request to each Member Hosting CSE in the multicast group. See clause 7.2.2.1.

When the group-hosting CSE receives the corresponding response from each member-hosting CSE:

a)	If at least two member-hosting CSEs respond successfully, the group-hosting CSE shall remove the member ID(s) from the memberList for any member-hosting CSEs whose response indicates failure.

b)	If no member-hosting CSE responds successfully, the group-hosting CSE shall delete the Multicast Group Information locally.

c)	If only one member-hosting CSEs responds successfully, the group-hosting CSE shall delete the local Multicast Group Information data object and send a <localMulticastGroup> delete request to that Member Hosting CSE. See clause 7.2.2.1.

7.5.3.2	Multicast group Update procedure

If the memberIDs attribute of the <group> resource was updated, the receiver shall check the multicastCapability attribute of each remote Member Hosting CSE's <remoteCSE> resource according to the new memberIDs and then make modifications to the <localMulticastGroup> resources on the remote Member Hosting CSEs as appropriate.

The steps involved are illustrated here with an example. In this example two new members (/CSE6/aa and /CSE7/aa) are added to memberIDs and two of the old members (/CSE2/aa and /CSE5/aa) are deleted. Table 7.5.3.2-1 shows the old and new memberIDs in the example.

Table 7.5.3.2-1: memberIDs in the example <group> resource

Prior to the update, the example group has two Multicast Group Information data objects as illustrated in Table 7.5.3.2-2.

Table 7.5.3.2-2: Old Multicast Group Information Data Objects

The group-hosting CSE shall perform the following operations:

If there are fewer than two new member-hosting CSEs supporting multicast, the receiver shall delete all the local Multicast Group Information data objects and send <localMulticastGroup> delete requests to each old Member Hosting CSE before updated. See clause 7.2.2.1.

If there are at least two new member-hosting CSEs supporting multicast, the receiver shall create new local Multicast Group Information data objects according to the new Member Hosting CSEs.

In this example, the new Multicast Group Information is illustrated in Table 7.5.3.2-3. The IP multicast is deleted because there is only one Member Hosting CSE (CSE1) left. The two MBMS multicast group data objects are created because there are two different externalGroupIDs.

Table 7.5.3.2-3: New Multicast Group Information Data Object Example of <group> resource

The receiver compares each new Multicast Group Information data object with the each of the old data objects:

If a member-hosting CSE exists in one of the new data objects and does not exist in any of the old ones, the receiver shall send a <localMulticastGroup> create request to that member-hosting CSE. See clause 7.2.2.1.

If a member-hosting CSE exists in an old data object and does not exist in any of the new ones, the receiver shall send a <localMulticastGroup> delete request to that member-hosting CSE. See clause 7.2.2.1.

If a member-hosting CSE exists in both a new data object and an old one, the receiver shall compare the memberList in the two data objects. If the result is different, the receiver shall send a <localMulticastGroup> update request to the member-hosting CSE, see clause 7.2.2.1.

In this example, the operations for each member-hosting CSE are illustrated in Table 7.5.3.2-4.

Table 7.5.3.2-4: <localMulticastGroup> Operation for Member-Hosting CSEs Example

When the group-hosting CSE receives the corresponding response from each member-hosting CSE in the new Multicast Group Information data object, the receiver shall remove the member ID(s) from the memberList for any member-hosting CSEs whose response indicates failure:

If at least two member-hosting CSEs exist in the data object, the receiver shall keep the Multicast Group Information data object.

If no member-hosting CSE exists in the data object, the receiver shall delete the Multicast Group Information data objects held locally.

If only one member-hosting CSE exists in the data object, the receiver shall delete the local Multicast Group Information data object and send a <localMulticastGroup> delete request to that member-hosting CSE. See clause 7.2.2.1

The receiver shall delete all the old Multicast Group Information data objects.

In this example, the responses for each Member Hosting CSE are illustrated in Table 7.5.3.2-5.

Table 7.5.3.2-5: <localMulticastGroup> Operation Result for Member-Hosting CSEs Example

In this example, the new Multicast Group Information after the responses have been processed is illustrated in Table 7.5.3.2-6.

Table 7.5.3.2-6: Multicast Group Information Data Object Example of <group> resource

7.5.3.3	Multicast group Delete procedure

If there are one or more Multicast Group Information data objects associated with the deleted group, the receiver shall delete all the Multicast Group Information data objects and send <localMulticastGroup> delete requests to each Member Hosting CSE, refer to the clause 7.2.1.


## 7.6	Security Procedures



### 7.6.1	Introduction


oneM2M TS-0003 [7] specifies a range of security procedures. Clause 7.6 describes how to use the security procedures as part of the general procedures, common operations, resource type-specific procedures and primitive-specific procedures. The following security procedures are described:

End-to-End security of primitives (ESPrim): securing a primitive so that CSEs (forwarding the primitive) do not need to be trusted with the confidentiality and integrity of the primitive.


### 7.6.2	Procedure for applying End-to-End Security of Primitives (ESPrim)


End-to-End Security of Primitives (ESPrim) provides an interoperable framework for securing oneM2M primitives so CSEs (forwarding the primitive) do not need to be trusted with the confidentiality and integrity of the primitive. ESPrim provides mutual authentication, confidentiality, integrity protection and a freshness guarantee (bounding the age of ESPrims). Credential management aspects and data protection aspects for ESPrim are specified in oneM2M TS-0003 [7]. Architecture-level-details for the transport of ESPrim are specified in oneM2M TS-0001 [6].

The primitive to be secured is called the inner primitive. All operations (Create, Retrieve, Update, Delete, or Notify) are allowed for an inner request primitive and inner response primitive. The inner primitives are encrypted to form an ESPrim Object. A Notify Request and corresponding Notify Response primitives (called the outer request primitive and outer response primitive) are used to transport the ESPrim Objects containing this encrypted inner request primitive and inner response primitive respectively.

There are three parallel procedures which shall be considered when using ESPrim to protect primitives:

Inner primitive processing: The general procedure for the inner request primitive and corresponding inner response primitive.

ESPrim processing: Encrypting inner primitives to form ESPrim objects, and decrypting ESPrim objects to obtain the inner primitives.

Outer primitive processing: The general procedure for the outer request primitive and corresponding outer response primitive used to transport the ESPrim objects.

There are three actors impacted:

Originator: The CSE or AE which originates the inner primitive procedure, the ESPrim protocol and the outer Notify primitive procedure.

Hosting CSE: The Hosting CSE from the perspective of the outer primitive procedure, hosting the <CSEBase> or <AE> resource of the Target.

Target CSE or AE: The CSE or AE terminating the ESPrim protocol and inner primitive procedure. The Target shall be either the Hosting CSE or an AE registered to the Hosting CSE. The Target also applies some processing of the outer primitive procedure: extracting the ESPrim objects form the outer request primitives, and composing the outer response primitives.

Other Receiver CSEs on the delivery path (apart from the Originator and Hosting CSE) process and forward the outer Notify primitives according to the general procedure in clause 7.2.2.2. These Receiver CSEs do not process the ESPrim Objects nor the inner primitives. The procedures for these Receiver CSEs are not affected when ESPrim is being used.

The present clause describes the relationship between the steps of the general procedures applied to the inner primitives, the ESPrim processing and the general procedures applied to the outer primitives.

Figure 7.6.2-1 and the following text describe the procedure for applying ESPrim to protect an exchange of inner primitives.

Figure 7.6.2-1: Procedure for applying End-to-End Security of Primitives (ESPrim)
to protect an exchange of inner primitives

Pre-Condition: The Originator and Target have established a pairwiseESPrimKey and steps have been performed for establishing a sessionESPrimKey at the Originator (phases A and B in clause 8.4.2 of oneM2M TS-0003 [7]).

Originator:

The Originator's inner primitive processing shall apply Orig-1.0 "Compose of a Request primitive" to compose the inner request primitive. The inner request should not include the delivery-related parameters Response Type, Event Category, and Delivery Aggregation.

NOTE 1:	Delivery-related parameters Response Type, Event Category, and Delivery Aggregation in the inner request (composed at step A) will be ignored – see step K. When appropriate, these parameters are provided in the outer request primitive only (composed at step F).

The Originator shall not apply Orig-2.0 "Send a Request primitive to the Receiver CSE", but instead shall pass the inner request primitive to the Originator's ESPrim processing for further processing in Step E.

The Originator's inner primitive processing shall apply Orig-3.0 "Check Response Type". The Response Type is blockingRequest, see step A.

The Originator's inner primitive processing shall apply Orig-4.0 "Wait for Response primitive", entering a waiting state until the inner response primitive is received (at step P).

The Originator's ESPrim processing shall apply ESPrim encryption to the inner request primitive, resulting in an ESPrim Object. The ESPrim encryption process is specified in oneM2M TS-0003 [7]. The ESPrim Object is passed to the Originator's outer primitive processing. The Originator's ESPrim processing enters waiting state until the corresponding ESPrim Object is received (at step O).

The Originator's outer primitive processing shall apply Orig-1.0 "Compose of a Request primitive" to compose the outer request primitive. The outer request primitive shall include the following parameters:

Operation: Notify (N)

To: An address of the <CSEBase> or <AE> resource associated with the Target.

From: An address of the Originator.

Request Identifier: may be independent of the Request Identifier in the inner request primitive.

Content: a securityInfo element with child elements

securityInfoType:	"5" (ESPrim Object).

esprimObject:		the ESPrim Object generated at step E.

The outer request primitive may include further optional parameters as described in clause 11.4.2 of oneM2M TS-0001 [6], including the delivery-related parameters Response Type, Event Category, and Delivery Aggregation.

The general procedures in clause 7.2.2.1 and clause 7.2.2.2 are followed for delivering the outer Notify request primitive from the Originator to the Hosting CSE of the addressed resource, in accordance with the communication mode of the outer request primitive. The outer Notify request primitive may be forwarded by one or more transit CSEs, which are not shown in Figure 7.6.2-1. The Originator's outer primitive processing enters a waiting state until the corresponding outer response primitive is received (at step N). The details of the delivery to and from the Hosting CSE have no impact on any other steps. The present step includes all Receiver steps in clause 7.2.2.2 up to Recv-6.4. If any errors are encountered during this step, then the Notify request primitive is rejected with a Response Status Code indicating the appropriate error code.

Hosting CSE:

The Hosting CSE's outer primitive processing applies Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed" to the outer Notify request primitive. This triggers "Notify processing" (clause 7.3.3.9), and the Hosting CSE passes the outer request primitive to the Target identified by the To parameter:

If the To parameter is an address for the Hosting CSE's <CSEBase> resource, then the Target is the Hosting CSE.

If the To parameter is an address for an <AE> resource, then the Target is the associated AE.

If any errors are encountered during this step, then the Notify request primitive is rejected with a Response Status Code indicating the appropriate error code. The Hosting CSE's outer request processing enters waiting state until the corresponding outer response primitive is received at step M.

Target:

The Target's outer primitive processing shall examine the securityInfoType element of the securityInfo element in the Content parameter of the outer Notify request primitive. The value "5" of the securityInfoType indicates that the securityInfo element contains an ESPrim object. The Target shall extract the ESPrim Object contained in the esprimObject element of the securityInfo element and pass the ESPrim Object to the Target's ESPrim processing.

The Target's ESPrim processing shall apply ESPrim decryption to the ESPrim Object, resulting in the verified inner request primitive. The ESPrim decryption process is specified in oneM2M TS-0003 [7]:

If the Target's ESPrim processing encounters one of the error cases in Table 7.6.2-1, then the corresponding Response Status Code is returned to the Hosting CSE's outer primitive processing, and the call flow skips to step M.

If decryption is successful, then the verified inner request primitive is passed to the Target's inner primitive processing, and the Target's ESPrim processing enters waiting state until the corresponding inner response primitive processing Object is received (at step M).

The Target shall process the verified inner request primitive according to the general procedure for Receiver, see clause 7.2.2.2:

The Target shall ignore delivery-related parameters in the inner primitive, such as the Response Type, Event Category, or Delivery Aggregation. See note 1.

An inner response primitive is returned to the Target's ESPrim processing.

NOTE 2:	This call flow does not distinguish between successful and unsuccessful inner response primitives. Both will have ESPrim encryption applied prior to delivery back to the Originator.

The Target's ESPrim processing shall apply ESPrim encryption to the inner response primitive, resulting in an ESPrim Object. The ESPrim encryption process is specified in oneM2M TS-0003 [7]. If the Target's ESPrim processing encounters one of the error cases in Table 7.6.2-1, then the corresponding Response Status Code returned to the Hosting CSE's outer primitive processing and the call flow skips to step M. If the ESPrim processing is successful, then the ESPrim Object is passed to the Hosting Target's outer primitive processing.

If the Target's ESPrim processing returned a Response Status Code indicating an error, then the Hosting CSE's outer primitive processing forms an error Notify response as described in clause 7.3.3.13. If the Target's ESPrim processing returned an ESPrim Object, then the Target's outer primitive processing forms a successful Notify Response as described in clause 7.3.3.12, with the Content containing a securityInfo element with the following child elements:

securityInfoType:	"5" (ESPrim Object).

esprimObject:		the ESPrim Object received from the Target's ESPrim processing.

The outer response primitive is passed to the Hosting CSE's outer primitive processing.

Hosting CSE:

The general procedures in clauses 7.2.2.1 and 7.2.2.2 are followed for delivering the outer response primitive from the Hosting CSE to the Originator, in accordance with the communication mode of the outer response primitive. The outer Notify response primitive may be forwarded by one or more transit CSEs, which are not shown in Figure 7.6.2-1.

Originator:

The Originator's outer primitive processing shall apply Orig-6.0 "Process Response primitive" to the outer response primitive, extracting the ESPrim Object and forwarding this to the Originator's ESPrim processing.

The Originator's ESPrim processing shall apply ESPrim decryption to the ESPrim Object, resulting in the verified inner response primitive. The ESPrim decryption process is specified in oneM2M TS-0003 [7]. If decryption is successful, then the verified inner response primitive is passed to the Originator's inner primitive processing.

The Originator's inner primitive processing shall apply Orig-6.0 "Process Response primitive" to the verified inner response primitive.

Table 7.6.2-1: End-to-End security of Primitives (ESPrim) processing error cases
with corresponding error message


# 8	Representation of primitives in data transfer



## 8.1	Introduction


This clause defines the representation of request and response primitives as XML documents, JSON texts or CBOR data format. The process of translating objects (i.e. primitives in the present context) into a format that can be stored or exchanged between network entities is commonly denoted as serialization or marshalling.

The serialization described here is used in two places:

It can be used when transmitting primitives over communication protocols such as HTTP, CoAP, MQTT and WebSocket. When applying a particular protocol binding, it is permitted to adapt the serialization approach, in order to make use of protocol-specific features. For example, a particular protocol binding may require that one or more primitive parameters be mapped to protocol-specific header fields rather than being included in the protocol-specific serialized JSON, XML or CBOR which represents the message body.

Certain instances of resource types, e.g. instances of the <delivery> resource, include serialized primitives embedded in one of their resource attributes.

In order to enable efficient communication, the short names introduced in clause 8.2 shall be applied in XML, JSON and CBOR serializations to identify primitive parameters and resource attribute names. This implies that short names are applied in any communication over the Mca, Mcc and Mcc' reference points.


## 8.2	Short names



### 8.2.1	Introduction


XML, JSON and CBOR representations require encoding of the names of primitive parameters, resource attributes, resource types and complex data type members. Whenever a protocol binding transfers such a name over a oneM2M reference point, it shall use a shortened form of that name, rather than the full name that is used elsewhere in this and other oneM2M specifications. Short names enable payload reduction on involved telecommunication interfaces.

The mapping between the full names and their shortened form is given in the clauses 8.2.2 to 8.2.5.

These names are case-sensitive. A oneM2M implementation shall use the letter casing given in these clauses.


### 8.2.2	Primitive parameters


In protocol bindings primitive parameter names shall be translated into short names of Table 8.2.2-1.

Table 8.2.2-1: Primitive parameter short names

XML serialized representations of primitives employ root elements to differentiate between request and response primitive types (see clause 8.3). These elements are also embedded in some oneM2M-defined complex datatypes. These root element names shall be translated into short names as in Table 8.2.2-2. Their short name serialization shall include the namespace prefix.

Table 8.2.2-2: Primitive root element short names


### 8.2.3	Resource attributes


In protocol bindings, resource attributes names shall be translated into short names shown in the following tables.

Table 8.2.3-1: Resource attribute short names (1/6)

Table 8.2.3-2: Resource attribute short names (2/6)

Table 8.2.3-3: Resource attribute short names (3/6)

Table 8.2.3-4: Resource attribute short names (4/6)

Table 8.2.3-5: Resource attribute short names (5/6)

Table 8.2.3-6: Resource attribute short names (6/6)


### 8.2.4	Resource types


In protocol bindings resource type names shall be translated into short names of Table 8.2.4-1.

Table 8.2.4-1: Resource and specialization type short names


### 8.2.5	Complex data types members


In protocol bindings complex data types member names shall be translated into short names of Table 8.2.5-1.

Table 8.2.5-1: Complex data type member short names


### 8.2.6	Trigger payload fields


Trigger payload fields shall be translated into short names of Table 8.2.6-1.

Table 8.2.6-1: Trigger payload field short names

8.2.7	TimeSeries notification fields

TimeSeries notification fields shall be translated into short names of Table 8.2.7-1.

Table 8.2.7-1: TimeSeries notification field short names


## 8.3	XML serialization



### 8.3.1	Method


XML serialization of request or response primitives refers to the process of representing the primitive as an XML document.

The XML document shall be a well-formed XML document compliant with W3C XML 1.0 [1]. It shall be restricted to Unicode characters and encoded using UTF-8 as described in IETF RFC 3629 [21].

The structure and data types of XML serialized request and response primitives shall be consistent with the XSD defined in CDT-requestPrimitive-v3_32_0.xsd and CDT-responsePrimitive-v3_32_0.xsd, respectively. The data types used in these XSD files comply with the definitions in clause 6 and clause 7 of the present document.

XML serializations shall comply with the order of resource attributes and elements imposed by the XML schema definition. If an implementation uses modified XSD modified from the original files for schema validation of partial resource representations (see note 2 in clause 6.1), the order of resource attributes shall not be changed.

If an element instance is NULL then it is serialized into the XML as an empty element (as defined in W3C XML 1.0 [1]) regardless of the data type that it has in the corresponding XSD.

Note that the XSD files included in the present release employ the long names for primitive parameters and other XML elements and attributes, but the primitive serialization is required to use the corresponding short names (as defined clause 8.2 of the present document).

NOTE:	XML Schema files are available with both long and short names.

The primitive Content parameter is serialized just like any other element of complex type. Generally, the Content parameter may include only a partial set of attributes specified for the resource type as indicated in the Resource Type parameter, e.g. for partial Update or Retrieve Request procedures. For Notification Request primitives, the Content parameter includes a Notification data object as defined in clause 7.5.1.1 and the datatype definition given in CDT-notification-v3_32_0.xsd.


### 8.3.2	Examples


An example that shows a request primitive serialized into an XML document is shown below. This example shows the create request for an instance of a <contentInstance> resource. Only mandatory primitive parameters and resource attributes are shown.

<?xml version="1.0" encoding="UTF-8"?>
<m2m:rqp xmlns:m2m="http://www.onem2m.org/xml/protocols">
    <op>1</op>
    <to>//example.net/myCSE/-/Cont1</to>
    <fr>/myCSE/C2345</fr>
    <rqi>0002bf63</rqi>
    <ty>4</ty>
    <pc>
        <m2m:cin>
            <cnf>application/xml:1</cnf>
            <con>PHRpbWU+MTc4ODkzMDk8L3RpbWU+PHRlbXA+MjA8L3RlbXA+DQo=</con>
        </m2m:cin>
    </pc>
</m2m:rqp>

The XML elements have the following meaning:

rqp: Root element of the Request primitive, which includes a reference to an XSD file which defines its datatype.

op: 	Operation parameter of datatype m2m:operation: in this example value = 1 indicates a "Create" operation.

to: 	To parameter of type xs:anyURI: URI of the target resource.

fr: 	From parameter of type m2m:ID: ID of the Originator (either AE-ID or CSE-ID).

rqi: 	Request Identifier parameter of type m2m:requestID: this could e.g. represent a counter number.

ty: 	Resource Type parameter of datatype m2m:resourceType: indicating type of the resource to be created (value = 4 indicates that a <contentInstance> resource shall be created).

pc: 	Content parameter of datatype m2m:primitiveContent: the attributes of the resource to be provided by the Originator.

cin: Root element of the <contentInstance> resource of datatype m2m:contentInstance: this includes the mandatory attributes (and optional attributes not shown in this example) supplied by the request Originator. In this example, the Content parameter includes an instance of a <contentInstance> resource which consists of two attributes: contentInfo (cnf) – which specifies base64 encoding - and the content (con) itself.

The following example shows the Content of a request deleting the maxNrOfMembers attribute of a <group> resource. This is done by sending a NULL value which is represented in XML as an empty element.

<?xml version="1.0" encoding="UTF-8"?>
    <m2m:grp>
        <mnm></mnm>
    </m2m:grp>


## 8.4	JSON serialization



### 8.4.1	Terminology


The following conventions are used in clause 8.4.2.

The italicized terms object, member, name, array, number, string, boolean and null are to be interpreted as in IETF RFC 8259 [19].

The italicized term element is to be interpreted to encompass oneM2M Primitive Parameters, Resource Attributes and other elements or attributes used inside oneM2M complex type definitions.


### 8.4.2	Method


The primitive shall be encoded as a JSON object, conforming to the requirements of IETF RFC 8259 [19]. This JSON object shall be restricted to Unicode characters defined in The Unicode Standard and encoded using UTF-8 as described in IETF RFC 3629 [21]. The names in each object in the JSON shall be unique.

The structure of the top-level primitive object shall be determined by the data type definitions in clause 6 and clause 7 of the present document, as follows:

All member's names shall use the short name defined in clause 8.2.

If an element is defined in the present document as having a complex type, then it is serialized in the JSON member as an object and its children are recursively serialized as members of that object, using short names as defined in clause 8.2.

Where an element has a Global Element Declaration in the XSD its member name in the JSON serialization shall be prefixed with a namespace identifier followed by a ":" character. In particular, if the member serializes a Resource defined in the present specification its name shall have the prefix "m2m:".

The membership of each nested object shall respect the cardinality constraints from the corresponding XSD complex type definition.

If an element is defined in the present document as having an atomic data type that is numeric (including enumeration data types in clause 6.3.4) then its value is serialized into the JSON member as a number.

If an element is defined as having an atomic data type that is non-numeric then its value is serialized into the JSON member as a string.

If an element is defined as xs:boolean (or a type derived from xs:boolean) then it is serialized in the JSON member as a boolean.

If an element is defined as having an xs:list type in the corresponding XSD then it is serialized in the JSON member as an array. A list element that contains no values shall be represented as an empty array.

If an element instance has a NULL value then it is serialized into the JSON member as a null, regardless of the data type that it has in the corresponding XSD.

If an element is defined as having maxOccurs > 1 in the corresponding XSD then its occurrences are serialized in a single JSON member as an array.

If an element has an XSD data type that is a simple type with XML attributes, then it is serialized in the JSON member as an object. The XML attributes appear as members of that object (using their short names) and the value of the element is serialized as a member of that object with the special short name "val" (lower case).

The members (at each level) may be serialized in any order. The order in which they appear in the corresponding XSD file is immaterial.

If an element has an XSD data type that is a complex type with XML attributes, then it is serialized in JSON as an object. The XML attributes appear as members of that object (using their short names) as do the XML elements.

The Content parameter is serialized as an object containing a single member, as defined in the first column of Tables 7.5.2-1 and 7.5.2-2 using the short name from Table 8.2.4-1 or Table 8.2.3-2.

JSON serialized representations of request and response primitives shall not be encapsulated under member names m2m:rqp and m2m:rsp. Note that this is in contrast to XML serialized representations of primitives which shall include such root elements in order to assert XSD compliance, see clause 8.3.2.


### 8.4.3	Examples


EXAMPLE 1 starts:

An example of a request message serialized using JSON is given below:

{

"op": 1,

"fr": "Clight_ae1",

"to": "/homegateway/light",

"rqi": "A1234",

"pc": {

"m2m:sch": {

"se": {

"sce": ["* 0-5 2,6,10 * * * *"]

}

}

},

"ty": 18

}

op: operation (in this case it is Create)

fr: ID of the Originator (an AE in this example)

to: URI of the target resource

rqi: request identifier (this is a string)

pc: attributes of the <schedule> resource, with member name "m2m:sch", as provided by the Originator. This is serialized as a nested JSON object

ty: type of resource to be created (in this case a Schedule resource). This is a number.

Note that the Operation (op) parameter is present only in Request primitives. The presence of this parameter in JSON serialized primitive representations allows to differentiate Request primitives from Response primitives.

EXAMPLE 1 ends.

EXAMPLE 2 starts:

The next example shows an <AE> resource serialized using JSON.

The top level member, m2m:ae, is an object whose name consists of the prefix m2m: followed by the short name for the <AE> resource defined in Table 8.2.4-1. The members of this object are the attributes of <AE> using the short names from Table 8.2.3-2.

In this example the <AE> has just two direct child resources.They are <container> resources (resource type 3) and the second of them has a child <subscription> (resource type 23). The Result Content parameter in the request that was used to retrieve the <AE> resource was set to “attributes and child resource references” and the Filter Criteria level was 2.

The ch member is an array containing references to the child resources. Note the use of the special short name val to hold the reference itself, as specified by clause 8.4.2, rule 10.

{ 
 "m2m:ae": { 
   "rn": "appname", 
   "aei": "CAE01", 
   "ct": "20160404T132648", 
   "et": "20160408T004648", 
   "lt": "20160404T132648", 
   "pi": "ONET-CSE-02", 
   "ri": "REQID1", 
   "ty": 2,
   "ch": [{"nm":"container1", "typ":3,  "val":"mn-cse/appname/container1"},
          {"nm":"container2", "typ":3,  "val":"mn-cse/appname/container2"},
 		  {"nm":"sub1", "typ":23, "val":"mn-cse/appname/container2/sub1"}] 
 } 
}

EXAMPLE 2 ends.

EXAMPLE 3 starts:

The third example shows the same <AE> resource, but this time shows what would have been returned if the Result Content parameter in the request had been set to "attributes and child resources".

The child resources are serialized inline, using the shortnames from short names from Table 8.2.4-1. The child resources are nested according to their parent-child relationship, so the subscription resource (sub1) appears nested inside its parent (container2).

Since the inlined resources have XML Schema global element definitions they appear in the JSON with the prefix m2m: as required by clause 8.4.2, rule 3. As there can be more than one occurrence of each child resource type, they are serialized as JSON arrays as required by clause 8.4.2, rule 11.

For brevity this example does not show all the attributes of the child resources.

{ 
 "m2m:ae": { 
   "rn": "appname", 
   "aei": "CAE01", 
   "ct": "20160404T132648", 
   "et": "20160408T004648", 
   "lt": "20160404T132648", 
   "pi": "ONET-CSE-02", 
   "ri": "REQID1", 
   "ty": 2,
   "m2m:cnt":[{"rn":"container1", "ty":3,  …},
              {"rn":"container2", "ty":3,  … ,
 	 		   "m2m:sub":[{"rn":"sub1", "ty":23, …}]}

]
  } 
}

EXAMPLE 3 ends.


## 8.5	CBOR serialization



### 8.5.1	Method


Concise Binary Object Representation (CBOR) is a binary serialization format of structured data specified in IETF RFC 7049 [39]. CBOR provides unambiguous encoding of structured data into a binary representation and reverse decoding.

The specifics on how CBOR can be negotiated between protocol endpoints is protocol specific and defined by the individual bindings.

This clause defines the relationship between JSON objects as defined in clause 8.4 and CBOR representations.

Section 2 of IETF RFC 7049 [39] specifies the applicable CBOR encoding rules.

In particular, the following rules shall apply when using CBOR serialization:

Text strings (i.e. any names/keys and text string values) shall be encoded as UTF-8 strings, CBOR major type 3.

Integer numbers shall be encoded as CBOR major types 0 or 1.

Floating point numbers shall be encoded as CBOR major type 7 with Additional Information 26 for single precision (32-bit) and Additional Information 27 for double precision (64-bit) formats.

Note that CBOR ignores whitespace characters (including space, LF/CR) if used for formatting of JSON objects in textual representations.

If decoding of CBOR serializations results in JSON objects with member names or values not compliant with the underlying XSD, this shall be interpreted as an error by the receiver of the primitive.


### 8.5.2	Examples


This clause presents some examples of CBOR serialized primitives. Note that due to given encoding options, a CBOR encoder may produce somewhat different binary serializations. However, in any case the CBOR decoding shall produce an equivalent representation in JSON format as shown in the examples below.

EXAMPLE 1:

JSON representation (a request primitive of message length: 160 bytes):

{"op":1,"to":"//example.net/mncse1234","rqi":"A1000", "rcn":7,"pc":{"m2m:ae":{"rn":"SmartHomeApplication", "api":"Na56", "apn":"app1234"}},"ty":2}

CBOR representation as sequence of hexadecimal characters (length: 108 bytes):

a6427063a1466d326d3a6165a342726e54536d617274486f6d654170706c69636174696f6e43617069444e6135364361706e47617070313233344274790242746f572f2f6578616d706c652e6e65742f6d6e637365313233344372636e07426f700143727169454131303030

EXAMPLE 2:

JSON representation (a response primitive of message length: 266 bytes):

{"rsc":2001,"rqi":"A1000","pc":{"m2m:ae":{"rn":"SmartHomeApplication","ty":2,"ri":"ae1","api":"Na56","apn":"app1234","pi":"cb1","ct":"20160506T153208", "lt":"20160506T153208","acpi":["acp1","acp2"],"et":"20180506T153208", "aei":"S_SAH25"}}}

CBOR representation as sequence of hexadecimal characters (length: 178 bytes):

a3427063a1466d326d3a6165ab43617069444e6135364361706e47617070313233344265744f3230313830353036543135333230384263744f323031363035303654313533323038427479024272694616531426c744f3230313630353036543135333230384361656947535f534148323542726e54536d617274486f6d654170706c69636174696f6e427069436362314461637069824461637031446163703243727169454131303030437273631907d1

EXAMPLE 3:

JSON representation (request primitive of message length: 174 bytes):

{"op":1,"to":"//example.net/mncse1234/SmartHomeApplication", "rqi":"A1001","rcn":7,"pc":{"m2m:cnt":{"rn":"SmartHomeContainer","mbs":100000, "mni":500}},"ty":3}

CBOR representation as sequence of hexadecimal characters (length: 124 bytes):

a6427063a1476d326d3a636e74a3436d6e691901f442726e52536d617274486f6d65436f6e7461696e6572436d62731a000186a04274790342746f582c2f2f6578616d706c652e6e65742f6d6e637365313233342f536d617274486f6d654170706c69636174696f6e4372636e07426f700143727169454131303031

EXAMPLE 4:

JSON representation (response primitive of message length: 393 bytes):

{"rsc":2001,"rqi":"A1001","pc":{"m2m:cnt":{"rn":"SmartHomeContainer", "ty":3,"ri":"cnt1","pi":"ae1","ct":"20160506T154048", "lt":"20160506T154048","acpi":["acp1"],"et":"20180506T154048","cr":" S_SAH25","st":0,"mni":500,"mbs":100000,"cni":0,"cbs":0,"mia":3600}}}

CBOR representation as sequence of hexadecimal characters (length: 188 bytes):

a3427063a1476d326d3a636e74af436362730042726944636e7431436d6e691901f442637247535f53414832354265744f3230313830353036543135343034384263744f323031363035303654313534303438436d62731a000186a042747903436d6961190e1042737400426c744f32303136303530365431353430343842726e52536d617274486f6d65436f6e7461696e657242706943616531446163706981446163703143636e690043727169454131303031437273631907d1


# 9	Mcn procedure



## 9.1	Introduction


The following clauses describe procedural details and message format bindings for various Mcn procedures.


## 9.2	Triggering



### 9.2.1	Introduction


A trigger originator (i.e. IN-CSE) may send a trigger request to an underlying network that addresses a trigger recipient (i.e. ASN/MN-CSE or an ADN-AE). A trigger request may include a payload. If the trigger has no payload, the trigger recipient shall just re-establish a network connection, so that the trigger originator can send requests to the trigger recipient. If the request contains a payload, the trigger recipient shall re-establish the network connection and perform additional actions as requested by the payload. The trigger payload fields are described in Table 9.2.1-1.

Table 9.2.1-1: Trigger payload short names and field descriptions

NOTE:	Mandatory payload fields are only mandatory if the trigger payload is present.

The trigger payload may be serialized in XML, JSON or CBOR format. The IN-CSE shall serialize the trigger payload based on the contentSerialization attribute of the trigger recipient's <AE> or <remoteCSE> resource. If the trigger recipient has not yet registered to the IN-CSE, and the contentSerialization attribute of the trigger recipient's <AE> or <remoteCSE> resource is not available to the IN_CSE, the IN-CSE may use any of the supported serialization formats.

Annex A (normative):
Binding Mch to Diameter for Charging


# A.1	Introduction


The present clause provides Diameter binding of Mch.


# A.2	Diameter Commands on Mch



## A.2.1	Accounting Request Command


The ACR command is sent from the Charging Function (CHF included within the SCA CSF) embedded within the M2M IN to the Charging Server using the Mch reference point. This command is used for Event Based requests.

The ACR message format is defined according to the Diameter Base Protocol in IETF RFC 6733 [14] as follows:

<ACR> ::= < Diameter Header: 271, REQ, PXY >

< Session-Id >

{ Origin-Host }

{ Origin-Realm }

{ Destination-Realm }

{ Accounting-Record-Type }

{ Accounting-Record-Number }

[ Acct-Application-Id ]
          [ Vendor-Specific-Application-Id ]

[ User-Name ]

[ Destination-Host ]

[ Accounting-Sub-Session-Id ]

[ Acct-Session-Id ]

[ Acct-Multi-Session-Id ]

[ Acct-Interim-Interval ]

[ Accounting-Realtime-Required ]

[ Origin-State-Id ]

[ Event-Timestamp ]

* [ Proxy-Info ]

* [ Route-Record ]

* [ AVP ]


## A.2.2	Accounting Answer Command


The ACA command is sent from the Charging Server to the Charging Function (CHF included within the SCA CSF) embedded within the M2M IN in response to the ACR command and is used to acknowledge reception of the charging data. This command is used for Event Based responses.

The ACA message format is defined according to the Diameter Base Protocol in IETF RFC 6733 [14] as follows:

<ACA> ::= < Diameter Header: 271, PXY >

< Session-Id >

{ Result-Code }

{ Origin-Host }

{ Origin-Realm }

{ Accounting-Record-Type }

{ Accounting-Record-Number }

[ Acct-Application-Id ]
          [ Vendor-Specific-Application-Id ]

[ User-Name ]

[ Accounting-Sub-Session-Id ]

[ Acct-Session-Id ]

[ Acct-Multi-Session-Id ]

[ Error-Message ]

[ Error-Reporting-Host ]

[ Failed-AVP ]

[ Acct-Interim-Interval ]

[ Accounting-Realtime-Required ]

[ Origin-State-Id ]

[ Event-Timestamp ]

* [ Proxy-Info ]

* [ AVP ]


# A.3	Mapping of M2M Recorded Information Elements to AVPs


Table A.3-1 describes the mapping of the M2M Recorded Information Elements identified in oneM2M TS-0001 [6] to the Diameter AVPs.

Table A.3-1: Mapping of Recorded M2M Information Elements to Diameter AVPs


# A.4	Summary of AVPs used


Table A.4-1 lists the Diameter AVPs specifically used for the offline charging interface.

In Table A.4-1, columns "Used in ACR" and "Used in ACA" identify at a protocol level if the AVP is mandatory, optional, or not allowed. When identified as optional here, an AVP may be considered mandatory for certain conditions as identified in Table 12.1.2.2-1 of oneM2M TS-0001 [6].

AVPs defined for oneM2M specific usage are assigned Vendor-Id of 45687. The formats and usage of oneM2M specific AVPs are defined in the present document in clause A.5.

The table contains the following information:

AVP Name: The name used in Diameter.

AVP Vendor ID: The entity defining the AVP code in the next column.

AVP Code: The AVP Code used in the Diameter AVP Header.

Used in ACR: Indicates if it is mandatory, optional or not used in the ACR command.

Used in ACA: Indicates if it is mandatory, optional or not used in the ACA command.

Used in CCR: Not in the present document.

Used in CCA: Not in the present document.

AVP Defined: A reference to where this AVP is defined.

Value Type: The Diameter format of the AVP data as defined in Basic or Derived AVP Data Format.

AVP Flag Rules: The rules for how the AVP Flags in the AVP Header may be set.

May Encrypt: Indicates if the AVP may be encrypted or not.

Table A.4-1: Use Of Diameter AVPs


# A.5	oneM2M Specific AVP Usage



## A.5.1	Access-Network-Identifier AVP


The Access-Network-Identifier AVP (AVP Code 1000) is of type Unsigned32 and identifies the access network associated with the request triggering the M2M Event Record. The IN-CSE detects the link on which a request came from or was sent to and that link maps to a specific Network and locally configured identifier.


## A.5.2	Acct-Application-Id AVP


Since the protocol used on Mch is Diameter Accounting, this AVP shall contain the value of 3 as defined in IETF RFC 6733 [14].


## A.5.3	Accounting-Record-Type AVP


The Accounting-Record-Type AVP (AVP Code 480) is of type Enumerated and contains the type of accounting record being sent. The following value is currently defined for the Accounting-Record-Type AVP: EVENT_RECORD (value 1) for an Event Based request.


## A.5.4	Application-Entity-ID AVP


The Application-Entity-ID AVP (AVP Code 1001) is of type UTF8String and represents the identity of the M2M Application Entity when it is applicable. The format of the AE-ID is specified in clause 6.2.3.


## A.5.5	Control-Memory-Size AVP


The Control-Memory-Size AVP (AVP Code 1002) is of type Unsigned32 and represents the storage memory (in bytes) used to store control related information associated with the M2M event record (excludes data storage associated with container related operations).


## A.5.6	Current-Number-Members AVP


The Current-Number-Members AVP (AVP Code 1003) is of type Unsigned32 and represents the current number of members in a group as determined by the responses to a request transmitted to a group. This is the same as the attribute "currentNrOfMembers" for the group as described in Table 7.4.13.1-3.


## A.5.7	Data-Memory-Size AVP


The Data-Memory-Size AVP (AVP Code 1004) is of type Unsigned32 and represents the storage memory in bytes, where applicable, to store data associated with container related operations.


## A.5.8	External-ID AVP


The External-ID AVP (AVP Code 1005) is of type UTF8String and contains the external ID used to communicate over Mcn where applicable. The format is the same as the M2M-Ext-ID in clause 6.2 Addressing.


## A.5.9	Group-Name AVP


The Group-Name AVP (AVP Code 1006) is of type UTF8String and identifies the group associated with a request. It shall be included when the IN initiates a fanning operation. This is the same as the attribute "groupName" for the group as described in Table 7.4.13.1-3.


## A.5.10	Hosting-CSE-ID AVP


The Hosting-CSE-ID AVP (AVP Code 1007) is of type UTF8String and represents the identity of the Hosting CSE for the request in case the receiver is not the host. The format of the CSE-ID is specified in clause 6.2.3.


## A.5.11	Originator AVP


The Originator AVP (AVP Code 1008) is of type UTF8String and identifies the originator (i.e. from party) of the M2M request. This can be any M2M Node with format as per clause 6.2.3.


## A.5.12	Maximum-Number-Members AVP


The Maximum-Number-Members AVP (AVP Code 1009) is of type Unsigned32 and represents the maximum number of members of the group for the Create and Update operations. This is the same as the attribute "maxNrOfMembers" for the group as described in Table 7.4.13.1-3.


## A.5.13	M2M-Event-Record-Timestamp AVP


The M2M-Event-Record-Timestamp AVP (AVP code 1010) is of type Time and represents the time for recording the M2M event record.


## A.5.14	M2M-Information AVP


The M2M-Information AVP (AVP code 1011) is of type Grouped. Its purpose is to allow the transmission of service information elements used for OneM2M specific charging.

It has the following ABNF grammar:

M2M-Information :: =  < AVP Header: 1011>

[ Application-Entity-ID ]

[ External-ID ]

[ Receiver ]

[ Originator ]

[ Hosting-CSE-ID ]

[ Target-ID ]

[ Protocol-Type ]

[ Request-Operation ]

[ Request-Headers-Size ]

[ Request-Body-Size ]

[ Response-Headers-Size ]

[ Response-Body-Size ]

[ Response-Status-Code ]

[ Rating-Group ]

[ M2M-Event-Record-Timestamp ]

[ Control-Memory-Size ]

[ Data-Memory-Size ]

[ Access-Network-Identifier ]

[ Occupancy ]

[ Group-Name ]

[ Maximum-Number-Members ]

[ Current-Number-Members ]

[ Subgroup-Name ][ Node-Id ]

* [ AVP ]


## A.5.15	Node-ID AVP


The Node-Id AVP (AVP Code 2064) is of type UTF8String and includes an optional, operator configurable identifier string for the node generating the Accounting-Record-Number for the Diameter ACR.


## A.5.16	Occupancy AVP


The Occupancy AVP (AVP Code 1012) is of type Unsigned32 and represents the overall size (in bytes) of the containers generated by a set of AEs identified by the M2M Service Subscription Identifier.


## A.5.17	Protocol-Type AVP


The Protocol-Type AVP (AVP Code 1013) is of type Enumerated and indicates the protocol used for the request. The values are given below:

0	HTTP

1	CoAP

2	MQTT

3	WebSocket

4 .. 99	Reserved for oneM2M defined protocol types

100 .. 199	Operator and vendor specific protocol types


## A.5.18	Rating-Group AVP


The Rating-Group AVP (AVP Code 432) is of type Unsigned32 and represents a classification of M2M event records for charging purposes. This is assigned by the IN and is M2M SP specific.


## A.5.19	Receiver AVP


The Receiver AVP (AVP Code 1014) is of type UTF8String and identifies the receiver (i.e. to party) of the M2M request. This can be any M2M Node with format as per clause 6.2.3.


## A.5.20	Request-Body-Size AVP


The Request-Body-Size AVP (AVP Code 1015) is of type Unsigned32 and represents the number of bytes of the body transported in the Request.


## A.5.21	Request-Headers-Size AVP


The Request-Headers-Size AVP (AVP Code 1016) is of type Unsigned32 and represents the number of bytes in the control information header in the Request.


## A.5.22	Request-Operation AVP


The Request-Operation AVP (AVP Code 1017) is of type Enumerated and identifies the type of operation requested. The values are defined in Table 6.3.4.2.5-1.


## A.5.23	Response-Body-Size AVP


The Response-Body-Size AVP (AVP Code 1018) is of type Unsigned32 and represents the number of bytes of the body transported in the Response.


## A.5.24	Response-Headers-Size AVP


The Response-Headers-Size AVP (AVP Code 1019) is of type Unsigned32 and represents the number of bytes in the control information header in the Response.


## A.5.25	Response-Status-Code AVP


The Response-Status-Code AVP (AVP Code 1020) is of type Enumerated and identifies the value of returned in the Response Status Code parameter of the Response. The values are defined in clause 6.6.3.


## A.5.26	Service-Context-Id AVP


This AVP is of type UTF8String and contains a unique identifier of the Diameter charging specific document that applies the request. This is an identifier allocated by the service provider, by the service element manufacturer, or by a standardization body, and shall uniquely identify a given Diameter charging specific document.

The format of the Service-Context-Id is:

"extensions"."Release"."service-context" "@" "domain"

The OneM2M specific values "service-context" "@" "domain" are:

ts0004@oneM2M.org for OneM2M charging

The "Release" indicates the OneM2M Release the service specific document is based upon e.g. 1 for Release 1.

The "extensions" is operator specific information to any extensions in a service specific document.


## A.5.27	Service-Information AVP


The Service-Information AVP (AVP code 873) is of type Grouped. Its purpose is to allow the transmission of additional OneM2M specific information elements.

The complete ABNF syntax is defined and maintained in 3GPP TS 32.299 [31]. The group structure includes zero or more occurrences of the Subscription-Id AVP and the M2M-Information AVP.

The format and content of the M2M-Information AVP which includes the OneM2M specific AVPs are specified in the present document.


## A.5.28	Subgroup-Name AVP


The Subgroup-Name AVP (AVP Code 1021) is of type UTF8String and identifies the subgroup associated with a request. It shall be included when the IN initiates a fanning operation and one of the members of the group is a. This is the same as the attribute "groupName" for the subgroup as described in Table 7.4.13.1-3.


## A.5.29	Subscription-Id AVP


The Subscription-Id AVP (AVP Code 443) is of type Grouped with structure defined in IETF RFC 4006 [32]. The Subscription-Id AVP includes a Subscription-Id-Data AVP that holds the identifier and a Subscription-Id-Type AVP that defines the identifier type.

For M2M, this identifies the M2M Service Subscription ID associated with the request. This is determined by association maintained by the M2M SP as per clause 12.1.3 in oneM2M TS-0001 [6].


## A.5.30	Subscription-Id-Data AVP


The Subscription-Id-Data AVP (AVP Code 444) is of type UTF8String as defined in IETF RFC 4006 [32]. The Subscription-Id-Data is used to identify the M2M Service Subscription. The Subscription-Id-Type AVP defines which type of identifier is used.


## A.5.31	Subscription-Id-Type AVP


The Subscription-Id-Type AVP (AVP Code 450) is of type Enumerated as defined in IETF RFC 4006 [32]. It is used to determine which type of identifier is carried by the Subscription-Id AVP. The type(s) to be supported is(are) determined by the M2M SP.


## A.5.32	Target-ID AVP


The Target-ID AVP (AVP Code 1022) is of type UTF8String and identifies the target URL for the M2M request if available.

Alternatively the Target-ID AVP can identify the target resource identifier with format defined in clause 6.3.4.

Annex B (normative):
3GPPTM  MTC Interworking Device triggering

Refer to oneM2M TS-0026 3GPP Interworking [43].

Annex C (informative):
XML examples


# C.1	XML schema for container resource type


<?xml version="1.0" encoding="UTF-8"?>
<!-- 
Copyright Notification


The oneM2M Partners authorize you to copy this document, or any components thereof, provided that you retain all copyright and other proprietary notices 
contained in the original materials on any copies of the materials and that you comply strictly with these terms. 
This copyright permission does not constitute an endorsement of the products or services, nor does it encompass the granting of 
any patent rights. The oneM2M Partners assume no responsibility for errors or omissions in this document. 
© 2021, oneM2M Partners Type 1 (ARIB, ATIS, CCSA, ETSI, TIA, TSDSI, TTA, TTC). All rights reserved.

Notice of Disclaimer & Limitation of Liability 

The information provided in this document is directed solely to professionals who have the appropriate degree of experience 
to understand and interpret its contents in accordance with generally accepted engineering or other professional standards 
and applicable regulations. No recommendation as to products or vendors is made or should be implied. 

NO REPRESENTATION OR WARRANTY IS MADE THAT THE INFORMATION IS TECHNICALLY ACCURATE OR SUFFICIENT OR CONFORMS TO ANY STATUTE, 
GOVERNMENTAL RULE OR REGULATION, AND FURTHER, NO REPRESENTATION OR WARRANTY IS MADE OF MERCHANTABILITY OR FITNESS FOR ANY 
PARTICULAR PURPOSE OR AGAINST INFRINGEMENT OF INTELLECTUAL PROPERTY RIGHTS. 
NO oneM2M PARTNER TYPE 1 SHALL BE LIABLE, BEYOND THE AMOUNT OF ANY SUM RECEIVED IN PAYMENT BY THAT PARTNER FOR THIS DOCUMENT, 
WITH RESPECT TO ANY CLAIM, AND IN NO EVENT SHALL oneM2M BE LIABLE FOR LOST PROFITS OR OTHER INCIDENTAL OR CONSEQUENTIAL DAMAGES. 
oneM2M EXPRESSLY ADVISES ANY AND ALL USE OF OR RELIANCE UPON THIS INFORMATION PROVIDED IN THIS DOCUMENT IS AT THE RISK OF THE USER.

-->
	
<xs:schema targetNamespace="http://www.onem2m.org/xml/protocols"
	xmlns:m2m="http://www.onem2m.org/xml/protocols" elementFormDefault="unqualified"
	xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<xs:include schemaLocation="CDT-commonTypes-v3_32_0.xsd"/>
	<xs:include schemaLocation="CDT-contentInstance-v3_32_0.xsd"/>
	<xs:include schemaLocation="CDT-subscription-v3_32_0.xsd"/>
	<xs:include schemaLocation="CDT-semanticDescriptor-v3_32_0.xsd"/>

<xs:include schemaLocation="CDT-timeSeries-v3_32_0.xsd"/>

<xs:include schemaLocation="CDT-transaction-v3_32_0.xsd"/>


	<xs:element name="container" substitutionGroup="m2m:sg_announceableResource">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="m2m:announceableResource">
					<xs:sequence>
						<!-- Common Attribute, specific to <container>, <contentInstance>, <request>							and <delivery> and other resources -->
						<xs:element name="stateTag" type="xs:nonNegativeInteger"/>
						<xs:element name="creator" type="m2m:ID" minOccurs="0"/>
						<!-- Resource Specific Attributes -->
						<xs:element name="maxNrOfInstances" type="xs:nonNegativeInteger"
							minOccurs="0"/>
						<xs:element name="maxByteSize" type="xs:nonNegativeInteger" minOccurs="0"/>
						<xs:element name="maxInstanceAge" type="xs:nonNegativeInteger"											minOccurs="0"/>
						<xs:element name="currentNrOfInstances" type="xs:nonNegativeInteger"/>
						<xs:element name="currentByteSize" type="xs:nonNegativeInteger"/>
						<xs:element name="locationID" type="xs:anyURI" minOccurs="0"/>
						<xs:element name="ontologyRef" type="xs:anyURI" minOccurs="0"/>
						<xs:element name="disableRetrieval" type="xs:boolean" minOccurs="0"/>

						<!-- Child Resources -->

<xs:choice minOccurs="0" maxOccurs="1">
							<xs:element name="childResource" type="m2m:childResourceRef"
								minOccurs="1" maxOccurs="unbounded"/>
							<xs:choice minOccurs="1" maxOccurs="unbounded">
								<xs:element ref="m2m:contentInstance"/>
								<xs:element ref="m2m:container"/>
								<xs:element ref="m2m:subscription"/>
								<xs:element ref="m2m:semanticDescriptor"/>

<xs:element ref="m2m:sg_flexContainerResource"/>

<xs:element ref="m2m:timeSeries"/>

<xs:element ref="m2m:transaction"/>

</xs:choice>
						</xs:choice>
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>

	<xs:element name="containerAnnc" substitutionGroup="m2m:sg_announcedResource">
		<xs:complexType>
			<xs:complexContent>
				<xs:extension base="m2m:announcedResource">
					<xs:sequence>
						<!-- Common Attribute, specific to <container>, <contentInstance>, <request>							and <delivery> resources -->
						<xs:element name="stateTag" type="xs:nonNegativeInteger"/>
						<!-- Resource Specific Attributes -->
						<xs:element name="maxNrOfInstances" type="xs:nonNegativeInteger"
							minOccurs="0"/>
						<xs:element name="maxByteSize" type="xs:nonNegativeInteger" minOccurs="0"/>
						<xs:element name="maxInstanceAge" type="xs:nonNegativeInteger"											minOccurs="0"/>
						<xs:element name="currentNrOfInstances" type="xs:nonNegativeInteger"
							minOccurs="0"/>
						<xs:element name="currentByteSize" type="xs:nonNegativeInteger"
							minOccurs="0"/>
						<xs:element name="locationID" type="xs:anyURI" minOccurs="0"/>
						<xs:element name="ontologyRef" type="xs:anyURI" minOccurs="0"/>
						<xs:element name="disableRetrieval" type="xs:boolean" minOccurs="0"/>

						<!-- Child Resources -->
						<xs:choice minOccurs="0" maxOccurs="1">
							<xs:element name="childResource" type="m2m:childResourceRef"
								minOccurs="1" maxOccurs="unbounded"/>
							<xs:choice minOccurs="1" maxOccurs="unbounded">
								<xs:element ref="m2m:contentInstance"/>
								<xs:element ref="m2m:contentInstanceAnnc"/>
								<xs:element ref="m2m:container"/>
								<xs:element ref="m2m:containerAnnc"/>
								<xs:element ref="m2m:subscription"/>
								<xs:element ref="m2m:semanticDescriptor"/>
								<xs:element ref="m2m:semanticDescriptorAnnc"/>

<xs:element ref="m2m:sg_flexContainerResource"/>

<xs:element ref="m2m:sg_announcedFlexContainerResource"/>

<xs:element ref="m2m:timeSeries"/>

<xs:element ref="m2m:timeSeriesAnnc"/>

<xs:element ref="m2m:transaction"/>
							</xs:choice>
						</xs:choice>
					</xs:sequence>
				</xs:extension>
			</xs:complexContent>
		</xs:complexType>
	</xs:element>
</xs:schema>


# C.2	Container resource that conforms to the Schema given above (see clause C.1)


<?xml version="1.0" encoding="UTF-8"?>

<m2m:container xmlns:m2m="http://www.onem2m.org/xml/protocols"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

xsi:schemaLocation=

"http://www.onem2m.org/xml/protocols CDT-container-v3_32_0.xsd"

resourceName="12xx">

<resourceType>3</resourceType>

<resourceID>96719</resourceID>

<parentID>96734</parentID>

<creationTime>20141003T112032</creationTime>

<lastModifiedTime>20141003T112032</lastModifiedTime>

<labels>label1 label2</labels>

<accessControlPolicyIDs >

//example.net/IN_CSEID/93405

</accessControlPolicyIDs/>

<expirationTime>20141130T120000</expirationTime>

<stateTag>0</stateTag>

<creator>C2345</creator>

<maxNrOfInstances>5</maxNrOfInstances>

<maxByteSize>104857600</maxByteSize>

<maxInstanceAge>3600</maxInstanceAge>

<currentNrOfInstances>2</currentNrOfInstances>

<currentByteSize>6</currentByteSize>

<locationID>//example.net/IN_CSEID/1112</locationID>

<ontologyRef>http://tempuri.org/ontologies/xyz</ontologyRef>

<childResource name="ci1234" type="4">mn-cse/12xx/ci1234</childResource>

<childResource name="ci1235" type="4">mn-cse/12xx/ci1235</childResource>

<childResource name="sub1" type="23">mn-cse/12xx/sub1</childResource>

</m2m:container>

Annex D (normative):
<mgmtObj> Resource specializations


# D.1	Introduction


The annex defines the structure and procedure for the <mgmtObj> resource specializations. The resource specializations specified in the following clauses of this annex shall be created on the IN-CSE when the management request is performed using external technology specific protocols. The IN-CSE further interacts with the management server to perform management requests towards the managed entity. If the management request is performed solely over the M2M Service Layer, the <mgmtObj> resource specializations are created on the managed entity if the managed entity is equipped with a CSE. If the managed entities are non-oneM2M Nodes, the resources are created on the MN-CSE of the managed entity. The details can be found in the oneM2M TS-0001 [6].


# D.2	Resource [firmware]



## D.2.1	Introduction


The detailed description of the [firmware] resource can be found in clause D.2 of the oneM2M TS-0001 [6].

Table D.2.1-1: Data Type Definition of [firmware]

Table D.2.1-2: Resource specific attributes of [firmware]


## D.2.2	Resource specific procedures for CRUD operations



### D.2.2.0	Introduction


When management is performed using technology specific protocols, the procedures defined in clause 7.4.15.2 <mgmtObj> specific procedures shall be used. The following clauses define additional procedures besides the generic procedure defined in clause 7.2.2.


### D.2.2.1	Create


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific step after generic procedure defined in clause 7.2.2.2.

May start to download the firmware image from the location indicated by attribute URL in the firmware resource.


### D.2.2.2	Update


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operations to be performed after Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed":

If the attribute update is present in the request and set to true, download the new firmware image from the address indicated by attribute URL of the firmware resource if it is not already downloaded else use the downloaded firmware image to update the current using firmware. The Receiver may need to update the fwVersion attribute of the [deviceInfo] resource.


### D.2.2.3	Retrieve


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.2.2.4	Delete


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific step after generic procedure defined in clause 7.2.2.2:

Delete the downloaded firmware image locally.


# D.3	Resource [software]



## D.3.1	Introduction


The detailed description of the [software] resource can be found in clause D.3 of oneM2M TS-0001 [6].

Table D.3.1-1: Data Type Definition of [software]

Table D.3.1-2: Resource specific attributes of [software]


## D.3.2	Resource specific procedures for CRUD operations



### D.3.2.0	Introduction


When management is performed using technology specific protocols, the procedures defined in clause 7.4.15.2 <mgmtObj> resource specific procedures shall be used. The following clauses define additional procedures besides the generic procedure defined in clause 7.2.2.


### D.3.2.1	Create


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.

May start the download of the software package from the location indicated by the URL attribute in the software resource.


### D.3.2.2	Update


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operations to be performed after Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed":

If the attribute install is present in the request and set to true, install the new software package downloaded from the address indicated by attribute URL of the [software] resource.

When the attribute uninstall of the [software] resource is updated to true, uninstall the corresponding software of the [software] resource.

When the attribute install and uninstall of the [software] resource are simultaneously set to true in request, the CSE shall reject the request with a Response Status Code indicating "BAD_REQUEST" error.

When the attribute activate of the [software] resource is updated to true, activate the corresponding software of the [software] resource.

When the attribute deactivate of the [software] resource is updated to true, deactivate the corresponding software of the [software] resource.

When the attribute activate and deactivate of the [software] resource are simultaneously set to true in request, the CSE shall reject the request with a Response Status Code indicating "BAD_REQUEST" error.

The Receiver may need to update the swVersion attribute of the [deviceInfo] resource.


### D.3.2.3	Retrieve


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.3.2.4	Delete


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific step after generic procedure defined in clause 7.2.2.2.

Delete the downloaded software package locally.


# D.4	Resource [memory]



## D.4.1	Introduction


The detailed description of the [memory] resource can be found in clause D.4 of oneM2M TS-0001 [6].

Table D.4.1-1: Data Type Definition of [memory]

Table D.4.1-2: Resource specific attributes of [memory]


## D.4.2	Resource specific procedures for CRUD operations



### D.4.2.0	Introduction


When management is performed using technology specific protocols, the procedures defined in clause 7.4.15.2 <mgmtObj> specific procedures shall be used. The following clauses define additional procedures besides the generic procedure defined in clause 7.2.2.


### D.4.2.1	Create


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.4.2.2	Update


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.4.2.3	Retrieve


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.4.2.4	Delete


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


# D.5	Resource [areaNwkInfo]



## D.5.1	Introduction


The detailed description of the [areaNwkInfo] resource can be found in clause D.5 of oneM2M TS-0001 [6].

Table D.5.1-1: Data Type Definition of [areaNwkInfo]

Table D.5.1-2: Resource specific attributes of [areaNwkInfo]


## D.5.2	Resource specific procedures for CRUD operations



### D.5.2.0	Introduction


When management is performed using technology specific protocols, the procedures defined in clause 7.4.15.2 <mgmtObj> specific procedures shall be used. The following clauses define additional procedures besides the generic procedure defined in clause 7.2.2.


### D.5.2.1	Create


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.5.2.2	Update


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.5.2.3	Retrieve


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.5.2.4	Delete


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


# D.6	Resource [areaNwkDeviceInfo]



## D.6.1	Introduction


The detailed description of the [areaNwkDeviceInfo] resource can be found in clause D.6 of oneM2M TS-0001 [6].

Table D.6.1-1: Data Type Definition of [areaNwkDeviceInfo]

Table D.6.1-2: Resource specific attributes of [areaNwkDeviceInfo]


## D.6.2	Resource specific procedures for CRUD operations



### D.6.2.0	Introduction


When management is performed using technology specific protocols, the procedures defined in clause 7.4.15.2 <mgmtObj> specific procedures shall be used. The following clauses define additional procedures besides the generic procedure defined in clause 7.2.2.


### D.6.2.1	Create


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation additional to Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed".

When the [areaNwkDeviceInfo] is successfully created, the receiver shall update the [areaNwkInfo] resource corresponding to the areaNwkId attribute provided in [areaNwkDeviceInfo]. The receiver shall update this [areaNwkInfo] by adding the resourceID of the [areaNwkDeviceInfo] to the listOfDevices attribute.


### D.6.2.2	Update


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation additional to Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed":

When the attribute listOfNeighbors of the [areaNwkDeviceInfo] resource is updated, the receiver shall modify the corresponding connection relationship among devices in the M2M Area Network by sending signals to non-oneM2M Nodes which is out of scope of oneM2M. According to the response from the non-oneM2M nodes of the modify signal, the receiver shall corresponding update the [areaNwkDeviceInfo] resource which may include the update of the listOfNeighbors and the devType attribute. The modification may include change of the attach point of the device or removal from the area network.


### D.6.2.3	Retrieve


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.6.2.4	Delete


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation additional to Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed":

When the [areaNwkDeviceInfo] is successfully deleted, the receiver shall update the [areaNwkInfo] resource corresponding to the areaNwkId attribute that was in [areaNwkDeviceInfo]. The receiver shall update this [areaNwkInfo] by removing the resourceID of the [areaNwkDeviceInfo] from its listOfDevices attribute.


# D.7	Resource [battery]



## D.7.1	Introduction


The detailed description of the [battery] resource can be found in clause D.7 of oneM2M TS-0001 [6].

Table D.7.1-1: Data Type Definition of [battery]

Table D.7.1-2: Resource specific attributes of [battery]


## D.7.2	Resource specific procedures for CRUD operations



### D.7.2.0	Introduction


When management is performed using technology specific protocols, the procedures defined in clause 7.4.15.2 <mgmtObj> specific procedures shall be used. The following clauses define additional procedures besides the generic procedure defined in clause 7.2.2.


### D.7.2.1	Create


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.7.2.2	Update


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.7.2.3	Retrieve


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.7.2.4	Delete


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


# D.8	Resource [deviceInfo]



## D.8.1	Introduction


The resource [deviceInfo] is used to provide information regarding the device.

The detailed description of the [deviceInfo] resource can be found in clause D.8 of oneM2M TS-0001 [6].

Table D.8.1-1: Data Type Definition of [deviceInfo]

Table D.8.1-2: Resource specific attributes of [deviceInfo]


## D.8.2	Resource specific procedures for CRUD operations



### D.8.2.0	Introduction


When management is performed using technology specific protocols, the procedures defined in clause 7.4.15.2 <mgmtObj> specific procedures shall be used. The following clauses define additional procedures besides the generic procedure defined in clause 7.2.2.


### D.8.2.1	Create


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.8.2.2	Update


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.8.2.3	Retrieve


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.8.2.4	Delete


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


# D.9	Resource [deviceCapability]



## D.9.1	Introduction


The resource [deviceCapability] is used to provide information regarding the device.

The detailed description of the [deviceCapability] resource can be found in clause D.9 of oneM2M TS-0001 [6].

Table D.9.1-1: Data Type Definition of [deviceCapability]

Table D.9.1-2: Resource specific attributes of [deviceCapability]


## D.9.2	Resource specific procedures for CRUD operations



### D.9.2.1	Introduction


When management is performed using technology specific protocols, the procedures defined in clause 7.4.15.2 <mgmtObj> specific procedures shall be used. The following clauses define additional procedures besides the generic procedure defined in clause 7.2.2.


### D.9.2.2	Create


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.9.2.3	Update


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation additional to Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed":

When the attribute enable of the [deviceCapability] resource is updated to true, enable the device capability of the [deviceCapability] resource.

When the attribute disable of the [deviceCapability] resource is updated to true, disable the device capability of the [deviceCapability] resource.

When the attribute enable and disable of the [deviceCapability] resource are simultaneously set to true in request, the CSE shall reject the request with a Response Status Code indicating "BAD_REQUEST" error.


### D.9.2.4	Retrieve


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.9.2.5	Delete


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


# D.10	Resource [reboot]



## D.10.1	Introduction


The resource [reboot] is used to provide information regarding the device.

The detailed description of the [reboot] resource can be found in clause D.10 of oneM2M TS-0001 [6].

Table D.10.1-1: Data Type Definition of [reboot]

Table D.10.1-2: Resource specific attributes of [reboot]


## D.10.2	Resource specific procedures for CRUD operations



### D.10.2.0	Introduction


When management is performed using technology specific protocols, the procedures defined in clause 7.4.15.2 <mgmtObj> specific procedures shall be used. The following clauses define additional procedures besides the generic procedure defined in clause 7.2.2.


### D.10.2.1	Create


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.10.2.2	Update


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation additional to Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed":

When the attribute reboot of the [reboot] resource is updated to true, reboot the corresponding node.

When the attribute factoryReset of the [reboot] resource is updated to true, factory reset the corresponding node shall be applied.

When the attribute reboot and factoryReset of the [reboot] resource are simultaneously set to true in request, the CSE shall reject the request with a Response Status Code indicating "BAD_REQUEST" error.


### D.10.2.3	Retrieve


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.10.2.4	Delete


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


# D.11	Resource [eventLog]



## D.11.1	Introduction


The Resource [eventLog] is used to provide information regarding the device.

The detailed description of the [eventLog] resource can be found in clause D.11 of oneM2M TS-0001 [6].

Table D.11.1-1: Data Type Definition of [eventLog]

Table D.11.1-2: Resource specific attributes of [eventLog]


## D.11.2	Resource specific procedures for CRUD operations



### D.11.2.0	Introduction


When management is performed using technology specific protocols, the procedures defined in clause 7.4.15.2 <mgmtObj> specific procedures shall be used. The following clauses define additional procedures besides the generic procedure defined in clause 7.2.2.


### D.11.2.1	Create


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.11.2.2	Update


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

Primitive specific operation additional to Recv-6.5 "Create/Update/Retrieve/Delete/Notify operation is performed":

When the attribute logStart of the [eventLog] resource is updated to true, start the logging.

When the attribute logStop of the [eventLog] resource is updated to true, stop the logging.

When the attribute logStart and logStop of the [eventLog] resource are simultaneously set to true in request, the CSE shall reject the request with a Response Status Code indicating "BAD_REQUEST" error.


### D.11.2.3	Retrieve


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


### D.11.2.4	Delete


Originator:

No change from the generic procedures in clause 7.2.2.1.

Receiver:

No change from the generic procedures in clause 7.2.2.2.


# D.12	Resource [cmdhPolicy]



## D.12.1	Introduction


The resource [cmdhPolicy] represents a set of rules associated with a specific CSE that govern the behaviour of that CSE regarding rejecting, buffering and sending request or response messages via the Mcc reference point.

The detailed description can be found in clause D.12 of oneM2M TS-0001 [6].

Table D.12.1-1: Data Type Definition of [cmdhPolicy]

Note that the optional <subscription> child resources are not used for CMDH policies.

Table D.12.1-2: Resource specific attributes of [cmdhPolicy]

The Resource Specific Procedures for CRUD Operations as specified in clause 7.4.15 for the generic <mgmtObj> resource type apply.


## D.12.2	Resource [activeCmdhPolicy]


The resource [activeCmdhPolicy] provides a link to the currently active set of CMDH policies.

The detailed description can be found in clause D.12.1 of oneM2M TS-0001 [6].

Table D.12.2-1: Data Type Definition of [activeCmdhPolicy]

Table D.12.2-2: Resource specific attributes of [activeCmdhPolicy]


## D.12.3	Resource [cmdhDefaults]


The resource [cmdhDefaults] defines which CMDH related parameters will be used by default when a request or response message contains the Event Category parameter but not any other CMDH related parameters and which default Event Category parameter shall be used when none is given in the request or response message. The detailed description can be found in clause D.12.2 of oneM2M TS-0001 [6].

Table D.12.3-1: Data Type Definition of [cmdhDefaults]

Table D.12.3-2: Resource specific attributes of [cmdhDefaults]


## D.12.4	Resource [cmdhDefEcValue]


The resource [cmdhDefEcValue] represents a default value for the Event Category parameter of an incoming request or response message. This default Event Category becomes applicable when certain conditions are matched which are defined by the other attributes of this resource. The detailed description can be found in clause D.12.3 of oneM2M TS-0001 [6].

Table D.12.4-1: Data Type Definition of [cmdhDefEcValue]

Table D.12.4-2: Resource specific attributes of [cmdhDefEcValue]


## D.12.5	Resource [cmdhEcDefParamValues]


The resource [cmdhEcDefParamValues] represents a specific set of default values for the CMDH related parameters Request Expiration Timestamp, Result Expiration Timestamp, Operational Execution Time, Result Persistence and Delivery Aggregation that are applicable for a given Event Category if these parameters are not specified in the message. The detailed description can be found in clause D.12.4 of oneM2M TS-0001 [6].

Table D.12.5-1: Data Type Definition of [cmdhEcDefParamValues]

Table D.12.5-2: Resource specific attributes of [cmdhEcDefParamValues]


## D.12.6	Resource [cmdhLimits]


The resource [cmdhLimits] represents limits for CMDH related parameter values. The detailed description can be found in clause D.12.5 of oneM2M TS-0001 [6].

Table D.12.6-1: Data Type Definition of [cmdhLimits]

Table D.12.6-2: Resource specific attributes of [cmdhLimits]


## D.12.7	Resource [cmdhNetworkAccessRules]


The resource [cmdhNetworkAccessRules] defines the usage of underlying networks for forwarding information to other CSEs during processing of CMDH-related requests in a CSE. The detailed description can be found in clause D.12.6 of oneM2M TS-0001 [6].

Table D.12.7-1: Type Definition of [cmdhNetworkAccessRules]

Table D.12.7-2: Resource specific attributes of [cmdhNetworkAccessRules]


## D.12.8	Resource [cmdhNwAccessRule]


The resource [cmdhNwAccessRule] defines limits in usage of specific underlying networks for forwarding information to other CSEs during processing of CMDH-related requests. The detailed description can be found in clause D.12.7 of oneM2M TS-0001 [6].

Table D.12.8-1: Data Type Definition of [cmdhNwAccessRule]

Table D.12.8-2: Resource specific attributes of [cmdhNwAccessRule]


## D.12.9	Resource [cmdhBuffer]


The resource [cmdhBuffer] represents limits in usage of buffers for temporarily storing information that needs to be forwarded to other CSEs during processing of CMDH-related requests in a CSE. The detailed description can be found in clause D.12.8 of oneM2M TS-0001 [6].

Table D.12.9-1: Data Type Definition of [cmdhBuffer]

Table D.12.9-2: Resource specific attributes of [cmdhBuffer]

Annex E (informative):
Procedures for accessing resources


# E.1	Accessing resources in CSEs – blocking requests


The result of a Request is sent back to the Originator as part of the Response of the Request. This communication mode could result in long blocking times.

The interaction employing blocking involves the following steps in this order:

Figure E.1-1: Blocking access to resource

The Originator sends a request to access a resource. The Response Type parameter of the request is set to 'blockingRequest'. The Response Type parameter can be omitted in this case since 'blockingRequest' is its default value.

The Hosting CSE receives the request, and it completes the requested processing of resources.

The Hosting CSE responds to Originator, the response contains the requested results in resource content, and the Response Status Code parameter of response is set to "OK".


# E.2	Accessing Resources in CSEs - non-blocking requests



## E.2.1	Non-blocking models


If the Originator chooses the Blocking mode described in clause E.1, it might have to wait a long time for a response from the Receiver. To avoid this possibility it can choose a Non-Blocking mode. In Non-blocking modes, the Receiver sends an Acknowledgement of the request, which provides a reference to the result of the requested operation. The Originator can retrieve the result at a later time.

There are two forms of Non-blocking mode: Synchronous and Asynchronous.


## E.2.2	Synchronous case


The Originator asks for non-Blocking Communication by setting the Response Type parameter of the Request to 'nonBlockingRequestSynch'. The Receiver CSE responds after acceptance with an Acknowledgement confirming, that it will process the Request further. The Receiver CSE creates a local <request> resource pertaining to the Request received and returns a reference to this created <request> resource as the Content of the acknowledgement Response. Then the Receiver needs to forward the Request to the next CSE if the Receiver CSE is not the Hosting CSE of the addressed resource. Or the Hosting CSE needs to start handling the Request if the Receiver CSE is the Hosting CSE of the addressed resource.

The Originator of the Request may retrieve the <request> resource afterwards to check on the status of its Request and to inspect the final result of the Request when this is available.

Figure E.2.2-1 illustrates the steps involved in a synchronous non-blocking interaction. In this example the Receiver CSE is the CSE that hosts the resource that is the target of the Originator's request.

Figure E.2.2-1: Non-Blocking access to resource in synchronous mode (no hop)

The originator sends a request to access a resource, setting the Response Type parameter of request to 'nonblockingRequestSynch'.

If the Receiver CSE supports non-blocking synchronous interactions (this is indicated by its support for the <request> resource), it creates an instance of the <request> resource. The requestStatus attribute of the <request> resource is set to "PENDING". Refer to Table 7.3.2.2-1 and Table 7.3.2.2-2 for other attributes.

The Hosting CSE sends a response to the Originator, the Response Status Code parameter of its response is set to "ACCEPTED", and a reference to the <request> resource is provided in the Content.

The Hosting CSE processes the resource according to the requested operation. When the requested operation has finished, the Hosting CSE will UPDATE the <request> resource, putting the results of the operation into the operationResult attribute, and updating the value of requestStatus to "COMPLETED", also the values of stateTag and lastModifiedTime.

The Originator requests to RETRIEVE the original requested results by addressing the <request> resource.

The Hosting CSE responds to Originator. The response contains the <request> resource as its Content, and the Originator can examine the <request> resource's requestStatus attribute to check that the operation has completed and retrieve its results from the operationResult attribute.

A variation of synchronous case is depicted in the following clauses. In this variation it is assumed that the addressed resource is not stored in the Registrar CSE, then the Registrar CSE needs to be a Transit CSE to forward the request to the Hosting CSE.

Figure E.2.2-2 illustrates this case.

Figure E.2.2-2: Non-Blocking access to resource in synchronous mode (one hop)

The Originator sends a request to its Registrar CSE (this is a Transit CSE, not the Hosting CSE), setting the Response Type parameter of the request to 'nonblockingRequestSynch'.

If the Transit CSE supports non-blocking synchronous interactions (this is indicated by its support for the <request> resource), it creates an instance of <request> resource. The requestStatus attribute of the <request> resource is set to "PENDING". Refer to Table 7.3.2.2-1 and Table 7.3.2.2-2 for other attributes.

The Transit CSE sends a response to the Originator, the Response Status Code parameter of its response is set to acknowledgement, and a reference to the <request> resource is provided in the Content.

The Transit CSE forwards the original request to the Hosting CSE.

If the Hosting CSE supports non-blocking synchronous interactions (this is indicated by its support for the <request> resource), it creates an instance of <request> resource. The requestStatus attribute of the <request> resource is set to "PENDING". Refer to Table 7.3.2.2-1 and Table 7.3.2.2-2 for other attributes.

The Hosting CSE sends a response to the Transit CSE, the Response Status Code parameter of its response is set to "ACCEPTED" and a reference to the <request> resource is provided in the Content.

When Transit CSE receives acknowledgment of this forwarded request, it shall update requestStatus attribute of its <request> resource to "FORWARDED". The Hosting CSE processes the resource according to the requested operation. When the requested operation has finished, the Hosting CSE will UPDATE the <request> resource, putting the results of the operation into the operationResult attribute, and updating the values of requestStatus to "COMPLETED", also the values of stateTag and lastModifiedTime.

The Transit CSE requests to RETRIEVE the original requested results by addressing the <request> resource.

The Hosting CSE sends a response to the Transit CSE. The response contains the <request> resource as its Content.

The Transit CSE UPDATEs its <request> resource, copying the operationResult from the response that it received from the Hosting CSE. It also updates the values of requestStatus, stateTag and lastModifiedTime.

The Originator requests to RETRIEVE the original requested results by addressing the <request> resource.

The Transit CSE responds to Originator. The response contains the <request> resource as its Content, and the Originator can examine the <request> resource's requestStatus attribute to check that the operation has completed and retrieve its results from the operationResult attribute.

Annex F (informative):
Guidelines for oneM2M resource type XSD

This annex contains rules to be followed when creating XML Schema Definitions (XSD files to represent the oneM2M resources). The XSD files themselves form part of the oneM2M protocol specification, but the rules used to construct them do not, hence this annex is informative.

The purpose of these rules is:

To keep a consistent style between the schemas for different resources

To keep the XSD simple

To allow individual resource schemas to be authored and maintained separately, while minimizing the risk of conflict when they are all used together

Each XSD file should include a schema element with following namespace declaration:

<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" 	
            targetNamespace="http://www.onem2m.org/xml/protocols" 
            xmlns:m2m="http://www.onem2m.org/xml/protocols"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            elementFormDefault="unqualified" attributeFormDefault="unqualified" >

This defines the prefix xs: for the XML Schema namespace, a target namespace http://www.onem2m.org/xml/protocols, and the prefix m2m: as equivalent for the target namespace. The xsi: namespace can be omitted if the resource has no nillable attributes (see below).
Locally declared elements and attributes will be unqualified (elementFormDefault and attributeFormDefault declarations are not strictly required since "unqualified" is the default value setting).

Each Resource XSD file will contain a Global Element Declaration whose name is the name of the Resource Type in accordance with oneM2M TS-0001 [6]. This means that the root element of a Resource (when represented as an XML instance) contains an m2m: (or equivalent) namespace prefix. If the Resource is announceable, the XSD file will contain a second Global Element Declaration that is used for the Announced variant of the resource. The name of that element will be formed by adding the suffix Annc to the name of the first Global Element. The XSD should not contribute anything to the m2m: namespace other than these root elements.

The root element of each resource will have a required attribute called "resourceName" which gives an identifier for that particular resource instance. A URI to the resource instance can be constructed by taking the URI of its parent and appending /<name> where <name> is the value of the resourceName attribute.

Each resource attribute of the Resource Type in accordance with TS-0001 Functional Architecture [6] is represented as a child element of the top level element. It will be declared as an element that is local to the resource that contains it, and so does not have a namespace prefix in any XML instance representation of the resource.

Each child resource will be represented as a child element of the top level element by referring to the global element definition of the child Resource (this allows the child Resource representation to be returned inline). The resource schemas will also include – as an alternative – an element called 'childResource' which is used to return a non-hierarchical URI for the associated child resource, if this has been requested. This element will have two attributes (in XSD):

type; Data type ID of instances;

name; the name of a child resource instance.

Each Resource attribute will be declared to use one of the following data types:

a)	A data type listed in clause 6.3.2 or 6.3.3.

b)	A list of one of the data types listed in clause 6.3.2 or 6.3.3. If the list type is not already included in clause 6.3.3 it may be defined inside the XSD file for the resource, but if so it will be defined as an anonymous type in the attribute declaration itself.

c)	A data type derived by restriction from one of the types listed in clause 6.3.2 or 6.3.3. This may be added to clause 6.3.3, or defined inside the XSD file for the resource, but in the latter case it will be defined as an anonymous type in the attribute declaration itself.

d)	An anonymous complex type defined as part of the attribute declaration (inside the XSD file for the resource). The complex type should only be composed out of the types listed in clause 6.3.2 or 6.3.3.

If a data type is used by more than one attribute (either in the same resource or in two different resources) it will be included in clause 6.3.3, and referenced by each attribute that uses it. Options 6b, 6c, 6d should only be used in cases where the type is only used by one attribute.

All Resource types will extend one of the XML complex types described in clause 6.5 and included in the file CDT-commonTypes-v3_32_0.xsd.

The resource-specific attributes and child resources will appear as a sequence of elements in the XSD file, with their order being determined by the order shown in the tables in clause 7.4.

Each XSD file will include an XML comment that contains a oneM2M Copyright Notification Notice of Disclaimer & Limitation of Liability, and a change history. The change history is to be filled in only after the initial release.

To enable distinction between element names used for resource attributes and their data types in the m2m: namespace, the use of identical names should be avoided. It is recommended to use the text suffix 'Type' in data type names.

EXAMPLE:	<xs:element name="status" type="m2m:statusType />

Each mgmtLink will be represented as a child element 'mgmtLink' which is used to return a non-hierarchical URI for the associated management resource. This element has two attributes (in XSD):

type; Data type ID of instances,

name; the name of a child resource instance.

Annex G (normative):
Location request


# G.1	Introduction


Location Request is a means by which a CSE requests the geographical or physical location information of a target Node to the location server located in the Underlying Network over Mcn reference point. This annex describes only the case of location request when the attribute locationSource of <locationPolicy> resource type is set to Network Based. Please see clause 7.4.10.

The specific interface used for this request depends on the capabilities of the Underlying Network and other factors. This annex provides the interfaces for location request used for the communication between the CSE and the location server.


# G.2	Location request by means of OMA-REST-NetAPI-TerminalLocation interface



## G.2.1	Introduction


This OMA REST Network API for Terminal Location specification v1.0 [28] is generally used to open up service capabilities, especially location capability, in the underlying network toward applications. This clause introduces the resources structure and procedures to handle the oneM2M-specified location request. In addition, since this OMA Network API uses only HTTP as underlying message protocol, some binding mapping are mentioned in the procedures in clause G.2.3.


## G.2.2	Resource structure of OMA NetAPI for terminal location


When a CSE needs to request the geographical or physical location information of a target CSE or AE hosted in a M2M Node toward a location server located in the Underlying Network over Mcn reference point. The CSE shall request Terminal Location Query following Procedures for Terminal Location (see clause G.2.3).

The OMA REST NetAPI for Terminal Location allows CSE to obtain information about geographical location of a terminal (e.g. Node in oneM2M TS-0001 [6]). In order to obtain location information, CSE shall use one of two services of the Terminal Location API:

request the current Terminal Location in a single query toward a Location Server;

subscribe to notifications of periodic Terminal Location updates.

Additionally, in order to track the terminal's movement in relation to the geographic area (circle), crossing in and out (more detail usage is defined in annex E of oneM2M TS-0003 [7]) it is also proposed to use a service of the Terminal Location API:

subscribe to notification of area updates.

Since oneM2M system utilizes the three services mentioned above, this clause introduces the capabilities that is related to the services from OMA REST NetAPI for Terminal Location [28].

A CSE and a Node shall act as an application and a terminal respectively as described in [28].

Figure G.2.2-1: Resource Structure defined by NetAPI for Terminal Location

The capabilities used for oneM2M system location request are 'Terminal location'. 'Periodic location notification subscriptions' and 'Area notification subscriptions'. Table G.2.2-1 describes the URL structure, data structure and mapping with CRUD operation of each resource.

Table G.2.2-1: Applicable NetAPI for Terminal Location

Based on Table G.2.2-1, three resource types, TerminalLocation, PeriodicNotificationSubscription and CircleNotificationSubscription shall be used for the location request specified in the oneM2M system. The resource types are described in the tables below. These tables also contain a column that shows the mapping to attributes in the <locationPolicy> or <accessControlPolicy> resource types. Only attributes that may be utilized by oneM2M system are described. For the detailed information, see [28].

Table G.2.2-2: Resource Type Definition - TerminalLocation

Table G.2.2-3: Resource Type Definition - PeriodicNotificationSubscription

Table G.2.2-4: Resource Type Definition – CircleNotificationSubscription


## G.2.3	Procedures for terminal location



### G.2.3.1	Request in a single query toward a location server


This procedure shows how to request and return location for a M2M Node.

Figure G.2.3.1-1: Single Query Toward Location Server

A Hosting CSE requests location for a single terminal (Node) by means of OMA REST NetAPI for terminal location API. This request message shall contain terminal address and Request URL with the address of Location Server using RETRIEVE operation.
In this step, the TerminalLocation resource type described in Table G.2.2-1 shall be used with RETRIEVE operation.

NOTE:	GET operation is used for this RETRIEVE operation.

The Location Server shall retrieve the location information of the terminal.

After the successful retrieve, the Hosting CSE receives the location information.


## G.2.4	Subscribe to notifications for periodic location updates


This procedure shows how to control subscriptions for periodic notifications about terminal location.

Figure G.2.4-1: Subscribe to Notification for Periodic Location Updates

A Hosting CSE shall create a new periodic notification subscription for obtaining location information of a terminal periodically.
In this step, the PeriodicNotificationSubscription resource type described in Table G.2.2-1 shall be used with CREATE operation.

NOTE 1:	POST operation is used for this CREATE operation.

After the successful creation of subscription, the Hosting CSE shall receive the response.

When the set up timer is expires, the location server shall notify the application of current location information.
In this step, the notification message shall be used as NOTIFY operation.

NOTE 2:	Alternatively, the Hosting CSE obtains the notifications using a Notification Channel [i.3]. This is repeated at specific frequency (periodic information) when the CSE is not reachable.

NOTE 3:	POST operation is used for this NOTIFY operation.

After the successful receiver of notification, the Hosting CSE shall send a response to the location server.

Based upon the location configuration change by the Hosting CSE, it updates an individual subscription for periodic location notification.
In this step, the PeriodicNotificationSubscription resource type described in the Table G.2.2-1 shall be used with UPDATE operation.

NOTE 4:	PUT operation is used for this UPDATE operation.


## G.2.5	Subscribe to notifications for area updates


This procedure shows how to subscribe to area update notification.

Figure G.2.5-1: Subscribe to Notification for Area Updates

A Hosting CSE shall create a new area notification subscription to track the terminal's movement in relation to the geographical area (circle), crossing in and out. In this step, the CircleNotificationSubscription resource type described in Table G.2.2-4 shall be used with CREATE operation.

NOTE 1:	POST operation is used for this CREATE operation.

After the successful creation of subscription, the Hosting CSE shall receive the response.

When the target terminal crosses in or out the specified area (circle), the location server shall notify the application of current location information. In this step, the notification message shall be used as NOTIFY operation.

NOTE 2:	Alternatively, the Hosting CSE obtains the notifications using a Notification Channel [i.3].

NOTE 3:	POST operation is used for this NOTIFY operation.

After the successful receiver of notification, the Hosting CSE shall send a response to the location server.

Based upon the location configuration change by the Hosting CSE, it updates an individual subscription for area location notification.

In this step, the CircleNotificationSubscription resource type described in Table G.2.2-4 shall be used with UPDATE operation.

NOTE 4:	PUT operation is used for this UPDATE operation.


# G.3	Location request by means of 3GPPTM  MonitoringEvent API



## G.3.1	Introduction


This 3GPP MonitoringEvent API for UE location reporting is used to expose location capabilities in the underlying network. The API interface and parameters to handle the oneM2M-specified location request is specified in clause 7.4.7 of oneM2M TS-0026 [43].

Annex H (normative):
CMDH message processing


# H.1	Pre-requisites


The scope of CMDH processing is to decide at which time and via which communication path to forward request or response messages from a receiver CSE to another CSE. A number of message parameters impact the CMDH processing. CMDH-related request message parameters are:

Event Category ('ec')

Request Expiration Timestamp ('rqet')

Result Expiration Timestamp ('rset')

Operation Execution Time ('oet')

Result Persistence ('rp')

Originating Timestamp ('ot')

Delivery Aggregation ('da')

CMDH-related response message parameters are:

Event Category ('ec'):

'ec' is needed for response messages as well since response messages can go over multiple hops and CMDH needs to know how to handle them.

Result Expiration Timestamp ('rset')

Delivery Aggregation ('da'):

When a request message was carried inside a <delivery> resource type, also the corresponding response message shall be carried in a <delivery> resource, i.e. the CSE requested to carry out an operation indicated in a request message that reached that CSE via a <delivery> resource, shall also send the response within a <delivery> resource.

The details on how those parameters impact the CMDH processing are described in clause H.2. This annex uses the short names as listed above to refer to request and response parameters.

In the following description it is assumed that the CSE behaviour for CMDH processing is governed by CMDH policies that are represented by [cmdhPolicy] resources and their child resources which are effective for the respective CSE. If legacy device management technologies are used to provision these policies, the information represented by the effective [cmdhPolicy] resources and their child resources may not be available as oneM2M defined resources on the field nodes hosting the respective CSE. This CMDH related policy information may only be available in form of managed objects specific to the used device management technology. In that case the mapping from oneM2M specified [cmdhPolicy] resources and their child resources to equivalent objects of the deployed legacy device management technology shall be used to substitute the respective information contained in [cmdhPolicy] resources and their child resources in the description below. Therefore, whenever reference to [cmdhPolicy] resources, child resources thereof or any attributes of [cmdhPolicy] resources and their children are used in the description of CMDH processing below, they shall be read as a placeholder for the equivalent objects provided by legacy device management technologies on field nodes that are provisioned with such legacy device management technologies.

For a CSE that is processing request or response messages in CMDH, exactly one set of policies represented by a [cmdhPolicy] resource shall be active, as defined by the [activeCmdhPolicy] child resource of the <node> resource that represents the node which hosts the respective CSE. In case of field nodes that are managed via legacy device management technologies, the active CMDH policy can be represented by management objects of that device management technology. For the sake of simplicity, the term 'active [cmdhPolicy]' is used in this and the following clauses to refer to the active CMDH policy information even if no oneM2M specified resources are used to represent CMDH policies. Before any provisioning of CMDH policies has occurred, the 'active [cmdhPolicy]' and its corresponding managed objects defined for legacy device management technologies shall contain the specified default values as described in the [cmdhPolicy] specific procedures and procedures specific for all its child resources. For that reason, it can be assumed that information for an 'active [cmdhPolicy]' is always present on a CMDH capable CSE.

In addition, the active [cmdhPolicy] can have at least one or more [cmdhLimits] child resources and the active [cmdhPolicy] Hosting CSE shall lookup all [cmdhLimits] child resources. If the attribute requestContextNotification of any of found [cmdhLimits] resources is present and set to true, the CSE shall establish a subscription to the dynamic context information of the CSE defined in requestContext attribute of the found [cmdhLimits] as well as subscription to this [cmdhLimits] resource for all AEs corresponding to the AE-ID or an App-ID appearing in the requestOrigin attribute. The subscription(s) shall be established when the [cmdhPolicy] is provisioned or pre-provisioned and any of found [cmdhLimits] child resource has the attribute requestContextNotification that is set to true. Hence, both this policy establishment and changes of the context information and the [cmdhLimits] resource shall be notified to the respective AEs and the notification shall contain the limits for CMDH related parameter values defined in [cmdhLimits], context information and subscription reference ID. After this, the AEs which received the notification shall send only allowed 'ec' messages if 'ec' is specified by the AEs.


# H.2	CMDH processing: processing request or response messages requiring the receiver CSE to forward information to another CSE



## H.2.1	Applicability of CMDH processing


If a request or response message that is targeting an entity or a resource in the 'to' parameter that is not among any of:

the receiver CSE itself;

an AE registered with the receiver CSE;

a resource hosted on the receiver CSE,

and if the message is not a response message with an acknowledgement response code, the receiver CSE of that message needs to forward the message to another CSE via CMDH processing, see also the description in clause 7.2.2. Description of Generic Procedures of the present document. For forwarding a message to the target CSE indicated by the 'to' parameter of the message, the receiver CSE shall determine to which CSE the message needs to be forwarded next. In the following clauses this CSE is referred to as the 'next CSE'. CMDH processing shall be carried out as described in the following clauses.


## H.2.2	Partitioning of CMDH processing


The CMDH processing consists of two parts:

A.	CMDH message validation: This includes message parameter pre-processing, deciding on acceptance for transporting the message, and buffering of messages.
This procedure defines how incoming request or response messages that need to be forwarded to other CSE(s) shall be pre-processed, how a decision on acceptance of the message for forwarding to another CSE shall be derived and how the messages shall be queued up before the actual forwarding can happen. Details of CMDH validation are defined in clause H.2.3.

B.	CMDH message forwarding: This includes selecting buffered messages and communication path for forwarding the message to another CSE.
This procedure defines how to select among the messages buffered for forwarding to other CSEs the ones that need to be transported at a certain time and how to select an appropriate communication path for transporting the message(s). Details of CMDH message forwarding are defined in clause H.2.4.

CMDH message validation (Part A) will be carried out for each incoming new message for which CMDH processing is applicable.

If CMDH message validation is successful, the received message shall be queued up for the CMDH message forwarding process (Part B) including the associated storagePriority attribute as defined in the applicable [cmdhBuffer] resource (see details in the CMDH message validation procedure).

If the queued message was a request message and it was done in non-blocking mode then:

if the Receiver CSE supports the <request> resource type, it shall create a <request> resource representing the pending non-blocking request;

the Receiver CSE shall send an acknowledgement response message to the entity that sent the request message directly via Mca or Mcc to the receiver CSE indicating the acceptance of the request;

if the receiver CSE supports the <request> resource type it shall provide a reference to the created <request> resource in the 'cn' parameter of the response.

After successful forwarding of such a request message, any incoming response message matching with the Request-ID and the Originator in the <request> resource shall be parsed to update the corresponding attributes of the <request> resource. In case a non-blocking synchronous request was forwarded successfully and a response with acknowledgement was received, it is the responsibility of the CSE that forwarded the message to periodically poll the status of the <request> resource created on the next CSE and update the locally created <request> resource accordingly. When the locally created <request> resource expires the Hosting CSE can remove it. Details on <request> resource specific procedures for polling results are defined in clause 7.3.1.4.

If the queued message was a request message and it was done in blocking mode then memorize the open blocking request by storing its Request-ID and Originator and set a timer for a timeout until which a matching response message with the same Request-ID and Originator shall be received by the CSE processing this message. If no matching response is received when the timeout expires, the receiver CSE shall send a response message to the entity that sent the request to the Receiver CSE indicating unsuccessful processing of the request, unless the Receiver CSE and the Originator are the same. If Receiver CSE and Originator are the same, the Originator can decide internally whether to retry forwarding of the message.

If CMDH message validation is not successful, then the received message shall either get ignored – in case the received message is a response message – or a new error response message shall be sent back to the entity that sent the message to the Receiver CSE – in case the received message is a request message and the Originator is not the Receiver CSE. If Receiver CSE and Originator are the same, the Originator can decide internally whether to create a new request message.

The CMDH message forwarding process (Part B) will handle all queued up messages that shall be forwarded to another CSE. This process shall always be carried out when messages are pending for forwarding to another CSE.

The flow of CMDH processing is depicted in Figure H.2.2-1.

Figure H.2.2-1: CMDH Processing


## H.2.3	CMDH message validation procedure


In CMDH message validation, pre-processing of CMDH related parameters of a message for which CMDH-processing applies, deriving the decision on acceptance of a message and the buffering of that messages shall be carried out in line with the following steps. A summary of this processing is depicted in the flow chart at the end of this clause.

1)	Filling in missing CMDH-related parameters:

1.1)	Determine the value that shall be used for the 'ec' parameter of the processed message:

1.1.1)	If the message contains an 'ec' parameter: Use the value of the 'ec' parameter provided in the message.

1.1.2)	If the message does not contain an 'ec' parameter:

1.1.2.1)	Lookup all [cmdhDefEcValue] child resources of the [cmdhDefaults] resource that is a child resource of the provisioned active [cmdhPolicy] resource.

1.1.2.2)	If the message is a request message and any of the attributes requestContext, and requestCharacteristics are present in the found [cmdhDefEcValue] resources, discard all [cmdhDefEcValue] resources from the list of found items for which the context conditions or the request characteristics at time of processing the request message are not met, respectively.

1.1.2.3)	Among the remaining found [cmdhDefEcValue] resources do the following selection:

1.1.2.3.1)	If present, select the [cmdhDefEcValue] resource containing the AE-ID in the list defined by the requestOrigin attribute which matches with the 'fr' parameter in case of a request message or with the 'to' parameter in case of a response message. If multiple [cmdhDefEcValue] resources match, select the one with the lowest value in the order attribute. Continue processing with step 1.1.2.4.

1.1.2.3.2)	If present, select the [cmdhDefEcValue] resource containing the App-ID in the list defined by the requestOrigin attribute which matches with the 'fr' parameter in case of a request message or with the 'to' parameter in case of a response message. If multiple [cmdhDefEcValue] resources match, select the one with the lowest value in the order attribute. Continue processing with step 1.1.2.4.

1.1.2.3.3)	If present, select the [cmdhDefEcValue] resource containing the string 'localAE' in the list defined by the requestOrigin attribute in case of processing a message where the 'fr' parameter is the AE-ID of an AE registered with the CSE processing this message. If multiple [cmdhDefEcValue] resources match, select the one with the lowest value in the order attribute. Continue processing with step 1.1.2.4.

1.1.2.3.4)	If present, select the [cmdhDefEcValue] resource containing the string 'thisCSE' in the list defined by the requestOrigin attribute in case of processing a message where the 'fr' parameter is the CSE-ID of the CSE processing this message. If multiple [cmdhDefEcValue] resources match, select the one with the lowest value in the order attribute. Continue processing with step 1.1.2.4.

1.1.2.3.5)	Select the [cmdhDefEcValue] resource containing the string 'default' in the list defined by the requestOrigin attribute in case of processing a message where no other matches were found.

1.1.2.4)	If a [cmdhDefEcValue] resource has been selected in steps 1.1.2.3.1 through 1.1.2.3.4: Use the value of the defEcValue attribute of the selected [cmdhDefEcValue] resource as the value for the 'ec' parameter of the message. Else use the enumeration value of 'bestEffort' for the 'ec' parameter of the message.

1.2)	Filling in values that shall be used for the remaining CMDH-related parameters of messages:

1.2.1)	If the message contains any of the CMDH-related parameters 'rqet', 'rset', 'oet', 'rp': The provided values of the respective parameters in the message shall be used. No filling in is needed for those parameters. If any of the parameters 'rqet', 'rset', 'oet', 'rp' present in the message is represented in relative time format (i.e. as a duration in units of milliseconds), the receiving CSE shall translate the values of those parameters into absolute time format by adding the duration to the originating timestamp in the 'ot' parameter of the message. This 'ot' parameter is an optional message parameter and in case it is not present in a message, it shall be filled in by the first receiving CSE of a message using the time when the message was received.

1.2.2)	If the message parameter 'ec' has a value corresponding to 'bestEffort', use the following values for any missing CMDH-related parameters: For a request message use 'rqet' = -1('infinite'), 'rset' = -1 ('infinite'), 'oet' = 0 ('now'), 'rp' = 0 ('none'), 'da' = 'true'. For a response message use 'rset' = -1 ('infinite'), 'da' = 'true'. Continue with step 2.

1.2.3)	If the message parameter 'ec' has a value corresponding to 'immediate', do not fill in any remaining missing CMDH-related parameters and continue with step 2.

1.2.4)	For any of the missing CMDH-related parameters fill in values as follows:

1.2.4.1)	Lookup all [cmdhEcDefParamValues] child resources of the [cmdhDefaults] resource that is a child resource of the provisioned active [cmdhPolicy] resource.

1.2.4.2)	Among the found [cmdhEcDefParamValues] resources do the following selection:

1.2.4.2.1)	If present, select the [cmdhEcDefParamValues] resource containing the value of the 'ec' parameter of the message in the list defined by the applicableEventCategory attribute. If a match is found, continue processing with step 1.2.4.3.

1.2.4.2.2)	Select the [cmdhEcDefParamValues] resource that contains the string 'default' in the list defined by the applicableEventCategory attribute.

1.2.4.3)	Use the following attributes of the selected [cmdhEcDefParamValues] resource to fill in any missing CMDH-related message parameters: Fill in the value of the attribute defaultRequestExpTime for the parameter 'rqet' if it is missing. Fill in the value of the attribute defaultResultExpTime for the parameter 'rset' if it is missing. Fill in the value of the attribute defaultOpExecTime for the parameter 'oet' if it is missing. Fill in the value of the attribute defaultRespPersistence for the parameter 'rp' if it is missing. Fill in the value of the attribute defaultDelAggregation for the parameter 'da' if it is missing. Convert the values of 'rqet', 'rset', 'oet' and 'rp' into absolute time representations if they were filled in during this step, by adding the respective durations to the 'ot' parameter value. In case where the time duration of the default parameter indicates 'infinity', the absolute time representation of the corresponding primitive parameter shall be set to the largest possible date "99993112T000000".

2)	Compare CMDH parameters with allowed CMDH parameter limits:
Check if CMDH-related parameters effective for the message are with allowed limits.

2.1)	Lookup all [cmdhLimits] child resources of the provisioned active [cmdhPolicy] resource.

2.2)	If the message is a request message and any of the attributes requestContext, and requestCharacteristics are present in the found [cmdhLimits] resources, discard all [cmdhLimits] resources from the list of found items for which the context conditions or the request characteristics at time of processing the request message are not met, respectively.

2.3)	Among the remaining found [cmdhLimits] resources do the following selection:

2.3.1)	If present, select the [cmdhLimits] resource(s) containing the AE-ID in the list defined by the requestOrigin attribute which matches with the 'fr' parameter in case of a request message or with the 'to' parameter in case of a response message. If multiple [cmdhLimits] resources match, select the one with the lowest value in the order attribute. Continue processing with step 2.4.

2.3.2)	If present, select the [cmdhLimits] resource(s) containing the App-ID in the list defined by the requestOrigin attribute which matches with the 'fr' parameter in case of a request message or with the 'to' parameter in case of a response message. If multiple [cmdhLimits] resources match, select the one with the lowest value in the order attribute. Continue processing with step 2.4.

2.3.3)	If present, select the [cmdhLimits] resource(s) containing the string 'localAE' in the list defined by the requestOrigin attribute in case of processing a message where the 'fr' parameter is the AE-ID of an AE registered with the CSE processing this message. If multiple [cmdhLimits] resources match, select the one with the lowest value in the order attribute. Continue processing with step 1.1.2.4.

2.3.4)	If present, select the [cmdhLimits] resource(s) containing the string 'thisCSE' in the list defined by the requestOrigin attribute in case of processing a message where the 'fr' parameter is the CSE-ID of the CSE processing this message. If multiple [cmdhLimits] resources match, select the one with the lowest value in the order attribute. Continue processing with step 2.4.

2.3.5)	Select the [cmdhLimits] resource containing the string 'default' in the list defined by the requestOrigin attribute in case of processing a message where no other matches were found.

2.4)	Validate if 'ec' parameter is within allowed range:
If the 'ec' parameter of the message is not within the list defined by the limitsEventCategory attribute of the selected [cmdhLimits] resource, mark CMDH message validation for this message as not successful and exit CMDH message validation.

2.5)	Validate if 'rqet' parameter is within allowed range:
If the 'rqet' parameter is present in the message and if it is not within the range defined by the 'ot' parameter and limitsRequestExpTime attribute of the selected [cmdhLimits] resource, mark CMDH message validation for this message as not successful and exit CMDH message validation.

2.6)	Validate if 'rset' parameter is within allowed range:
If the 'rset' parameter is present in the message and if it is not within the range defined by the 'ot' parameter and limitsResultExpTime attribute of the selected [cmdhLimits] resource, mark CMDH message validation for this message as not successful and exit CMDH message validation.

2.7)	Validate if 'oet' parameter is within allowed range:
If the 'oet' parameter is present in the message and if it is not within the range defined by the 'ot' parameter and limitsOpExecTime attribute of the selected [cmdhLimits] resource, mark CMDH message validation for this message as not successful and exit CMDH message validation.

2.8)	Validate if 'rp' parameter is within allowed range:
If the 'rp' parameter is present in the message and if it is not within the range defined by the 'ot' parameter and limitsRespPersistence attribute of the selected [cmdhLimits] resource, mark CMDH message validation for this message as not successful and exit CMDH message validation.

2.9)	Validate if 'da' parameter is within allowed range:
If the 'da' parameter is present in the message and if it is not within the list of allowed values defined by the limitsDelAggregation attribute of the selected [cmdhLimits] resource, mark CMDH message validation for this message as not successful and exit CMDH message validation.

3)	Check if message complies with network access rules and buffer limits:

3.1)	Check if 'ec' parameter has enumeration value for 'immediate':
If the 'ec' parameter of the message is 'immediate' bypass any checks on buffering or access network usage rules. Mark the CMDH message validation for this message as successful and end CMDH message validation.

3.2)	Check if delivering the message is possible within the boundaries of access network usage rules in CMDH policies:

3.2.1)	Lookup all [cmdhNetworkAccessRules] child resources of the provisioned active [cmdhPolicy] resource.

3.2.2)	Among the all found [cmdhNetworkAccessRules] resources do the following selection:

3.2.2.1)	If present, select the [cmdhNetworkAccessRules] resource containing the value of the 'ec' parameter of the message in the list defined by the applicableEventCategory attribute. If a match is found, continue processing with step 3.2.3.

3.2.2.2)	Select the [cmdhNetworkAccessRules] resource that contains the enumeration value for 'default' in the list defined by the applicableEventCategory attribute.

3.2.3)	Lookup all [cmdhNwAccessRule] child resources of the selected [cmdhNetworkAccessRules] resource.

3.2.4)	Among all found [cmdhNwAccessRule] resources find at least one for which the <schedule> child resource 'allowedSchedule' is allowing usage of the corresponding target network consistent with the 'rqet' parameter in case of a request message being processed or in line with the 'rset' parameter in case of a response message being processed. If no matching [cmdhNwAccessRule] resource is found, mark CMDH validation for this message as not successful due to lack of scheduling opportunities and end CMDH message validation. Otherwise continue.

3.3)	Check if delivering the message is possible within the boundaries of buffer usage rules in CMDH policies:

3.3.1)	Lookup all [cmdhBuffer] child resources of the provisioned active [cmdhPolicy] resource.

3.3.2)	Among the all found [cmdhBuffer] resources do the following selection:

3.3.2.1)	If present, select the [cmdhBuffer] resource containing the value of the 'ec' parameter of the message in the list defined by the applicableEventCategory attribute. If a match is found, continue processing with step 3.3.3.

3.3.2.2)	Select the [cmdhBuffer] resource that contains the enumeration value for 'default' in the list defined by the applicableEventCategory attribute.

3.3.3)	Check if the amount of memory needed to buffer the message being validated in addition to the already buffered messages matching with the same buffer usage policy in the selected [cmdhBuffer] resource would exhaust the limit defined by the maxBufferSize attribute of the selected [cmdhBuffer] resource or if the available memory for CMDH forwarding on the receiver CSE would get exhausted even when purging buffered messages with lower storage priority.

3.3.3.1)	If the check is negative, mark the CMDH message validation for the message being validated as successful, assign the storage priority defined in the storagePriority attribute of the selected [cmdhBuffer] resource to the validated message, and end CMDH message validation.

3.3.3.2)	If the check is positive, mark the CMDH message validation for the message being validated as not successful and end CMDH message validation.

Figure H.2.3-1: CMDH message validation procedure


## H.2.4	CMDH message forwarding procedure


The high-level sequence of processing steps for the CMDH message forwarding process is depicted in the flow chart below. Note that this flow chart only represents the reference flow for implementing a standard compliant behaviour. Other standard compliant implementations may be possible as long as the events defined below will result in the same normative message exchanges via reference points.

Occurrence of the following events shall trigger processing in the CMDH message forwarding:

One or more new message(s) get(s) queued up for CMDH message forwarding.

Any of the underlying networks becomes usable for message forwarding due to transition(s) in allowed schedule(s) or due to establishing of availability of connectivity (e.g. cable plugged-in, coverage established).

Any of the underlying networks becomes unusable for message forwarding due to transition(s) in allowed schedule(s) or due to loss of availability of connectivity (e.g. cable unplugged, coverage lost).

Any message buffered for CMDH forwarding expires.

Figure H.2.4-1: CMDH message forwarding procedure

When a new message is being queued up for CMDH message forwarding, carry out the following:

If the 'ec' parameter of the messages has the value 'immediate':

Forward message as soon as possible to the next CSE. The processing in this situation is described by the flow chart in Figure H.2.4-2.

If a Mcc communication connection to the next CSE for forwarding the message is already established, continue with step 1.3.

If no Mcc communication connection to the next CSE for forwarding the message is established pick one underlying network among all underlying networks that can provide communication to the next CSE and establish a Mcc communication connection to the next CSE in line with the rules outlined in clause H.2.5. If establishment of a Mcc communication connection to the next CSE was not successful before the message expires, continue with step 1.4.

Determine whether delivery aggregation or forwarding of the message itself shall be used:

If the message contains a 'da' parameter set to the value 'true', the Receiver CSE shall forward this message by creation of a <delivery> resource on the next CSE as outlined in clause 7.4.11. The receiver CSE can combine the forwarded message in the same <delivery> resource with other messages for which the 'da' parameter set to 'true' and which need to be forwarded to the same target CSE.

If the message is not forwarded using a <delivery> resource, the receiver CSE shall forward the message as is to the next CSE via the established Mcc communication connection.

If the message could not be forwarded successfully to the next CSE before it expired (e.g. due to repeated unsuccessful attempts to establish a Mcc communication connection or due to the lack of usable underlying networks), the receiver CSE shall carry out the following:

If the message was a response message, ignore the message. End this cycle of CMDH message forwarding and wait for new triggering events.

If the message was a request message:

If the request was a blocking request:
Send an error response to the pending blocking request with a matching Request-ID and Originator indicating the reason for failure and close the blocking request. End this cycle of CMDH message forwarding and wait for new triggering events.

If the request was a non-blocking request:
Update the associated <request> resource with matching Request-ID and Originator using an error response code indicating the reason for failure. If the non-blocking request was made in asynchronous mode, send a notification with the error response to the notification target(s) of the request. End this cycle of CMDH message forwarding and wait for new triggering events.

Else, i.e. if the message was forwarded successfully to the next CSE:

If the message was a response and the Receiver CSE has an open blocking request context with a matching Request-ID and matching Originator, mark the open blocking request as closed, end this cycle of CMDH message forwarding and wait for new triggering events.

If the message was a request message:

If the request was a blocking request:
Keep the context of the pending blocking request with matching Request-ID and matching Originator open and wait for an incoming response message with the same Request-ID and Originator. End this cycle of CMDH message forwarding and wait for new triggering events.

If the request was a non-blocking request:
Wait for a response to the forwarded request (e.g. response with acknowledgement or error response). Update the associated <request> resource with the matching Request-ID and Originator using a response code that reflects the status of the forwarded request (e.g. accepted by next CSE, unsuccessful). If the next CSE responded with an error response message and the request was in non-blocking asynchronous mode, send a notification request message to the Originator of the forwarded request containing the error response of the next CSE. End this cycle of CMDH message forwarding and wait for new triggering events.

Else, i.e. when the 'ec' parameter of the messages does not have the value corresponding to 'immediate':

Buffer the message to be forwarded in the CMDH forwarding buffer:
The processing in this situation is described by the flow chart in Figure H.2.4.2. If the message is a request message and the 'ec' parameter of the messages has the value corresponding to "latest":

If the request message is a notification triggered by a subscription:

Find any buffered request message that is a notification triggered by a subscription with the same subscription reference.

Else, i.e. if the request message is not a notification triggered by a subscription:

Find any buffered request message that has the same values in the ('fr', 'to', 'op') parameters as the message being processed.

If any request message was found in steps 2.1.1.1.1 or 2.1.1.2.1, purge the found message from the CMDH forwarding buffer.

If there is not enough memory available to buffer the message being processed in the CMDH forwarding buffer:

Find any buffered messages with storage priority values lower than the one assigned to the message being processed.

If any messages are found:
Purge enough messages among the found messages so that the message being processed can be buffered in the CMDH forwarding buffer. Messages which entered the buffer later shall be purged first. In case any request messages need to be purged, carry out the following:

In case of purging a non-blocking request messages:
Update the associated <request> resource with the same Request-ID as the purged request message with a status indicating unsuccessful completion. If the purged message was made in asynchronous mode, send a response to the notification target(s) of the pending non-blocking request.

In case of purging a blocking request message:
Send an error response to the open blocking request with the same Request-ID as in the purged request message and close the blocking request.

Due to the checking of sufficient memory in CMDH message forwarding buffer during CMDH message validation, there should be enough memory available to accommodate the message to be buffered at this point. If that is still not the case, then do the following:

In case the message to be buffered is a response message:
Ignore the message to be buffered. End this cycle of CMDH message forwarding and wait for new triggering events.

In case the message to be buffered is a non-blocking request message:
Update the associated <request> resource with the same Request-ID as the request message to be buffered with a status indicating unsuccessful completion. If the request message to be buffered was made in asynchronous mode, send a response to the notification target(s) of the pending non-blocking request. End this cycle of CMDH message forwarding and wait for new triggering events.

In case the message to be buffered is a blocking request message:
Respond with an error response message to the open blocking request with the same Request-ID as in the request message to be buffered and close the blocking request. End this cycle of CMDH message forwarding and wait for new triggering events.

Store the message to be buffered with its assigned storage priority in the CMDH forwarding buffer. Include it in future evaluations for possible message forwarding.

Evaluate if any message forwarding is currently allowed:

For all buffered messages that are pending in CMDH message forwarding carry out the following evaluation steps:

Among all [cmdhNetworkAccessRules] child resources of the provisioned active [cmdhPolicy] resource do the following selection:

If present, select the [cmdhNetworkAccessRules] resource containing a value in the list defined by the applicableEventCategory attribute that is equal to the value of the 'ec' parameter of the buffered message to be evaluated for forwarding. If a match is found, continue processing with step 2.2.1.2.

Select the [cmdhNetworkAccessRules] resource that contains the string 'default' in the list defined by the applicableEventCategory attribute.

Lookup all [cmdhNwAccessRule] child resources of the selected [cmdhNetworkAccessRules] resource.

If the attribute otherConditions is present in any of the found [cmdhNwAccessRule] resources, discard all [cmdhNwAccessRule] resources from the list of found items for which the conditions expressed by otherConditions at time of evaluation of the message for forwarding are not met, respectively.

Among the all remaining found [cmdhNwAccessRule] resources find those for which

the <schedule> child resource allowedSchedule is currently allowing usage of the corresponding target network, and

the corresponding target network could be used to reach the next CSE for forwarding the message under evaluation.

If any allowed target network was found, memorize the message under evaluation as an allowed message and the allowed target network(s) for the message under evaluation and continue with the next evaluation of buffered messages

When all buffered messages have been evaluated, remove from the memorized list of allowed messages and their allowed target networks those target networks where the amount of data to be forwarded – accumulated over all allowed messages of the same event category – is less than the amount of data indicated in the minReqVolume attribute of the corresponding [cmdhNwAccessRule] resource.

Remove any messages from the list of allowed messages for forwarding if no allowed target network is left for that message after the previous step.

Process messages allowed for forwarding to the next CSE:
If any messages can be forwarded, i.e. if any evaluation of step 2.2 was positive, apply the following steps:

Reuse already established Mcc communication connections or – if needed – establish new Mcc communication connection(s) so that all the messages that are allowed to be forwarded to their next CSE can be forwarded. Some messages may be allowed on the same target network. Follow the procedure outlined in clause H.2.5 for setting up a Mcc communication connection to another CSE via a particular target network. If no usable Mcc communication connection could be established for forwarding a particular allowed message before the message expires, execute step 1.4 in this clause for that message.

For all messages allowed for forwarding and for which Mcc communication connections are established, apply steps 1.3 through 1.5 in this clause.

Else, i.e. currently no message forwarding is allowed:
End this cycle of CMDH message forwarding and wait for new triggering events.

When any of the underlying networks becomes usable for message forwarding due to transition(s) in allowed schedule(s) or due to establishing of availability of connectivity (e.g. cable plugged-in, coverage established), carry out the processing above in this clause starting with step 2.2.

When any of the underlying networks becomes unusable for message forwarding due to transition(s) in allowed schedule(s) or due to loss of availability of connectivity (e.g. cable unplugged, coverage lost), complete – if at all possible – any ongoing message forwarding procedures. End this cycle of CMDH message forwarding and wait for new triggering events.

When any message buffered for CMDH forwarding expires, carry out step 1.4 in this clause above. End this cycle of CMDH message forwarding and wait for new triggering events.

Figure H.2.4-2: Forwarding of messages with 'ec' = 'immediate'

Figure H.2.4-3: Buffering of messages for CMDH message forwarding


## H.2.5	Establishment of Mcc communication connection to another CSE


When a Mcc communication connection shall be established via a specific target network for forwarding a message of a specific event category indicated by the 'ec' parameter of the message, the process of establishing the Mcc communication connection shall be governed by values contained in the backOffParameters attribute of the [cmdhNwAccessRule] resource that was used to evaluate whether the message was allowed to be forwarded, as defined in step 2.2 in the procedure outlined in clause H.2.4.

When connectivity via the selected target network to reach the next CSE has not already been established for other reasons, then the CSE that is trying to forward a message buffered for CMDH message forwarding shall establish a new Mcc communication connection via the selected target network for transporting oneM2M messages to the next CSE via a new Mcc instance. This communication connection shall be established following the procedures for authentication and security association using TLS or DTLS as defined in the oneM2M TS-0003 [7] taking into account provisioned security settings. The protocol mapping for transporting oneM2M specified messages via this instance of Mcc shall be selected according to the capabilities of the two end-points of the Mcc instance.

If establishing the Mcc communication connection via the selected target network fails, a new attempt to establish that communication connection shall only be made after waiting for a back-off time according to the value given in the 'back-off time' component of the backOffParameters attribute of the effective [cmdhNwAccessRule] resource.

When establishing the Mcc communication connection via the selected target network still fails, for each subsequent new attempt to establish the Mcc communication connection without any successful attempts in-between, the back-off time shall be increased by the value given in the 'back-off time increment' component of the backOffParameters attribute of the effective [cmdhNwAccessRule] resource.

The back-off time for waiting before making any new attempt to establish the Mcc communication connection via the selected target network shall not exceed the value given by the 'maximum back-off time' component of the backOffParameters attribute of the effective [cmdhNwAccessRule] resource.

When the next CSE is hosted on a node for which a usable Mcc communication connection for forwarding a message to the next CSE can only be established by the next CSE itself, device triggering mechanisms as defined in the oneM2M TS-0001 [6] shall be used.

In case the next CSE can only be reached via communication connections originating from the node that hosts the next CSE, while it is capable of processing incoming oneM2M messages, it is assumed that such a CSE establishes a polling channel as defined in the oneM2M TS-0001 [6] in order to effectively receive unsolicited oneM2M messages.

Annex I (informative):
Guidelines for using XSD files in AE and CSE code


# I.1	Usage of the oneM2M developed XSD files


The primary purpose of the XSD files developed by oneM2M is described in clause 6.1. This informative annex provides an example of potential usage of the XSD in practical implementations of oneM2M entities (AE and CSE).

As has been specified in clause 8, to enable efficient communication, the short names introduced in clause 8.2 are used in XML and JSON serializations of request and response primitives to identify primitive parameters, and to identify resource names, resource attribute names and their complex data type members when included in the Content primitive parameter. This implies that short names are applied in any communication over the Mca, Mcc and Mcc' reference points. Nevertheless, the XSD files included in the present release employ the long names for primitive parameters and any other XML elements and attributes.

This annex provides a possible use case of the oneM2M developed XSD files for information.


# I.2	Example AE/CSE implementation featuring mapping between short and long names for XML serialization


Figure I.2-1 shows an example where the oneM2M defined XSD files are used as input to a code generator. Such code generators are available for most object-oriented programming languages such as e.g. Java, C++ and Python. The following descriptions include some code examples given in Python syntax. However, corresponding expressions in C++ or Java look very similar.

Code generators generate a library of XSD binding classes corresponding to each of the data types defined in the input XSD files. This library can then be imported into the source code of the respective programming language which implements an AE or CSE.

For example, if this library is denoted schemaLib, instances of a request primitive and of a resource type <contentInstance>, denoted in the Python source code fragment below as reqPrimInstance (internal representation of m2m:requestPrimitive) and contentInstance1 (as internal representation of m2m:contentInstance), respectively, can simply be generated as follows:

import schemaLib

…

reqPrimInstance = schemaLib.requestPrimitive()

contentInstance1 = schemaLib.contentInstance()

Each of the instances created in this way represents a data object reflecting the same tree structure as defined in the XSD files that served as input to the code generator.

Any request primitive parameter in reqPrimInstance as defined above can be addressed and assigned values as follows:

reqPrimInstance.operation = operation     #e.g. operation = 1 for CREATE

reqPrimInstance.to = path                 #path = address of target resource

reqPrimInstance.from_ = originator  #originator=identifier representing the originator

reqPrimInstance.requestIdentifier = str(requestIDCounter) #counter in string format

reqPrimInstance.resourceType = resourceType #e.g. resourceType = 4 for <contentInstance>

Parameters defined as complex type in the XSD such as e.g. the Filter Criteria primitive parameter can be assigned values as follows:

reqPrimInstance.filterCriteria.createdBefore = '20161201T000000'

reqPrimInstance.filterCriteria.createdAfter = '20150501T123000'

reqPrimInstance.filterCriteria.labels = 'label1 label2 label3'

reqPrimInstance.filterCriteria.attribute.append(pyxb.BIND())

reqPrimInstance.filterCriteria.attribute[0] = schemaLib.attribute("name0","value0")

Note that the class attribute names in the source code are identical with the XML element or attribute names as used in the XSD files (sometimes minor exceptions can occur, for instance in case that a name used in the XSD represents a reserved name in the source code. In such case the code generator typically would append a special suffix to the name, e.g. "_"). Since the XSD uses the long parameter and resource attribute names, these also appear as class attributes in the source code. From an implementation perspective, this is preferable compared to using short names. Using short names in the XSD would result in short names in the source code. However, these short names have essentially lost their semantics and are therefore more difficult do memorize. Any misspelling in the code may easily result in another well-defined short name such that identifying errors in the source code becomes more difficult.

A code generator as considered here, typically also provides a set of class methods and utility functions which allow to generate code objects from a given XML representation, and inversely, to generate XML representations from a code object. For example, consider that a string variable, denote reqPrimXML represents a serialized request primitive as follows (note that this representation corresponds to the example given in clause 8.3.2 but with long names used here):

reqPrimXML =

'<?xml version="1.0" encoding="UTF-8"?>
     <m2m:requestPrimitive xmlns:m2m="http://www.onem2m.org/xml/protocols"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.onem2m.org/xml/protocols CDT-requestPrimitive-v3_32_0.xsd">
        <operation>1</operation>
        <to>//cse1.mym2msp.org/</to>
        <from>//cse1234/app567</from>
        <requestIdentifier>0002bf63</requestIdentifier >
        <resourceType>4</resourceType>
        <primitiveContent>
            <contentInstance resourceName="temp754">
               <contentInfo>application/xml:1</contentInfo>
               <content>PHRpbWU+MTc4ODkzMDk8L3RpbWU+PHRlbXA+MjA8L3RlbXA+DQo=</content>
            </contentInstance>
        </ primitiveContent>
    </m2m:requestPrimitive>'

Assuming that the auto-generated library schemaLib includes a utility function createFromDocument(), the following code statement creates an instance reqPrimInstance from the XML serialized request primitive in the string variable reqPrimXML:

reqPrimInstance = schemaLib.createFromDocument(reqPrimXML)

The root element of the XML string (i.e. m2m:requestPrimitive in this example) identifies the template (class) that need to be used to create the data object reqPrimInstance. All value settings of the parameters are taken from the XML string, e.g. reqPrimInstance.operation is set to 1.

The reverse operation, i.e. generation of an XML string from the data object reqPrimInstance is typically possible with a class method toxml() as follows:

reqPrimXML = reqPrimInstance.toxml()

If any value settings of reqPrimInstance have not been changed in the given code, the above statement generates the same XML string as given above. Both operations, createFromDocument() and toxml(), also allow to verify the compliance of the XML representations with the XSD that was used as input when generating the schemaLib source code.

The question arises, if there is a way to generate XML or JSON representations that include the short names as defined in clause 8.2 when employing XSD with the long names as described above.

The following outlines two possible ways to resolve this issue.

The first straightforward approach is to use a text parser which replaces the long names used in XML or JSON strings with their corresponding short names, or vice-versa. It is denoted such functions as map_L2S() and map_S2L(). This approach is illustrated in the box labelled "AE or CSE source code" in Figure I.2-1 for an XML serialized string.

Given a string reqPrimXML representing an XML serialized request primitive with long names as described above, the statement:

reqPrimXML_sh = map_L2S(reqPrimXML)

would produce an XML string that includes the short names as shown in the representation already given in clause 8.3.2.

The reverse operation, generating an XML representation with long names from a representation with short names could be done with:

reqPrimXML = map_S2L(reqPrimXML_sh)

Both mapping functions require a mapping table which includes all long names and their associated short names. The required mapping table can be derived from Tables 8.2.2-1, 8.2.2-2, 8.2.3-1 to 8.2.3-6, 8.2.4-1 and 8.2.5-1.

In order to work in both mapping directions, the mapping table represents a one-to-one relationship between short and long names.

The second approach is essentially a code-optimized variant of the above first approach.

The source code of the described createFromDocument() and toxml() functions could be extended by the programmer by including the functionality of map_S2L() directly into createFromDocument() and including the functionality of map_L2S() directly into toxml(). An additional function argument could be included which allows to enable and disable the mapping function.

Figure I.2-1: Example AE or CSE implementation: processing based on long names,
XML representations using short names


# I.3	Example AE/CSE implementation featuring mapping between short and long names for JSON serialization


Figure I.3-1 shows an example implementation which employs JSON serialization. The core of this example implementation is identical with the one described above for XML serialization. In the example it is assumed that for producing a JSON representation which is valid against its associated XSD, an XML file is generated first by means of the toxml() function described in clause I.2 above. In this case the mapping from long to short names can be accomplished also with the map_L2S() function used in the XML serialization example. This XML file can then be converted into a structured data representation that allows direct conversion into JSON. When using Python programming language, the most suitable representation is the dictionary format. In Figure I.3-1, the function denoted as xml2dict(), generates a Python dictionary object which in the final operation step is serialized into the XSD-valid JSON representation by means of the json.dumps() function. In order to comply with the requirements for the JSON representation as defined in clause 8.4, it is necessary to adjust the data type of numeric and list-type elements.

At the receiving side of the described implementation example, received JSON data is converted into a Python dictionary object by means of the json.loads() function. This dictionary object is unparsed by means of a function denoted dict.unparse() in Figure I.3-1 which generates directly an instance of the class applicable to the received data which is defined in SchemaLib. During the unparse operation, the mapping is accomplished between the short names included in the received JSON data object and the long names employed in the class definition included in SchemaLib. The unparse operation also implements validation of the compliance of the received JSON data with the XSD.

Figure I.3-1: Example AE or CSE implementation with processing based on long names

Annex J (normative):
Specializations of <flexContainer> resource


# J.1	Introduction


This annex defines each specialization of <flexContainer> resource that are used for generic interworking [36] and AllJoyn interworking [37]. The <flexContainer> resource and procedures are defined in the clause 7.4.37. Since the specialization resources handling procedures are the same as <flexContainer> resource, this annex does not specify them. Also, since all the specialization inherits the universal/common attributes of <flexContainer> resource, this annex does not specify that information.


# J.2	Void



# J.3	Void



# J.4	Resource type [svcObjWrapper]


This specialization of <flexContainer> is intended to be used to wrap a group of child resources related to AllJoyn service objects with minimal overhead. No custom attributes are needed for this specialization.

Table J.4-1: Data type definition of [svcObjWrapper] resource

Table J.4-2: Resource Specific Attributes of [svcObjWrapper] resource

Table J.4-3: Child Resources of [svcObjWrapper] resource


# J.5	Resource type [svcFwWrapper]


This specialization of <flexContainer> is intended to be used to wrap a group of child resources related to AllJoyn framework services with minimal overhead. No custom attributes are needed for this specialization.

Table J.5-1: Data type definition of [svcFwWrapper] resource

Table J.5-2: Resource Specific Attributes of [svcFwWrapper] resource

Table J.5-3: Child Resources of [svcFwWrapper] resource


# J.6	Resource type [allJoynApp]


This specialization of <flexContainer> is used to represent a specific instance of an AllJoyn application. This resource shall include the direction custom attribute.

Table J.6-1: Data type definition of [allJoynApp] resource

Table J.6-2: Resource Specific Attributes of [allJoynApp] resource

Table J.6-3: Child Resources of [allJoynApp] resource


# J.7	Resource type [allJoynSvcObject]


This specialization of <flexContainer> is used to represent a specific instance of an AllJoyn application. This resource shall include the objectPath and enable custom attributes.

Table J.7-1: Data type definition of [allJoynSvcObject] resource

Table J.7-2: Resource Specific Attributes of [allJoynSvcObject] resource

Table J.7-3: Child Resources of [allJoynSvcObject] resource


# J.8	Resource type [allJoynInterface]


This specialization of <flexContainer> is used to represent a specific implementation of an AllJoyn interface residing in an AllJoyn service object. This resource shall include the interfaceIntrospectXmlRef custom attribute.

Table J.8-1: Data type definition of [allJoynInterface] resource

Table J.8-2: Resource Specific Attributes of [allJoynInterface] resource

Table J.8-3: Child Resources of [allJoynInterface] resource


# J.9	Resource type [allJoynMethod]


This specialization of <flexContainer> is used to represent a specific method of an AllJoyn interface residing in an AllJoyn service object. No custom attributes are needed for this specialization.

Table J.9-1: Data type definition of [allJoynMethod] resource

Table J.9-2: Resource Specific Attributes of [allJoynMethod] resource

Table J.9-3: Child Resources of [allJoynMethod] resource


# J.10	Resource type [allJoynMethodCall]


This specialization of <flexContainer> is used to represent a specific calling instance of a method of an AllJoyn interface residing in an AllJoyn service object. This resource shall include the input, output and callStatus custom attributes.

Table J.10-1: Data type definition of [allJoynMethodCall] resource

Table J.10-2: Resource Specific Attributes of [allJoynMethodCall] resource

Table J.10-3: Child Resources of [allJoynMethodCall] resource


# J.11	Resource type [allJoynProperty]


This specialization of <flexContainer> is used to represent a specific property of an AllJoyn interface residing in an AllJoyn service object. This resource shall include the currentValue and requestedValue custom attributes.

Table J.11-1: Data type definition of [allJoynProperty] resource

Table J.11-2: Resource Specific Attributes of [allJoynProperty] resource

Table J.11-3: Child Resources of [allJoynProperty] resource

Annex K (Informative):
Optionality of resource attributes in requests


# K.1	Introduction


This annex shows how the optionality of attributes in a Create or Update request corresponds to the WO/RO/RW annotation to be found in oneM2M TS-0001 [6]).


# K.2	Possible values of Create/Update request optionality with respect to WO/RO/RW attributes


The optionality of attributes in the Content parameter of a request should be consistent with the following table:

Table K.2-1: Request Optionality of Attributes in Content


# History
