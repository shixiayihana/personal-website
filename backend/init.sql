USE `cn_index_percentile`;

-- A股分位观测站数据库初始化脚本
-- 请先在 Navicat 中选中已经创建好的 cn_index_percentile 数据库。


-- 指数基本信息表：一条记录对应一个指数
CREATE TABLE IF NOT EXISTS `index_info` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '数据库自增主键',
    `index_code` VARCHAR(16) NOT NULL COMMENT '指数代码，例如SH000300',
    `index_name` VARCHAR(32) NOT NULL COMMENT '指数名称，例如沪深300',
    PRIMARY KEY (`id`),
    UNIQUE KEY `uk_index_code` (`index_code`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci COMMENT = '指数基本信息表';

-- 每日估值历史表：一条记录对应一个指数的一个日期
CREATE TABLE IF NOT EXISTS `index_valuation` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '数据库自增主键',
    `index_code` VARCHAR(16) NOT NULL COMMENT '指数代码',
    `data` DATE NOT NULL COMMENT '估值数据对应的完整日期',
    `pe_percentile` DECIMAL(8, 6) NOT NULL COMMENT 'PE历史百分位，保存为0到1的小数',
    `pb_percentile` DECIMAL(8, 6) NOT NULL COMMENT 'PB历史百分位，保存为0到1的小数',
    PRIMARY KEY (`id`),
    UNIQUE KEY `uk_index_data` (`index_code`, `data`),
    KEY `idx_data` (`data`),
    CONSTRAINT `fk_valuation_index_code` FOREIGN KEY (`index_code`) REFERENCES `index_info` (`index_code`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci COMMENT = '指数每日估值百分位历史表';

-- 初始化当前关注的三个指数
INSERT INTO
    `index_info` (`index_code`, `index_name`)
VALUES ('SH000300', '沪深300'),
    ('SH000905', '中证500'),
    ('SZ399006', '创业板')
ON DUPLICATE KEY UPDATE
    `index_name` = VALUES(`index_name`);

-- 可选：执行后检查表结构和索引
-- SHOW CREATE TABLE `index_info`;
-- SHOW CREATE TABLE `index_valuation`;
-- SHOW INDEX FROM `index_valuation`;