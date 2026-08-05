**ATP 4-0.6** 

## **Sustainment Automation Support Management Office Operations** 

### **JANUARY 2024** 

**DISTRIBUTION RESTRICTION:** Approved for public release; distribution is unlimited. This publication supersedes ATP 4-0.6, dated 5 April 2013. 

## **Headquarters, Department of the Army** 

This publication is available at the Army Publishing Directorate site <u>(https://armypubs.army.mil) and the Central Army Registry site (https://atiam.train.army.mil/catalog/dashboard).</u> 

***ATP 4-0.6** 

Army Techniques Publication No. 4-0.6 

Headquarters Department of the Army Washington, DC, 17 January 2024 

# **Sustainment Automation Support Management Office Operations** 

### **Contents** 

||**Page**|
|---|---|
||**PREFACE.................................................................................................................... iii**|
||**INTRODUCTION .......................................................................................................... v**|
|**Chapter 1**|**SASMO OVERVIEW ................................................................................................. 1-1**<br>|
||Fundamentals ............................................................................................................ 1-1|
||SASMO Role ............................................................................................................. 1-1<br>|
||Sustainment Automation Defined .............................................................................. 1-6<br>|
||Roles and Responsibilities in a Web-Based Environment ........................................ 1-7|
|**Chapter 2**|**SUSTAINMENT AUTOMATION ORGANIZATIONAL STRUCTURE ...................... 2-1**|
||Sustainment Automation Support By Echelon .......................................................... 2-1<br>|
||Technical Channels ................................................................................................... 2-5<br>|
||Operations Coordination ............................................................................................ 2-8|
|**Chapter 3**|**SUSTAINMENT AUTOMATION ............................................................................... 3-1**|
||Automation Fundamentals......................................................................................... 3-1<br>|
||Network and Communications................................................................................... 3-2<br>|
||Army Sustainment Enterprise Business Systems ..................................................... 3-5|
|**Chapter 4**|**PLANNING AND COORDINATION .......................................................................... 4-1**|
||Planning Considerations ............................................................................................ 4-1|
||Operations Process ................................................................................................... 4-3<br>|
||Communication and Coordination ............................................................................. 4-9|
|**Chapter 5**|**SASMO OPERATIONS ............................................................................................. 5-1**|
||Establish Communications ........................................................................................ 5-1<br>|
||Sustainment Automation Maintenance ...................................................................... 5-7<br>|
||Roles and Responsibilities ........................................................................................ 5-8|
||Deployment and Redeployment .............................................................................. 5-12|
|**Appendix A**|**TRAINING ................................................................................................................ A-1**|
||**GLOSSARY ................................................................................................ Glossary-1**|
||**REFERENCES ........................................................................................ References-1**|
||**INDEX ................................................................................................................ Index-1**|



**DISTRIBUTION RESTRICTION:** Approved for public release; distribution is unlimited. 

*This publication supersedes ATP 4-0.6, dated 5 April 2013. 

**17 January 2024** 

**ATP 4-0.6** 

**i** 

**Contents** 

### **Figures** 

|Figure 1-1. Distribution management process ............................................................................... 1-4|
|---|
|Figure 1-2. Notional combat service support very small aperture terminal fielding report ............ 1-5|
|Figure 2-1. Sustainment brigade SPO staff ................................................................................... 2-3|
|Figure 2-2. Combat sustainment support battalion staff ................................................................ 2-3|
|Figure 2-3. Division sustainment brigade ...................................................................................... 2-4|
|Figure 2-4. Technical channel coordination map ........................................................................... 2-6|
|Figure 2-5. Organizational relationships ........................................................................................ 2-9|
|Figure 3-1. Combat service support very small aperture network ................................................. 3-3|
|Figure 3-2. Combat service support automated information systems interface network .............. 3-4|
|Figure 4-1. Notional CSS VSAT communications status report .................................................... 4-2|
|Figure 4-2. Collaboration between the S-3 and support operations .............................................. 4-5|
|Figure 4-3. Logistics synchronization meeting............................................................................... 4-8|
|Figure 5-1. Tier support concept .................................................................................................... 5-2|
|Figure 5-2. Notional network diagram ............................................................................................ 5-4|
|Figure 5-3. Sustainment automation support management office composition ............................ 5-9|
|Figure 5-4. Notional sustainment automation support management office ................................. 5-10|
|Figure A-1. Notional concept of operations gunnery training exercise .......................................... A-7|



### **Tables** 

|Table 1-1. Hardware, systems, and network support .................................................................... 1-8|
|---|
|Table 3-1. Enterprise business systems ........................................................................................ 3-5|
|Table 3-2. Applications supported by the network ......................................................................... 3-9|
|Table 4-1. Notional PACE plan ...................................................................................................... 4-3|
|Table 5-1. Trouble shooting tasks ................................................................................................. 5-6|
|Table A-1. Platform training ........................................................................................................... A-3|
|Table A-2. Score card .................................................................................................................... A-8|



**ATP 4-0.6** 

**17 January 2024** 

**ii** 

### **Preface** 

ATP 4-0.6 provides information on sustainment automation support management office (SASMO) operations. It is intended for use by commanders, support operations officers, planners, and SASMO teams. The focus of this publication is on the SASMO’s role, characteristics, functions, capabilities, and techniques that underpin the distribution management process. The Department of Defense considers data a strategic asset and the network a weapons system. This manual describes SASMOs as information managers that enable knowledge management for sustainment centers of operations executing the distribution management process. Sustainment automation support operations involve systems administration (maintaining enterprise business system applications) and network administration (maintaining the sustainment transport system). 

The principal audience for ATP 4-0.6 is any member of the profession of arms. Commanders and staffs of Army headquarters serving as joint task force or multinational headquarters should also refer to applicable joint or multinational doctrine concerning the range of military operations and joint or multinational operations. Trainers and educators throughout the Army will also use this publication. 

Commanders, staffs, and subordinates must ensure that their decisions and actions comply with applicable United States, international, and, in some cases, host-nation laws and regulations. Commanders at all levels will ensure that their Service members operate in accordance with the law of armed conflict and the rules of engagement. (See FM 6-27 for legal compliance.) 

This publication implements or is in consonance with STANAG 2543. 

ATP 4-0.6 uses joint terms where applicable. Selected joint and Army terms and definitions appear in both the glossary and the text. For definitions shown in the text, the term is italicized, and the number of the proponent publication follows the definition. This publication is not the proponent for any Army terms. 

ATP 4-0.6 applies to the Active Army, Army National Guard/Army National Guard of the United States, and United States Army Reserve unless otherwise stated. 

The proponent of ATP 4-0.6 is the United States Army Combined Arms Support Command. The preparing agency is the G-3/5/7 Doctrine Division, United States Army Combined Arms Support Command. Send comments and recommendations on a DA Form 2028 ( _Recommended Changes to Publications and Blank Forms_ ) to Commander, United States Army Combined Arms Support Command, ATTN: ATCL-TDID (ATP 4-0.6), 2221 A Avenue, Building 5020, Fort Lee, VA 23801-1809 or submit an electronic DA Form 2028 by e-mail to: usarmy.lee.tradoc.list.cascom-g3-5-7-tdid-doc@army.mil. 

**17 January 2024** 

**ATP 4-0.6** 

**iii** 

This page intentionally left blank. 

### **Introduction** 

_Sustainment Automation Support Management Office Operations_ is a title change from the previous edition of ATP 4-0.6. The new title reflects this publication’s shift in focus. The previous version focused on information technology. This edition focuses on SASMO operations as information management and the section’s significance in knowledge management for the delivery of sustainment products and services. SASMOs maintain the automation employed by all four of the sustainment elements (logistics, financial management, personnel services, and health service support). This revision reflects the Army’s shift to multidomain operations with a continued emphasis on large-scale combat operations against peer threats. 

The information environment is a significant part of what makes the operational environment complex. It includes cyberspace, the electromagnetic spectrum, data flow, encryption and decryption, the media, biases, perceptions, decisions, managers, and leaders. Sustainment automation is the combination of all sustainment transport systems, enterprise business systems, information collection devices, and decision support tools used to collect, store, display, and disseminate information. These include computer hardware and software as well as policies and procedures governing information management processes. This combination includes the development, maintenance, sustainment, and security of all communications devices, networks, systems, and associated contracts. 

The Army is becoming increasingly dependent upon its extensive suite of enterprise business systems. The SASMO role is to perform systems administration for select sustainment enterprise business systems and network administration for the sustainment transport system. Network and systems administration ensure the readiness of the tools depended upon by leaders and staffs for collecting, interpreting, and broadcasting data between sustainment providers, supported units, staff sections, and echelons. Network administration is the most important and most complex day-to-day operation the SASMO performs. SASMOs do not perform hardware maintenance because assigned military occupational specialties are not trained in computer or communications equipment repair. 

Systems administration involves updating software, troubleshooting, and other technical support. Network administration involves installing and maintaining the data transport infrastructure (video, voice, and data); maintaining local area networks and wide area networks; maintaining network security of routers and transmission systems; and troubleshooting physical layer network problems. SASMOs perform cybersecurity functions (identify, protect, detect, respond, and recover) according to the prescribed risk management framework. SASMOs track trends and historical data to preserve confidentiality, integrity, and availability of the enterprise business systems, applications, and networks for which they are responsible. 

ATP 4-0.6 contains five chapters and one appendix: 

**Chapter 1** describes the SASMO in the broader context of the Army. 

**Chapter 2** contains information about where the SASMO fits into the overall Army organizational structure and the elements with which the SASMO interacts. 

**Chapter 3** provides introductory information about the automation supported. 

**Chapter 4** describes the SASMO as part of the distribution network infrastructure. 

**Chapter 5** provides an overview of internal SASMO operations. 

**Appendix A** discusses formal platform training, gunnery testing, and provides a list of courses recommended by product developers. 

**17 January 2024** 

**ATP 4-0.6** 

**v** 

This page intentionally left blank. 

##### **Chapter 1** 

### **SASMO Overview** 

The sustainment automation support management office provides sustainment automation support to sustainment and maneuver units. This chapter provides an overview of sustainment automation operations. 

#### **FUNDAMENTALS** 

1-1. Every Army unit relies on the sustainment automation that is supported by sustainment automation support management offices (SASMOs). SASMOs provide network administration and Tier 0/Tier 1 systems administration. They also provide sustainment expertise on select applications, Global Combat Support System-Army (GCSS-Army), Integrated Personnel and Pay System-Army (IPPS-A), Operational Medical Information Systems-Army (OMIS-A), and Financial Management Tactical Platform (FMTP). Depending on unit of assignment, the SASMO is organic to either the support operations (SPO) section or distribution management center (DMC). The SASMO is the only Army section that supports the warfighter with sustainment expertise (limited), systems administration, and network administration. 

1-2. Two of the most critical tools used by sustainers are enterprise business systems (EBSs) and the sustainment transport system (STS). The EBS is used for day-to-day operations. The STS transports data among leaders, staffs, and sustainment managers. These systems help commanders and staffs understand the operational environment (OE). 

1-3. A significant part of what makes the OE complex is the information environment. The information environment includes cyberspace, the electromagnetic spectrum, data flow, encryption and decryption, the media, biases, perceptions, decisions, managers, and leaders. 

#### **SASMO ROLE** 

1-4. The SASMO role consists of two parts: 

- ⚫ Network administration—provides end-to-end connectivity for the sustainment warfighting function (logistics, financial management, personnel services, and health service support). 

- ⚫ Systems administration—ensures the readiness of the EBSs relied upon by leaders and staffs for collecting, interpreting, and broadcasting data between providers, units, staff sections, and echelons. 

**_Note:_** SASMOs do not perform hardware maintenance because assigned military occupational specialties are not trained in computer or communications equipment repair. 

1-5. The Army’s EBSs require continuous network access to support command and control, decision making, and generating readiness across the warfighting functions. SASMO technicians, consisting of signal and sustainment Soldiers, facilitate data transport over a footprint that may extend over thousands of square miles. 

1-6. The STS replaces legacy system equipment known as the Combat Service Support Very Small Aperture Terminal (CSS VSAT) and the Combat Service Support Automated Information System Interface (CAISI). STS’s modernization and its convergence with the Army tactical network provide more effective and secure sustainment communications while streamlining materiel and support requirements for the network. The STS is comprised of three elements. 

- ⚫ Satellite communications (SATCOM) terminal systems for beyond-line-of-sight communications. 

**17 January 2024** 

**ATP 4-0.6** 

**1-1** 

**Chapter 1** 

- ⚫ Wireless capability that provides Wi-Fi to support multiple sustainment applications. 

- ⚫ Line-of-sight capability that extends connectivity between distant Wi-Fi enclaves. 

1-7. Knowledge management and information management are actions that support decision-making. Information management consists of procedures and information systems. SASMOs execute the information management process that enables knowledge management. Figure 1-1 on page 1-4 illustrates the complexity of collecting, processing, and transforming data into usable information by sustainers. Leaders and planners execute data analytics to refine information into knowledge. Commanders and staffs apply judgment to transform information into knowledge. See FM 6-0 and ATP 6-01.1 for more information about knowledge management. Sustainment automation is the physical dimension that enables information sharing when merged into a single, integrated network. 

1-8. Six information management tasks enable knowledge management and facilitate situational understanding and decision-making. The six tasks are: collect, process, store, display, disseminate, and protect. Knowledge provides meaning or value for the operation. It is gained through study, experience, practice, and human interaction and is the basis for expertise and skilled judgment. Knowledge management aligns an organization's people, processes, and tools to distribute knowledge and promote shared situational understanding. The tools are non-digital, digital, or a combination of the two. Digital tools include information systems storage, inputs, processing, outputs, formats, content, software, and capabilities. 

##### **NETWORK ADMINISTRATION** 

1-9. Sustainment network connectivity enables delivery of logistics, personnel services, financial management, and Army Health System services. SASMOs set up and operate the STS at every echelon from theater to tactical level, which entails mapping units and applications on the network. Sustainment automation is typically widely separated, often beyond line-of-sight distances from command posts and tactical operations centers. Units are responsible for setting up their own CSS VSATs or STS (future). 

**Note:** Effective use of EBSs depends upon the STS to transport data among the sustainment and the maneuver leaders and staffs. 

1-10. The Army has long maintained separate tactical transport networks to support the communications requirements of different functional areas—command and control, intelligence, logistics, and medical. A unit uses four separate SATCOM terminals and four sets of networking hardware with all the associated manning, physical security, configuration and patching, and logistics support requirements; four separate operations chains of authority; and up to four separate commercial satellite leases. The Army is working to unify these networks to make better use of resources and assets, leverage existing infrastructure, increase network security, and simplify network administration while reducing reliance on leased commercial satellite resources. 

1-11. SASMOs install, operate, and secure the STS in locations where friendly and enemy cyberspace operations occur. The STS, previously known as the logistics network (called LOGNet), has been in operation since 2004. The STS is separate from Army's tactical network, the Department of Defense Information Network-Army (DODIN-A). The DODIN-A is an Army-operated enclave of the Department of Defense information network (DODIN). Network administration ensures the functionality and performance of the network infrastructure to provide the desired level of services. Network administration involves critical capabilities associated with information technology (IT) services. The critical capabilities for network management are— 

- ⚫ Fault management. This includes incident management and problem management and is associated with failure of the network or information systems, which impacts connectivity and functionality. Fault management involves a five-step process of detecting faults, locating faults, restoring services, identifying the root cause of the fault, and establishing solutions so that similar faults do not occur in the future. 

- ⚫ Configuration management. This is used to discover specific network and information system architecture requirements and then develop configuration parameters. Network and information systems are designed and built according to the needs of the end users. The product is referred to 

**1-2** 

**ATP 4-0.6** 

**17 January 2024** 

**SASMO Overview** 

as the architecture. Configuration parameters deal with establishing and maintaining the consistency of the network and information systems. 

- ⚫ Performance management. This includes monitoring and managing parameters related to networks and information systems. It involves data monitoring, problem isolation, performance tuning, and analysis of statistical data to identify trends, resource planning, and proactive management of network performance. 

1-12. Every aspect of Army operations from the highest echelon commander to EBS operators relies on networked communications. The SASMO manages, maintains, and restores tactical sustainment communication networks by addressing vulnerabilities and improving systems security. SASMOs track trends and historical data to preserve confidentiality, integrity, and availability of all forms of information systems, applications, and networks for which they are responsible. Connectivity integrates sustainment automation into the mission and enables delivery of sustainment support required by the warfighter. The Army tactical network does not fully extend to dispersed and forward deployed sustainment units leaving a substantial communications gap that is filled by the STS. SASMOs perform cybersecurity functions (identify, protect, detect, respond, and recover) according to higher headquarters prescribed risk management framework. Refer to DODI 8510.01 for detailed information. 

1-13. Network operations are the most important and most complex day-to-day operation the SASMO performs. STS operations require deliberate planning because the STS is the foundation for all distribution management functions and has a wide-ranging impact on the information environment. STS operations should be a commander-focused activity. The SASMO teams prepare STS operations plans and courses of action that align available communication and network support to the highest mission priorities. 

**Note:** Network operations are not individual or crew tasks, but multifaceted military operations that take place at all echelons. 

1-14. Given the threats to the network, SASMOs continuously mitigate cybersecurity risks to secure the STS. SASMOs perform the network operations and security functions of monitoring the health of the network and directing fault, configuration, accounting, performance, and security management. See ATP 6-02.60 for indepth information about network operations. As the network administrator, the SASMO installs and maintains the transport infrastructure (video, voice, and data); installs, operates, and maintains local area networks (LANs); maintains network security of routers and transmission systems; and troubleshoots physical layer network problems. Network administrators react to a network intrusion by speedily countering effects of an incident on the network. SASMOs initiate their disaster recovery response processes to halt the breach and restore essential information services. SASMOs maintain network security through the following activities: 

- ⚫ Data backup and migration. 

- ⚫ Website interface maintenance. 

- ⚫ Monitoring and protecting the STS. 

- ⚫ Responding to STS outages or attacks. 

- ⚫ Reporting on STS outages or attacks. 

- ⚫ Troubleshooting. 

- ⚫ Submitting service access requests to the integrated network operation center every 90 days. 

- ⚫ Coordinating and cooperating with the G-6 or S-6. 

**17 January 2024** 

**ATP 4-0.6** 

**1-3** 

**Chapter 1** 



**Figure 1-1. Distribution management process** 

**1-4** 

**ATP 4-0.6** 

**17 January 2024** 

**SASMO Overview** 

##### **SYSTEMS ADMINISTRATION** 

1-15. The SASMO provides technical and functional assistance to its supported units. Technical and functional services include the diagnosing and troubleshooting of software, hardware, and communication interfaces. It is more economical for the government to purchase and field items with contract maintenance and warranties rather than develop its own Service-unique test and maintenance equipment and support infrastructure. Most EBSs are protected by a contracted maintenance plan established during the procurement process. As a result, SASMOs work closely with the program management offices’ logistics assistance representatives and liaison officers for assistance with technical and functional systems problems. 

1-16. The decision to centralize or decentralize the fielding of new sustainment automation depends upon the organization, available facilities, and its geographical location. SASMOs may assist with new sustainment automation fielding. This requires close coordination with the new equipment training teams, property book office, and supported units. SASMOs may work with the sustainment automation developers to simplify new equipment fielding to reduce disruption to the unit and its mission. The new equipment fielding team provides training related to the fielding, ensures that each new system is operational, and then helps the unit transfer files from the old to the new system. 

**Note:** Contracted Army Sustainment Command regional SASMOs are not equipped and do not have the depth to execute new equipment fielding for the Logistic Readiness Centers, Continental Army Pre-Positioned Stocks site, and the continental United States (U.S.) Army garrisons. 

1-17. See Figure 1-2 for an example of information that the SASMO might report to the SPO officer, S-4 or G-4, or higher headquarters during fielding of sustainment automation. 



**Figure 1-2. Notional combat service support very small aperture terminal fielding report** 

**_Note:_** SASMOs are not responsible for equipment inventory, physical security, equipment setup, or disassembly for supported activities. 

**17 January 2024** 

**ATP 4-0.6** 

**1-5** 

**Chapter 1** 

#### **SUSTAINMENT AUTOMATION DEFINED** 

1-18. Sustainment automation encompasses the STS, EBSs, information collection devices, and automated decision support tools used to collect, store, display, and disseminate sustainment information. This also includes computer hardware and software as well as policies and procedures governing information management processes. The management processes include the development, maintenance, sustainment, and security of all communications devices, networks, systems, and associated contracts. See AR 25-1 for a complete discussion of IT policy. 

1-19. Sustainment automation is not only an IT asset but also, in accordance with the Army Unified Network Plan, a basic weapons system for operations. EBSs generate enormous volumes of data. It is critical that data be of high quality, accurate, complete, timely, and protected to allow staffs to turn the data into knowledge used to inform command decisions. This is explained further in the Department of Defense Data Strategy. 

1-20. Data generated by sustainment automation enables leaders to make effective decisions through the application of information management and knowledge management. Sustainment automation allows commanders and staffs to process the volume of sustainment-related data generated during combat operations. 

1-21. EBSs integrate basic business processes (taking orders, processing requisitions, monitoring inventory levels, financial accounting, and human resource management) from the tactical through strategic level. Commanders and staffs use web-based EBSs to develop a real-time and near-real-time sustainment common operational picture. The sustainment common operational picture provides commanders with a snapshot of battlefield support that is critical to extend operational reach, enable freedom of action, and prolong endurance. 

1-22. An information network linked by tactical satellite and ground telecommunications equipment connects all echelons of sustainment. When functioning properly, IT adds precision to the sustainment mission because it facilitates more accurate budgeting, planning, and forecasting. It enhances the ability to communicate status; monitor near, mid, and long-term capabilities; and anticipate requirements. Properly maintained sustainment automation enables shared situational awareness among all echelons within the four elements of the sustainment warfighting function to— 

- ⚫ Analyze force requirements and sourcing to support multidomain operations. 

- ⚫ Identify materiel requirements, select supply sources, acquire materiel, schedule deliveries, and receive, store, and issue all classes of supply. 

- ⚫ Assess the transportation workload capacity of each route by mode, the capabilities at each node, available transportation assets, loading and unloading capability (materials handling equipment, ramps), storage capability, and any other factors that affect transportation services. 

- ⚫ Coordinate health service support, providing direct patient care, medical evacuation, and medical logistics. 

- ⚫ Establish theater personnel accountability and personnel tracking. 

- ⚫ Establish and operate a theater casualty information center. 

- ⚫ Conduct casualty operations. 

- ⚫ Establish a military mail terminal. 

- ⚫ Estimate intra-theater mail movement. 

- ⚫ Assess the four distribution networks (physical, information, communication, and financial). 

- ⚫ Ensure protection. 

**_Note:_** Automation is a tool for maintaining and gathering information; it is not the decision maker. It takes human interaction coupled with automated procedures to manage logistics, financial management, personnel services, and the health service support. 

**1-6** 

**ATP 4-0.6** 

**17 January 2024** 

**SASMO Overview** 

#### **ROLES AND RESPONSIBILITIES IN A WEB-BASED ENVIRONMENT** 

1-23. SASMOs provide mission critical services to their supported units. Because no other element in the Army has the responsibility to support sustainment automation, SASMO sections should be fully trained and manned for optimal performance. This enables them to provide protection against cyber-attacks to ensure network access for mission-capable workstations. Maneuver and sustainment leaders at all levels are responsible for ensuring that unified network tactical assemblages (for example, CSS VSAT) and EBS are operational to provide access to the sustainment enterprise architecture. 

1-24. The G-6 or S-6, the SASMO, and the communication and electronics maintenance shop appear to perform identical functions. While some functions are alike, each element operates independently with a distinct focus that the other two do not have. Materiel managers also have a role in maintaining sustainment automation. See Table 1-1 for specific responsibilities performed by the materiel managers, G-6 or S-6, SASMO, and the maintenance activities with communications and electronics repair capabilities. 

1-25. The SASMO enables knowledge management by providing network architecture and maintaining the technological tools necessary to support content management and knowledge-sharing exclusively for EBS and the STS. The G-6 or S-6 enables knowledge management by providing network architecture and maintaining the technological tools necessary to support content management and knowledge-sharing exclusively for the command systems and the tactical network (see ATP 6-02.45 for more information about the tactical network). The SASMO determines sustainment automation requirements and compares them to available assets, identifies potential shortfalls, and recommends actions to eliminate or reduce their effects exclusively for EBS and the STS. The G-6 or S-6 determines communications systems requirements and compares them to available assets, identifies potential shortfalls, and recommends actions to eliminate or reduce their effects exclusively for the command systems and the tactical network. 

1-26. Maintenance companies provide field-level maintenance for ground equipment, armament, and communications and electronics. They also provide allied trades, recovery, and repair parts support. Communications and electronics maintenance shops focus on repair or replacement of end items, line replaceable units, shop replaceable units, modules, subassemblies, subcomponents, circuit card assemblies, plug-in units, and repair parts; fault verification; and troubleshooting assistance. They do not maintain sustainment applications, command systems applications, or perform network administration. See ATP 4-33 for information about Army maintenance processes and procedures. 

1-27. All sustainment automation is an authorized line on the modified table of organization and equipment and the table of distribution and allowance. The property book office, located in the G-4 or S-4, maintains accountable records of assigned nonexpendable property. Sustainment automaton is typically managed by serial number and hand-receipted to the company commander and then to the operator. Through coordination with the supporting maintenance activity, materiel managers decide to repair or replace unserviceable IT hardware and communications assemblages. If the SASMO finds a hardware or assemblage problem, the operator may be directed to turn-in the unserviceable item to the unit supply room or supply support activity. SASMOs are not issued hardware or assemblages for replacement of operator unserviceable equipment. The operator’s property book office returns the unserviceable hardware or assemblage to the supply system. The supply system replaces the unserviceable equipment through the property book office. See ATP 4-42 for information about unit supply and property book operations and procedures. 

**17 January 2024** 

**ATP 4-0.6** 

**1-7** 

**Chapter 1** 

**Table 1-1. Hardware, systems, and network support** 

||**_Element_**|**_STS_**<br>**_Network_**<br>**_Admin_**|**_EBS_**<br>**_Systems_**<br>**_Admin_**|**_Cyber_**<br>**_Security_**|**Tactical**<br>**Network**<br>**Admin**|**_Hardware_**<br>**_Repair_**|**_Repair or_**<br>**_Replace_**<br>**_Decision_**|
|---|---|---|---|---|---|---|---|
|SASMO||Yes|Yes|Yes|No|No|No|
|S-6/G-6||No|No|Yes|Yes|No|No|
|C&E Ma|intenance Section|No|No|No|No|Yes|No|
|PBO/Ma|teriel Manager|No|No|No|No|No|Yes|
|**Admin**|administration||**PBO**|property b|ook office|||
|**C&E**|communication and elec|tronics|**S-6**|battalion o|r brigade sign|al staff officer||
|**EBS**<br>**G-6**|enterprise business syst<br>assistant chief of staff, s|em<br>ignal|**SASMO**<br>**STS**|sustainme<br>sustainme|nt automation<br>nt transport sy|support manage<br>stem|ment office|



**1-8** 

**ATP 4-0.6** 

**17 January 2024** 

##### **Chapter 2** 

### **Sustainment Automation Organizational Structure** 

Sustainment automation support involves complex activities that require SASMO teams to coordinate with signal elements, system developers, supported unit operators, and supported unit staff sections. This chapter discusses the organizations that provide guidance, technical information, and technical assistance. There is also a brief discussion of the staff sections supported by the SASMO teams for familiarization with the roles of these elements. 

#### **SUSTAINMENT AUTOMATION SUPPORT BY ECHELON** 

2-1. The following organizations have SASMOs within their command. This publication will only discuss organizational roles, core competencies, or characteristics that are directly related to SASMO operations. See the appropriate doctrinal publication for in-depth discussion. 

2-2. The higher echelon SASMO is responsible for establishing sustainment automation plans, policies, and procedures and providing visibility of sustainment automation readiness. Higher echelon SASMOs serve as systems integrators for their areas of responsibility (AORs). These SASMOs coordinate new EBS and communication assemblage fielding, software changes, cyber security, and any other sustainment automation actions requiring coordination between agencies within and outside the commands. 

2-3. Lower echelon SASMOs implement higher headquarters’ sustainment automation plans, policies, and procedures. They submit the service access request for CSS VSAT. They perform testing and hardware troubleshooting but do not perform hardware maintenance. SASMO personnel function at Information Assurance Technical Level I (minimum) as prescribed by DODM 8140.03 and AR 25-2. They execute systems administration, network administration, and cybersecurity in the organizations introduced in the following paragraphs. Network administration involves installing and maintaining the sustainment data transport infrastructure (video, voice, and data); installing, operating, and maintaining LANs and wide area networks; maintaining network security of routers and transmission systems; and troubleshooting physical layer network problems. Systems administration involves tracking trends and historical data to preserve confidentiality, integrity, and availability of the EBS applications for which they are responsible. System administration involves serving as the focal point for new EBS fielding, software changes, engineer change proposals, and other sustainment automation actions for the command. Cybersecurity functions involves identify, protect, detect, respond, and recover according to the prescribed risk management framework. 

##### **THEATER ARMY** 

2-4. The theater Army's primary role is as the Army Service component command (ASCC) assigned to a combatant commander. As the ASCC, it is responsible for administration and support of all Army forces assigned, attached, or under the operational control of the combatant commander or transiting the AOR (see ATP 3-93). The theater Army receives SASMO support through an attached theater sustainment command (TSC), enabling it to provide— 

- ⚫ Sustainment estimates that outline the responsibilities and requirements for setting the theater. 

- ⚫ AOR-wide distribution, recovery, and redistribution of materiel and troop movement. 

**17 January 2024** 

**ATP 4-0.6** 

**2-1** 

**Chapter 2** 

##### **ASCC G-4 LOGISTICS OPERATIONS AUTOMATION ELEMENT** 

2-5. The ASCC G-4 logistics operations automation element establishes sustainment automation policy and coordinates with the TSC SASMO. Their coordination includes designing the systems architecture for the STS and monitoring its operational status across the AOR. 

##### **THEATER SUSTAINMENT COMMAND** 

2-6. The TSC is a theater enabling sustainment command that connects strategic enablers to tactical formations. The TSC integrates and synchronizes sustainment support to Army and unified action partners conducting military operations across a multidomain battlefield. The TSC is tailorable and task organized. It can be augmented as necessary with a combination of combat sustainment support units and functional logistics units based on the mission. The TSC SASMO responsibilities include executing ASCC sustainment automation policy and designing the systems architecture for the STS to ensure connectivity at the theater echelon. The SASMO serves as the focal point for new EBS fielding, software changes, engineer change proposals, and other sustainment automation actions for the ASCC, to include coordination with organizations external to the command. 

##### **EXPEDITIONARY SUSTAINMENT COMMAND** 

2-7. An expeditionary sustainment command (ESC) may be attached to the TSC under a theater Army, directly to a theater Army, or to a corps within a subordinate area of operations (AO) or joint operations area within the geographic theater. When attached to the TSC, the ESC typically executes the sustainment mission for the TSC throughout the AOR. When an ESC is attached to a field army or assigned to a corps, it focuses on sustaining the specific AO or joint operations area and only has a coordinating relationship with the TSC. During large-scale combat operations, multiple ESCs may be operating in the same theater. One or more could be attached to the TSC or field army and one or more could be assigned to a corps. 

2-8. The ESC SASMO establishes sustainment automation policy, designs the systems architecture for the STS, and monitors its operational status across the corps. The ESC SASMO serves as the focal point for new EBS fielding, software changes, engineer change proposals, and other sustainment automation actions for the corps, to include coordination with organizations external to the command. 

##### **SUSTAINMENT BRIGADE** 

2-9. The sustainment brigade is a multifunctional headquarters that integrates and employs all assigned and attached units while planning and synchronizing sustainment operations (see ATP 4-93). It is the Army’s primary brigade-level sustainment headquarters. The sustainment brigade supports Army forces at the tactical and operational levels, providing support to brigade combat teams (BCTs); multifunctional and functional support brigades; deployable, self-contained division and corps headquarters; and other units operating in its assigned support area. Depending upon operational and mission variables, the sustainment brigade commands between three and seven battalions. Sustainment brigades are usually assigned or attached to a sustainment command. The sustainment brigade and its attached units will normally have a general support relationship with supported organizations. Figure 2-1 depicts the SPO staff section in a sustainment brigade. 

**2-2** 

**ATP 4-0.6** 

**17 January 2024** 

**Sustainment Automation Organizational Structure** 



**Figure 2-1. Sustainment brigade SPO staff** 

##### **COMBAT SUSTAINMENT SUPPORT BATTALION** 

2-10. The combat sustainment support battalion (CSSB) is a multifunctional logistics headquarters (see ATP 4-93.1). It is task organized with capability required to support specified mission requirements. The CSSB supports echelon above brigade units, multifunctional brigades (maneuver enhancement, field artillery, and combat aviation brigades), functional support brigades (military police, signal, and engineer brigades), and BCTs. The CSSB may support Army special operations forces as part of their area support task. Figure 2-2 depicts a CSSB staff. 



**Figure 2-2. Combat sustainment support battalion staff** 

**17 January 2024** 

**ATP 4-0.6** 

**2-3** 

**Chapter 2** 

##### **CORPS** 

2-11. The corps headquarters is the Army’s primary operational-level headquarters. It controls Army forces engaged in multidomain operations and identifies requirements and establishes priorities to support Army forces conducting sustaining operations for units within the corps AO. The corps headquarters can command Army divisions, BCTs, functional and multifunctional brigades, and joint and multinational forces engaged in crisis response, limited contingency operations, and during major operations and campaigns across the conflict continuum. The corps headquarters is deployable and scalable. (See ATP 3-92 and ATP 4-92.) 

##### **DIVISION** 

2-12. A division is an Army echelon of command above brigade and below corps. It is a tactical headquarters which employs a combination of BCTs, multifunctional brigades, and functional brigades in land operations. As a tactical echelon of command, the division commander task-organizes subordinate units and specifies the command or support relationships of those subordinate units. The division headquarters is a self-contained organization with a command group and a fully functional staff, which requires limited staff support from subordinate units to provide functional staff capabilities for its primary role as a tactical headquarters. The division headquarters provides a flexible base where the division commander can command and control and execute decision-making. (See ATP 3-91 and ATP 4-91.) 

##### **DIVISION SUSTAINMENT BRIGADE** 

2-13. The division sustainment brigade and its subordinate units provide sustainment support to all units assigned or attached to the division. The division sustainment brigade depends on the division staff for longrange planning capability. It may command up to seven battalions based on operational and mission variables. A division sustainment brigade includes an organic division sustainment troops battalion and an organic division sustainment support battalion to support tactical-level sustainment operations. Additional modular CSSBs and companies may be attached to a division sustainment brigade to sustain large-scale combat operations. The staff of the division sustainment brigade SPO section is depicted in Figure 2-3. 



**Figure 2-3. Division sustainment brigade** 

##### **BRIGADE SUPPORT BATTALION** 

2-14. The brigade support battalion (BSB) supports the BCT and the other brigade formations that constitute most of the close combat capability in the Army. The BCT AO is expansive and its missions diverse. The BSB provides logistics and medical support to a BCT and multifunctional support brigades. The BSB SASMO executes division sustainment automation policy (for additional information see ATP 4-90). 

##### **FIELD ARTILLERY BRIGADE SUPPORT BATTALION** 

2-15. A field artillery brigade’s primary task is to provide fires and precision strike by employing joint and organic fires capability. The field artillery brigade is comprised of a combination of rocket and cannon artillery systems to support a corps, division, or BCT. The field artillery brigade is not organic to any Army organization or echelon but often has a habitual relationship with a specific division or corps. 

**2-4** 

**ATP 4-0.6** 

**17 January 2024** 

**Sustainment Automation Organizational Structure** 

##### **COMBAT AVIATION BRIGADE AVIATION SUPPORT BATTALION** 

2-16. The aviation support battalion consists of a headquarters support company, a distribution company, an aviation support company, and a brigade signal company. The aviation support battalion provides aviation and ground field maintenance, ground and aviation recovery, network communications, resupply, and Role 1 medical support for the combat aviation brigade. The aviation support battalion provides maintenance augmentation to aviation battalions when required. The battalion supports the forward support elements, aviation maintenance elements, the brigade headquarters and headquarters company, and the unmanned aircraft systems, if applicable. 

#### **TECHNICAL CHANNELS** 

2-17. SASMOs should work closely with the signal community and EBS product managers to remain up to date on EBS changes and the measures to combat electromagnetic warfare and cyber-attacks. This section provides brief high-level descriptions of the signal echelons and the product managers that shape the day-today complexity of SASMO operations. 

##### **SIGNAL** 

2-18. Signal elements that support theaters are typically under the operational control of the theater Army or ASCC. The theater-level signal commander is dual-hatted as the theater Army or ASCC G-6. The theaterlevel signal command plans, engineers, installs, operates, maintains, and defends communications and information systems in support of theater Army headquarters, subordinate Army units, and joint and multinational organizations throughout the AOR as required. While the signal commands are not deployable, they can deploy various capabilities to support specific mission requirements. Signal commands have one or more theater network operations and security centers assigned, which serve as the operational arm for network operations. The theater network operations and security centers are under the operational control of Army Cyber Command (ARCYBER) for day-to-day defense of the Army's portion of the global information grid. They do include SASMOs in their planning and cybersecurity considerations. 

###### **Chief Information Officer** 

2-19. The chief information officer (CIO) is the principal staff assistant and advisor to the Secretary of the Army for information management and IT. The CIO establishes policy for Army use of IT systems and networks. This responsibility includes evaluating existing Army information management and IT policies and overseeing their implementation. The CIO sets the strategic direction for, and supervises the execution of, Army information management programs and policy. These include network architecture, information sharing policy, cybersecurity policy, the Army cybersecurity program, resource management, process modernization, and synchronization of the Army’s network activities. 

###### **Assistant Chief of Staff, Signal** 

2-20. The G-6 is the principal staff officer for integration and management of the tactical network command networks for the theater signal commands, theater network operations, and security centers, ensuring the TSC has interoperability with joint and multinational networks. The G-6 also collaborates with the TSC and ASCC knowledge management officers to enable information producers and consumers the ability to share information. Subordinate G-6s or S-6s monitor the health of the tactical network. They also direct the management of network faults, configurations, resource allocation, performance, and security in support of the command. The G-6 or S-6 also manages network transport, network services, communications security, and the viability of information systems. Neither the G-6 nor S-6 administer the STS. However, the G-6 or S-6 includes SASMO operations in electromagnetic warfare plans to ensure the security of the STS. The SASMO must understand the electromagnetic warfare plan to mitigate STS vulnerability to enemy efforts. (See JP 3-85 for more information about electromagnetic spectrum operations.) 

**17 January 2024** 

**ATP 4-0.6** 

**2-5** 

**Chapter 2** 

###### **United States Army Cyber Command** 

2-21. ARCYBER is the primary Army headquarters responsible for cyberspace operations that support joint requirements. It is the single point of contact for reporting and assessing cyberspace incidents, events, and operations in Army networks, and for synchronizing and integrating Army responses. When directed, ARCYBER conducts offensive and defensive cyberspace operations to support other Army operations, ensures U.S. and allied freedom of action in cyberspace, and denies the same to adversaries and enemies. ARCYBER provides appropriate-level interactions both as a supported and as a supporting command to Army commands, other ASCCs, direct reporting units, and joint, interorganizational, and multinational elements. 

###### **_Army Cyber Operations and Integration Center_** 

2-22. The Army Cyber Operations and Integration Center is an operational element of the ARCYBER headquarters. It is the top-level control center for Army cyberspace activities that provides situational understanding for Army networks and situational awareness of the wider DODIN (and the STS). It also provides worldwide operational signal support by Army echelon in coordination with the theater Armies. The Army Cyber Operations and Integration Center directs the regional cyber centers through operational channels. It interfaces with the functional network operations (includes the STS) and security centers, and coordinates with other Service and agency DODIN operations centers through technical channels. Figure 2-4 illustrates a notional technical channel coordination map with the SASMO. 



**Figure 2-4. Technical channel coordination map** 

2-23. The Army Cyber Operations and Integration Center analyzes threat information and directs network security actions through the regional cyber centers, in coordination with theater Armies. It develops technical solutions to secure Army networks and helps Army units and regional cyber centers implement cybersecurity policy. (Refer to ATP 6-02.71 for more information about the Army Cyber Operations and Integration Center.) 

**2-6** 

**ATP 4-0.6** 

**17 January 2024** 

**Sustainment Automation Organizational Structure** 

###### **_United States Army Network Enterprise Technology Command_** 

2-24. The United States Army Network Enterprise Technology Command is the Army’s global enterprise network service provider. It is subordinate to ARCYBER, provides global DODIN operations oversight, and performs inter-theater DODIN operations functions to ensure interoperability across the DODIN-A. It enforces Army-wide standards established by the CIO and the G-6 to preserve joint, interorganizational, and multinational interoperability. 

2-25. The  U.S. Army Network Enterprise Technology Command integrates Army IT to achieve a single, virtual enterprise network. It enforces service delivery activities, cybersecurity policies, and processes, procedures, and protocols for operation of Army networks. To ensure unity of effort in DODIN operations, the U.S. Army Network Enterprise Technology Command has direct liaison authority to the CIO, with notification to ARCYBER. 

2-26. The U.S. Army Network Enterprise Technology Command manages the DODIN-A, including enforcing technical standards and configuration management. It is the single-entry point to submit validated, approved telecommunications requirements for coordination and implementation by the Defense Information Systems Agency. 

##### **ENTERPRISE BUSINESS SYSTEM DEVELOPERS** 

2-27. SASMOs rely upon the program management offices for technical assistance and guidance. EBS developers inform the SASMOs when systems are changed, where the changes are located, and how to update the systems. Program managers, project managers, product managers, and IT materiel developers develop and acquire technical support solutions and ensure they are within the policy and guidance constraints of the Army Enterprise architecture. The Army Enterprise architecture defines the baseline architecture, a target architecture, and a sequencing of plans to match the mission. Developing the Army Enterprise architecture involves the technologies and the transition processes for implementing new organizations, processes, and technologies in response to changing mission needs. SASMOs interact with and rely upon the program managers for guidance and technical support throughout each system’s lifecycle that includes the following: 

- ⚫ Software and firmware updates. 

- ⚫ Implementation guides. 

- ⚫ Fielding guidance. 

###### **United States Army Materiel Command** 

2-28. United States Army Materiel Command (USAMC) develops and acquires sustainment technology through its subordinate life cycle management commands. USAMC oversees 10 major subordinate commands that provide materiel life-cycle management for USAMC and the Army. Together they develop and acquire sustainment technology to support Army operations. 

###### **Program Executive Office-Enterprise Information Systems** 

2-29. The mission of the Program Executive Office-Enterprise Information Systems (an element of Assistant Secretary of the Army for Acquisition, Logistics and Technology), is to enable information dominance by developing, acquiring, integrating, and deploying enterprise-wide, network-centric information management and communications to meet the Army’s current and future mission requirements. Its vision is to rapidly deliver cost-effective, easy-to-use, IT-based capabilities to the Army Enterprise. It provides products and services that cover support for the Army and Department of Defense (DOD) including financial, personnel, health service support, logistics, and communications infrastructure support. 

###### **_Product Manager, Defense Communications and Army Transmission Systems_** 

2-30. Product Manager, Defense Communications and Army Transmission Systems manages a suite of projects that support servicemembers, major commands, and combatant commanders worldwide. Projects include strategic SATCOM and wideband control systems, long-haul terrestrial microwave and fiber optic communications systems, tech control facilities, sustainment automation communications systems, critical power infrastructure, and combat vehicle intercom systems. 

**17 January 2024** 

**ATP 4-0.6** 

**2-7** 

**Chapter 2** 

###### **_Product Manager, Defense Wide Transmission Systems_** 

2-31. Product Manager, Defense Wide Transmission Systems manages projects including transmission systems, SATCOM systems, fiber optic networks, microwave networks, tech control facilities, power systems, wireless networks, and services including operation of network management centers. The company supports customers that include the Army, Marine Corps, Air Force, Defense Intelligence Agency, Surface Deployment and Distribution Command, and Department of State. 

###### **_Product Manager, Joint-Automatic Identification Technology_** 

2-32. Product Manager, Joint-Automatic Identification Technology is the Army product management office for total automatic identification technology and radio frequency identification solutions. It offers a single point of contact for acquisition support and technical expertise for Services, federal agencies, North Atlantic Treaty Organization, and multinational forces. It provides global asset tracking, web-based radio frequency in-transit visibility services, and program life cycle support. 

###### **_Project Manager, Global Combat Support System-Army_** 

2-33. Project Manager, GCSS-Army oversees the field enterprise resource planning component executing logistics support, implementing tactical financial processes relating to supply and maintenance. GCSS-Army is the primary tactical logistics enabler and combat multiplier. 

###### **_Product Lead Unified Network Capabilities and Integration_** 

2-34. Product Lead Unified Network Capabilities and Integration consolidates tactical network integration efforts for current, evolving, and future capabilities. It establishes best practices and provides a holistic approach to the delivery of a unified network. The product office supports the end-to-end integration of lineof-sight and beyond-line-of-sight tactical network transport systems and capabilities. These include hardware and software. The product lead is aligned with Army Futures Command objectives, including the Army Network Modernization Strategy and the incremental capability set design, acquisition, and fielding processes. 

###### **Combined Arms Support Command** 

2-35. The  Combined Arms Support Command is the functional proponent and capabilities developer that coordinates documentation, manpower, and equipment for sustainment automation requirements. USAMC, Department of the Army level assistant chief of staff G-4, and assistant chief of staff G-6 work closely with the Enterprise Systems Directorate to integrate combat capabilities for sustaining, bridging, and modernizing sustainment automation. 

#### **OPERATIONS COORDINATION** 

2-36. To understand the significance of systems and network administration, sustainment leaders should be familiar with all operations supported by the SASMO. Logistics, financial management, personnel services, and health service support systems enable Army sustainment with the capability to synchronize and integrate national and global resources. This section provides a brief description of the staff sections supported by sustainment automation and their functions. Each SASMO team member should not only be proficient in their military occupational specialty (MOS), but should also be capable of understanding the responsibilities of the operations they support to provide effective information management. 

##### **DISTRIBUTION MANAGEMENT AND INTEGRATION PROCESS** 

2-37. The distribution management process involves data pulls from multiple automated systems, manual requests for information, and coordination among many different elements. Sustainment operations on a multidomain battlefield require dispersed EBSs backed by a network with the capabilities to reduce the vulnerability of distribution operations. Network access is critical to sustainment operations and properly trained SASMO teams provide the expertise to maintain connectivity. Distribution and integration process managers rely upon EBSs and the STS for synchronizing and optimizing troop movement and movement of 

**2-8** 

**ATP 4-0.6** 

**17 January 2024** 

**Sustainment Automation Organizational Structure** 

materiel to meet combatant commander priorities. See Figure 2-5 for organizational relationships between SASMOs, their supported units, and their support structure. 



**Figure 2-5. Organizational relationships** 

##### **SUPPORTING SUSTAINMENT OPERATIONS** 

2-38. The SASMO supports staff sections by ensuring that the network is secure and that the EBSs are up to date. This requires continuous coordination and synchronization between the SASMO and staff sections to install, test, diagnose, and troubleshoot tactical, operational, and strategic sustainment automation software, hardware platforms, and peripheral devices. The following list of systems displays SASMO support across the four elements of the sustainment warfighting function. Chapter 3 contains a more comprehensive list of automation supported by the SASMO: 

- ⚫ GCSS-Army supports logistics. 

- ⚫ OMIS-A supports the Army Health System. 

- ⚫ FMTP supports financial management. 

- ⚫ IPPS-A supports personnel and pay services. 

- ⚫ CSS VSAT provides the network. 

- ⚫ CAISI provides wireless access points. 

###### **Logistics Staff Office** 

2-39. At the Department of the Army level, the G-4 provides sustainment automation governance, policy, and investment strategy. The G-4, in coordination with the G-6, focuses on sustaining, bridging, and 

**17 January 2024** 

**ATP 4-0.6** 

**2-9** 

**Chapter 2** 

modernizing sustainment automation; influencing and managing sustainment automation capability; managing sustainment automation investments; providing strategic communication and policy; and performing logistics domain data steward responsibilities and functions. The activities that impact the SASMO include the following: 

- ⚫ Developing sustainment automation policy and preparing sustainment automation plans for the Army. 

- ⚫ Developing, implementing, fielding, and sustaining logistics information systems. 

- ⚫ Designing systems architecture for sustainment automation to ensure connectivity from tacticallevel systems to the national systems. 

- ⚫ Ensuring that sustainment automation architecture supports command policies. 

- ⚫ Coordinating with the G-6/CIO to ensure sustainment automation complies with network architecture guidelines. 

- ⚫ Maintaining a common operational picture by monitoring the STS between tactical, operational, and strategic nodes. 

- ⚫ Monitoring and reporting the status of all sustainment automation equipment. 

- ⚫ Planning, integrating, and employing sustainment automation equipment. 

###### **Assistant Chief of Staff, Personnel** 

2-40. The G-1 or S-1 is responsible for all matters concerning human resources support, to include the EBSs that support personnel functions. Primary staff functions include planning and prioritizing human resources support to maximize the readiness and operational capabilities of forces. Specific responsibilities center on manning the force to build and sustain combat power and providing human resources services, postal support, and morale, welfare, and recreation operations support. 

###### **Assistant Chief of Staff, Financial Management** 

2-41. The G-8 is the commander’s principal advisor on financial management and chief of the financial management element. This staff section obtains guidance on policy, appropriations, and funding levels and provides it to tactical financial managers. The staff uses sustainment automation to prepare financial management plans and operations, financial management budget execution, and financial management special programs. 

###### **Surgeon** 

2-42. The surgeon provides clinical, medical, and technical control (to include EBSs supporting health services functions). This staff section plans, coordinates, and synchronizes Army Health System operations. The division surgeon is a member of the commander’s personal and special staff. The division surgeon is the principal advisor to the commander on the health status of the division and advises the division commander and staff on medical capabilities, capacities, and medical-related issues. The surgeon provides clinical, medical, and technical control to plan, coordinate, and synchronize the medical functions in operations plans and orders. The surgeon coordinates with many personal, special, and coordinating staff at higher, adjacent, and supported elements that may include Army special operations forces operating within the division’s AO. The surgeon staff section plans, coordinates, and synchronizes Army Health System support by tracking patients, assisting the G-1 with the patient aspect of reconciling the personnel status report, and receiving medical reports from operational medical units operating in the division AO. It tracks admissions and bed and cot status of all medical treatment facilities, status of medical evacuation platforms, and patients requiring aeromedical evacuation out of theater. It coordinates with the division G-4 and division sustainment brigade for distribution of Class VIII. The surgeon section uses sustainment automation to monitor the implementation of automated medical systems, with the patient administration or medical logistics sergeant in the SASMO playing a critical role in ensuring the medical regulation of patients out of the division area in large-scale combat operations. 

**2-10** 

**ATP 4-0.6** 

**17 January 2024** 

##### **Chapter 3** 

### **Sustainment Automation** 

Data analytics shorten decision cycles, lead to more informed decisions, and improve the success rate of the chosen course of action. SASMOs are not involved in data analytics. However, they ensure the readiness of the equipment described in this chapter that are used by leaders, staff, and managers to collect information for analysis. 

#### **AUTOMATION FUNDAMENTALS** 

3-1. The preceding chapters described how commanders and staffs use sustainment automation to make decisions, maintain situational awareness, and build a common operational picture. This chapter discusses the components of sustainment automation, which consists of the EBS and STS hardware and software employed throughout the Army. 

##### **HARDWARE** 

3-2. Hardware is the fundamental physical element for sustainment automation. Web-based sustainment IT provides the capability to use any common commercial off-the-shelf hardware products. Computer hardware consists of the following: 

- ⚫ Monitors. 

- ⚫ Keyboards. 

- ⚫ Mouse. 

- ⚫ Peripherals. 

- ⚫ Power backups and uninterrupted power supply. 

- ⚫ Printers. 

- ⚫ Cables. 

- ⚫ Common access card reader. 

- ⚫ Handheld devices. 

- ⚫ Network servers and firewall servers. 

- ⚫ Hubs, switches, and routers. 

- ⚫ CSS VSAT. 

- ⚫ CAISI. 

##### **SOFTWARE** 

3-3. Software includes the written programs, procedures, or rules and associated documentation pertaining to the operation of a computer system, stored in read only memory or programmable read only memory (typically called firmware). Closely related to software is computer code, which is made up of symbols from a source alphabet that is used to represent the set of rules that the program is expected to perform regardless of the purpose of the software. Software can be split into the following two main types: 

- ⚫ Application software or application programs include an accounts package or a computer-aided design program. Other broad classes of application software include real-time software, business software, scientific and engineering software, embedded software, personal computer software, and artificial intelligence software. 

**17 January 2024** 

**ATP 4-0.6** 

**3-1** 

**Chapter 3** 

- ⚫ System software is any software required to support the production or execution of application programs, but which is not specific to any application. Examples of system software would include the operating system, compilers, editors, and sorting programs. 

#### **NETWORK AND COMMUNICATIONS** 

3-4. The DOD considers data a strategic asset and the network a weapons system. Network communications enable the SPO or DMC distribution integrators to aggregate information to develop a distribution plan that will satisfy the requirements by commodity, troop movement, quantity, priority, recommended mode, route, and node. Since 2004, motor pools, supply points, SPOs, S-1s, aid stations, and many other activities have depended upon the logistics network, but technological advancements are making it obsolete. As a result, the Army developed the Army Unified Network Plan for network modernization that includes converging the tactical and logistics networks for an end-to-end capability in all operational domains (land, maritime, air, space, and cyberspace). The plan aligns to and underpins the Army's modernization priorities and supports the Army's intent to build a multidomain operations-capable force by 2030. See the Army Unified Network Plan for details. 

##### **COMBAT SERVICE SUPPORT VERY SMALL APERTURE TERMINAL** 

3-5. The CSS VSAT is a portable SATCOM terminal designed to provide global satellite video, voice, and data communications connectivity to forward-deployed sustainment units. It provides access to the Nonclassified Internet Protocol Router Network (the DOD’s version of the internet) and voice over internet protocol (commonly known as VoIP) from any location in the world where a satellite signal can be transmitted and received. During the system setup and initialization, the antenna pedestal automatically finds the desired satellite and brings up the desired circuit to the distant end within 30 minutes. It sends and receives data regardless of the distance between terrestrial switching offices. CSS VSAT's only requirements are a power source and shelter from the weather. Its components are prewired in a chassis mount for transport in four ruggedized transit cases designed to withstand outdoor storage. See Figure 3-1 for a notional CSS VSAT network diagram in a BSB. 

**3-2** 

**ATP 4-0.6** 

**17 January 2024** 

**Sustainment Automation** 



**Figure 3-1. Combat service support very small aperture network** 

##### **COMBAT SERVICE SUPPORT AUTOMATED INFORMATION SYSTEMS INTERFACE** 

3-6. CAISI, a commercial off-the-shelf communications solution, enables tactical wireless connectivity between forward deployed tactical users and their sustainment base networks. CAISI is not issued to SASMOs. It is authorized on the modified table of organization and equipment and fielded as user-owned and operated equipment to the sustainment elements. CAISI 2.0 is a wireless LAN infrastructure that can link up to 40 automation systems and transmit up to 32 miles (line of sight). Capabilities are listed below: 

- ⚫ Provides the backbone for a secure wireless LAN for sensitive and controlled unclassified information. 

- ⚫ Provides Nonclassified Internet Protocol Router Network access via the SATCOM network. See Figure 3-2 on page 3-4 for a depiction of a CAISI network topology. 

- ⚫ Provides unit commanders, sustainment leaders, staffs, and managers an interface device to support requirements for multidomain operations. 

- ⚫ Transmits encrypted max data rates that average greater than 15.0 megabits per second, depending on traffic types and signal strength. 

**17 January 2024** 

**ATP 4-0.6** 

**3-3** 

**Chapter 3** 

- ⚫ Can operate in 2.4 and 5.8 gigahertz frequency ranges. 

- ⚫ Provides 13 available connections and ports per CAISI bridge module. 



**Figure 3-2. Combat service support automated information systems interface network** 

##### **SUSTAINMENT TRANSPORT SYSTEM** 

3-7. The STS is a wireless tactical Army sustainment communications capability for facilitating reliable, secure, and continuous distribution management due to the capability to operate independently in the deep, close, and support areas. This capability supports over 120,000 EBS users who rely on sustainment communications connectivity to transmit and receive data to support the warfighter. The STS provides critical connectivity on the battlefield where the tactical network and other communication systems do not extend; to dispersed and forward deployed sustainment units. STS has SATCOM capability for beyond-line-of-sight communications. However, at higher echelons where sustainment units habitually collocate with maneuver units, they may use the tactical network environment for communications connectivity. The tactical network is the deployed portion of the unified network. The deployed portion of the network is functionally like the commercial internet because the communications infrastructure uses many of the same technologies. A distinction between the tactical network and the STS is that the STS is managed by sustainment elements and 

**3-4** 

**ATP 4-0.6** 

**17 January 2024** 

**Sustainment Automation** 

is typically the only communications resource available to forward sustainment forces. See ATP 6-02.60 for tactical network doctrine. 

#### **ARMY SUSTAINMENT ENTERPRISE BUSINESS SYSTEMS** 

3-8. SASMOs provide systems and network administration for EBS applications on the STS. See Table 3-1 for a list of EBS applications supported by SASMO teams. Due to constant changes in technology the list of applications supported by the SASMO often changes. 

**Table 3-1. Enterprise business systems** 

|**_Enterprise Business_**<br>**_System_**|**_Sustainment_**<br>**_Element_**|**_Functions_**|**_Using Units_**|**_Frequency of_**<br>**_Use_**|**_Frequency_**<br>**_of Patch_**|
|---|---|---|---|---|---|
|Aircraft Notebook|Logistics|Maintenance<br>support.<br>Multiple aircraft<br>interface.<br>Automatic at<br>system tester.<br>Employed on all<br>aircraft.|CAB.<br>AASF.<br>TASM.<br>ALMD Reset.|Daily|Monthly|
|Financial<br>Management Tactical<br>Platform|Financial<br>Management|Vending.<br>Military pay.<br>Disbursing.<br>Accounting.<br>Travel.<br>Resource<br>management.|Finance support<br>center.<br>Finance<br>battalion.<br>Finance<br>company.<br>Finance support<br>team.|Daily|Monthly|
|Global Combat<br>Support System-<br>Army|Logistics|Warehouse<br>activities.<br>Supply activities.<br>Property book<br>functions.<br>Maintenance<br>activities.<br>Aviation.<br>Business<br>intelligence/<br>business<br>warehouse.<br>Army<br>prepositioned<br>stock capabilities.|All units at all<br>echelons.|Daily|Monthly|
|General Fund<br>Enterprise Business<br>Systems|Financial<br>Management|Financial<br>management.<br>Distribution and<br>execution.<br>Appropriated<br>funds.<br>Cost<br>management.<br>Financial<br>reporting.<br>Trackingfunds.|All units at all<br>echelons.|Daily|Monthly|



**17 January 2024** 

**ATP 4-0.6** 

**3-5** 

**Chapter 3** 

**Table 3-1. Enterprise business systems (continued)** 

|**_Enterprise Business_**<br>**_System_**|**_Sustainment_**<br>**_Element_**|**_Functions_**|**_Using Units_**|**_Frequency of_**<br>**_Use_**|**_Frequency_**<br>**_of Patch_**|
|---|---|---|---|---|---|
|Integrated Personnel<br>and Pay System -<br>Army|Personnel<br>Services|Total force<br>visibility.<br>Auditability.<br>Talent<br>management.|All units at all<br>echelons.|Daily|Monthly|
|Maintenance Support<br>Device|Logistics|Maintenance data<br>storage tool.<br>Test and diagnose<br>communications<br>systems,<br>electronic<br>commodity<br>equipment,<br>missiles, aircraft,<br>and ground<br>vehicles.<br>Movement<br>management.<br>Planning, tracking,<br>and execution.|Unit/Field<br>Maintenance;<br>BSB.<br>CSSB.<br>SFAB.<br>FSC.<br>TSC.<br>ESC.<br>DIVARTY.<br>ADA.<br>ASB.|Daily|Monthly|
|Standard Army<br>Ammunition System|Logistics|Class V<br>Accountability.<br>Supply execution.<br>Inventory control.<br>Tactical-level<br>munitions<br>management.<br>In-transit visibility<br>data.|BSB.<br>CSSB.<br>ASP.<br>Sustainment<br>brigade.<br>ESC.<br>TSC.<br>ASC.|Daily|Monthly|
|Radio Frequency In<br>Transit Visibility|Logistics|Radio frequency<br>identification<br>service.|All units at all<br>echelons.|Daily|Monthly|
|Transportation<br>Coordinator’s<br>Automated<br>Information for<br>Movement System II|Logistics|Force deployment.<br>Convoy planning.<br>Highway<br>scheduling.<br>Movement control.<br>Container<br>management.<br>Mode<br>management.|DISA Computing<br>Center.<br>Unit ITO.|Daily|Monthly|
|AASF<br>Army aviation s<br>ALMD<br>Aviation Logisti|upport facility<br>cs Management D|DI<br>ivision<br>DI|SA<br>Defense In<br>VARTY<br>division art|formation Systems<br>illery|Agency|
|<br>ASB<br>aviation suppor|<br>t battalion|<br>ES|<br>C<br>expedition|<br>ary sustainment com|mand|
|<br>ADA<br>air defense artil|<br>lery|FS|<br>C<br>forward su|<br>pport company||
|<br>ASC<br>Army Sustainm|<br>ent Command|IT|<br>O<br>installation|<br>transportation office||
|ASP<br>ammunition sup|ply point|SF|AB<br>security for|ce assistance briga|de|
|BSB<br>brigade suppor|t battalion|TA|SM<br>theater avi|ation single manage|r|
|CAB<br>combat aviation<br>CSSB<br>combat sustain|brigade<br>ment support batta|TS<br>lion|C<br>theater sus|tainment command||



**3-6** 

**ATP 4-0.6** 

**17 January 2024** 

**Sustainment Automation** 

##### **ENTERPRISE APPLICATIONS** 

3-9. Commanders, SPO officers, and SASMO teams should be familiar with the sustainment automation they use and support. This section provides brief descriptions of the applications listed in Table 3-1 for which the SASMO provides systems and network administration. See the appropriate end user manual for sustainment automation details. 

###### **Aircraft Notebook Server** 

3-10. The Aircraft Notebook is a software-only program used in aviation maintenance activities for the documentation for all U.S. Army aircraft. The Aircraft Notebook platform provides a single-point access for maintainers to record and report maintenance activities. The Platform Maintenance Application gathers requirements for the platform project manager offices and implements needed interfaces with numerous Army information systems. Examples of these systems include platform ground station software, the Centralized Aircrew Flight Records System, Maintenance Consolidated Database System, and Enterprise Material Status Reporting System. 

###### **Financial Management Tactical Platform** 

3-11. The FMTP is a deployable, modular, LAN-configured hardware platform, supporting deployed financial management staff operations. The FMTP system is a modular design with financial management applications necessary to perform mission tasks at the deployed location. FMTP transports information via the CSS VSAT. FMTP functionality includes Commercial Vendor Services, Pay Support, Disbursing, Accounting, Travel, Resource Management, and can provide access to GCSS-Army and General Fund Enterprise Business Systems (GFEBS) via a browser. FMTP improves internal controls, reducing loss of fund and accountability risk, and complies with congressional/DOD mandated financial management reporting requirements. 

###### **Integrated Personnel and Pay System-Army** 

3-12. IPPS-A provides end-to-end tracking of pay and personnel data and gives individual Soldiers access to their personnel information. It is an online human resource system that provides integrated personnel, pay, and talent management capabilities in a single system. The system automates human resource and pay processes while linking human resource transactions, such as dependent changes and promotions. IPPS-A also provides integrated access by granting visibility and transaction functionality to commanders, Soldiers, and Army human resource professionals. 

###### **Global Combat Support System-Army** 

3-13. GCSS-Army is an integrated system that enables users (multiclass supply support activities, unit supply rooms, property book offices, and maintenance supply rooms) to perform their missions regardless of their location on the battlefield. Enterprise-wide forecasting, planning, and scheduling tools provide the capability to track transactional data to link customers and suppliers for more efficient supply pipeline management. Its core functionality is based upon Army regulations, Department of the Army pamphlets, field manuals, training circulars, technical manuals and bulletins, directives, policies, and procedures governing supply support activities, unit supply rooms, shop supply rooms, and property book offices. 

###### **General Fund Enterprise Business System** 

3-14. GFEBS is the financial asset and accounting management system that provides real-time visibility of accounting data across the Active Army, the Army National Guard, and the Army Reserve. GCSS-Army receives budget distribution from GFEBS for budget execution within the GCSS-Army system. GFEBS interfaces through the Army Enterprise Systems Integration Program with the Army logistics and strategic partner EBS to create the federated financial system of record. Under the federated approach to accounting, GCSS-Army coupled with GFEBS allows the Army to integrate logistics, financial, maintenance, property book, and accounting data. Standardized transactional input and business processes across the Army enable common cost management activities through accurate and reliable budget execution. 

**17 January 2024** 

**ATP 4-0.6** 

**3-7** 

**Chapter 3** 

###### **Maintenance Support Device** 

3-15. The Maintenance Support Device semi-rugged system is part of the integrated family of test equipment and the at-platform multipurpose standard automatic test equipment. This system is used throughout all levels of maintenance as the Army’s standard general purpose at-platform automatic test system to test and diagnose highly complex communications, other electronic commodity equipment, missiles, aircraft, and ground vehicles and to identify failed line replaceable units. Maintainers also use it to host interactive Electronic Technical Manuals, run specific applications, and upload or download mission data or software. 

###### **Standard Army Ammunition System** 

3-16. The Standard Army Ammunition System is the Army's system of record for munitions stock status reporting. It provides informational processing support for conventional ammunition logistical support applications at installations, divisions, corps, and echelons above corps. It employs product code and radio frequency identification technology to support these tasks. See ATP 4-35 for class V management doctrine. 

###### **Radio Frequency - In Transit Visibility** 

3-17. Radio frequency - in transit visibility devices facilitate visibility from the point where materiel enters the distribution system until it reaches the end user. Radio frequency - in transit visibility devices are a suite of technologies that enable the automated capture of source data for electronic transmission to and from automated information systems. This enhances the ability to identify, track, document, and control deploying forces, equipment, personnel, and cargo. They include, but are not limited to, bar codes, magnetic stripes, common access cards, optical memory cards, touch buttons, and satellite tracking devices. These technologies facilitate the capture of supply, maintenance, and transportation information for inventory and movement management, shipment diversion and reconstitution, and personnel or patient identification. Radio frequency - in transit visibility devices require minimal human intervention to capture detailed information with which to develop a more accurate common operational picture. 

###### **Transportation Coordinator’s Automated Information for Movement System II** 

3-18. Transportation Coordinator’s Automated Information for Movement System II (TC-AIMS II) provides web-based and stand-alone movement planning capabilities for automated transportation management of materiel and equipment. TC-AIMS II is the system of record for U.S. Army unit deployment and redeployment missions, establishing fort-to-port, port-to-port, and highway regulation movements and convoy planning. TC-AIMS II facilitates planning and execution of unit movements and enables movement control elements to manage and coordinate transportation services. 

##### **OTHER ENTERPRISE APPLICATIONS** 

3-19. Sustainment EBSs are essential for providing commanders and staffs with situational awareness and building the common operational picture. These systems enable command and control and support the centralized planning and decentralized execution of operations. The SASMO does not provide systems administration for all sustainment applications used by sustainment and maneuver units. Typically, applications not administered by the SASMO are maintained by the system product manager. However, these applications are supported on the STS. While the SASMO does not provide systems administration for the applications listed in Table 3-2, the users should provide contact information to be added to the network diagram. It is important for sustainment leaders to know size of the communications footprint. 

**3-8** 

**ATP 4-0.6** 

**17 January 2024** 

**Sustainment Automation** 

**Table 3-2. Applications supported by the network** 

|**_Application_**|**_Acronym _**|
|---|---|
|Account Management and ProvisioningSystem|AMPS|
|Ammunition SupplyPoint Management System|ASPMP|
|ArmyEnterprise Systems Integration Program Hub|AESIP|
|Aviation and Missile Command Ammunition TrackingSystem|AMCATS|
|Cargo Movement Operations Systems|CMOS|
|Commander's Actionable Readiness Dashboard|C@RD|
|Defense Civilian Intelligence Personnel System|DCIPS|
|Defense Medical Logistics Standard Support|DMLSS|
|Deployed Theater AccountabilitySystem|DTAS|
|eNOVA System|not an acronym|
|Explosive Ordnance Disposal Management Information System|EODMIS|
|Industrial Base Assessment Tool|IBAT|
|Joint Battle Command–Platform|JBC-P|
|Joint Battle Command-Platform Logistics|JBC-PL|
|Logistics Modernization Program|LMP|
|MortuaryAffairs Reportingand TrackingSystem|MARTS|
|Munitions HistoryProgram|MHP|
|Munitions Items Disposition Actions System|MIDAS|
|Munitions Total Management System|MTMS|
|National Level Ammunition Capability|NLAC|
|Operational Medical Information System - Army|OMIS-A|
|Operational Logistics Planner|OPLOG Planner|
|Stockpile InventoryList Comparator|SILC|
|Tactical Personnel System|TPS|
|Total Ammunition Management Information System|TAMIS|



**17 January 2024** 

**ATP 4-0.6** 

**3-9** 

This page intentionally left blank. 

##### **Chapter 4** 

### **Planning and Coordination** 

In large-scale combat operations, units can expect to establish communications where there is no preexisting network. The SASMO enables the commander to establish and maintain sustainment communications for theater distribution. This chapter discusses how leaders and planners can best employ the SASMO teams. It provides dashboard information for planning, preparing, executing, and assessing SASMO operations. 

#### **PLANNING CONSIDERATIONS** 

4-1. Commanders require tailorable communications capabilities. SASMO branch chiefs should provide leaders and planners with an overview on the mission relevance of the signal flow from the EBS, through the LAN, through the wide-area network, the STS, and on to the DODIN-A. SASMO branch chiefs should update the SPO regarding available communications capabilities during critical points of an operation and how these capabilities support combatant commander’s priorities. SASMO branch chiefs coordinate with the G-6 or S-6 to obtain current cybersecurity concerns. These include the prevention of damage to, protection of, and restoration of computers, communications systems, communications services, wire communication, and electromagnetic communication as it relates to distribution management. These concerns should be briefed to the SPO. 

4-2. Threat cyberspace capabilities may disrupt sustainment automation to interrupt the distribution management process. STS considerations should be included in Annex E of operation orders and plans under the Electromagnetic Protection and Cyberspace Security and Defense paragraphs. These paragraphs describe how units plan, integrate, and synchronize defensive cyberspace operations-internal defensive measures as part of the operations process. Failure to achieve this synchronization may result in a distribution plan that cannot be executed (which might not be evident until the operation begins). Planners should integrate considerations for the proliferation of cyberspace capabilities (both friendly and threat) and their impact on sustainment operations into the distribution management plan. See ATP 4-42 for in-depth discussion about the distribution management process. See FM 3-12 for doctrine on cyberspace operations. 

**_Note:_** Leaders and staffs should understand the capabilities, limitations, and constraints of the communications platforms (including the STS) organic to their units. 

4-3. SASMOs need to know the sustainment commander's signal expectations. SASMO capabilities should be nested with the communications plan because the STS is a primary component of the Army's sustainment infrastructure. Sustainment unit staffs should consult with the SASMO throughout the operations planning process to ensure that sustainment automation can support the plans. Sustainment leaders and staffs should consider the following sustainment automation planning considerations during the operations process: 

- ⚫ Available communications resources from a communications status report. See figure 4-1 on page 4-2 for one way to report the status of communications resources. Reporting format and the information reported depends upon the commander, SPO, and unit standard operating procedure (SOP). 

- ⚫ Special and additional training requirements. 

- ⚫ Potential frequency changes and the alternate means of communications. 

- ⚫ Size of the current communications footprint. 

- ⚫ Vulnerabilities of the STS. ▪ Size of the network. 

**17 January 2024** 

**ATP 4-0.6** 

**4-1** 

**Chapter 4** 

   - Potential dead-space locations. 

   - Bandwidth requirements and potential workarounds if the bandwidth is not sufficient or available. 

- ⚫ Communications requirements. 

   - Identify and diagram client node network locations. 

   - Authorized communications equipment. 

   - Required communications equipment. 

   - Available communications equipment. 

   - Available flat surfaces to set up the CSS VSAT to facilitate ability of the equipment’s navigation pendulum to locate a satellite to connect. 

   - Status of communications assemblages. 

      - Fully functional EBS and STS equipment with the latest software updates. 

      - EBS and STS equipment protected by the latest cybersecurity measures. 

   - EBS requiring communications. 

- ⚫ Determine who the sustainment leaders and staff communicate with and why to provide communications system information on actual or anticipated changes that may have a major effect on operational capability. 

- ⚫ Do the sustainment leaders and staff need collaboration tools, or does messaging satisfy the requirement? 

- ⚫ Anticipated timetable or event schedule associated with the commander’s most likely course of action? 



**Figure 4-1. Notional CSS VSAT communications status report** 

4-4. Leaders need the ability to command their formations when communication networks are disrupted, while on the move, and without perfect situational awareness (FM 3-0). A primary, alternate, contingency, and emergency (PACE) communications plan provides predictability and redundancy for communications in congested or contested environments. Redundant communications systems and methods enable communications throughout the corps and division areas of operations in contested environments. A viable, effective PACE plan may be the most valuable contribution of a SASMO in the planning process. A PACE plan is a key requirement for operations in a contested environment: 

- ⚫ Primary—the best, and intended, method of communications. 

**4-2** 

**ATP 4-0.6** 

**17 January 2024** 

**Planning and Coordination** 

- ⚫ Alternate—another common, but perhaps less optimal method. 

- ⚫ Contingency—method may not be as fast, convenient, or reliable, but it can still accomplish the task. 

- ⚫ Emergency—communications method of last resort. Emergency methods may cause delays or otherwise affect operations. 

4-5. The STS supports multiple EBSs that together comprise the automated portion of the sustainment infrastructure. Typically, sustainment units use the STS for SATCOM and wireless. On occasion a sustainment unit may use the Army's tactical network environment. Sustainment commanders should be made aware when this occurs. This highlights the need for PACE plans based on the unit's assigned Army tactical network or STS. The SASMO should work with the G-6 or S-6 to develop PACE plans to minimize the negative impact of system outages and denial of service events with a routine method for transitioning from a primary means of communications to an alternate. A PACE plan is a tactical SOP for handling communications disruptions. See Table 4-1 for a notional PACE plan. The maneuver operations, logistics, and signal staff elements should continuously collaborate with sustainment staffs (including SASMO) through the phases of planning, preparation, execution, and assessment to make the best recommendations for decision making. During the operations process, maneuver, signal, and sustainment staff elements are inextricably linked even though they are in separate units. 

**Table 4-1. Notional PACE plan** 

|**_Priority_**|**_System_**|
|---|---|
|Primary|STS/CSS VSAT/CAISI|
|Alternate|NIPR-Strategic|
|Contingency|NIPR-JNN/TCN/CPN|
|Emergency|JBCP|
|CAISI<br>Combat Service Support Automated<br>Information Systems Interface|JNN<br>joint network node|
|CPN<br>command post node|NIPR<br>Nonclassified Internet Protocol Router|
|CSS VSAT<br>Combat Service Support Very Small<br>Aperture Terminal|STS<br>sustainment transport system|
|JBCP<br>Joint Battle Command–Platform|TCN<br>tactical communications node|



#### **OPERATIONS PROCESS** 

4-6. Commanders and staffs should integrate sustainment automation factors into the operations planning process because these are part of the distribution infrastructure. Communications are critical for the effective provision of logistics, financial management, personnel services, and the health service support. Commanders should consider the types and quantity of communications equipment required while planning for unit communications systems, leveraging all communications assets available. This includes all sustainment automation. Failure to consider sustainment automation as a weapons system during the operations process may lead to a distribution plan that cannot execute because of problems with the enterprise systems, problems with the communications equipment, or a poorly planned network. 

##### **PLANNING** 

4-7. _Planning_ is the art and science of understanding a situation, envisioning a desired future, and determining effective ways to bring that future about (ADP 5-0). Unit operations staff elements should collaborate with the SPO throughout the military decision-making process from receipt of the mission until the operation order is published and disseminated. Figure 4-2 on page 4-5 represents one way in which unit operations staff elements may interact with the SPO during planning to develop an order. Each of the military decision-making process steps contains assumptions, facts, planning considerations, and hundreds of details 

**17 January 2024** 

**ATP 4-0.6** 

**4-3** 

**Chapter 4** 

that influence mission success. The top lane illustrates the military decision-making process steps undertaken by commanders and staffs. The three lanes within the SPO lane display the functions that distribution integrators, materiel managers, and transportation managers perform separately and together. Arrows between the functions and the military decision-making process steps demonstrate the complexity of the coordination between the SPO, the S-3 or G-3, the commander’s staff, and the commander as they identify and evaluate courses of action. Sustainment automation transports information in real-time and near-realtime among the staffs within and outside their lanes. The bottom lane presents a very high-level view of how and when supply points for all classes of supply come into the process. The arrows between the functions represent communication between leaders, staffs, and managers. These arrows also represent communication between the EBSs via the STS. SASMOs perform the systems administration and network administration that facilitates this communication. 

**4-4** 

**ATP 4-0.6** 

**17 January 2024** 

**Planning and Coordination** 



**Figure 4-2. Collaboration between the S-3 and support operations** 

**17 January 2024** 

**ATP 4-0.6** 

**4-5** 

**Chapter 4** 

**_Note:_** The DMC or the SPO should be prepared to coordinate sustainment automation considerations (especially for the STS) into the operation order and the distribution concept of operations. 

4-8. Leaders and staffs within all four sustainment elements rely upon sustainment automation to transport information for forecasting, assessing, and executing requirements. See FM 4-0 for more information on the sustainment elements. Figure 4-2 highlighted materiel management, but the overall collaboration process applies within each of the four sustainment elements. The SASMO’s crucial role during the operations process is to provide a comprehensive and current analysis of all the factors typically at play that influence sustainment automation. SASMO contributions to planning include the following: 

- ⚫ Advising the commander and staff on current computer industry technology, including the practices on data security, integrity, availability, audit compliance, product evaluation, installation, maintenance, and control of information systems software. 

- ⚫ Providing status on shortfalls in security configurations, to include software and hardware configurations for supported EBS. 

- ⚫ Interpreting sustainment automation computer network configurations and security countermeasures for the commander and staff. 

- ⚫ Determining communications requirements by— 

   - Comparing with available assets. 

   - Identifying potential shortfalls. 

   - Recommending actions to eliminate or reduce effects of shortfalls. 

- ⚫ Developing and maintaining a sustainment automation running estimate for— 

   - STS and EBS security posture. 

   - Maintenance status (reported during logistics synchronization meetings). 

   - Network administration consisting of coordinating, planning, and directing STS cybersecurity activities, information operations vulnerability, and scan assessments. 

- ⚫ Coordinating with the G-6 or S-6 staff to ensure sustainment automation and administrative procedures are joint and Army compliant. 

- ⚫ Coordinating with the S-2 and S-3 to provide sustainment automation status. 

- ⚫ Coordinating with all staff sections to ensure that their applications and connections to the STS are mission capable. 

- ⚫ Identifying user requirements by number and service type. 

- ⚫ Supporting units conducting sustainment automation validation. 

- ⚫ Installing and operating the help desk. 

- ⚫ Providing sustainment EBS assistance. 

- ⚫ Coordinating satellite access requests and de-conflicting frequencies with the unit frequency manager. 

- ⚫ Submitting communications status reports to advise leaders and staff on the status of EBSs and the STS. 

4-9. Failure to integrate SASMO functions into operations planning may lead to systems and network problems that hinder collection and transport of the critical data required for fulfilling sustainment requirements. SASMOs can develop the CSS VSAT and CAISI communication plan that lays out SATCOM and line-of-sight infrastructures. During course of action development, they can assess the communications and computer requirements and prepare the sustainment automation portions of plans and orders. SASMOs consider the following during STS planning to ensure timely information and knowledge management: 

- ⚫ Supported unit locations. 

- ⚫ Supported unit missions (for example, maneuver or sustainment.) 

- ⚫ Available equipment for moving the CSS VSAT and CAISI into place. 

- ⚫ Timeframe for emplacement of CSS VSAT and CAISI. 

**4-6** 

**ATP 4-0.6** 

**17 January 2024** 

**Planning and Coordination** 

- ⚫ Locating the CSS VSAT (line of sight, terrain). 

- ⚫ Locating the CAISI (line of sight, terrain). 

- ⚫ Weather and terrain when placing the CSS VSAT and CAISI. 

- ⚫ Distance between the CSS VSATs. 

- ⚫ Distance between the CAISIs. 

- ⚫ Identification of communications links with higher, adjacent, subordinate, and supported units. 

- ⚫ Requirements for elevated privileges to the system. 

- ⚫ Nearest hardware maintenance support. 

- ⚫ Number of connections needed. 

- ⚫ Purchasing sufficient airtime. 

- ⚫ Solar flare activity. 

- ⚫ Supported units outside of organic unit. 

##### **PREPARATION** 

4-10. Preparation creates conditions that improve sustainment unit opportunities for success and include activities such as rehearsals, training, and inspections. It requires commander, staff, unit, and Soldier actions to ensure units are ready to execute operations. 

###### **Boards, Bureaus, Centers, Cells, and Working Groups** 

4-11. SASMOs should be included on boards, bureaus, centers, cells, and working groups that rely on sustainment automation infrastructure. SASMO representatives provide situational awareness regarding sustainment infrastructure. Commanders and the battle rhythm determine when and where to include SASMO participation. A guiding rule is where the G-6 or S-6 plays a major role, the SASMO should also be included for two reasons: 

- ⚫ SASMOs perform all the same functions to maintain the STS that the G-6 or S-6 does to maintain the tactical network. 

- ⚫ Situational awareness gives the SASMO the information needed to develop PACE plans. 

4-12. Effective sustainment and operations synchronization meetings have appropriate participation for validating logistic status reports, communications status reports, and coordinating sustainment operations. Leaders use the synchronization meeting to update a preformatted and practiced synchronization matrix. See Figure 4-3 on page 4-8 for a depiction of a logistics synchronization meeting agenda. Examples of meetings that should include the SASMO are: 

- ⚫ Operations synchronization meeting. 

- ⚫ Logistics synchronization meeting. 

- ⚫ Commander’s update brief. 

- ⚫ Operations update and assessment. 

- ⚫ Sustainment working groups. 

**17 January 2024** 

**ATP 4-0.6** 

**4-7** 

**Chapter 4** 



**Figure 4-3. Logistics synchronization meeting** 

###### **Battle Drills and Rehearsals** 

4-13. SASMOs should participate in battle drills and rehearsals. Commanders perform rehearsals to ensure staffs and subordinates understand the concept of operations and commander’s intent. Four primary types of rehearsals are the back brief, combined arms rehearsal, sustainment rehearsal, and battle drill or SOP rehearsal. Support rehearsals and combined arms rehearsals complement preparations for the operation. Throughout preparation, the commander executes support rehearsals that typically involve coordination and procedure drills for sustainment, aviation, fires, engineer support, and medical and casualty evacuation. 

##### **EXECUTION** 

4-14. Major activities of execution include assessment, decision-making, and directing action. Sustainment commanders develop situational understanding that may prompt them to adjust plans to exploit opportunities or counter threats. SPOs maintain a running estimate in accordance with the battle rhythm or leader requirements. Decision-making is necessary when commanders determine that the situation requires an unanticipated decision to alter the plan. Execution decisions implement actions that are anticipated and planned into the order. Adjustment decisions include reallocating resources, changing the operations concept, or changing the mission. SASMO contributions to execution include— 

- ⚫ Providing status on shortfalls in security configurations, to include software and hardware configurations for supported EBS. 

- ⚫ Interpreting sustainment automation network configurations and security counter measures. 

- ⚫ Coordinating unsupported network requirements with the S-4 or S-3. 

- ⚫ Coordinating with the G-6 or S-6 staff to ensure sustainment automation and administrative procedures are joint and Army compliant. 

- ⚫ Coordinating with the S-2 and S-3. 

**4-8** 

**ATP 4-0.6** 

**17 January 2024** 

**Planning and Coordination** 

- ⚫ Providing sustainment EBS assistance. Please note that the SASMO does not provide systems administration for all EBS supported on the STS. 

- ⚫ Implementing cybersecurity measures to maintain compliant systems. 

   - Protect information, detect and react to intrusions, and restore access to information to include shared data sources. 

   - Restore information by incorporating detection and reaction capabilities. 

   - Conduct real-time network monitoring, threat identification, access control, event logging, and reporting across the environment. 

- ⚫ Coordinating satellite access requests and de-conflicting frequencies with the unit frequency manager. 

- ⚫ Establishing connectivity. 

- ⚫ Validating connectivity. 

- ⚫ Documenting the communication grid. 

- ⚫ Submitting communications status reports to advise leaders, staff, and planners on status concerning EBSs and the STS. 

##### **ASSESSMENT** 

4-15. Commanders integrate their own assessments with those of the staff, subordinate commanders, and unified action partners throughout the operations process. Since SASMOs are a critical component of the theater distribution infrastructure, the commander and staff should continuously assess SASMO capabilities, capacities, and task organization against requirements. Briefings and reports are tools that the SASMO branch chief may provide to communicate information to the SPO officer, higher headquarters, supported units, and adjacent units. SASMOs should submit commander's critical information requirements, significant acts reports, communications status reports, battle damage assessments, and any other reporting in accordance with the tactical SOP or the battle rhythm. SASMOs should be assessed on the following tasks, which should drive running estimates: 

- ⚫ Network performance. 

- ⚫ Status of synchronization with other SASMOs to ensure maximum network support to units in the AO, units en route to the AO, and units at home station. 

- ⚫ Status of network connectivity across the AOR. 

- ⚫ Status of the applications residing on individual platforms from origin to where the unit connects to the unified network. 

- ⚫ Status of network modifications to meet the needs of the mission. 

- ⚫ Status of network security. 

- ⚫ Status of communications hardware maintenance. 

- ⚫ Status of PACE plans for each phase of the operation. 

#### **COMMUNICATION AND COORDINATION** 

4-16. DMCs and SPOs develop and execute strategies to work around choke points and bottlenecks. They seek opportunities to nest SASMO support planning with the maneuver plan by leveraging relationships in each staff section. When deployed, SASMO branch chiefs should constantly assess the battlefield to protect EBSs and the STS from disruption, damage, or destruction. SASMOs should communicate vertically and laterally across organizations regarding EBS and STS support. SASMO branch chiefs should learn the functions, outputs, and individual personalities of the supporting and supported staff sections to develop an in-depth picture to support the operation. Ideally, the branch chief should visit each supported location; however, this is often too dangerous or impractical. In these cases, branch chiefs should establish relationships through other means such as the telephone. The following staff section descriptions are offered to familiarize SPO officers and SASMO branch chiefs with key tasks for which these sections rely upon sustainment automation. See FM 6-0 for in-depth discussion about staff operations. 

**17 January 2024** 

**ATP 4-0.6** 

**4-9** 

**Chapter 4** 

##### **OPERATIONS OFFICE** 

4-17. The G-3 or S-3 operations officer is the chief of the movement and maneuver warfighting function and the principal staff officer responsible for all matters concerning training, operations, plans, force development, and modernization. In addition to coordinating movement and maneuver activities, the operations officer is the primary staff officer for integrating and synchronizing the operation across the planning horizons in current operations, future operations, and plans integrating cells. 

4-18. Current operations sections provide forecasts for tactical pauses that may offer resupply windows or changes in movement priority on supply routes. As opportunities arise, they support timely analysis for sustainment units to coordinate logistics requirements and establish support priorities in accordance with the commander's guidance. The future operations section plans for the mid-range horizon by focusing on the “what if” analysis. The future operations section refines and modifies operations plans and orders based on the current situation, develops branch plans, and assesses mid-range progress of operations. Normally, ongoing operations mean that several plans undergo refinement simultaneously with associated working groups and joint planning teams. Effective distribution managers frequently coordinate with supported unit current and future operations staff to provide timely supply support. 

##### **LOGISTICS STAFF OFFICE** 

4-19. The G-4 or S-4 serves as the sustainment integrator for the commander and develops the logistics plan in support of the operational plan. The staff provides recommendations on a variety of command priorities including host-nation support, commercial support, materiel management, and movement control. The logistics staff may incorporate divisions, branches, and specialized sections for supporting various types of operations. In addition, it may include joint and multinational capabilities for supporting requests for logistics support. The staff may also serve as the focal point for planning and integrating Logistics Civil Augmentation Program (commonly known as LOGCAP) and commercial support. 

**4-10** 

**ATP 4-0.6** 

**17 January 2024** 

##### **Chapter 5** 

### **SASMO Operations** 

SASMO sections provide network administration, systems administration, and sustainment expertise to supported units. This chapter discusses sustainment automation support during day-to-day operations. 

#### **ESTABLISH COMMUNICATIONS** 

5-1. The SASMO executes communications support by conducting network operations. Commanders and their staffs may be required to deploy under a scenario for which there is little or no planning. SASMOs should be prepared to establish communications in changing OEs. Optimal EBS performance can only be achieved when STS hardware is connected properly and running the most up-to-date firmware. The SASMO provides communications support via the STS according to the unit tactical SOP, the operation order, and the commander's guidance. The SASMO should prepare for communications support by conducting rehearsals and participating in battle rhythm events. See FM 6-02 for information about network operations and ATP 6-02.60 for networking techniques. 

##### **CONCEPT OF THE OPERATION** 

5-2. Support elements travel with the maneuver formations during combat operations to provide sustainment products and services. The SASMO performs systems and network administration from either a developed or an undeveloped location to ensure commanders have connectivity with higher, lower, and adjacent echelons. The requirement is to communicate at the quick halt (within 30 minutes) to exchange sustainment data to notify the enterprise of the formation’s capability, readiness, availability, and employability in a dynamic environment. For example: 

- ⚫ During reception, staging, onward movement, and integration as Soldiers arrive in a new AOR, IPPS-A updates their change in pay and allowances status from the force provider rolls to the gaining ASCC and ARFOR rolls. 

- ⚫ Radio frequency-in transit visibility devices track the arrival of equipment and supplies at the port of debarkation. 

- ⚫ Mortuary affairs teams require support from the SASMO (through STS administration) to report casualties, track human remains, track personal effects, and communicate with the casualty reporting personnel. 

5-3. All sustainment functions require network connectivity for the provision of logistics, financial management, personnel services, and health service support. Each SASMO establishes the sustainment automation information network as soon as possible after the unit enters its assigned area. It installs, operates, and maintains networks that ensure information systems and personnel can perform knowledge management activities. The SASMO must establish satellite network communications to support mission requirements in multiple terrain types, various weather conditions, and where a hybrid threat is possible. All SASMO team members, regardless of MOS, should develop the skills to perform all systems administration and all network administration tasks. See Appendix A for information about the conduct of sustainment automation gunnery training. See also TC 4-11.47 for information about gunnery training for sustainment functions. 

##### **SASMO SERVICES** 

5-4. The SASMO provides Tier 0 and Tier 1-level technical support consisting of installation, testing, and software and hardware troubleshooting to facilitate an uninterrupted, end-to-end distribution management process (see Figure 5-1on page 5-2). Tier 0 equals operator and Tier 1 equals first-level technical support, 

**17 January 2024** 

**ATP 4-0.6** 

**5-1** 

**Chapter 5** 

which is the SASMO help desk. SASMOs coordinate with field support representatives and field support engineers for repair of sustainment automation and report sustainment automation-specific statuses to the SPO officer and higher headquarters in accordance with the battle rhythm and SOP. 



**Figure 5-1. Tier support concept** 

##### **HELP DESK** 

5-5. SASMO operations are conducted from the strategic support area in the continental U.S. to the front line of troops in a theater. Sustainment automation configurations are detailed in end user manuals, system support manuals, and software version descriptions. Use of commercial proprietary software or altering hardware or software configurations can result in corruption, loss of data, or system malfunctions. Using unapproved supported hardware for approved software is authorized, but highly discouraged. It is only approved in special, emergency circumstances and is required to be fully documented with justification signed by the owning unit’s commander. Commanders should ensure that all users complete the following: 

- ⚫ Acceptable Use Policy agreement. 

- ⚫ Annual Cyber Awareness Training. 

- ⚫ Information Assurance Compliance. 

5-6. The help desk serves as the initial entry point for routine sustainment automation user inquiries and as a collaboration point for other SASMOs. Systems administration (help desk operations) includes answering phone calls, answering email requests, updating the support request database, and providing operator assistance via digital or analog medium or in person. The SASMO provides telephonic and hands-on technical assistance to ensure end user systems remain mission capable. The help desk tracks and maintains user acceptable use policies, annual information assurance training certificates, the support request database, and SASMO copies of key EBS backups. SASMO functions involve root-cause analysis, such as the following: 

- ⚫ STS communications links with higher, adjacent, subordinate, and supported units. 

- ⚫ Compromises of information assurance controls. 

- ⚫ Restoration of system and data files, fixing corrupt files, and rebuilding files. 

**5-2** 

**ATP 4-0.6** 

**17 January 2024** 

**SASMO Operations** 

###### **Network Documentation** 

5-7. SASMOs coordinate the movement of sustainment information through the STS. They create network diagrams to assess security risks during network design and continuously monitor for signs of malicious activity within the network. See figure 5-2 on page 5-4 for a network diagram. Each SASMO develops and maintains a network diagram for its assigned area. STS network diagrams change as supported units come and go, vary in size, vary in supported EBS, and will be much larger than the example shown. Due to the information required, networks are often tracked on spreadsheets rather than in picture format. The purpose of this figure is to illustrate a small slice of a notional network and EBS that may be supported. Network diagrams can include— 

- ⚫ On-the-move node planning. 

- ⚫ Local access waveform radios. 

- ⚫ High band networking radios. 

- ⚫ Network-centric waveform modems. 

- ⚫ High-capacity line-of-sight radios. 

- ⚫ Frequency division multiple access SATCOM planning. 

- ⚫ Combat net radio planning (single-channel ground and airborne radio system and Enhanced Position Location Reporting System). 

- ⚫ Quality of service planning. 

- ⚫ Internet protocol address and router planning. 

- ⚫ Voice service planning. 

- ⚫ Spectrum planning for all known emitters and management of network emitters (See ATP 6-02.70). 

- ⚫ Cybersecurity planning. 

- ⚫ Address book planning. 

**17 January 2024** 

**ATP 4-0.6** 

**5-3** 

**Chapter 5** 



**Figure 5-2. Notional network diagram** 

5-8. There are situations where the SASMO team may respond to onsite requests for assistance. The branch chief should actively engage supported activities and units to ensure their sustainment automation is fully mission capable. The branch chief should analyze the OE and plan an approach to problem solving that includes meeting with supported units and commanders. Document all sustainment automation (client hardware, operators, layout of tactical networks, terrain and geographic distances, and mission scope) on a spreadsheet and network topology map using network diagnostic software with the information listed below: 

- ⚫ Unit name. 

- ⚫ Unit points of contact. 

- ⚫ Phone numbers and email addresses. 

- ⚫ All sustainment automation serial numbers. 

- ⚫ All sustainment automation hostnames. 

- ⚫ Internet protocol addresses. 

- ⚫ Media Access Control addresses. 

5-9. The SASMO branch chief should use the information contained and analyzed through the network diagram to brief the SPO, planners, and commander on sustainment automation mission support requirements. The network diagram is not static because it changes as supported units move into and out of the SASMO’s area. It should be briefed to the SPO and higher headquarters leaders, used as a troubleshooting matrix, and provided to new team members during unit rotations or replacements. The diagram visually details manmade and terrain obstructions; lists all client workstations and locations, LAN configuration, wide-area network configuration, wireless access points, handheld terminals, private and public networks, and points of contact; and may also include access points to the installation Network Enterprise Center. Diagrams may be hand drawn at initial deployment as end user units position themselves. Once a force is 

**5-4** 

**ATP 4-0.6** 

**17 January 2024** 

**SASMO Operations** 

mature, SASMOs should use software applications to enhance the tactical network diagrams for the purpose of briefings, electronic file storage, use in email attachments, and general administrative use. The SASMO is responsible for network cybersecurity. It allows or blocks devices to ensure users follow AR 25-1 and AR 25-2. 

###### **Problem Assistance** 

5-10. Systems administration problems fit into one of three categories: hardware, software, or functional. Hardware problems are normally easy to identify. Error messages will display on the screen for hardware problems. System software problems may be divided in two parts: operating system and EBS application software. In most cases, errors in the operating system may cause the computer to shut down completely, while errors in the software application typically return the computer to a menu or the command line prompt. Functional or training problems arise when the operator is not functionally literate or able to use the system properly. Follow the suggested logical sequence below to assist with problem solving: 

- ⚫ Assist the operator in formulating a description of the problem. ▪ Ask the user to capture any error messages. 

   - Advise the user to ensure all system cables are attached and secure; ensure system is powered correctly. 

- ⚫ User should attempt to recreate the problem to help determine the problem category—hardware, system software, or functional. 

- ⚫ Consult the troubleshooting table in the user's or system support manual. 

- ⚫ Attempt to solve the problem following suggestions from the troubleshooting table. 

5-11. SASMOs are small teams, making it difficult to dispatch team members to operator locations, particularly because the supported units are widely dispersed. EBS application issues are typically solved through the SASMO or application help desk: 

- ⚫ If problem resolution can be achieved via telephone, the SASMO help desk provides instructions to the end user. 

- ⚫ If problem resolution cannot be achieved via telephone and workload allows for walk-in support, the end user may be encouraged to bring the system to the SASMO. 

- ⚫ SASMO personnel may schedule an appointment for the end user to transport their equipment for service. End users should provide relevant information for trouble ticket creation. 

- ⚫ Once service is completed, the SASMO notifies the end user of status and availability. The SASMO will close the ticket and require the end user to sign equipment out of the help desk, indicating equipment receipt. 

- ⚫ Before departing, the end user should perform an equipment serviceability check to validate that the problem was corrected, and the system is functional. 

###### **_Troubleshooting_** 

5-12. Hardware components are commercial off-the-shelf products designed for an office environment. They are extremely vulnerable to dirt and dust buildup on printed circuit boards and circuit cards, a condition that normally results in hardware failure. The following measures offer some protection from hardware failures: 

- ⚫ Perform cleaning on a regular basis. 

- ⚫ Keep the computer fully ventilated. 

- ⚫ Check voltage before plugging in computer. 

- ⚫ Perform data backups as specified by the end user manual. 

5-13. When an EBS fails, reference the end user manual to attempt to resolve the problem through the following troubleshooting procedures: 

- ⚫ Gather any output that the EBS system produced at the time of the failure. Capture any error messages displayed, either by writing them down or printing a hard copy. 

- ⚫ Ensure all system cables are attached and secure and the system is powered correctly. 

- ⚫ Attempt to recreate the problem. 

**17 January 2024** 

**ATP 4-0.6** 

**5-5** 

**Chapter 5** 

- ⚫ Attempt to identify the general problem as one of the following four categories: hardware, system software, functional, or network: 

   - Hardware problems will normally display error messages on the screen. 

   - System software problems may be divided into two parts—operating system and EBS application software. 

   - Functional problems result from end users not following proper procedures and cause problems such as ghost files. 

   - Network problems occur when the computer is unable to connect to the internet. 

5-14. Table 5-1 contains common issues with potential solutions. This table is not all inclusive and there may be other solutions to the issues listed. The purpose of this table is to provide a basis for understanding day-to-day tasks. 

###### **Table 5-1. Trouble shooting tasks** 

|**_Issue_**|**_Help Desk_**|**_Follow Up_**|
|---|---|---|
|Login /<br>Connectivity|• Verify all connections are seated properly and finger tight.<br>• Verify network link lights.<br>• Perform visual inspection of cabling and wiring.<br>• Verify time (right hand corner) is less than 15 minutes different<br>from real time.<br>• Verify user has privileges to log in and account is not locked out.<br>• Verify no higher-level outage (multiple calls from same building<br>or users could indicate bigger problems or server issues).<br>• Ping enterprise business system to test remote connectivity.|• Reconnect network<br>cables.<br>• Reboot.<br>• Submit support<br>request for incident.|
|Printing|• Verify all connections are seated properly and finger tight.<br>• Verify connectivity as outlined above.<br>• Verify printer is installed and functional (test page).<br>• Verify printer is installed, functional, and correct driver installed.<br>• Check for error codes and jamming.<br>• Verify configuration by using remote tools (as available).|• Reconnect cables,<br>print test page, and<br>verify connectivity<br>from enterprise<br>business system to<br>printer.<br>• Submit support<br>request for incident.|
|Power on /<br>Boot|• Verify power applied at correct voltage (120 volt/240 volt).<br>• Verify all connections are seated properly and finger tight.<br>• Check for hardware damage and software errors.|Submit support request<br>for incident.|
|Application<br>Failure|• Verify application performs other vital functions.<br>• Verify data for entry.<br>• Attempt to reproduce errors and fully document.<br>• Verify version in use, data entered; update as necessary.<br>• Back up user data, reimage.|Submit support request<br>for incident.|



**5-6** 

**ATP 4-0.6** 

**17 January 2024** 

**SASMO Operations** 

**Table 5-1. Trouble shooting tasks (continued)** 

|**_Issue_**|**_Help Desk_**|**_Follow Up_**|
|---|---|---|
|System<br>Failure|• Perform visual inspection of cabling and wiring.<br>• Verify all connections are seated properly and finger tight.<br>• Identify any strange noises or burning smell.<br>• Identify proper operation of mouse, keyboard, monitor, and other<br>key components.<br>• Verify power applied at correct voltage (120 volt/240 volt).<br>• Check for hardware damage and software errors.<br>• Attempt to reproduce errors and fully document.|Submit support request<br>for incident.|



###### **_Maintenance Request Procedures_** 

5-15. When an EBS end user calls the SASMO for maintenance support, the help desk technician should ask for the following information: 

- ⚫ Type of EBS (for example, OMIS-A, GCSS-Army). 

- ⚫ Name of the EBS end user. 

- ⚫ Unit. 

- ⚫ Telephone number. 

- ⚫ Address where the EBS equipment is located. 

- ⚫ EBS equipment serial number. 

- ⚫ A brief, but detailed description of the problem. 

#### **SUSTAINMENT AUTOMATION MAINTENANCE** 

5-16. The multidomain (land, sea, air, space, and cyberspace) capabilities of potential adversaries have expanded the battlefield beyond historic geographic and time constraints. As leaders and staffs work to understand situations, make and implement decisions, control operations, and assess processes, they should consider the maintenance of sustainment hardware, software, and network communications as high a priority as any other maintenance. 

##### **FIELD-LEVEL MAINTENANCE** 

5-17. Maintenance includes all actions necessary for retaining an item in, or restoring it to, a specified condition to ensure readiness. Typically, Army personnel think of equipment, but maintenance has a much broader meaning than reparable or end item repair when it concerns sustainment automation. Tasks associated with network and systems administration should be considered maintenance activities due to the criticality of properly functioning network infrastructure, hardware, and software. The SASMO maintains the STS to meet the challenges in all environments. The unique maintenance requirements of the network infrastructure require maintenance practices that ensure minimal downtime. SASMOs perform the following activities associated with maintaining the STS infrastructure: 

- ⚫ Generating and maintaining an STS diagram. 

- ⚫ Monitoring the STS and internet connections to ensure sustainers have connectivity. 

- ⚫ Website interface maintenance. 

- ⚫ Troubleshooting. 

- ⚫ Security. 

- ⚫ Cybersecurity. 

- ⚫ Configuration. 

**17 January 2024** 

**ATP 4-0.6** 

**5-7** 

**Chapter 5** 

5-18. Sustainment automation field-level maintenance does not include computer disassembly to replace internal components. SASMOs may perform the following field-level maintenance services: 

- ⚫ Diagnostic troubleshooting. 

- ⚫ Elimination of corrupt data. 

- ⚫ Removing unauthorized programs and files. 

- ⚫ Database backup. 

- ⚫ Monthly security rollup packages. 

- ⚫ Monthly file updates. 

- ⚫ Software patches. 

- ⚫ Data backup and migration. 

5-19. For redeploying units, field maintenance includes ensuring that sustainment EBS equipment is network configured to communicate with other systems as required. Field-level Tier 0 and Tier 1 maintenance includes the following tasks: 

- ⚫ Cleaning and defragging of hard drives. 

- ⚫ Elimination of corrupted data. 

- ⚫ Preparing system backups. 

- ⚫ Ensuring all security patches are loaded. 

- ⚫ Verifying that all components and peripherals are operational. 

##### **SUSTAINMENT-LEVEL MAINTENANCE** 

5-20. SASMO teams do not perform sustainment-level maintenance on sustainment automation components. Sustainment maintenance is off-system end item repair and reparable component repair for return to the supply system (or by exception to the owning unit), performed by national-level maintenance providers. 

#### **ROLES AND RESPONSIBILITIES** 

5-21. Chief warrant officer 2 information system technicians (a signal MOS) typically lead SASMOs. The exceptions are the TSC and ESC, which have an information systems officer (a signal MOS at the rank of captain). The SASMO team may consist of 4 to 12 Soldiers (lower, mid, and senior level) from signal, quartermaster, aviation, medical, ordnance, and transportation backgrounds—there is no singular MOS for this function. Personnel serving in SASMOs can be in the following MOSs: 68G (patient administration specialist), 68J (medical logistics specialist), 88N (transportation management coordinator), 92Y (unit supply specialist), or 92A (automated logistical specialist), 255A (information services technician), 25B (information technician) or 15T, (UH-60 helicopter repairer). Leaders should recognize the need for providing training for these Soldiers to ensure properly operating networks. See Figure 5-3 for SASMO composition by MOS and echelon. Figure 5-3 offers a snapshot that may change; the purpose of the graphic is to illustrate the mix of MOSs assigned to a SASMO team. 

**5-8** 

**ATP 4-0.6** 

**17 January 2024** 

**SASMO Operations** 



**Figure 5-3. Sustainment automation support management office composition** 

5-22. Figure 5-3 illustrates that the SASMO is comprised of sustainment, medical, aviation and signal Soldiers. These MOSs are not trained in repair of computer and communications equipment. The following titles and duty descriptions may vary depending upon the unit. Due to various sizes of SASMOs, one individual may perform the tasks of two or more of the following titles. Figure 5-4 depicts a notional SASMO. 

**17 January 2024** 

**ATP 4-0.6** 

**5-9** 

**Chapter 5** 



**Figure 5-4. Notional sustainment automation support management office** 

##### **COMMANDER** 

5-23. Commanders are responsible for the management of SASMO operations. Commanders should develop a clearly defined automation plan that includes the full range of network administration, systems administration, and hardware maintenance. A major part of the success in leveraging sustainment automation involves the development of an integrated maintenance plan for keeping all the associated hardware and software operational and functioning. Commanders engage in the planning and coordination of new equipment fielding to ensure that all sustainment automation is running on the correct baseline. Commanders ensure that new sustainment automation administrators are properly on-boarded for supported EBS, and that they are sufficiently trained to perform network administration and systems administration. Commanders also ensure that SASMO teams receive training on any business processes for supported EBS business processes. 

##### **SUPPORT OPERATIONS OFFICER** 

5-24. The SPO manages SASMO operations. This includes training on sustainment automation policy, systems administration, and network administration. SPOs are the focal point for new EBS fielding, software changes, engineer change proposals, and other sustainment automation actions requiring coordination between elements within and outside of the command. SPOs develop sustainment automation plans for supported units. They coordinate with the G-6/S-6 to ensure sustainment automation complies with network architecture guidelines. SPOs assist in maintaining a common operational picture by monitoring the STS between tactical, operational, and strategic nodes. They maintain, monitor, and report the status of the sustainment automation of their supported units. 

##### **BRANCH CHIEF** 

5-25. The SASMO branch chief reports to the SPO officer. The SASMO branch chief represents the SPO officer in formal and informal planning that involves sustainment automation. This includes participation on boards, bureaus, centers, cells, rehearsals, synchronization meetings, and working groups, in accordance with the battle rhythm and SPO priorities. The branch chief coordinates and synchronizes activities between the 

**5-10** 

**ATP 4-0.6** 

**17 January 2024** 

**SASMO Operations** 

technical channels (signal elements and EBS program managers) and the supported staff sections and units. SASMO branch chiefs coordinate with the G-6 or S-6 for significant network administration activities and with the G-4 or S-4 for significant systems administration activities. The branch chief provides sustainment information management by— 

- ⚫ Maintaining status of personnel, weapons, and equipment, and submitting standardized reports to the SPO officer. 

- ⚫ Planning sustainment automation data flow, diagramming network topology, and designing network architecture. 

- ⚫ Directing systems administration and network operations and developing the PACE plan for communications. 

- ⚫ Coordinating implementation of theater Army communications security policies and guidance. 

- ⚫ Maintaining tactical situational awareness and analyzing the elements of the information environment that support the commander’s intent and concept of the operation. 

- ⚫ Ensuring that technical assistance teams receive and rehearse guidance for operating in a forward area. 

- ⚫ Ensuring that communications status reports are accurately prepared and submitted according to unit SOP. 

- ⚫ Supervising quality control and adherence to policies and procedures, to include overall use of available personnel skills. 

- ⚫ Coordinating with other SASMO branch chiefs to ensure specific task coordination. 

- ⚫ Developing processes, procedures, policies, and the SASMO production control system. 

- ⚫ Developing a SASMO-specific training program that ensures a balanced knowledge base through the cross-training of personnel. 

- ⚫ Reviewing routine service and approving emergency support requests. 

##### **INFORMATION SYSTEMS SUPERVISOR** 

5-26. The information systems supervisor typically serves as the noncommissioned officer in charge (NCOIC) for the day-to-day management of SASMO operations. The NCOIC provides technical, operations, maintenance, and logistical support and tactical advice to the branch chief, information systems technician, commander, and staff sections. This individual also conducts briefings on the status, relationship, and interface of sustainment automation within the assigned area of interest; supervises or prepares technical studies, evaluations, reports, correspondence, and records pertaining to sustainment automation; and plans, organizes, and conducts technical inspections. The NCOIC's general responsibilities include, but are not limited to— 

- ⚫ Managing and supervising day-to-day operations and personnel, ensuring adherence to policies and procedures, quality control, on-the-job training, and daily duties 

- ⚫ Identifying critical system and user errors that degrade productivity. 

- ⚫ Preparing incident response communications. 

- ⚫ Preparing documentation of the user density (by location and quantity). 

- ⚫ Monitoring the effectiveness of access administrators. 

- ⚫ Validating and directing training execution. 

- ⚫ Validating and consolidating all functional training documentation. 

- ⚫ Validating help desk tickets to confirm system faults. 

- ⚫ Monitoring the disposition of users (by location and quantity). 

- ⚫ Maintaining the production control system; coordinating the release of on-site technical support and the issue of tactical computer exchange equipment. 

- ⚫ Coordinating routine service and making recommendations for emergency support requests. 

- ⚫ Coordinating and assisting with implementation plans for software change packages, interim change packages, and new equipment fielding. 

- ⚫ Tracking all supported sustainment automation; maintaining the list for all equipment on network, ensuring each is appropriately labeled and conforms to the established naming convention. 

**17 January 2024** 

**ATP 4-0.6** 

**5-11** 

**Chapter 5** 

##### **COMMUNICATIONS NCOIC** 

5-27. Communications NCOIC general responsibilities include, but are not limited to— 

- ⚫ Designing and managing the STS. 

- ⚫ Identifying and mitigating conditions that will disrupt network operations. 

- ⚫ Validating and consolidating all network diagrams. 

- ⚫ Validating technical faults of network components. 

- ⚫ Monitoring the effectiveness of system administrators. 

- ⚫ Reporting unplanned, planned, and scheduled service outages. 

- ⚫ Maintaining workstations and software. 

##### **COMMUNICATIONS TECHNICIAN** 

5-28. Communications technician general responsibilities include, but are not limited to— 

- ⚫ Configuring the STS. 

- ⚫ Configuring workstations and software. 

- ⚫ Developing unit technical training to sustain the proficiency of users required to set up network nodes. 

- ⚫ Executing technical training on the setup of network nodes. 

- ⚫ Identifying and documenting technical faults of network components. 

- ⚫ Implementing applicable cybersecurity requirements. 

##### **INFORMATION SYSTEMS TECHNICIAN** 

5-29. The information systems technician manages shop technical operations through the following activities: 

- ⚫ Monitoring the coordination of information assurance vulnerability alert updates. 

- ⚫ Developing and maintaining a production control system. 

- ⚫ Controlling issuance of computer exchange equipment. 

- ⚫ Maintaining operational control over organic elements performing software and hardware support. 

- ⚫ Coordinating the dispatch of technical assistance teams. 

- ⚫ Planning and coordinating the implementation of software change packages, interim change packages, and new equipment fielding; preparing and initializing requests for support; and acting as liaison between analysts and contract supported operations. 

- ⚫ Initiating contact with contract support personnel for evacuation or onsite repair of inoperable hardware. 

- ⚫ Notifying units when repairs are completed and equipment is ready for pickup. 

#### **DEPLOYMENT AND REDEPLOYMENT** 

5-30. Knowledge of the terrain is critical to planning. If possible, a SASMO team member accompanies the advance party to conduct a site survey and assess the potential of the selected space to establish the SASMO. Identify hazards that can result in injury, illness, or death of personnel; damage, loss, or destruction of equipment and other assets; or degradation of capabilities or mission failure. Hazards can be associated with enemy activity, accident potential, weather or environmental conditions, health, sanitation, and equipment. Hazards occur in combat operations, stability operations, base support operations, training, garrison activities, and off-duty activities. Consider hazard impacts on mission and non-mission-related aspects of the SASMO location. A SASMO may be required to jump from one location to another within an AO to support the maneuver commander's sustainment requirements. 

5-31. SASMOs may be deployed in support of combat operations, homeland defense operations, or defense support of civil authorities operations in response to domestic crises such as natural disasters. Thorough planning is the key to mission accomplishment. Regardless of the operation, the planning process is basically 

**5-12** 

**ATP 4-0.6** 

**17 January 2024** 

**SASMO Operations** 

the same. To meet contingency support requirements, units develop movement plans and SOPs. An effective movement plan contains sufficient detail to prepare units to execute deployments. The SOP outlines functions that should occur upon notification of a unit movement. These documents are typically compiled in a binder. 

5-32. The SASMO’s deployment binder serves as a continuity bridge from one leader to the next. The SASMO SOPs should cover pre-movement checks, pre-movement inspections, who to report to, and who executes which tasks. SOPs should address standard locations, location of mission-essential equipment, and vehicle load plans. The SOP should address all roles and responsibilities for the deployment. Every Soldier should know their part of every mission. Every leader should practice troop leading procedures. Rehearsals and precombat inspections cannot be emphasized enough. Rehearsals ensure that the SASMO will be ready when the commander needs it. Develop a key task list for the SASMO and ensure that all Soldiers are trained on those tasks. During training exercises and rehearsals, ask questions about the commander's intent and the desired end state. 

5-33. SASMOs should rehearse basics and add specifics to the rehearsals as details emerge. Each SASMO develops specific battle-oriented, pre-movement checks focused on specific SASMO requirements. As a minimum, each Soldier should understand the nature of the operation: 

- ⚫ Participants. 

- ⚫ Time of the operation. 

- ⚫ Assigned tasks. 

- ⚫ The route (briefed to all drivers). 

- ⚫ Call signs, passwords, and number combinations. 

- ⚫ Location of objective. 

- ⚫ Individual’s job and job of immediate leader. 

- ⚫ Location of leaders. 

- ⚫ Location of other friendly units (situational awareness). 

5-34. Load planning is a critical part of deployment planning. Prior to the move, the SASMO should perform a 100% inventory; the SASMO should know what it is moving and where every item is packed. When the SASMO arrives at its destination, it should perform a 100% inventory to ensure that nothing was lost in transit. Leaders should prepare a detailed load plan and ensure that all SASMO team members are familiar with the plan. The load plan details the storage locations by container or bumper number. SASMOs should maximize vehicle and container load capacities. The packing list will change from mission to mission, but most of the items on the list are necessary for the completion of every mission. 

**17 January 2024** 

**ATP 4-0.6** 

**5-13** 

This page intentionally left blank. 

### **Appendix A Training** 

To successfully conduct military operations in any OE, SASMO teams should be technically competent and tactically proficient in the employment of their platform weapons systems. This appendix provides a list and descriptions of recommended training for Soldiers assigned to SASMOs. 

#### **REQUIRED TRAINING** 

A-1. SASMOs require time and resources for training to gain proficiency in their role. SASMO teams administer to multiple systems. They require training on system-specific software operations, hardware operations, maintenance, and troubleshooting for the STS and applicable EBSs. SASMO training should be a deliberate, continuous, sequential, and progressive process embedded in the Army training plan. SASMO teams should be skilled in operating the systems used by their MOS, plus have the capability to become proficient in other EBSs. Most signal personnel lack the necessary background to support sustainment operations, just as system and network administration is foreign to most sustainers. Because SASMOs are relatively small, team members should cross train on individual tasks of other team members. Sustainment Soldiers should learn signal fundamentals and the fundamentals of other sustainment MOSs. Signal Soldiers should learn sustainment fundamentals regarding supported EBS. Development and implementation of an effective training strategy can decrease the time needed to achieve the level of competency required and increase the time a command reaps the benefits of a competent SASMO team. Normally, SASMO personnel require 60 days to become proficient. 

##### **ENTERPRISE BUSINESS SYSTEMS TRAINING** 

A-2. Prior to a SASMO assignment Soldiers with a sustainment MOS normally receive institutional sustainment automation (for the applications used by their MOS) as well as new equipment training. New equipment developers’ mobile training teams typically provide hardware or software training when new technology emerges. SASMO team members from a signal MOS typically do not have this training background. 

A-3. Institutional training incorporates sustainment automation training into existing or newly developed programs. Since nearly all sustainment activities use EBS, training on operating and maintaining sustainment automation is part of programs of instruction spanning all levels of professional military education. The following courses provide this institutional training: 

- ⚫ Advanced Leaders Course. 

- ⚫ Senior Leaders Course. 

- ⚫ Warrant Officer Basic and Advanced Courses. 

- ⚫ Advanced Individual Training. 

- ⚫ Basic Officer Leader Course. 

- ⚫ Captain’s Career Course (provides training on information systems as a staff integration tool). 

- ⚫ The Command and General Staff College provides training on using information systems to conduct combat operations as a combined arms team at division and corps level. 

A-4. Embedded training supports individual skill development and sustainment training in the institutional and unit sustainment training environments. Embedded training includes a capability to link one or several information systems to a local or remote simulation system to support collective training. Embedded training incorporates performance support systems. Embedded training provides— 

**17 January 2024** 

**ATP 4-0.6** 

**A-1** 

**Appendix A** 

- ⚫ A means to track individual user proficiency and automatically modify the amount of assistance that the system provides during operation or training. 

- ⚫ A context-sensitive help feature that provides information on system operation (tailored to the process or function) upon request. 

- ⚫ Mini tutorials that are more extensive than a help screen. This feature provides a short and contextsensitive lesson aimed at helping to negotiate complex functions. 

- ⚫ Courseware that provides interactive, scenario-based instruction on all or a part of the operational software. 

- ⚫ Technical and field manuals via electronic media. This feature enables the user to call up a reference to a tactical or technical problem without leaving the keyboard. 

A-5. To maintain electronic health records, the SASMO teams must be trained on the Health Insurance Portability and Accountability Act. The Health Insurance Portability and Accountability Act Privacy Rule establishes national standards to protect individual medical records and other personal health information and applies to health plans, health care clearinghouses, and those health care providers that conduct certain health care transactions electronically. It requires appropriate safeguards to protect the privacy of personal health information and sets limits and conditions on the uses and disclosures that may be made of such information without patient authorization. It also gives patient rights over their health information, including rights to examine and obtain a copy of their health records and to request corrections. The following DOD publications govern requirements for personnel who encounter personally identifiable information and personal health information: 

- ⚫ DOD 5400.11-R. 

- ⚫ DODM 5400.11. 

- ⚫ DODM 6025.18. 

A-6. Units should provide sustainment training to prevent individual skill decay and attain collective proficiency to support mission accomplishment. SASMO teams typically undergo on-the-job training for sustainment automation training rather than a specific training program aimed at SASMO operations. 

##### **CYBERSECURITY TRAINING** 

A-7. The Department of Defense Cyber Workforce Strategy provides the basis for an enterprise-wide solution to train, certify, and manage the DOD cybersecurity workforce. The policy requires cyberspace (formerly known as information assurance) technicians and managers to be trained and certified to a DOD baseline requirement. The accompanying manual, DODM 8140.03 identifies the specific certifications mandated by the directive’s enterprise-wide certification program. 

###### **Who Needs To Be Certified?** 

A-8. All Soldiers and DOD Civilians serving in a SASMO position, regardless of MOS or job description, are required to obtain a DOD baseline certification in accordance with DODM 8140.03. This policy defines cybersecurity workforce members as anyone with privileged information system access performing cyberspace functions. The training, certification, and workforce management requirements apply to all members of the DOD cyberspace and information assurance workforce, including military, civilians, foreign nationals, local nationals, non-appropriated fund workers, and contractors. They apply whether the duties are performed full-time, part-time, or as an embedded duty. 

###### **Baseline Certification Requirements** 

A-9. The Cyberspace and Information Assurance Workforce Improvement Program is a workforce management program. Since SASMO staffs perform network administration and systems administration tasks, leaders should consider the following information to ensure that their SASMOs can execute the complexities of managing sustainment automation. The key to workforce management is the position. All positions required to perform cyberspace or information assurance functions should be identified. Any person filling that position is then automatically part of the cyberspace and information assurance workforce. This 

**A-2** 

**ATP 4-0.6** 

**17 January 2024** 

**Training** 

includes whether it is full time, part-time, or embedded duty or whether it is their primary specialty, secondary specialty, or a non-specialty-related assigned duty. 

A-10. DODM 8140.03 includes Service members, DOD Civilian employees (including non-appropriated fund employees), contractors, and foreign nationals. For the purposes of accountability, oversight, and reporting, each cyberspace workforce position is aligned to a workforce element that is reviewed annually and updated under the authority of the Cyberspace Workforce Management (see DODD 8140.01). The program details qualification requirements for each DOD Cyberspace Workforce Framework work role up to three levels of proficiency. The proficiency level describes the levels of a capability required to successfully perform work and defines performance expectations for the following: 

- ⚫ Basic. 

   - Familiarity with basic concepts and processes and the ability to apply these with frequent, specific guidance. 

   - Perform successfully in routine, structured situations. 

- ⚫ Intermediate. 

   - Extensive knowledge of basic concepts and processes and experience applying these with only periodic high-level guidance. 

   - Perform successfully in non-routine and sometimes complicated situations. 

- ⚫ Advanced. 

   - In-depth understanding of advanced concepts and processes and experience applying these with little or no guidance. 

   - Provide guidance to others. 

   - Perform successfully in complex, unstructured situations. 

   - May require the performance of multiple work roles at different levels of proficiency. In such cases, individuals must be qualified at the levels dictated by the requirements of the position. 

A-11. Table A-1 contains the titles for online platform training typically offered by the proponent. The user resource links are not provided, as these are subject to change. Due to rapid changes in technology, the following list may also become outdated prior to the next revision of this publication. Unit training managers should seek advice from, and coordinate with, sustainment automation proponents to verify that the SASMO teams are receiving the most relevant and up-to-date training. 

**Table A-1. Platform training** 

|**_PLATFORM_**|**_SUBSYSTEM_**|**_TITLE_**|
|---|---|---|
|Financial<br>Management|Financial Management Tactical<br>Platform|Finance Software Automation Training (CAC<br>Required)|
|Logistics|Global Combat Support System –<br>Army Training and Certification<br>system|Familiarization Training|
|Medical|HALO|HALO|
|Medical|TC2|GUI Nurse|
|Medical|TC2|GUI PAD|
|Medical|TC2|GUI Provider|
|Medical|TC2|Laboratory|
|Medical|TC2|Nurse|
|Medical|TC2|PAD|
|Medical|TC2|Pharmacy|
|Medical|TC2|Provider|



**17 January 2024** 

**ATP 4-0.6** 

**A-3** 

**Appendix A** 

**Table A-1. Platform training (continued)** 

|**_PLAT_**|**_FORM_**|**_SUBSYSTEM_**|**_TITLE_**|
|---|---|---|---|
|Medical||TC2|Radiology|
|Medical||Certification requirement|Health Insurance Portabilityand AccountabilityAct|
|JOMIS||TMIP|TMIP Reporting|
|JOMIS||DCAM|DCAM Level 1|
|JOMIS||DCAM|DCAM Level 2|
|JOMIS||TMDS|Behavioral Health|
|JOMIS||TMDS|Facilityand CASF Reports|
|JOMIS||TMDS|Guidelines InfoLinks and Admin Tabs|
|JOMIS||TMDS|Introduction|
|JOMIS||TMDS|Level 4 & 5 Reports|
|JOMIS||TMDS|Patient Registration|
|JOMIS||TMDS|Patient Search and Patient Information|
|JOMIS||TMDS|Patients ByService|
|JOMIS||TMDS|TMDS Level 4 Functionality|
|MTS||Movement TrackingSystem|TrainingMaterials|
|RF-ITV||Radio Frequency-Intransit Visibility|TagRead Operations|
|RF-ITV||Radio Frequency-Intransit Visibility|TagWrite Operations|
|RF-ITV||Radio Frequency-Intransit Visibility|RF-ITV TrackingPortal(simulation)|
|RF-ITV||Radio Frequency-Intransit Visibility|Savi Client Tools 4.3 B0023|
|RF-ITV||Radio Frequency-Intransit Visibility|Savi Site Manager 5.6|
|RF-ITV||Radio Frequency-Intransit Visibility|Sensor Tag|
|RF-ITV||Radio Frequency-Intransit Visibility|SmartChain Workstation 6.0|
|RF-ITV||Radio Frequency-Intransit Visibility|TIPS-Read 4.3|
|RF-ITV||Radio Frequency-Intransit Visibility|TIPS-Write 4.1|
|SAAS||Standard Army Ammunition<br>System|SAAS Performance Support Tool|
|TC-AIM|S II|Barstow 6.3.0|Unit Move 1 Course Slides|
|TC-AIM|S II|Barstow 6.3.0|Unit Move 1 Course Student Guide|
|TC-AIM|S II|Barstow 6.3.0|Unit Move 1 Course Student Guide Hope|
|TC-AIM|S II|Barstow 6.3.0|Unit Move 2 Course Slides|
|TC-AIM|S II|Barstow 6.3.0|Unit Move 2 Course Student Guide|
|TC-AIM|S II|Barstow 6.3.0|Unit Move 2 Course Student Guide Hope|
|CAC<br>CASF<br>DCAM<br>GUI<br>HALO<br>JOMIS|common<br>continge<br>Defense<br>Custom<br>Graphic<br>Health A<br>Joint Op|access card<br>ncy aeromedical staging facility<br>Medical Logistics Standard Support<br>er Assistance Module<br>al User Interface<br>ssessment Lite Operations<br>erational Medicine Information Systems|RF-ITV<br>Radio Frequency-Intransit Visibility<br>SAAS<br>Standard Army Ammunition System<br>TC2<br>Theater Medical Information Program<br>Composite Health Care System Cache<br>TC-AIMS II<br>Transportation Coordinators' Automated<br>Information for Movements System II<br>TMIP<br>Theater Medical Information Program|
|MTS<br>PAD|Moveme<br>Patient|nt Tracking System<br>Administration Division|TMDS<br>Theater Medical Data Store|



**A-4** 

**ATP 4-0.6** 

**17 January 2024** 

**Training** 

###### **Sustainment Systems Master Gunner Course** 

A-12. Army Sustainment University at Fort Lee offers a course for Soldiers assigned to SASMO positions. Soldiers in qualified MOSs earn the additional skill identifier N8 upon completing this course. An additional skill identifier recognizes specialized skills qualifications, and requirements (acquired through formal school training or civilian certification) that are closely related to and are in addition to those inherent to the MOS. N8 refers to Soldiers qualified in SASMO operations. See DA Pam 611-21 for more information about additional skill identifiers. 

A-13. The Sustainment Systems Master Gunner Course teaches functional and technical skills required to establish, manage, and sustain Army EBS (specifically GCSS-Army, ACN, Standard Army Ammunition System, TC AIMS-II, and OMIS-A) and the STS (CSS VSAT and CAISI). Students will graduate with the technical expertise to help ensure the sustainment automation connectivity that enables the EBS tools for retaining unit operational reach. See Chapter 3 for the list of sustainment automation for which the SASMO provides network but not systems administration. Course requirements are met through a blended learning experience consisting of distance and resident classroom participation. At the end of the course students have the tools to manage (create) work centers, create and close maintenance notification work orders in GCSSArmy. Successful completion of the gunnery scenario demonstrates that the student has acquired the tools for installing, configuring, and troubleshooting software and hardware components while establishing network connectivity. 

#### **UNIT-LEVEL TRANING** 

A-14. Log into the Army Training Network (https://atn.army.mil/) to download collective and individual tasks. These tasks have been developed and approved by Army Training Development and hosted on the Central Army Registry to develop unit training plans. SASMO teams should have a basic knowledge of computer hardware, operating systems, network operation, and computer security and possess the elevated system privileges to execute the following: 

- ⚫ Coordination with maintenance facility for field-level hardware maintenance of desktops, laptops, printers, communications, and all other peripherals. 

- ⚫ Coordination for sustainment-level exchange of hardware. 

- ⚫ Computer hardware and internet communications operation installation and setup. 

- ⚫ Software installation. 

- ⚫ Upgrading. 

- ⚫ Diagnostic troubleshooting. 

- ⚫ Client/server connectivity and network protocols. 

- ⚫ Connection to the internet. 

- ⚫ Configuration of operating systems. 

- ⚫ Troubleshooting system errors. 

##### **GUNNERY SKILLS TEST** 

A-15. With DOD’s emphasis on automation, becoming data-centric, and IT as a weapons system, EBSs must be capable of “talking” to each other via the STS. The Army adopted the enterprise approach to integrate sustainment organizations and functions from the battlefield back to the strategic level, to include the commercial sector. Sustainment leaders, planners, and managers should know the physical and the automated sustainment processes to manage and mitigate bottlenecks that could hamper support. All units with CSS VSAT and EBS should develop, coordinate, publish, rehearse, and conduct sustainment automation gunneries as routine unit training. Frequent gunnery skills training will help to ensure end-to-end connectivity under deployed conditions. 

**Note:** CAISIs and CSS VSATs are assigned to the using unit, not to the SASMO. Commanders should ensure that end user personnel are fully trained in set-up and preventive maintenance. CAISI and CSS VSAT maintenance should be treated with the same level of urgency as any other end item. 

**17 January 2024** 

**ATP 4-0.6** 

**A-5** 

**Appendix A** 

A-16. Gunnery skills tests were developed and used to test and evaluate individual and crew skills for stabilized and mounted weapons platforms. The gunnery skills test has been found to be an effective tool for training SASMO teams to establish communications connectivity. Because SASMO sections are small, it is prudent to cross train team members to perform all systems and network administration tasks for that section. Sustainment automation gunneries should focus on the unit’s capability to set up its CSS VSAT, maintain CSS VSAT equipment, and establish network connectivity. Each functional participant assigned a CSS VSAT (for example, maintenance company, supply support activity, personnel, financial, health services) plays a separate but crucial role in establishing communication from the foxhole back to the strategic base. Due to reliance on networked communications, failure to establish connectivity negatively impacts operational readiness and combat power. To properly evaluate gunnery skills tests, units should consider the following factors: 

- ⚫ Administrative requirements. 

- ⚫ Evaluator availability based on requirements and certifications. 

- ⚫ Test locations. 

- ⚫ Resource requirements. 

- ⚫ Time. 

- ⚫ Retraining. 

- ⚫ Retests. 

##### **PLANNING CONSIDERATIONS** 

A-17. The SASMO team establishes network connectivity and verifies that automation works correctly. SPOs should conduct a sustainment automation gunnery prior to and upon arrival in the OE to ensure that communications equipment is operational and that the SASMO team knows how to establish the network quickly and effectively. See Figure A-1 for a notional concept of operations for a sustainment automation gunnery training exercise. The gunnery exercise should include end-user system operators, the communications and electronics maintenance shop, and the SASMO. End-user system operators should be fully trained in the capabilities of their applications, maintenance facilities should be fully trained in maintaining sustainment automation equipment while the SASMOs should be fully trained in launching the network. Sustainment automation training may focus on any of the following missions: 

- ⚫ Homeland defense. 

- ⚫ Security cooperation. 

- ⚫ Host-nation cooperation. 

- ⚫ Defense support of civil authorities. 

   - Disaster response. 

   - Wildland fire fighting. 

   - National special security events. 

A-18. This gunnery is a sustainment automation and organizational connectivity test. As such, a successful gunnery test is the result of coordination and planning between the SPO and the S-4 or G-4. The following gunnery planning considerations focus on short-term and long-term core missions and timelines. Short-term means 30 days or less, and long-term means 30 days or more: 

- ⚫ Short-term deployment glide path. ▪ Contingency DOD activity address code dime-test. 

   - Letter of authorization. 

   - Military interdepartmental purchase request. 

- ⚫ Long-term deployment glide path. 

   - STS architecture (current baseline updates). 

   - EBS hierarchy build. 

   - Contingency DOD activity address code dime-test. 

   - Army in-motion unit transfers in or out. 

- ⚫ Additional deployment considerations. 

**A-6** 

**ATP 4-0.6** 

**17 January 2024** 

**Training** 

- Number of users to be supported. 

- Sustainment automation equipment density. 

- Location of users. 

- Inability to use certain frequencies. 

- Type of terrain where deployed. 

- Antenna orientation and line of sight. 

- Location of wide area network communications. 



**Figure A-1. Notional concept of operations gunnery training exercise** 

**17 January 2024** 

**ATP 4-0.6** 

**A-7** 

**Appendix A** 

##### **EVALUATION** 

A-19. The foundation of a viable sustainment automation gunnery is to achieve seamless connectivity of EBS to support the maneuver commander's plan. Develop a ranking system that standardizes scores regardless of evaluator. See table A-2 for a sample score card. The gunnery test should be adapted to fit the commander’s needs for all phases of deployment. 

###### **Table A-2. Score card** 

||**_Gunnery Scorec_**<br>|**_ard_**<br>||
|---|---|---|---|
|**_(97-100) = Exceptional_**<br>Demonstrated a complete<br>mastery of this task.<br>Individual performance<br>includes insightful thought,<br>understanding, and<br>performance of this task.|**_(94-96) = Outstanding_**<br>Demonstrated a nearly<br>complete mastery of this<br>task.<br>Individual performance is<br>nearly always marked by<br>insightful thought,<br>understanding, and<br>performance of this task.|**_(90-93) = Excellent_**<br>Demonstrated an<br>extensive mastery of<br>this task.<br>Individual<br>performance is<br>marked by insightful<br>thought,<br>understanding, and<br>performance of this<br>task.|**_(87-89) = Very_**<br>**_Good_**<br>Consistently meets<br>all standards for<br>this task with no<br>unusual time, effort<br>or assistance<br>required.<br>Individual<br>performance is<br>often marked by<br>insightful thought,<br>understanding, and<br>performance of this<br>task.|
|**_(84-86) = Satisfactory_**<br>Requires above average<br>time or individual effort<br>but achieves all standards<br>for this task.<br>Individual performance is<br>sometimes marked by<br>insightful thought,<br>understanding, and<br>performance of this task.<br>*Repeated assistance|**_(80-83) = Average_**<br>Requires occasional<br>instructor assistance to<br>meet all standards for this<br>task.<br>Individual performance is<br>seldom marked by<br>insightful thought,<br>understanding, and<br>performance of this task.|**_(70-79) = Marginal_**<br>Requires<br>substantial<br>instructor<br>assistance to<br>achieve most of the<br>course standards.<br>Demonstrates low<br>comprehension of<br>this task and poor<br>ability to understand<br>or perform it.|**_<70 =_**<br>**_Unsatisfactory_**<br>Failed to achieve<br>many of the basic<br>standards in most<br>or all areas for the<br>assignment or<br>course.<br>Demonstrates<br>little<br>comprehension<br>and is not<br>competent in its<br>application.|



**A-8** 

**ATP 4-0.6** 

**17 January 2024** 

### **Glossary** 

The glossary lists acronyms and terms with Army or joint definitions and other selected terms. Where Army and joint definitions differ, (Army) precedes the definition. The proponent publication for terms is listed in parentheses after the definition. 

|**SECTION I – ACRO**|**NYMS AND ABBREVIATIONS**|
|---|---|
|**ADP**|Army doctrine publication|
|**AO**|area of operations|
|**AOR**|area of responsibility|
|**AR**|Army regulation|
|**ARCYBER**|United States Army Cyber Command|
|**ASCC**|Army Service component command|
|**ATP**|Army techniques publication|
|**BCT**|brigade combat team|
|**BSB**|brigade support battalion|
|**CAISI**|Combat Service Support Automated Information Systems Interface|
|**CIO**|chief information officer|
|**CSSB**|combat sustainment support battalion|
|**CSS VSAT**|Combat Service Support Very Small Aperture Terminal|
|**DA**|Department of the Army|
|**DA Pam**|Department of the Army pamphlet|
|**DMC**|distribution management center|
|**DOD**|Department of Defense|
|**DODI**|Department of Defense instruction|
|**DODIN**|Department of Defense information network|
|**DODIN-A**|Department of Defense information network-Army|
|**DODM**|Department of Defense manual|
|**EBS**|enterprise business system|
|**ESC**|expeditionary sustainment command|
|**FM**|field manual|
|**FMTP**|Financial Management Tactical Platform|
|**G-1**|assistant chief of staff, personnel|
|**G-3**|assistant chief of staff, operations|
|**G-4**|assistant chief of staff, logistics|
|**G-6**|assistant chief of staff, signal|
|**G-8**|assistant chief of staff, financial management|
|**GCSS-Army**|Global Combat Support System-Army|



**Glossary-1** 

**17 January 2024** 

**ATP 4-0.6** 

**Glossary** 

|**GFEBS**|General Fund Enterprise Business Systems|
|---|---|
|**IPPS-A**|Integrated Personnel and Pay System-Army|
|**IT**|information technology|
|**JP**|joint publication|
|**LAN**|local area network|
|**MOS**|military occupational specialty|
|**NCOIC**|noncommissioned officer in charge|
|**OE**|operational environment|
|**OMIS-A**|Operational Medical Information Systems-Army|
|**PACE**|primary, alternate, contingency, and emergency|
|**S-1**|battalion or brigade personnel staff officer|
|**S-2**|battalion or brigade intelligence staff officer|
|**S-3**|battalion or brigade operations staff officer|
|**S-4**|Battalion or brigade logistics staff officer|
|**S-6**|battalion or brigade signal staff officer|
|**SASMO**|sustainment automation support management office|
|**SATCOM**|satellite communications|
|**SOP**|standard operating procedure|
|**SPO**|support operations|
|**STS**|sustainment transport system|
|**TC**|training circular|
|**TC-AIMS II**|Transportation Coordinator’s Automated Information for Movement System II|
|**TSC**|theater sustainment command|
|**U.S.**|United States|
|**USAMC**|United States Army Materiel Command|



##### **SECTION II – TERMS** 

###### **battle damage assessment** 

The estimate of damage composed of physical and functional damage assessment, as well as target system assessment, resulting from the application of fires. (JP 3-0) 

###### **battle drill** 

Rehearsed and well understood actions made in response to common battlefield occurrences. (ADP 3-90) 

###### **command and control** 

The exercise of authority and direction by a properly designated commander over assigned and attached forces in the accomplishment of the mission. (JP 1, Vol 2) 

###### **common operational picture** 

(joint) A single identical display of relevant information shared by more than one command that facilitates collaborative planning and assists all echelons to achieve situational awareness. (JP 3-0) 

###### **concept of operations** 

(Army) A statement that directs the manner in which subordinate units cooperate to accomplish the mission and establishes the sequence of actions the force will use to achieve the end state. (ADP 5-0) 

**Glossary-2** 

**ATP 4-0.6** 

**17 January 2024** 

**Glossary** 

###### **distribution management** 

Synchronizes and optimizes transportation, its networks, and materiel management with the warfighting functions to move personnel and materiel from origins to the point of need in accordance with the supported commander's priorities. (ADP 4-0) 

###### **information environment** 

The aggregate of social, cultural, linguistic, psychological, technical, and physical factors that affect how humans and automated systems derive meaning from, act upon, and are impacted by information, including the individuals, organizations, and systems that collect, process, disseminate, or use information. (JP 3-04) 

###### **information management** 

(Army) The science of using procedures and information systems to collect, process, store, display, disseminate, and protect data, information, and knowledge products. (ADP 6-0) 

###### **knowledge management** 

(Army) The process of enabling knowledge flow to enhance shared understanding, learning, and decision making. (ADP 6-0) 

###### **line of sight** 

The unobstructed path from a Soldier’s weapon, weapon sight, electronic sending and receiving antennas, or piece of reconnaissance equipment from one point to another. (ATP 2-01.3) 

###### **materiel** 

All items necessary to equip, operate, maintain, and support military activities without distinction as to its application for administrative or combat purposes. (JP 4-0) 

###### **operational environment** 

The aggregate of the conditions, circumstances, and influences that affect the employment of capabilities and bear on the decisions of the commander. (JP 3-0) 

###### **operations process** 

The major command and control activities performed during operations: planning, preparing, executing, and continuously assessing the operation. (ADP 5-0) 

###### **planning** 

The art and science of understanding a situation, envisioning a desired future, and determining effective ways to bring that future about. (ADP 5-0) 

###### **redeployment** 

(joint) The transfer or rotation of forces and materiel to support another commander’s operational requirements, or to return personnel, equipment, and materiel to the home and/or demobilization stations for reintegration and/or out-processing. (JP 3-35) 

###### **situational understanding** 

The product of applying analysis and judgment to relevant information to determine the relationship among the operational and mission variables. (ADP 6-0) 

###### **technical channels** 

The chain of authority for ensuring the execution of clearly delineated technical tasks, functions, and capabilities to meet the dynamic requirements of Department of Defense information network operations. (ATP 6-02.71) 

###### **troop movement** 

The movement of Soldiers and units from one place to another by any available means. (ADP 3-90) 

**Glossary-3** 

**17 January 2024** 

**ATP 4-0.6** 

This page intentionally left blank. 

### **References** 

All websites accessed on 4 October 2023. 

#### **REQUIRED PUBLICATIONS** 

These documents must be available to intended users of this publication. 

- _DOD Dictionary of Military and Associated Terms_ . September 2023. 

- FM 1-02.1. _Operational Terms_ . 9 March 2021. 

- FM 1-02.2. _Military Symbols_ . 18 May 2022. 

#### **RELATED PUBLICATIONS** 

These documents are cited in this publication. 

##### **JOINT AND DEPARTMENT OF DEFENSE PUBLICATIONS** 

Most Department of Defense publications are available online: https://www.esd.whs.mil/dd/. Most joint publications are available online: https://www.jcs.mil/Doctrine/. 

- DOD 5400.11-R. _Department of Defense Privacy Program_ . 14 May 2007. 

- DODD 8140.01. _Cyberspace Workforce Management_ . 5 October 2020. 

- DODI 8510.01. _Risk Management Framework for DOD Systems_ . 19 July 2022. 

- DODM 5400.11, Volume 2. _DOD Privacy and Civil Liberties Programs: Breach Preparedness and Response Plan_ . 6 May 2021. 

- DODM 6025.18. _Implementation of the Health Insurance Portability and Accountability Act (HIPAA) Privacy Rule in DOD Health Care Programs_ . 13 March 2019. 

- DODM 8140.03. _Cyberspace Workforce Qualification and Management Program_ . 15 February 2023. 

- JP 1, Volume 2. _The Joint Force_ . 19 June 2020. 

- JP 3-0. _Joint Campaigns and Operations_ . 18 June 2022. 

- JP 3-04. _Information in Joint Operations_ . 14 Sep 2022. 

- JP 3-35. _Joint Deployment and Redeployment Operations_ . 31 March 2022. 

- JP 3-85. _Joint Electromagnetic Spectrum Operations._ 22 May 2020. 

- JP 4-0. _Joint Logistics_ . 20 July 2023. 

##### **ARMY PUBLICATIONS** 

Most Army doctrinal publications are available online: https://armypubs.army.mil. 

- ADP 3-90. _Offense and Defense_ . 31 July 2019. 

- ADP 4-0. _Sustainment_ . 31 July 2019. 

- ADP 5-0. _The Operations Process_ . 31 July 2019. 

- ADP 6-0. _Mission Command: Command and Control of Army Forces_ . 31 July 2019. 

- AR 25-1. _Army Information Technology_ . 15 July 2019. 

- AR 25-2. _Army Cybersecurity_ . 4 April 2019. 

- ATP 2-01.3. _Intelligence Preparation of the Battlefield_ . 1 March 2019. 

- ATP 3-91. _Division Operations_ . 17 October 2014. 

- ATP 3-92. _Corps Operations_ . 7 April 2016. 

- ATP 3-93. _Theater Army Operations_ . 27 August 2021. 

**References-1** 

**17 January 2024** 

**ATP 4-0.6** 

**References** 

- ATP 4-33. _Maintenance Operations_ . 9 July 2019. 

- ATP 4-35. _Munitions Operations_ . 31 January 2023. 

- ATP 4-42. _Materiel Management, Supply, and Field Services Operations_ . 2 November 2020. 

- ATP 4-90. _Brigade Support Battalion_ . 18 June 2020. 

- ATP 4-91. _Division Sustainment Operations_ . 8 November 2022. 

- ATP 4-92. _Field Army and Corps Sustainment Operations_ . 14 March 2023. 

- ATP 4-93. _Theater Sustainment Operations_ . 1 May 2023. 

- ATP 4-93.1. _Combat Sustainment Support Battalion_ . 19 June 2017. 

- ATP 6-01.1. _Techniques for Effective Knowledge Management_ . 6 March 2015. 

- ATP 6-02.45. _Techniques for Tactical Signal Support to Theater Operations_ . 7 November 2019. 

- ATP 6-02.60. _Tactical Networking Techniques for Corps and Below_ . 9 August 2019. 

- ATP 6-02.70. _Techniques for Spectrum Management Operations_ . 16 October 2019. 

- ATP 6-02.71. _Techniques for Department of Defense Information Network Operations_ . 30 April 2019 . 

- DA Pam 611-21. _Military Occupational Classification and Structure_ . 20 December 2022. 

- FM 3-0. _Operations_ . 1 October 2022. 

- FM 3-12. _Cyberspace Operations and Electromagnetic Warfare_ . 24 August 2021. 

- FM 4-0. _Sustainment Operations_ . 31 July 2019. 

- FM 6-0. _Commander and Staff Organization and Operations_ . 16 May 2022. 

- FM 6-02. _Signal Support to Operations_ . 13 September 2019. 

- FM 6-27/MCTP 11-10C. _The Commander's Handbook on the Law of Land Warfare_ . 7 August 2019. 

- TC 4-11.47. _The Senior Gunner Program for Sustainment Units._ 26 October 2020. 

##### **OTHER PUBLICATIONS** 

_Army Unified Network Plan 2021_ . _The Army Unified Network Plan Enabling Multi-Domain Operations_ . Available at https://api.army.mil/e2/c/downloads/2021/10/07/d43180cc/army- <u>unified-network-plan-2021.pdf.</u> 

- _DOD Cyber Workforce Strategy 2023-2027_ . 1 March 2023. Available at <u>https://dodcio.defense.gov/Portals/0/Documents/Library/CWF-Strategy.pdf.</u> 

- _Department of Defense Data Strategy 2020_ . Available at 

- <u>https://media.defense.gov/2020/Oct/08/2002514180/-1/-1/0/DOD-DATA-STRATEGY.PDF.</u> 

- NATO Standard AMedP-5.2. _Standards for Data Interchange Between Health Information Systems_ . - 

- August 2018. Available at <u>https://www.coemed.org/files/stanags/03_AMEDP/AMedP 5.2_EDA_V1_E_2543.pdf.</u> 

#### **PRESCRIBED FORMS** 

This section contains no entries. 

#### **REFERENCED FORMS** 

Unless otherwise indicated, DA Forms are available online : https://armypubs.army.mil. 

DA Form 2028. _Recommended Changes to Publications and Blank Forms._ 

**References-2** 

**ATP 4-0.6** 

**17 January 2024** 

### **Index** 

Entries are by paragraph number. 

###### **A-C** 

Combat Service Support Automated Information Systems Interface, 3-6 

Combat Service Support Very Small Aperture Terminal, 3-5 communications status report, 4-3, 4-8, 4-12, 4-13, 4-15, 5-25 

###### **D** 

Department of Defense Information Network-Army, 1-11 distribution management process, 2-37 

###### **E-G** 

enterprise business systems, 1-2 

###### **H** 

hardware, 3-2 

###### **I-J** 

information environment, 1-3 information management, 1-8, 1-18, 5-25 

###### **K-M** 

knowledge management, 1-9 

###### **N-O** 

network administration, 1-6 network operations, 1-16 

###### **P-R** 

primary, alternate, contingency, and emergency (PACE) plan, 4-4, 4-5 

###### **S** 

satellite communications (SATCOM) terminal, 1-8, 3-5 software, 3-3 sustainment automation, 1-3 sustainment transport system, 1-2, 1-8, 3-7 systems administration, 1-6 

###### **T-Z** 

Tier 0, 1-1, 5-4, 5-19 Tier 1, 1-1, 5-4, 5-19, 1-1, 2-1, 3-1 

**17 January 2024** 

**ATP 4-0.6** 

**Index-1** 

This page intentionally left blank. 

**ATP 4-06 17 JANUARY 2024** 

By Order of the Secretary of the Army: 

**RANDY A. GEORGE** _General, United States Army Chief of Staff_ 

Official: 



**MARK F. AVERILL** _Administrative Assistant_ 

_to the Secretary of the Army_ 2400905 

##### **DISTRIBUTION:** 

_Active Army, Army National Guard, and United States Army Reserve._ Distributed in electronic media only (EMO). 

This page intentionally left blank. 

**PIN: 103011-001** 

