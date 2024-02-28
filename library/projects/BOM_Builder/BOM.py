from selenium.webdriver.common.by import By


class BOMLocators(object):
    def __init__(self, context=None):
        # create BOM
        self.new_bom_headings = (By.XPATH, "(//p[@class='font-work-sans text-black dark:text-white text-4xl'])[1]")
        self.step_1 = (By.XPATH, "(//p[@class='font-work-sans text-black dark:text-white text-[1.25rem]'])[1]")
        self.create_bom_btn = (By.XPATH, "//button[normalize-space()='Create BOM']")
        self.current_assignee_lbl = (By.XPATH, "//label[normalize-space()='Current Assignee']")
        self.assigned_team_lbl = (By.XPATH, "//label[normalize-space()='Assigned Team']")
        self.project_lbl = (By.XPATH, "(//label[normalize-space()='Project #'])[1]")
        self.pre_deply_lbl = (By.XPATH, "(//label[normalize-space()='Pre-Deployment Start Date'])[1]")
        self.wrehouse_stgng_lbl = (By.XPATH, "//label[normalize-space()='Warehouse Staging Location']")
        self.bom_type_lbl = (By.XPATH, "//label[normalize-space()='BOM Type']")
        self.site_name_lbl = (By.XPATH, "(//label[normalize-space()='Site Name'])[1]")
        self.site_installation_lbl = (By.XPATH, "//label[normalize-space()='Site Installation Type']")
        self.ntlink_owned_lbl = (By.XPATH, "//label[normalize-space()='Nextlink Owned Tower Type (New Build Only)']")
        self.highest_lbl = (By.XPATH, "(//label[normalize-space()='Highest Height to hoist grip/break out box'])[1]")
        self.horizontal_lbl = (By.XPATH,
                               "(//label[normalize-space()='Horizontal Lenght to hoist grip/break out box'])[1]")
        self.ice_bridge_lbl = (By.XPATH, "(//label[contains(.,'Ice Bridge')])")
        self.cabinet_type_lbl = (By.XPATH, "//label[normalize-space()='Cabinet Type']")
        self.cabinet_kit_lbl = (By.XPATH, "//label[normalize-space()='Cabinet Kit Needed']")
        self.cabinet_needed_lbl = (By.XPATH, "//label[normalize-space()='Cabinet Needed']")
        self.batteries_needed_lbl = (By.XPATH, "//label[normalize-space()='Batteries Needed']")
        self.cabinet_pentration_lbl = (By.XPATH, "//label[normalize-space()='Cabinet Penetration Kit Needed']")
        self.breakout_box_lbl = (By.XPATH, "//label[normalize-space()='Breakout box type']")
        self.nmber_breakout = (By.XPATH, "(//label[normalize-space()='Number of breakout boxes'])[1]")
        self.verticals_lbl = (By.XPATH, "(//label[normalize-space()='Verticals'])[1]")
        self.horizontal_lbl = (By.XPATH, "(//label[normalize-space()='Horizontal'])[1]")
        self.save_bom_btn = (By.ID, "save-bom-btn")
        self.conitnue_bom_btn = (By.ID, "continueBomBtn")
        self.close_x_btn = (By.XPATH, "(//*[name()='svg'][@id='step-close-button'])[1]")
        self.val_error1 = (By.XPATH, "//div[5]//div[1]//p[1]")
        self.val_error2 = \
            (By.XPATH, "(//div[contains(@class, 'joy-1s3sf3m') and contains(., 'This field is required')])")
        self.val_error3 = (By.XPATH, "//div[8]//div[1]//p[1]")
        self.first_bom_list = (By.XPATH, " //a[normalize-space()='BOM #1']")
        self.bom_menu_btn = \
            (By.XPATH, "/html[1]/body[1]/div[1]/section[1]/aside[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]/div[1]/div[2]/p[1]")
        # Edit BOM
        self.edit_button = (By.XPATH, "//button[normalize-space()='Edit']")
        self.current_assignee_edt = (By.XPATH, "//p[normalize-space()='Current Assignee']")
        self.assigned_team_edt = (By.XPATH, "//p[normalize-space()='Assigned Team']")
        self.project_id_edt = (By.XPATH, "//p[normalize-space()='Project ID']")
        self.pre_deplymnt_edt = (By.XPATH, "//p[normalize-space()='Pre-deployment start date']")
        self.requested_date_edt = (By.XPATH, "//p[normalize-space()='Requested date']")
        self.ste_instlltn_edt = (By.XPATH, "//p[normalize-space()='Site Installation Type']")
        self.wrhouse_stgng_edt = (By.XPATH, "//p[normalize-space()='Warehouse Staging Location']")
        self.bom_status_edt = (By.XPATH, "//p[normalize-space()='BOM Status']")
        self.bom_total_edt = (By.XPATH, "//p[normalize-space()='BOM Total']")
        self.pick_list_heading = \
            (By.XPATH, "(//p[contains(.,'Pick List')])")
        self.equipmnt_pcklst_view = (By.XPATH, "//p[normalize-space()='Equipment']")
        self.vendor_pcklst_view = (By.XPATH, "//p[normalize-space()='Vendor']")
        self.edit_pcklist_btn = (By.XPATH, "//button[normalize-space()='Edit Picklist']")
        # create bom step 1
        self.current_assigned_options = (By.XPATH, "(//div[@class='my-react-select__input-container joy-19bb58m'])[1]")
        self.assigned_team_options = (By.XPATH, "(//div[@class='my-react-select__input-container joy-19bb58m'])[2]")
        self.toast_msg_success = (By.XPATH, "//p[normalize-space()='BOM Updated successfully']")
        self.selected_assignee = (
        By.XPATH, "(//div[@class='my-react-select__single-value joy-1dimb5e-singleValue'])[1]")
        self.selected_team = (By.XPATH, "(//div[@class='my-react-select__single-value joy-1dimb5e-singleValue'])[2]")
        self.warehouse_loc_options = (By.XPATH, "(//div[@class='my-react-select__input-container joy-19bb58m'])[3]")
        self.selected_warehouse = (
        By.XPATH, "(//div[@class='my-react-select__single-value joy-1dimb5e-singleValue'])[3]")
        self.site_installation_options = (By.XPATH, "(//div[@class='my-react-select__input-container joy-19bb58m'])[4]")
        self.selected_site = (By.XPATH, "(//div[@class='my-react-select__single-value joy-1dimb5e-singleValue'])[4]")
        self.dismiss_btn = (By.XPATH, "//button[normalize-space()='Dismiss']")
        # create BOM step 2
        self.hose_clamp_label = \
            (By.XPATH, "(//label[normalize-space()='Hose Clamp Needed for Cable Run (Round Member)'])[1]")
        self.y_mount_label = (By.XPATH, "(//label[normalize-space()='Y Mount needed?'])[1]")
        self.fiber_trunk_checkbox = \
            (By.CSS_SELECTOR,
             "body > div:nth-child(2) > section:nth-child(2) > section:nth-child(4) > div:nth-child(1) > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > span:nth-child(1) > input:nth-child(1)")
        self.fiber_trunk_cable_label = (By.XPATH, "//label[normalize-space()='Fiber Trunk Cable Make']")
        self.fiber_trunk_model_label = (By.XPATH, "(//label[normalize-space()='Fiber Trunk Model #'])[1]")
        self.fiber_trunk_total_length_label = \
            (By.XPATH, "(//label[normalize-space()='Fiber Trunk Cable Total Length'])[1]")
        self.fiber_trunk_override_label = \
            (By.XPATH, "(//label[normalize-space()='Fiber Trunk Cable Length Override'])[1]")
        self.planned_equipment_heading = (By.XPATH, "//h4[normalize-space()='Planned Equipment']")
        self.add_equipment_btn = (By.ID, "addEquipmentBtn")
        self.fiber_trunk_cable_make_options = \
            (By.XPATH, "(//div[@class='my-react-select__input-container joy-19bb58m'])[2]")
        # create step 3
        self.backhauls_heading = (By.XPATH, "//h4[normalize-space()='Backhauls']")
        self.add_backhaul = (By.ID, "addBackhaulBtn")
        self.step_back_button = (By.CSS_SELECTOR, "#step-back-button")

        # BOM detail
        self.cur_assignee_dtl = \
            (By.XPATH, "/html[1]/body[1]/div[1]/section[1]/section[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/p[2]")
        self.assgnd_tm_dtl = \
            (By.XPATH, "/html[1]/body[1]/div[1]/section[1]/section[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/p[2]")
        self.ste_instlltn_dtl =\
            (By.XPATH, "/html[1]/body[1]/div[1]/section[1]/section[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[6]/p[2]")
        self.wrhse_dtl =\
            (By.XPATH, "/html[1]/body[1]/div[1]/section[1]/section[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[7]/p[2]")
